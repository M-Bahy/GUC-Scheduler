from data import serialize, deserialize, DAY_MAPPING, SLOT_MAPPING
from schedule import Schedule

core_schedules = deserialize("core_schedules")
subjects = deserialize("all_subjects")


def generate(seminar_code, elective_codes):
    seminar = None
    for subject in subjects:
        if subject.code == seminar_code:
            seminar = subject
            break
    day = DAY_MAPPING[seminar.day]
    slot = SLOT_MAPPING[seminar.slot]
    for core in core_schedules:
        core.set_slot(day, slot, seminar.name)


print(core_schedules)
generate("CSEN1140", ["DMET1072", "DMET1001"])
print(core_schedules)
