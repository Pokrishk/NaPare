list1 = [1, 2, 3, 4, 4, 4, 5, 6, 7, 2]
list2 = [8,9,10]
pustlist = []
kor1 = (1,3,8,9,3)
kor2 = (8,5,3,4,6,8)
def sumlits():
   return sum(list1)
def duble():
    list1.sort()
    for i in list1:
       if i not in pustlist:
           pustlist.append(i)
    return pustlist
def poisk():
        while True:
            try:
                j=int(input("Что хотите найти? "))
                break
            except ValueError:
                print("Нужно число")
        for i in kor1:
            if j in kor1:
                nash=kor1.index(j)
                return nash
                break
            else:
                print("Нет такого элемента")
                break
def udl():
        print("Дан кортеж: ", kor1)
        while True:
            try:
                d=int(input("Что хотите удалить?" ))
                break
            except ValueError:
                print("Нужно число")
        for i in kor1:
         if d in kor1:
            z=kor1.index(d)
            newlist=list(kor1)
            for i in kor1:
                if d==i:
                    newlist.remove(d)
            obrkor=tuple(newlist)
            return obrkor
            break
         else:
            print("Такого значения нет")
            break
def podshet():
    while True:
        try:
            dd=int(input("Какой элемент хотите проверить на повторяемость? "))
            break
        except ValueError:
            print("Нужно число")
        for i in kor1:
         if dd in kor1:
            c = kor1.count(dd)
            return c
            break
         else:
            print("Такого значения нет")
            break
sumlist=sumlits()
print(sumlist)
list1.sort()
print(list1[-1])
double=duble()
print(double)
vmest = list1 + list2
print(vmest)
poiskk=poisk()
print("Он под индексом: ", poiskk)
korall = kor1 + kor2
print(korall)
udal=udl()
print(udal)
skolyk=podshet()
print("Оно повторялось: ", skolyk, " раз.")