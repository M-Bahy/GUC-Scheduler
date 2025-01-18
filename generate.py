from data import deserialize
from data import DAY_MAPPING, SLOT_MAPPING, ELECTIVE_TUTS

# from schedule import Schedule

core_schedules = deserialize("core_schedules")
subjects = deserialize("all_subjects")


def add_seminar(cores, seminar_code):
    seminar = None
    for subject in subjects:
        if subject.code == seminar_code:
            seminar = subject
            break
    day = DAY_MAPPING[seminar.day]
    slot = SLOT_MAPPING[seminar.slot]
    for core in cores:
        core.set_slot(day, slot, seminar.name)
    return cores


def add_elective(seminars, elective_codes):
    elect_1_tuts = ELECTIVE_TUTS[elective_codes[0]]
    elect_2_tuts = ELECTIVE_TUTS[elective_codes[1]]
    print(elect_1_tuts)
    print(elect_2_tuts)
    return seminars


to_func = core_schedules.copy()
seminars = add_seminar(to_func, "CSEN1140")
final_schedules = add_elective(seminars, ["CSEN907", "CSEN1076"])

