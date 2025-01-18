from data import deserialize
from data import DAY_MAPPING, SLOT_MAPPING, LECTURE

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


def add_elective_lecture(schedules, elective_code):
    lecs = []
    results = []
    for subject in subjects:
        if subject.code == elective_code and subject.type == LECTURE:
            lecs.append(subject)

    counter = 4

    for schedule in schedules:
        counter += 1
        group_code = "L001" if counter < 16 else "L002"
        for lec in lecs:
            if lec.group == group_code:
                day = DAY_MAPPING[lec.day]
                slot = SLOT_MAPPING[lec.slot]
                schedule.set_slot(day, slot, lec.name + " Lecture")
        results.append(schedule)
    # print(results)
    return results


def add_elective(seminars, elective_codes):
    with_lecs = add_elective_lecture(seminars, elective_codes[0])
    with_lecs = add_elective_lecture(with_lecs, elective_codes[1])
    return with_lecs


# print(core_schedules)
to_func = core_schedules.copy()
seminars = add_seminar(to_func, "CSEN1140")
final_schedules = add_elective(seminars, ["NETW1009", "DMET1001"])
print(final_schedules)
