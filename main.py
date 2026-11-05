def read_positive_integer() -> int:
    while True:
        user_input = input("Введите число: ")
        try:
            val = int(user_input)
            if val <= 0:
                print("должно быть больше нуля")
            else:
                return val
        except ValueError:
            print("не число")


if __name__ == "__main__":
    print(read_positive_integer())
