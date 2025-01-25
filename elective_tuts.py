import copy
from data import deserialize, serialize, get_subject
import os
from data import DAY_MAPPING, SLOT_MAPPING, SEMINARS, ELECTIVE_TUTS

elect1_code = "NETW1009"  # Cloud Computing
elect2_code = "DMET1067"  # Deep Learning

elect1_tuts = ELECTIVE_TUTS[elect1_code]  # 1-16
elect2_tuts = ELECTIVE_TUTS[elect2_code]  # 1-14


def add_tuts(tut1, tut2, group1="L001", group2="L001"):
    schedules = deserialize(
        f"Seminars with elective lectures/{elect1_code}_{elect2_code}/{elect1_code}_{group1}_{elect2_code}_{group2}/{elect1_code}_{group1}_{elect2_code}_{group2}"
    )
    tutorial1 = get_subject(elect1_code, tut1)
    tutorial2 = get_subject(elect2_code, tut2)

    # Try to add the first tutorial, remove schedules with conflicts
    valid_schedules = []
    for schedule in schedules:
        day = DAY_MAPPING[tutorial1.day]
        slot = SLOT_MAPPING[tutorial1.slot]
        try:
            name = tutorial1.name + " " + tutorial1.type
            schedule.set_slot(day, slot, name)
            valid_schedules.append(schedule)
        except ValueError:
            continue

    # Try to add the second lecture, remove schedules with conflicts
    final_schedules = []
    for schedule in valid_schedules:
        day = DAY_MAPPING[tutorial2.day]
        slot = SLOT_MAPPING[tutorial2.slot]
        try:
            name = tutorial2.name + " " + tutorial2.type
            schedule.set_slot(day, slot, name)
            final_schedules.append(schedule)
        except ValueError:
            continue

    return final_schedules


# possible combinations
# t1 + t1 , t1 + t2 , t1 + t3 , t1 + t4 , t1 + t5 , t1 + t6 , t1 + t7 , t1 + t8 , t1 + t9 , t1 + t10 , t1 + t11 , t1 + t12 , t1 + t13 , t1 + t14
# t2 + t1 , t2 + t2 , t2 + t3 , t2 + t4 , t2 + t5 , t2 + t6 , t2 + t7 , t2 + t8 , t2 + t9 , t2 + t10 , t2 + t11 , t2 + t12 , t2 + t13 , t2 + t14
# t3 + t1 , t3 + t2 , t3 + t3 , t3 + t4 , t3 + t5 , t3 + t6 , t3 + t7 , t3 + t8 , t3 + t9 , t3 + t10 , t3 + t11 , t3 + t12 , t3 + t13 , t3 + t14
# t4 + t1 , t4 + t2 , t4 + t3 , t4 + t4 , t4 + t5 , t4 + t6 , t4 + t7 , t4 + t8 , t4 + t9 , t4 + t10 , t4 + t11 , t4 + t12 , t4 + t13 , t4 + t14
# t5 + t1 , t5 + t2 , t5 + t3 , t5 + t4 , t5 + t5 , t5 + t6 , t5 + t7 , t5 + t8 , t5 + t9 , t5 + t10 , t5 + t11 , t5 + t12 , t5 + t13 , t5 + t14
# t6 + t1 , t6 + t2 , t6 + t3 , t6 + t4 , t6 + t5 , t6 + t6 , t6 + t7 , t6 + t8 , t6 + t9 , t6 + t10 , t6 + t11 , t6 + t12 , t6 + t13 , t6 + t14
# t7 + t1 , t7 + t2 , t7 + t3 , t7 + t4 , t7 + t5 , t7 + t6 , t7 + t7 , t7 + t8 , t7 + t9 , t7 + t10 , t7 + t11 , t7 + t12 , t7 + t13 , t7 + t14
# t8 + t1 , t8 + t2 , t8 + t3 , t8 + t4 , t8 + t5 , t8 + t6 , t8 + t7 , t8 + t8 , t8 + t9 , t8 + t10 , t8 + t11 , t8 + t12 , t8 + t13 , t8 + t14
# t9 + t1 , t9 + t2 , t9 + t3 , t9 + t4 , t9 + t5 , t9 + t6 , t9 + t7 , t9 + t8 , t9 + t9 , t9 + t10 , t9 + t11 , t9 + t12 , t9 + t13 , t9 + t14
# t10 + t1 , t10 + t2 , t10 + t3 , t10 + t4 , t10 + t5 , t10 + t6 , t10 + t7 , t10 + t8 , t10 + t9 , t10 + t10 , t10 + t11 , t10 + t12 , t10 + t13 , t10 + t14
# t11 + t1 , t11 + t2 , t11 + t3 , t11 + t4 , t11 + t5 , t11 + t6 , t11 + t7 , t11 + t8 , t11 + t9 , t11 + t10 , t11 + t11 , t11 + t12 , t11 + t13 , t11 + t14
# t12 + t1 , t12 + t2 , t12 + t3 , t12 + t4 , t12 + t5 , t12 + t6 , t12 + t7 , t12 + t8 , t12 + t9 , t12 + t10 , t12 + t11 , t12 + t12 , t12 + t13 , t12 + t14
# t13 + t1 , t13 + t2 , t13 + t3 , t13 + t4 , t13 + t5 , t13 + t6 , t13 + t7 , t13 + t8 , t13 + t9 , t13 + t10 , t13 + t11 , t13 + t12 , t13 + t13 , t13 + t14
# t14 + t1 , t14 + t2 , t14 + t3 , t14 + t4 , t14 + t5 , t14 + t6 , t14 + t7 , t14 + t8 , t14 + t9 , t14 + t10 , t14 + t11 , t14 + t12 , t14 + t13 , t14 + t14
# t15 + t1 , t15 + t2 , t15 + t3 , t15 + t4 , t15 + t5 , t15 + t6 , t15 + t7 , t15 + t8 , t15 + t9 , t15 + t10 , t15 + t11 , t15 + t12 , t15 + t13 , t15 + t14
# t16 + t1 , t16 + t2 , t16 + t3 , t16 + t4 , t16 + t5 , t16 + t6 , t16 + t7 , t16 + t8 , t16 + t9 , t16 + t10 , t16 + t11 , t16 + t12 , t16 + t13 , t16 + t14
# 224 possible combinations

