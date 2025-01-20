import copy
from data import deserialize, serialize, get_subject
import os
from data import DAY_MAPPING, SLOT_MAPPING, SEMINARS

cloud_l1 = get_subject("NETW1009")
cloud_l2 = get_subject("NETW1009", "L002")
image_l1 = get_subject("DMET1001")
image_l2 = get_subject("DMET1001", "L002")
code = "CSEN1140"


def add_elective_lecture(seminar_code, lecture1, lecture2):
    seminar_schedules = deserialize(f"Seminars/{seminar_code}")

    # Try to add the first lecture, remove schedules with conflicts
    valid_schedules = []
    for schedule in seminar_schedules:
        day = DAY_MAPPING[lecture1.day]
        slot = SLOT_MAPPING[lecture1.slot]
        try:
            name = lecture1.name + " " + lecture1.type
            schedule.set_slot(day, slot, name)
            valid_schedules.append(schedule)
        except ValueError:
            continue

    # Try to add the second lecture, remove schedules with conflicts
    final_schedules = []
    for schedule in valid_schedules:
        day = DAY_MAPPING[lecture2.day]
        slot = SLOT_MAPPING[lecture2.slot]
        try:
            name = lecture2.name + " " + lecture2.type
            schedule.set_slot(day, slot, name)
            final_schedules.append(schedule)
        except ValueError:
            continue

    return final_schedules


# possible combinations
# cloud_l1 + image_l1
# cloud_l1 + image_l2
# cloud_l2 + image_l1
# cloud_l2 + image_l2

c1 = add_elective_lecture(code, cloud_l1, image_l1)
c2 = add_elective_lecture(code, cloud_l1, image_l2)
c3 = add_elective_lecture(code, cloud_l2, image_l1)
c4 = add_elective_lecture(code, cloud_l2, image_l2)

os.makedirs(
    f"pickles/Seminars with elective lectures/NETW1009_DMET1001/NETW1009_L001_DMET1001_L001",
    exist_ok=True,
)
os.makedirs(
    f"pickles/Seminars with elective lectures/NETW1009_DMET1001/NETW1009_L001_DMET1001_L002",
    exist_ok=True,
)
os.makedirs(
    f"pickles/Seminars with elective lectures/NETW1009_DMET1001/NETW1009_L002_DMET1001_L001",
    exist_ok=True,
)
os.makedirs(
    f"pickles/Seminars with elective lectures/NETW1009_DMET1001/NETW1009_L002_DMET1001_L002",
    exist_ok=True,
)

serialize(
    c1,
    f"Seminars with elective lectures/NETW1009_DMET1001/NETW1009_L001_DMET1001_L001/NETW1009_L001_DMET1001_L001",
)
serialize(
    c2,
    f"Seminars with elective lectures/NETW1009_DMET1001/NETW1009_L001_DMET1001_L002/NETW1009_L001_DMET1001_L002",
)
serialize(
    c3,
    f"Seminars with elective lectures/NETW1009_DMET1001/NETW1009_L002_DMET1001_L001/NETW1009_L002_DMET1001_L001",
)
serialize(
    c4,
    f"Seminars with elective lectures/NETW1009_DMET1001/NETW1009_L002_DMET1001_L002/NETW1009_L002_DMET1001_L002",
)

print("Done")
