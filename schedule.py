import pandas as pd


class Schedule:
    def __init__(self, strict=False):
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
        self.strict = strict

    def __str__(self):
        return str(self.df)

    def __repr__(self):
        return str(self.df)

    def get_size(self):
        return self.df.shape

    def get_slot(self, day, slot):
        return self.df.iloc[day, slot]

    def set_slot(self, day, slot, value):
        if self.strict and not (pd.isna(self.df.iloc[day, slot])):
            message = (
                f"Slot {day} {slot} is already occupied"
                + f" with {self.df.iloc[day, slot]}"
                + f" and you are trying to set it to {value}"
            )
            raise ValueError(message)
        self.df.iloc[day, slot] = value

    def save(self, path):
        self.df.to_csv(path)

    def free(self):
        for i in range(0, len(self.df.index)):
            for j in range(0, len(self.df.columns)):
                # If no subjects were added, mark as "free"
                if pd.isnull(self.df.iloc[i, j]):
                    self.df.iloc[i, j] = "free"
