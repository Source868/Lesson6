my_dict = {'Vika': 1989, 'Denis': 1987, 'Anna': 1996}
print(my_dict)
print (my_dict['Denis'])
print (my_dict.get('Nik', 'Имя не найдено'))
my_dict.update({'Ivan': 1964, 'Marina': 2001})
my_dict.pop('Ivan')
print(my_dict)

my_set = {23, 55, 13, 88, 23, 55, 13, 88, 'Apple'}
my_set.update({'Source', 65})
print(my_set)
my_set.discard('Apple')
print(my_set)


