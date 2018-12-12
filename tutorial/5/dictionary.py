# key:value
tel ={'jack':4098,'sape':4139}
print(tel)
tel['guido']=4127
print(tel)
print(tel['jack'])

#delではなくリストから削除
del tel['sape']
print(tel)
tel['irv']=4127
print(tel)
print('guido' in tel)