# 1. Create a list of all possible combinations
# 2. For each combination, check if it is valid
# 3. If valid, save it to a list
# 4. Save the list to a file

# 1. Create a list of all possible combinations
possible_combinations = []
for t1 in elect1_tuts:
    for t2 in elect2_tuts:
        possible_combinations.append([t1, t2])

# 2&3. For each combination, check if it is valid
final_combinations = {}
# L001 + L001
for combination in possible_combinations:
    t1 = combination[0]
    t2 = combination[1]
    group1 = "L001"
    group2 = "L001"
    combination_name = f"{elect1_code}_{group1}_{t1}_{elect2_code}_{group2}_{t2}"
    combination = add_tuts(tut1=t1, tut2=t2, group1=group1, group2=group2)
    final_combinations[combination_name] = combination
# # L001 + L002
# for combination in possible_combinations:
#     t1 = combination[0]
#     t2 = combination[1]
#     group1 = "L001"
#     group2 = "L002"
#     combination_name = f"{elect1_code}_{group1}_{t1}_{elect2_code}_{group2}_{t2}"
#     combination = add_tuts(tut1=t1, tut2=t2, group1=group1, group2=group2)
#     final_combinations[combination_name] = combination

# L002 + L001
for combination in possible_combinations:
    t1 = combination[0]
    t2 = combination[1]
    group1 = "L002"
    group2 = "L001"
    combination_name = f"{elect1_code}_{group1}_{t1}_{elect2_code}_{group2}_{t2}"
    combination = add_tuts(tut1=t1, tut2=t2, group1=group1, group2=group2)
    final_combinations[combination_name] = combination

# # L002 + L002
# for combination in possible_combinations:
#     t1 = combination[0]
#     t2 = combination[1]
#     group1 = "L002"
#     group2 = "L002"
#     combination_name = f"{elect1_code}_{group1}_{t1}_{elect2_code}_{group2}_{t2}"
#     combination = add_tuts(tut1=t1, tut2=t2, group1=group1, group2=group2)
#     if combination:
#         final_combinations[combination_name] = combination

for combination_name, combination in final_combinations.items():
    serialize(
        combination,
        f"Seminars with elective lectures/{elect1_code}_{elect2_code}/{elect1_code}_{group1}_{elect2_code}_{group2}/Tutorials/{combination_name}",
    )
    print(f"Saved {combination_name}")
