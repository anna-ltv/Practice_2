#Дан файл с паролями. Провести проверку паролей на соответствие требованиям:
#Больше семи знаков, минимум 2 специальных знака, минимум 2 цифры, минимум 2 буквы.

with open('password.txt') as f:
    textfile = f.read()
textfile = textfile.split('\n')

for i in textfile:
    result = False
    password = i.split(' ')[1]
    email = i.split(' ')[0]
    b = list(password)
    symbols = '!"\'#$%&()*+-,/:;<=>?@[\\]^_{|}~'
    count_numb = [num for num in b if num.isnumeric()]
    count_letters = [lett for lett in b if lett.isalpha()]
    count_symb = [symb for symb in symbols if symb in password]
    if len(password) >= 7:
        if len(count_numb) >= 2:
            if len(count_letters) >= 2:
                if len(count_symb) >= 2:
                    print(email, password, 'Good password for use')
                else:
                    print(email, password, 'Not enought Symbols')
            else:
                print(email, password, 'Not enought Letters')
        else:
            print(email, password, 'Not enought Numbers')
    else:
        print(email, password, 'Too short')