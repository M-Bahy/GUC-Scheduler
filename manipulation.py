import pandas as pd


OG_PATH = "og.csv"
BETWEEN_CELLS_SPLIT = "      "
INNER_CELL_SPLIT = " "
LECTURE = "Lecture"
LAB = "Lab"
TUTORIAL = "Tut"
MAPPING = {"DMET1001": "Image Processing", "NETW1009": "Cloud Computing"}
df = pd.read_csv(OG_PATH, index_col=0)

for i in range(0, len(df.index)):  # loop through rows
    for j in range(0, len(df.columns)):  # loop through columns
        content = df.iloc[i, j].split(BETWEEN_CELLS_SPLIT)
        for subject in content:
            # loop through the content of the cell (contains multiple subjects)
            subject = subject.split(INNER_CELL_SPLIT)

            # remove empty strings
            subject = list(filter(None, subject))
            # skip free saturdays
            if len(subject) == 1:
                continue

            if subject[5] == LECTURE:
                subject = subject[2:]
            else:
                subject = subject[1:]
            code = subject[-3] + subject[-2]

            # replace the code with its mapping if it exists
            if code in MAPPING:
                code = MAPPING[code]
            # put the code back in the subject
            subject[-3] = code
            subject.pop(-2)
            subject = " ".join(subject)

            print(subject)
