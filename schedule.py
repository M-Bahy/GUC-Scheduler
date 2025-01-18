import pandas as pd
from subject import Subject


class Schedule:
    def __init__(self):
        self.columns = [
            "First Slot 8:15-9:45",
            "Second Slot 10:00-11:30",
            "Third Slot 11:45-1:15",
            "Fourth Slot 1:45-3:15",
            "Fifth Slot 3:45-5:15",
        ]
        self.index = [
            "Saturday",
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
        ]
        self.df = pd.DataFrame(index=self.index, columns=self.columns)

    def __str__(self):
        return str(self.df)

    def get_size(self):
        return self.df.shape

    def get_slot(self, day, slot):
        return self.df.iloc[day, slot]

    def set_slot(self, day, slot, value):
        self.df.iloc[day, slot] = value

    def save(self, path):
        self.df.to_csv(path)


# s = Schedule()
# print(s.get_size())  # (6, 5)
# sub = Subject("G1", "C7.404", "Math", "Lecture", "Saturday", "First Slot 8:15-9:45")
# s.set_slot(0, 0, sub)
# print(s.get_slot(0, 0))  # Math
# print(True if pd.isna(s.get_slot(0, 1)) else False)  # True
