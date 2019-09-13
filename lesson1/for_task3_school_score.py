list_of_classes = [
                    {'school_class': '4a', 'scores': [3,4,4,5,2]},
                    {'school_class': '4b', 'scores': [1,1,1,1,1]},
                    {'school_class': '4c', 'scores': [5,4,2,2,2]},
                    {'school_class': '4d', 'scores': [5,5,5,5,3]}
                  ]

whole_school = []
for i in list_of_classes:
    class_name = i.get('school_class')
    scores = i.get('scores') 
    print(f'avg {class_name} score is {sum(scores) / len(scores)}')
    whole_school += scores

print(f'avg school score is {sum(whole_school) / len(whole_school)}')