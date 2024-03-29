balance = 0.0
history = []


def incomes(balance_f):
    add_sum = float(input('Введите сумму для пополнения: '))
    return balance_f + add_sum


def expenses(balance_f, history_f):
    price = float(input('Введите сумму покупки: '))
    if price > balance_f:
        print('У вас не хватает средств!')
    else:
        product = input('Что вы хотите купить? ')
        balance_f = balance_f - price
        history_f.append({'product': product, 'price': price})

    return balance_f, history_f


def view_history(history_f):
    print('Ваша история покупок:')
    for element in history:
        print(f'Товар: {element["product"]}; цена: {element["price"]}')


while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')

    choice = input('Выберите пункт меню: ')
    if choice == '1':
        balance = incomes(balance)
    elif choice == '2':
        balance, history = expenses(balance, history)
    elif choice == '3':
        view_history(history)
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')