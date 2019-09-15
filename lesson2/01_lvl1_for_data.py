names = ['Оля', 'Петя', 'Вася', 'Маша']

is_male = {
  'Оля': False,  # если True, то пол мужской
  'Петя': True,
  'Вася': True,
  'Маша': False,
}

for i in names:
    print(i)
    
for i in names:
    print(i, len(i))

for name, gender in is_male.items():
    print(name, "male" if gender else "female")


groups = [
  ['Вася', 'Маша'],
  ['Оля', 'Петя', 'Гриша'],
]

print(f'Всего групп: {len(groups)}')
for group in groups:
    print(f'В группе {len(group)} ученика.')

for group_order, group in enumerate(groups):
    print(f'В группе {group_order + 1}: {", ".join(group)}')
    
    