import sys

def get_coefficient(str):
    while True:
        try:
            coefficient = float(input(str))
            return coefficient
        except ValueError:
            print("Ошибка: введите корректное значение.")

def second_determination(t):
    if t > 0:
        x1 = t ** 0.5
        x2 =  -(t ** 0.5)
        return x1, x2
    elif t == 0:
        return 0
    

def first_determination(a, b, c):
    D = b**2 - 4*a*c
    if D > 0:
        t1 = (-b + D**0.5) / (2*a)
        t2 = (-b - D**0.5) / (2*a)  
        if t1 >= 0 and t2 >= 0:
            return second_determination(t1), second_determination(t2)
        elif t1 < 0:
            return second_determination(t2)
        elif t2 < 0:
            return second_determination(t1)
        else:
            return None
    elif D == 0:
        t = -b / (2*a)
        return second_determination(t),
    else:
        return None

def main():
    if len(sys.argv) == 4:
        try:
            a = float(sys.argv[1])
            b = float(sys.argv[2])
            c = float(sys.argv[3])
        except ValueError:
            print("Ошибка: коэффициенты должны быть числами.")
            return
    else:
        a = get_coefficient("Введите коэффициент A: ")
        b = get_coefficient("Введите коэффициент B: ")
        c = get_coefficient("Введите коэффициент C: ")

    solution = first_determination(a, b, c)

    if solution:
        print("Корни уравнения:", solution)
    else:
        print("Уравнение не имеет действительных корней.")

if __name__ == "__main__":
    main()
