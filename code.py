import numpy as np

def game_core_v2(number):
    a = 0
    count = 0
    b = 100
    predict = 0
    while number != predict:
        count += 1
        predict = (a + b) // 2
        if number > predict:
            a = predict + 1
        elif number < predict:
            b = predict - 1

    return count


def score_game():
    count_ls = []
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core_v2(number))
    score = int(np.mean(count_ls))
    print(f"Мой алгоритм угадывает число в среднем за {score} попыток")
    return score


score_game()