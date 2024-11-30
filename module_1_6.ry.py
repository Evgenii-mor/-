my_dict={'Евгений': 1998 , 'Anton':1987 , "Nikita":2003}
print(my_dict)
print(my_dict['Anton'])
my_dict.update({'Ivan':2019, 'Anna':2003 })
print(my_dict)
del my_dict['Anton']
a = my_dict.pop('Nikita')
print(my_dict)
print(a)
my_set={9,6,5,7,4,5,7,9,"Anton"}
print(my_set)
my_set.add(614)
my_set.add('Anna')
print((my_set))
my_set.remove('Anna')
print(my_set)
