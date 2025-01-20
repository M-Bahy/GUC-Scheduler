import copy
from data import deserialize, serialize , get_subject
import os
from data import DAY_MAPPING, SLOT_MAPPING, SEMINARS

cloud_l1 = get_subject("NETW1009")
cloud_l2 = get_subject("NETW1009", "L002")
image_l1 = get_subject("DMET1001")
image_l2 = get_subject("DMET1001", "L002")

def add_elective_lecture(seminar_path , lecture1 , lecture2):
    pass

# possible combinations
# cloud_l1 + image_l1
# cloud_l1 + image_l2
# cloud_l2 + image_l1
# cloud_l2 + image_l2

