from collections import Counter
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'}
]

def get_most_popular_name(list_of_students):
    names = {}
    for name in [student.get('first_name') for student in list_of_students]:
        if name in names.keys():
            names[name] += 1
        else:
            names[name] = 1
    return names

names = get_most_popular_name(students)

for name, count in names.items():
    print(f'{name}: {count}')

students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'}
]

names = get_most_popular_name(students)
print(max(names.items(), key=lambda x: x[1])[0])

school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]

for class_order, student_list in enumerate(school_students):
    print(f"Самое частое имя в классе {class_order + 1}: {max(get_most_popular_name(student_list).items(), key=lambda x: x[1])[0]}")
    
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
def count_gender(item):
    is_male = {
          'Маша': False,
          'Оля': False,
          'Олег': True,
          'Миша': True,
        }
    boys_number = sum(map(lambda x: is_male.get(x.get('first_name')), item))
    return boys_number, len(item) - boys_number

for class_ in school:
    current_gender_numbers = count_gender(class_.get('students'))
    print(f'В классе {class_.get("class")} {current_gender_numbers[1]} девочки и {current_gender_numbers[0]} мальчика.')
          

for class_ in school:
    current_gender_numbers = count_gender(class_.get('students'))
    class_['girls_number'] = current_gender_numbers[0]
    class_['boys_number'] = current_gender_numbers[1]

print(f"Больше всего девочек в классе {max(school, key = lambda x: x.get('girls_number')).get('class')}")
print(f"Больше всего мальчиков в классе {max(school, key = lambda x: x.get('boys_number')).get('class')}")