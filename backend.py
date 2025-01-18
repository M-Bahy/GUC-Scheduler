import pickle
from schedule import Schedule

day_mapping = {
    "Saturday": 0,
    "Sunday": 1,
    "Monday": 2,
    "Tuesday": 3,
    "Wednesday": 4,
    "Thursday": 5,
    "Friday": 6,
}

slot_mapping = {
    "First Slot 8:15-9:45": 0,
    "Second Slot 10:00-11:30": 1,
    "Third Slot 11:45-1:15": 2,
    "Fourth Slot 1:45-3:15": 3,
    "Fifth Slot 3:30-5:00": 4,
}

TUT_G1 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
TUT_G2 = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]


def deserialize(name):
    name = f"pickles/{name}.pickle"
    with open(name, "rb") as infile:
        return pickle.load(infile)


subjects = deserialize("all_subjects")
# print(subjects[40].day)  # Sunday
# print(subjects[40].slot)  # First Slot 8:15-9:45
# s = Schedule()
# print(s)
# mapped_day = day_mapping[subjects[40].day]
# mapped_slot = slot_mapping[subjects[40].slot]
# s.set_slot(mapped_day, mapped_slot, subjects[40].name)
# s.free()
# print(s)
print(len(subjects))
