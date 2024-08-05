class Employe:
    def __init__(self,string):
        self.string = string

    def __getitem__(self, index):
        return self.string[index]

e = Employe([1,2,3,4])
print(f"First Element is {e[1]}")


class Employe:
    def __init__(self,string):
        self.string = string

    def __setitem__(self, index, value):
        self.string[index] = value

e = Employe([1,2,3])
print(e.string)
e[1] = 5
print(e.string)
