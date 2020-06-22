class Date:
    def __init__(self, date_str):
        self.parse_date(date_str)
        if not self.validate_date(self.day, self.month, self.year):
            self.day = None
            self.month = None
            self.year = None

    @classmethod
    def parse_date(cls, date_str):
        ls = date_str.split("-")
        cls.day = int(ls[0])
        cls.month = int(ls[1])
        cls.year = int(ls[2])

    @staticmethod
    def validate_date(day, month, year):
        if not (day <= 30 and day > 0 and month <= 12 and month > 0 and year > 0 and year < 9999):
            print("date invalid")
            return False
        return True

    def __str__(self):
        if self.day is not None and self.month is not None and self.year is not None:
            return f"Date: {self.day}.{self.month}.{self.year}"
        else:
            return ""


d = Date("1-12-2010")
print(d)
