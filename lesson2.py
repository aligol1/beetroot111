if __name__ == '__main__':
    #lesson 3
    #task 1 String manipulation

    s = 'dictionary'
    if len(s) >= 2:
        print(s[0: 2] + s[-2:])
    else:
        print("Error. Please write more then 3 letters")

        # lesson 3
        # task 2 the valid phone number program.
    phone = "0959999999"
    if phone.isdigit() and len(phone) == 10:
            print("красивый номер")
    else:
            print("введены некорректные данные")

    #lesson 3
        #task 3 The name check.
    name1 = input('Введите имя:').lower()
    if name1 == "игорь":
            print("Спасибо,"+name1.title())
    else:
        print("выбери другое имя")

