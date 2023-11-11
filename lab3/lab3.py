def options() -> None:
    print('Available options:\n1. a + b\n2. a - b\n3. a * b\n4. a / b\n5. factorial(a)\n6. exit')


def add(x: int, y: int) -> int:
    'Функция сложения'
    return x+y


def substract(x: int, y: int) -> int:
    'Функция вычитания'
    return x-y


def multiply(x: int, y: int) -> int:
    'Функция умножения'
    return x*y


def divide(x: int, y: int) -> float:
    'Функция деления'
    return x/y


def factorial(x: int) -> int:
    'Функция нахождения факториала'
    if x == 1:
        return 1
    if x == 2:
        return 2
    return factorial(x-1) * x


commands = {1: add, 2: substract, 3: multiply,
            4: divide, 5: factorial, 6: 'exit'}
while True:
    options()
    operation = int(input('Enter the number of an option: '))
    if 1<=operation<=4:
        a = int(input('Insert a: '))
        b = int(input('Insert b: '))
        print(f'Answer: {commands[operation](a,b)}')
    elif operation == 5:
        a = int(input('Insert a: '))
        print(f'Answer: {commands[5](a)}')
    elif operation == 6:
        print('Alright!')
        break
    else:
        print("There is no such option, please enter again")
    print()
