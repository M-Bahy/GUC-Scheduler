import pickle
from schedule import Schedule
from data import GS, LECTURE, DAY_MAPPING, SLOT_MAPPING


def deserialize(name):
    name = f"pickles/{name}.pickle"
    with open(name, "rb") as infile:
        return pickle.load(infile)


def serialize(obj, name):
    name = name + ".pickle"
    with open(name, "wb") as outfile:
        pickle.dump(obj, outfile)


subjects = deserialize("all_subjects")
iteration_counter = 0
schedules = [None] * 22
for number in GS:
    iteration_counter += 1
    schedule = Schedule(True)
    lec_group = "L001" if number > 16 else "L002"
    for subject in subjects:
        if "Seminar" in subject.name or not (subject.isCore):
            continue
        if subject.type == LECTURE and subject.group == lec_group:
            day = DAY_MAPPING[subject.day]
            slot = SLOT_MAPPING[subject.slot]
            schedule.set_slot(day, slot, subject.name + " Lecture")
    schedules[iteration_counter-1] = schedule

# print all the schedules in a file

with open("output.txt", "w") as file:
    for schedule in schedules:
        file.write(str(schedule) + "\n")
