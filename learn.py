number = input('Введите число рублей от 1 до 999999\n')
res = list(number)
check_len = len(res)
out = []
if len(res) > 6:
    print('Слишком большое число')
while len(res) < 6:
    zero = ['0']
    res = zero + res    
if res[0] != '0':
    if res[0] == '9': b0 = 'девятьсот'
    if res[0] == '8': b0 = 'восемьсот'
    if res[0] == '7': b0 = 'семьсот'
    if res[0] == '6': b0 = 'шестьсот'
    if res[0] == '5': b0 = 'пятьсот'
    if res[0] == '4': b0 = 'четыреста'
    if res[0] == '3': b0 = 'триста'
    if res[0] == '2': b0 = 'двести'
    if res[0] == '1': b0 = 'сто'
    out.append(b0)
if res[1] != '0':
    if res[1] == '9': b1 = 'девяносто'
    if res[1] == '8': b1 = 'восемьдесят'
    if res[1] == '7': b1 = 'семьдесят'
    if res[1] == '6': b1 = 'шестьдесят'
    if res[1] == '5': b1 = 'пятьдесят'
    if res[1] == '4': b1 = 'сорок'
    if res[1] == '3': b1 = 'тридцать'
    if res[1] == '2': b1 = 'двадцать'
    if res[1] == '1':
        if res[2] == '9': b1 = 'девятнадцать'
        if res[2] == '8': b1 = 'восемнадцать'
        if res[2] == '7': b1 = 'семнадцать'
        if res[2] == '6': b1 = 'шестнадцать'
        if res[2] == '5': b1 = 'пятнадцать'
        if res[2] == '4': b1 = 'четырнадцать'
        if res[2] == '3': b1 = 'тринадцать'
        if res[2] == '2': b1 = 'двенадцать'
        if res[2] == '1': b1 = 'одиннадцать'
        if res[2] == '0': b1 = 'десять'
    out.append(b1)
if res[2] != '0':
    if res[1] != '1':
        if res[2] == '9': b2 = 'девять'
        if res[2] == '8': b2 = 'восемь'
        if res[2] == '7': b2 = 'семь'
        if res[2] == '6': b2 = 'шесть'
        if res[2] == '5': b2 = 'пять'
        if res[2] == '4': b2 = 'четыре'
        if res[2] == '3': b2 = 'три'
        if res[2] == '2': b2 = 'две'
        if res[2] == '1': b2 = 'одна'
        out.append(b2)
if check_len > 3:
    out.append('тысяч')
if res[2] != '0':
    if res[1] != '1':
        if res[2] == '4':
            out.pop()
            out.append('тысячи') 
        if res[2] == '3':
            out.pop()
            out.append('тысячи')
        if res[2] == '2':
            out.pop()
            out.append('тысячи')
        if res[2] == '1':
            out.pop()
            out.append('тысяча')
if res[3] != '0':
    if res[3] == '9': b3 = 'девятьсот'
    if res[3] == '8': b3 = 'восемьсот'
    if res[3] == '7': b3 = 'семьсот'
    if res[3] == '6': b3 = 'шестьсот'
    if res[3] == '5': b3 = 'пятьсот'
    if res[3] == '4': b3 = 'четыреста'
    if res[3] == '3': b3 = 'триста'
    if res[3] == '2': b3 = 'двести'
    if res[3] == '1': b3 = 'сто'
    out.append(b3)
if res[4] != '0':
    if res[4] == '9': b4 = 'девяносто'
    if res[4] == '8': b4 = 'восемьдесят'
    if res[4] == '7': b4 = 'семьдесят'
    if res[4] == '6': b4 = 'шестьдесят'
    if res[4] == '5': b4 = 'пятьдесят'
    if res[4] == '4': b4 = 'сорок'
    if res[4] == '3': b4 = 'тридцать'
    if res[4] == '2': b4 = 'двадцать'
    if res[4] == '1':
        if res[5] == '9': b4 = 'девятнадцать'
        if res[5] == '8': b4 = 'восемнадцать'
        if res[5] == '7': b4 = 'семнадцать'
        if res[5] == '6': b4 = 'шестнадцать'
        if res[5] == '5': b4 = 'пятнадцать'
        if res[5] == '4': b4 = 'четырнадцать'
        if res[5] == '3': b4 = 'тринадцать'
        if res[5] == '2': b4 = 'двенадцать'
        if res[5] == '1': b4 = 'одиннадцать'
        if res[5] == '0': b4 = 'десять'
    out.append(b4)
if res[5] != '0':
    if res[4] != '1':
        if res[5] == '9': b5 = 'девять'
        if res[5] == '8': b5 = 'восемь'
        if res[5] == '7': b5 = 'семь'
        if res[5] == '6': b5 = 'шесть'
        if res[5] == '5': b5 = 'пять'
        if res[5] == '4': b5 = 'четыре'
        if res[5] == '3': b5 = 'три'
        if res[5] == '2': b5 = 'два'
        if res[5] == '1': b5 = 'один'
        out.append(b5)
out.append('рублей')
if res[5] != '0':
    if res[4] != '1':
        if res[5] == '4':
            out.pop()
            out.append('рубля') 
        if res[5] == '3':
            out.pop()
            out.append('рубля')
        if res[5] == '2':
            out.pop()
            out.append('рубля')
        if res[5] == '1':
            out.pop()
            out.append('рубль')
print('Вы ввели:', str.capitalize(' '.join(out)))