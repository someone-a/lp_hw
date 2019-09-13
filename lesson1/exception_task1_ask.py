# Из задачи не очень понятно кто у кого что спрашивает. 
# Вроде как изначально у пользователя спрашивают, а потом пользователь спрашивает

dict_of_questions = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую"}

def ask_user():
    while True:
        try:
            question = input('Как дела? ')
            if question == 'Хорошо!':
                break
            if question in list(dict_of_questions.keys()):
                print(dict_of_questions[question])
        except KeyboardInterrupt:
            print("Пока!")
            break
ask_user()