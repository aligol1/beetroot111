if __name__ == '__main__':
        #lesson 3
        #task c зирочкой 3

        palindrome = input('Введите слово полиндром:').lower()
        if not palindrome.isalpha():
                print("Слово должно состоять только из букв")
        elif palindrome == palindrome[::-1]:
                print("Ваше слово палиндром")
        else:
                print("Ваше слово не палиндром, выберите другое слово")





