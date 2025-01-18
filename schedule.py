from fpdf import FPDF
import pandas as pd


class Schedule:
    def __init__(self, strict, name):
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
        self.name = name
        self.number = 0
        self.elect1number = 0
        self.elect2number = 0

    def __str__(self):
        return "\n" + "\n" + self.name + "\n" + str(self.df)

    def __repr__(self):
        return "\n" + "\n" + self.name + "\n" + str(self.df)

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
        if self.strict:
            self.df.iloc[day, slot] = value
        else:
            self.df.iloc[day, slot] = self.df.iloc[day, slot] + "\n" + value

    def save(self, path):
        self.df.to_csv(path)

    def free(self):
        for i in range(0, len(self.df.index)):
            for j in range(0, len(self.df.columns)):
                # If no subjects were added, mark as "free"
                if pd.isnull(self.df.iloc[i, j]):
                    self.df.iloc[i, j] = "free"

    def save_as_pdf(self, path):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=8)

        # Add the schedule name
        pdf.cell(200, 10, txt=self.name, ln=True, align="C")

        # Add the table header
        pdf.cell(30, 10, txt="", border=1)
        for column in self.columns:
            pdf.cell(30, 10, txt=column, border=1)
        pdf.ln()

        # Add the table rows
        for index, row in self.df.iterrows():
            pdf.cell(30, 10, txt=index, border=1)
            for item in row:
                pdf.cell(30, 10, txt=str(item), border=1)
            pdf.ln()

        pdf.output(path)


# Example usage:
# schedule = Schedule(strict=True, name="Sample Schedule")
# schedule.save_as_pdf("sample_schedule.pdf")
