''' Программа выводит на экран числа от 1 до 100 включительно, каждое число с новой строки. 
Если число кратно трём, то вместо этого числа программа выводит слово "zip".
Если чисто кратно пяти, то вместо этого числа выводится слово "zap".
Если число кратно пятнадцати, то вместо этого числа выводится слово "zip-zap". '''


for digit in range(1, 101):
    if digit % 3 == 0:
      print('zip')
    elif digit % 5 == 0:
      print('zap')
    elif digit % 15 == 0:
      print('zip-zap')
    else:
      print(digit)
      