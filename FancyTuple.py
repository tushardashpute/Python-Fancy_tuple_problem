class FancyTuple:

# default constructor
    def __init__(self,*vartuple):
        try:
            self.first = vartuple[0]
        except IndexError:
            self.first = "AttributeError"
        try:
            self.second = vartuple[1]
        except IndexError:
            self.second = "AttributeError"

        try:
            self.third = vartuple[2]
        except IndexError:
            self.third = "AttributeError"
        try:
            self.fourth = vartuple[3]
        except IndexError:
            self.fourth = "AttributeError"

        try:
            self.fifth = vartuple[4]
        except IndexError:
            self.fifth = "AttributeError"


    def len(self):
            if self.first == "AttributeError":
                return 0
            elif self.second == "AttributeError":
                return 1
            elif self.third == "AttributeError":
                return 2
            elif self.fourth == "AttributeError":
                return 3
            elif self.fifth == "AttributeError":
                return 4    
            else:
                return 5

# t = FancyTuple("dog","cat","mouse")
t = FancyTuple("dog","cat","mouse","horse")
# t = FancyTuple("dog","cat","mouse","pig","rabbit")
print(t.first)
print(t.second)
print(t.third)
print(t.fourth)
print(t.fifth)
print(t.len())