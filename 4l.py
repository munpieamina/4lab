def del3():
    a=int(input('Введите число '))
    if a%3==0:
        print(a, 'делится на 3')
    else:
        print(a, 'не делится на 3')
def del100():
    b=input('Введите число ')
    try:
        res=100/int(b)
        print(100, '/', b, '=', res)
    except ValueError:
        print('ОШИБКА! вы ввели не число')
    except ZeroDivisionError:
        print('ОШИБКА! деление на 0')
def magic():
    dat=input('Введите дату в формате дд.мм.гггг ')
    dat=dat.split(sep='.')
    g=dat[2]
    if int(dat[0])*int(dat[1])==int(g[2:4]):
        print('дата магическая')
    else:
        print('дата не магическая((')
def bilet():
    ns=input('Введите номер билета(с четным кол-вом цифр) ')
    if len(ns)%2!=0:
        print('нечетный номер билета')
    else:
        p=len(ns)//2
        n1=ns[:p]
        n2=ns[p:]
        s1=0
        s2=0
        for i in range(p):
            s1=int(n1[i])+s1
            s2=int(n2[i])+s2
        if s1==s2:
            print('Ваш номер билета счастливый!^^')
        else:
            print('Ваш номер билета НЕсчастливый((')
del100()