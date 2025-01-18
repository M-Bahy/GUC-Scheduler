import pickle
import pandas as pd
from subject import Subject
from schedule import Schedule
from data import (
    BETWEEN_CELLS_SPLIT,
    INNER_CELL_SPLIT,
    MAPPING,
    CORES,
    G1_PATH,
    G2_PATH,
)


def serialize(obj, name):
    name = name + ".pickle"
    with open(name, "wb") as outfile:
        pickle.dump(obj, outfile)


def deserialize(name):
    name = name + ".pickle"
    with open(name, "rb") as infile:
        return pickle.load(infile)


def encode(CSV_PATH):
    df = pd.read_csv(CSV_PATH, index_col=0)
    output_df = pd.DataFrame(index=df.index, columns=df.columns)
    subjects = []
    schedule = Schedule()
    for i in range(0, len(df.index)):  # loop through rows
        for j in range(0, len(df.columns)):  # loop through columns
            content = df.iloc[i, j].split(BETWEEN_CELLS_SPLIT)
            new_content = []
            for subject in content:
                # loop through the content of the cell
                # (contains multiple subjects)
                subject = subject.split(INNER_CELL_SPLIT)

                # remove empty strings
                subject = list(filter(None, subject))
                # skip free saturdays
                if len(subject) == 1:
                    continue

                subject = subject[1:]
                code = subject[-3] + subject[-2]

                # replace the code with its mapping if it exists
                if code in MAPPING:
                    old_code = code
                    code = MAPPING[code]
                    # put the code back in the subject
                    subject[-3] = code
                    subject.pop(-2)
                    sub = Subject(
                        group=subject[0],
                        location=subject[1],
                        name=subject[2],
                        type=subject[3],
                        code=old_code,
                        isCore=old_code in CORES,
                        day=df.index[i],
                        slot=df.columns[j],
                    )

                    subjects.append(sub)
                    subject = " ".join(subject)
                    new_content.append(subject)

            # If no subjects were added, mark as "free"
            if not new_content:
                output_df.iloc[i, j] = "free"
            else:
                # Join subjects with a line break
                if schedule.strict and len(new_content) > 1:
                    schedule.set_slot(i, j, new_content[0])
                    schedule.set_slot(i, j, new_content[1])  # raise ValueError
                schedule.set_slot(i, j, "\n".join(new_content))
    schedule.free()
    return subjects, schedule


subjects_of_group_1, schedule_of_group_1 = encode(G1_PATH)
subjects_of_group_2, schedule_of_group_2 = encode(G2_PATH)
schedule_of_group_1.save("schedule1.csv")
schedule_of_group_2.save("schedule2.csv")
all_subjects = subjects_of_group_1 + subjects_of_group_2
serialize(all_subjects, "all_subjects")
serialize(schedule_of_group_1, "schedule1")
serialize(schedule_of_group_2, "schedule2")
