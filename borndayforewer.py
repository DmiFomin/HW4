def ask_question(text_question, true_answer):
    answer = input(text_question)
    while answer != true_answer:
        print("Не верно")
        answer = input(text_question)
    print('Верно')

ask_question('Ввведите год рождения А.С.Пушкина: ', '1799')
ask_question('Ввведите день рождения А.С.Пушкина: ', '26')