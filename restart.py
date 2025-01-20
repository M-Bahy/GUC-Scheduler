import copy
from data import deserialize, serialize
import os
from data import DAY_MAPPING, SLOT_MAPPING, SEMINARS

# from schedule import Schedule


def add_seminar(seminar_code):
    cores = deserialize("core_schedules_with_tuts")
    subjects = deserialize("all_subjects")
    seminar = None
    for subject in subjects:
        if subject.code == seminar_code:
            seminar = subject
            break
    if seminar is None:
        print(f"Seminar {seminar_code} not found")
        print("Skipping...")
        return
    day = DAY_MAPPING[seminar.day]
    slot = SLOT_MAPPING[seminar.slot]
    counter = 4
    for core in cores:
        counter += 1
        core.number = counter
        core.set_slot(day, slot, seminar.name)
    return cores


for seminar_code in SEMINARS.keys():
    seminar = add_seminar(seminar_code)
    if seminar :
        serialize(seminar, f"Seminars/{seminar_code}")
        print(f"Added {seminar_code}")
