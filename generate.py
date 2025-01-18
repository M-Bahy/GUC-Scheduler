from data import deserialize
from data import DAY_MAPPING, SLOT_MAPPING, ELECTIVE_TUTS
from itertools import product

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
    first_elective = None
    second_elective = None
    for subject in subjects:
        if subject.code == elective_codes[0]:
            first_elective = subject
        elif subject.code == elective_codes[1]:
            second_elective = subject
        if first_elective and second_elective:
            break

    elect_1_tuts = ELECTIVE_TUTS.get(elective_codes[0], [])
    elect_2_tuts = ELECTIVE_TUTS.get(elective_codes[1], [])

    def get_subject_by_tut(tut_code):
        for subject in subjects:
            if subject.code == tut_code:
                return subject
        return None

    elect_1_subjects = [get_subject_by_tut(tut) for tut in elect_1_tuts]
    elect_2_subjects = [get_subject_by_tut(tut) for tut in elect_2_tuts]

    possible_combinations = list(product(elect_1_subjects, elect_2_subjects))

    valid_combinations = []

    for combo in possible_combinations:
        if combo[0] is None or combo[1] is None:
            continue
        try:
            for seminar in seminars:
                seminar_copy = seminar.copy()
                seminar_copy.set_slot(
                    DAY_MAPPING[combo[0].day],
                    SLOT_MAPPING[combo[0].slot],
                    combo[0].name,
                )
                seminar_copy.set_slot(
                    DAY_MAPPING[combo[1].day],
                    SLOT_MAPPING[combo[1].slot],
                    combo[1].name,
                )
            valid_combinations.append(combo)
        except ValueError:
            continue

    print(valid_combinations)
    return seminars


to_func = core_schedules.copy()
seminars = add_seminar(to_func, "CSEN1140")
final_schedules = add_elective(seminars, ["CSEN907", "CSEN1076"])
