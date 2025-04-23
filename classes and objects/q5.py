class Time:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s
        self.standardise()

    def standardise(self):
        if self.s >= 60:
            self.m += self.s // 60
            self.s = self.s % 60
        if self.m >= 60:
            self.h += self.m // 60
            self.m = self.m % 60
        self.h = self.h % 24

    def __add__(self, other):
        return Time(self.h + other.h, self.m + other.m, self.s + other.s)

    def __sub__(self, other):
        total1 = self.h * 3600 + self.m * 60 + self.s
        total2 = other.h * 3600 + other.m * 60 + other.s
        diff = abs(total1 - total2)

        h = (diff // 3600) % 24
        m = (diff % 3600) // 60
        s = diff % 60

        return Time(h, m, s)

    def __str__(self):
        return f"{self.h:02}:{self.m:02}:{self.s:02}"

   
t1 = Time(24, 49, 40)
t2 = Time(2, 12, 30)

print("Addition:", t1 + t2)
print("Subtraction:", t1 - t2)
