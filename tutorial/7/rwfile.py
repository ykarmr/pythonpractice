#open(filename,mode)
#mode:読み出し専用　r,書き出し専用 r,両方　r+

with open('literal.py') as f:
    for line in f:
        print(line,end=' ')

    f.write('test')    
