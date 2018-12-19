class B(Exception):
    pass
class C(B):
    pass
class D(C):
    pass

for cis in [B,C,D]:
    try:
        raise cis()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
