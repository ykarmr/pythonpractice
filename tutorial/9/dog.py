class Dog:
    kind='canine'

    def __init__(self,name):
        self.name=name
        self.tricks=[]

    def add_trick(self,trick):
        self.tricks.append(trick)
d=Dog("Fido")
d.add_trick("roll over")
print(d.kind)
print(d.name)
print(d.tricks)
e=Dog("Buddy")
e.add_trick("play dead")
print(e.kind)
print(e.name)
print(e.tricks)
