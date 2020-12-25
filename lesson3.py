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
        pass

    #lesson 3
    #task c зирочкой 3

    palindrome = input('Введите слово полиндром:').lower()
    if not palindrome.isalpha():
        print("Слово должно состоять только из букв")
    elif palindrome == palindrome[::-1]:
         print("Ваше слово палиндром")
    else:
        print('Ваше слово не палиндром, выберите другое слово')

    # lesson 3
    # задание со звезочкой 1

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

    # lesson 3
    # задание со звезочкой 1
