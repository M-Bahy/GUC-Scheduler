import pickle

G1_PATH = "CSVs/g1 og.csv"
G2_PATH = "CSVs/g2 og.csv"
BETWEEN_CELLS_SPLIT = "      "
INNER_CELL_SPLIT = " "
LECTURE = "Lecture"
LAB = "Lab"
TUTORIAL = "Tut"
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
CORES = {
    "CSEN1001": "Security",
    "CSEN1003": "Compilers",
    "CSEN1002": "Scalable",
    "HUMA1001": "ITPM",
}

MAPPING = {**ELECTIVES, **SEMINARS, **CORES}

DAY_MAPPING = {
    "Saturday": 0,
    "Sunday": 1,
    "Monday": 2,
    "Tuesday": 3,
    "Wednesday": 4,
    "Thursday": 5,
    "Friday": 6,
}

SLOT_MAPPING = {
    "First Slot 8:15-9:45": 0,
    "Second Slot 10:00-11:30": 1,
    "Third Slot 11:45-1:15": 2,
    "Fourth Slot 1:45-3:15": 3,
    "Fifth Slot 3:45-5:15": 4,
}

G1 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
G2 = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
GS = G1 + G2

TUTORIALS = [
    "T005",
    "T006",
    "T007",
    "T008",
    "T009",
    "T010",
    "T011",
    "T012",
    "T013",
    "T014",
    "T015",
    "T016",
    "T017",
    "T018",
    "T019",
    "T020",
    "T021",
    "T022",
    "T023",
    "T024",
    "T025",
    "T026",
]

LABS = [
    "P005",
    "P006",
    "P007",
    "P008",
    "P009",
    "P010",
    "P011",
    "P012",
    "P013",
    "P014",
    "P015",
    "P016",
    "P017",
    "P018",
    "P019",
    "P020",
    "P021",
    "P022",
    "P023",
    "P024",
    "P025",
    "P026",
]

ELECTIVE_TUTS = {
    "CSEN907": [],  # KRR
    "CSEN1076": ["T001", "T002"],  # NLP
    "DMET1067": ["T001", "T002"],  # Deep Learning
    "ELCT1018": ["P001", "P002"],  # Quantum
    "NETW1009": [  # Cloud Computing
        "T001",
        "T002",
        "T003",
        "T004",
        "T005",
        "T006",
        "T007",
        "T008",
        "T009",
        "T010",
        "T011",
        "T012",
        "T013",
        "T014",
        "T015",
        "T016",
    ],
    "DMET1072": [],  # Computer Animation
    "DMET1001": [  # Image Processing
        "T001",
        "T002",
        "T003",
        "T004",
        "T005",
        "T006",
        "T007",
        "T008",
        "T009",
        "T010",
        "T011",
        "T012",
        "T013",
        "T014",
    ],
    "DMET1042": [],  # VOIP
    "DMET1075": [],  # AR/VR
    "MCTR1024": ["T003"],  # Reinforcement Learning
}


def deserialize(name):
    name = f"pickles/{name}.pickle"
    with open(name, "rb") as infile:
        return pickle.load(infile)


def serialize(obj, name):
    name = f"pickles/{name}.pickle"
    with open(name, "wb") as outfile:
        pickle.dump(obj, outfile)
