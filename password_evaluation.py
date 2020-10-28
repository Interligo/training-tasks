''' Программа оценивает сложность пароля. Просит ввести пароль и выводит на экран сообщение о его сложности. 
Сложным считается пароль, состоящий как минимум из 8-ми символов, включая цифры и алфавитные символы разного регистра. '''


def password_evaluation():
    user_password = input('Введите пароль: ')
 
    password_requirements = {'digits': 0, 'capital letters': 0}
 
    if len(user_password) >= 8 and user_password.isalnum():
        for symbol in user_password:
            if symbol.isdigit():
                password_requirements['digits'] += 1
            elif symbol.isupper():
                password_requirements['capital letters'] += 1
 
        if password_requirements['digits'] < 1:
            return 'Пароль должен содержать цифры.'         
        elif password_requirements['capital letters'] < 1:
            return 'Пароль должен содержать буквы в верхнем регистре.'        
        else:
            return 'Пароль отвечает всем требованиям безопасности.'
    else:
        return 'Пароль должен состоять, как минимум, из 8-ми алфавитных символов.'


if __name__ == '__main__':
    print(password_evaluation())
    
