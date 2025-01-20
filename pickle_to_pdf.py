import os
import pickle
from combine import combine_pdfs


def deserialize(name):
    with open(name, "rb") as infile:
        return pickle.load(infile)


# others/Fahim og files/ pickle1.pickle pickle2.pickle pickle3.pickle


def read_data(directory):
    schedules_dic = {}
    schedules_list = []
    # scan the directory for pickle files
    for file in os.listdir(directory):
        if file.endswith(".pickle"):
            schedule = deserialize(directory + file)
            file = file.replace(".pickle", "")
            schedules_dic[file] = schedule
            schedules_list.append(schedule)
    return schedules_dic, schedules_list


def create_pdfs(dic):
    for key in dic:
        schedules = dic[key]
        os.makedirs(f"PDFs/{key}", exist_ok=True)
        for schedule in schedules:
            schedule.save_as_pdf(f"PDFs/{key}/{schedule.name}.pdf")


dic, lis = read_data("others/Fahim og files/")

create_pdfs(dic)
