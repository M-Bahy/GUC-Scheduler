class Subject:
    def __init__(self, group, location, name, type, code, isCore, day, slot):
        self.group = group
        self.location = location
        self.name = name
        self.type = type
        self.code = code
        self.isCore = isCore
        self.day = day
        self.slot = slot

    def __str__(self):
        return f"{self.name} on {self.day} at {self.slot}"

    def __repr__(self):
        return f"{self.name} on {self.day} at {self.slot}"
