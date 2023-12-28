data = [4, -30, 100, -100, 123, 1, 0, -1, -4]

if __name__ == '__main__':
    # С использованием lambda-функции
    result = sorted(data, key=lambda x: abs(x), reverse=True)
    print(result)

    # Без использования lambda-функции
    result_without_lambda = sorted(data, key=abs, reverse=True)
    print(result_without_lambda)
