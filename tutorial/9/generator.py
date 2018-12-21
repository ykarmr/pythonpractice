#itetatorを作るもの
def reverse(data):
    for index in range(len(data)-1,-1,-1):
        #yield 途中の値を返す
        yield data[index]

for char in reverse("golf"):
    print(char)
