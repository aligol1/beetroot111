# lesson 3
    # задание со звезочкой 1
def subtraction(args):
    pass


if __name__ == '__main__':
    phonenumber = input("Введите номер телефона: ")
    phonenumber = phonenumber.lstrip("+38")
    phonenumber = phonenumber.replace(" ", "")
    phonenumber = phonenumber.replace("-", "")

    print(phonenumber)
    if phonenumber.isdigit():
        if len(phonenumber) <= 9:
            print("Мало Цифр")
        elif len(phonenumber) >= 11:
            print("Много цифр")
        else:
            print("Спасибо.Номер принят")
    else:
        print("Телефон должен состоять из цифр")