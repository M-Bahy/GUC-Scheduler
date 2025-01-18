import copy
from data import deserialize
import os
from data import (
    DAY_MAPPING,
    SLOT_MAPPING,
    LECTURE,
    ELECTIVE_TUTS,
    ELECTIVES,
    ELECTIVE_GROUPS,
)

# from schedule import Schedule

core_schedules = deserialize("core_schedules_with_tuts")
print(len(core_schedules))
subjects = deserialize("all_subjects")


def add_seminar(cores, seminar_code):
    seminar = None
    for subject in subjects:
        if subject.code == seminar_code:
            seminar = subject
            break
    day = DAY_MAPPING[seminar.day]
    slot = SLOT_MAPPING[seminar.slot]
    counter = 4
    for core in cores:
        counter += 1
        core.number = counter
        core.set_slot(day, slot, seminar.name)
    return cores


def add_elective_lecture(schedules, elective_code, group_code):
    lecs = []
    results = []
    for subject in subjects:
        if subject.code == elective_code and subject.type == LECTURE:
            lecs.append(subject)

    counter = 4

    for schedule in schedules:
        counter += 1
        # group_code = "L001" if counter < 16 else "L002"
        for lec in lecs:
            if lec.group == group_code:
                day = DAY_MAPPING[lec.day]
                slot = SLOT_MAPPING[lec.slot]
                try:
                    schedule.set_slot(day, slot, lec.name + " Lecture")
                    results.append(schedule)
                except ValueError:
                    continue
    # print(results)
    return results


def add_elective_tutorials(schedules, elective_code):
    elec_1_tut = ELECTIVE_TUTS[elective_code[0]]
    elec_2_tut = ELECTIVE_TUTS[elective_code[1]]
    if elec_1_tut and elec_2_tut:
        return add_both(schedules, elective_code, elec_1_tut, elec_2_tut)
    elif elec_1_tut:
        return add_one(schedules, elective_code[0], elec_1_tut)
    elif elec_2_tut:
        return add_one(schedules, elective_code[1], elec_2_tut)


def add_elective(seminars, elective_codes):
    # with_lecs = add_elective_lecture(seminars, elective_codes[0])
    # print(len(with_lecs))
    # with_lecs = add_elective_lecture(with_lecs, elective_codes[1])
    # print(len(with_lecs))
    # # with_tuts = add_elective_tutorials(with_lecs, elective_codes)
    # return with_lecs
    g1 = ELECTIVE_GROUPS[elective_codes[0]]
    g2 = ELECTIVE_GROUPS[elective_codes[1]]
    results = []
    x = []
    for group in g1:
        x += add_elective_lecture(seminars, elective_codes[0], group)
        print("Length of x: ", len(x))
        results += x
        x = []
    for group in g2:
        x += add_elective_lecture(seminars, elective_codes[1], group)
        print("Length of x: ", len(x))
        results += x
    return results


# print(core_schedules)
to_func = core_schedules.copy()
seminars = add_seminar(to_func, "CSEN1140")
print(len(seminars))
# print(seminars[0])
# final_schedules = add_elective(seminars, ["NETW1009", "DMET1001"])
print(len(seminars))
# print(final_schedules)

person = "Bahy"

# create a folder for the person
os.makedirs(person, exist_ok=True)

# put the schedules in the folder

for i, schedule in enumerate(seminars):
    schedule.free()
    saving_name = f"{person}/Tutorial {schedule.number}.pdf"
    schedule.save_as_pdf(saving_name)
    # serialize(schedule, f"{person}/schedule{i}")
