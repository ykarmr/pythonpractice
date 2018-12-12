#lambda 式:引数
def make_incrementor(n):
    return lambda x:x+n
f=make_incrementor(42)
print(f(0))
print(f(1))
print(f(5))

pairs=[(1,'one'),[2,'two'],[3,'three'],(4,'four')]
#pairs[pair[0],pair[1]]
pairs.sort(key=lambda pair:pair[1])
print(pairs)
