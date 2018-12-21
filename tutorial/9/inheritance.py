#慣習として非publicなものは__を先頭につける
#継承class DerivedClassName(BaseClassName):
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
a=Mapping("B,C")
a.update("C")
print(a.items_list)
b=MappingSubclass("acd")
b.update("a","b")
print(b.items_list)
