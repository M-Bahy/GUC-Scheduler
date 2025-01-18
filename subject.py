class Subject:
    def __init__(self, group, location, name, type, day, slot):
        self.group = group
        self.location = location
        self.name = name
        self.type = type
        self.day = day
        self.slot = slot

    def __str__(self):
        return f"{self.name} on {self.day} at {self.slot}"
