"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def get_predict(number: int = 1) -> int:
    """ Разбиваем список от 0 до 100 на диапазоны для уменьшения попыток нахождения загаданного числа

    Args:
        number ([type]): загаданное число. Defaults to 1.

    Returns:
        int: количество попыток
    """

    count = 0
    range = [0, 100]
    while True:
        count += 1
        predict_number = round(np.mean(range))

        if predict_number > number:
            range = [range[0], predict_number]

        elif predict_number < number:
            range = [predict_number, range[1]]
        else:
            break
    return count

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(get_predict)
