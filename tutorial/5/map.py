#map関数 map(function,list)
original_list=list(range(10))
mapped_list=map(lambda x:x**2,original_list)
print(list(mapped_list))
