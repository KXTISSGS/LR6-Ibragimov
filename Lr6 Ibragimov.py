import re


def recalc(letter, a, b, alphabet, m):
    if letter != " ":
        sr = alphabet[(a*(alphabet.index(letter)-b))%m]
    else:
        sr = " "
    return sr
def calc(letter, a, b, alphabet, m):
    if letter != " ":
        sr = alphabet[(a*(alphabet.index(letter))+b)%m]
    else:
        sr = " "
    return sr
with open('run.txt',"r+",encoding='utf-8') as text:

    ntext=''
    for line in text:
        for word in line.split():
            ntext+=word
            ntext+=' '
    alpha = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    spec = " .,:;"
    m = 33
    answer = ''
    if input("Выберите действие: \n 1 - шифровка \n 2 - дешифровка \n")=="1":
        a = int(input("Введите a: "))
        b = int(input("Введите b: "))

        for letter in ntext:
            answer += calc(letter, a, b, alpha, m)
    else:
        a = int(input("Введите обратное число  a по модулю 33: "))
        b = int(input("Введите b: "))
        for letter in ntext:
            answer += recalc(letter, a, b, alpha, m)
    f=open('answ','w')
    f.write(answer)
    f.close()