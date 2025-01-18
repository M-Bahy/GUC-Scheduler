import pickle


def deserialize(name):
    name = f"pickles/{name}.pickle"
    with open(name, "rb") as infile:
        return pickle.load(infile)


all = deserialize("all_subjects")

print(len(all))

for sub in all:
    if sub.code == "DMET1067":
        print(sub.type)
        print(sub.group)
