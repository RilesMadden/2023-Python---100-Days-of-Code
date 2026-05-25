numbers = [1,2,3]
new_list = [n+1 for n in numbers]
print(new_list)

num_list = [n*2 for n in range(1,5)]
print(num_list)

name_list = ['Alex', 'Beth', 'Caroline', 'David', 'Eleanor', 'Freddie']
short_names = [name for name in name_list if len(name)<5]
long_names = [name.upper() for name in name_list if len(name)>=5]
print(short_names)
print(long_names)