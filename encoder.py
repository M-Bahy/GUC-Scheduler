import pandas as pd
from subject import Subject
from schedule import Schedule

G1_PATH = "g1 og.csv"
G2_PATH = "g2 og.csv"
# OUTPUT_PATH = "output2.csv"
BETWEEN_CELLS_SPLIT = "      "
INNER_CELL_SPLIT = " "
LECTURE = "Lecture"
LAB = "Lab"
TUTORIAL = "Tut"
MAPPING = {"DMET1001": "Image Processing", "NETW1009": "Cloud Computing"}
ELECTIVES = {
    "CSEN907": "KRR",
    "CSEN1076": "NLP",
    "DMET1067": "Deep Learning",
    "ELCT1018": "Quantum",
    "NETW1009": "Cloud Computing",
    "DMET1072": "Computer Animation",
    "DMET1001": "Image Processing",
    "DMET1042": "VOIP",
    "DMET1075": "AR/VR",
    "MCTR1024": "Reinforcement Learning",
}
SEMINARS = {
    "CSEN1034": "Seminar - Haythem Ismail",
    "CSEN1118": "Seminar - Mervat Abuelkheir",
    "CSEN1088": "Seminar - Milad Ghantous",
    "CSEN1143": "Seminar - Yomna Hassan",
    "DMET1057": "Seminar - Hisham Othman",
    "DMET1076": "Seminar - Rimon Elias",
    "DMET1061": "Seminar - Mohammed Salem",
    "DMET1077": "Seminar - Mohammed Salem",
    "CSEN1127": "Seminar - Shereen Moataz",
    "CSEN1142": "Seminar - Shereen Moataz",
    "CSEN1008": "Seminar - Catherine Elias",
    "CSEN1139": "Seminar - Aya Salama",
    "CSEN1140": "Seminar - Aya Salama",
    "CSEN1126": "Seminar - Ahmed Abdelfattah",
    "CSEN1128": "Seminar - Mohamed Hamed",
    "CSEN1141": "Seminar - Mohamed Karam Gabr",
    "CSEN1134": "Seminar - Mohamed Karam Gabr",
    "CSEN1135": "Seminar - Mohamed Karam Gabr",
}


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
                    code = MAPPING[code]
                    # put the code back in the subject
                    subject[-3] = code
                    subject.pop(-2)
                    sub = (
                        Subject(  # group, location, name, type, code, isCore, day, slot
                            subject[0],
                            subject[1],
                            subject[2],
                            subject[3],
                            df.index[i],
                            df.columns[j],
                        )
                    )
                    subjects.append(sub)
                    subject = " ".join(subject)
                    new_content.append(subject)

            # If no subjects were added, mark as "free"
            if not new_content:
                output_df.iloc[i, j] = "free"
            else:
                # Join subjects with a line break
                schedule.set_slot(i, j, "\n".join(new_content))
    schedule.free()
    return subjects, schedule


subjects_of_group_1, schedule_of_group_1 = encode(G1_PATH)
subjects_of_group_2, schedule_of_group_2 = encode(G2_PATH)
schedule_of_group_1.save("schedule1.csv")
schedule_of_group_2.save("schedule2.csv")
print(subjects_of_group_1[0].group)
