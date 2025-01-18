import copy
from data import deserialize
from data import DAY_MAPPING, SLOT_MAPPING, LECTURE, ELECTIVE_TUTS, ELECTIVES

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
                try:
                    schedule.set_slot(day, slot, lec.name + " Lecture")
                    results.append(schedule)
                except ValueError:
                    continue
    # print(results)
    return results


def add_both(schedules, elective_code, tuts1, tuts2):
    results = []
    for tutorial1 in tuts1:  # [T005, T006, T007]
        working = [copy.deepcopy(schedule) for schedule in schedules]
        for subject in subjects:
            if subject.code == elective_code[0] and subject.group == tutorial1:
                day = DAY_MAPPING[subject.day]
                slot = SLOT_MAPPING[subject.slot]
                for schedule in working[:]:  # Iterate over a copy of the list
                    try:
                        schedule.set_slot(day, slot, subject.name + " Tutorial")
                    except ValueError:
                        working.remove(
                            schedule
                        )  # Remove the schedule if an error occurs
                        continue
        for tutorial2 in tuts2:
            working_copy = [copy.deepcopy(schedule) for schedule in working]
            for subject in subjects:
                if subject.code == elective_code[1] and subject.group == tutorial2:
                    day = DAY_MAPPING[subject.day]
                    slot = SLOT_MAPPING[subject.slot]
                    for schedule in working_copy[:]:  # Iterate over a copy of the list
                        try:
                            schedule.set_slot(day, slot, subject.name + " Tutorial")
                        except ValueError:
                            working_copy.remove(
                                schedule
                            )  # Remove the schedule if an error occurs
                            continue
                        new_schedule = copy.deepcopy(schedule)
                        tutorial_name = new_schedule.name
                        new_schedule.name = f"{tutorial_name} Core and Tutorial {tutorial1} in {ELECTIVES[elective_code[0]]} and Tutorial {tutorial2} in {ELECTIVES[elective_code[1]]}"
                        new_schedule.free()
                        new_schedule.number = tutorial_name
                        new_schedule.elect1number = tutorial1
                        new_schedule.elect2number = tutorial2
                        results.append(new_schedule)
    return results


def add_one(schedules, elective_code, tuts):
    pass


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
    with_lecs = add_elective_lecture(seminars, elective_codes[0])
    with_lecs = add_elective_lecture(with_lecs, elective_codes[1])
    with_tuts = add_elective_tutorials(with_lecs, elective_codes)
    return with_tuts


# print(core_schedules)
to_func = core_schedules.copy()
seminars = add_seminar(to_func, "CSEN1140")
print(len(seminars))
print(seminars[0])
# final_schedules = add_elective(seminars, ["NETW1009", "DMET1001"])
# print(len(final_schedules))

person = "OnlyFahim"

elective_1 = ELECTIVES["NETW1009"]
elective_2 = ELECTIVES["DMET1001"]
