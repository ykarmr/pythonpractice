class Complex:
    def __init__(self,realpart,imagepart):
        self.r=realpart
        self.i=imagepart
x=int(input("xを入力してください:"))
y=int(input("yを入力してください:"))
z=Complex(x,y)
print("x=",z.r,",","y=",z.i)
