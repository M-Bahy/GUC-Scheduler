import pickle


def deserialize(name):
    name = f"pickles/{name}.pickle"
    with open(name, "rb") as infile:
        return pickle.load(infile)


subjects = deserialize("all_subjects")
print(len(subjects))
print(subjects[0].type)
