import random


def attempts_word(n):
    if n == 1:
        return "попытку"
    elif n <= 4:
        return "попытки"
    else:
        return "попыток"


def play():
    try:
        limit = int(input("До какого числа играем? "))
    except ValueError:
        limit = 10
        print("Это не число, играем до 10")
    if limit < 1:
        limit = 10
        print("Число должно быть больше нуля, играем до 10")
    secret = random.randint(1, limit)
    guess = 0
    attempts = 0
    max_attempts = 5

    print(f"Я загадал число от 1 до {limit}")

    while guess != secret and attempts < max_attempts:
        try:
            guess = int(input("Твоя догадка: "))
            attempts = attempts + 1
            if guess == secret:
                word = attempts_word(attempts)
                print(f"Угадал за {attempts} {word}")
            elif secret > guess:
                print("Загаданное число больше")
            else:
                print("Загаданное число меньше")
        except ValueError:
            print("Нужно ввести число")

    if guess != secret:
        print(f"Попытки закончились. Я загадал {secret}")


play()