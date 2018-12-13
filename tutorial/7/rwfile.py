#open(filename,mode)
#mode:読み出し専用　r,書き出し専用 r,両方　r+

with open('rwfile.py') as f:
    read_data=f.read()
print(f.closed)
