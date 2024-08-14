#            ПЕРВЫЙ+
# a = int(input("ведите число: "))
# if a / 2 == 0:
#     print("число НЕ четное ")
# elif a / 2 != 0:
#     print("число  четное ")

#           ВТОРОЙ+


# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# a = [a,b,c,d,]
# b = min(a)
# print(b)

#                   ТРЕТИЙ+

# a = input("ведите чтото")
# b = a[:: - 1]
# if a == b:
#     print("слова палин четатам" )
# else:
#     print("да норм число ")    

#                  ЧЕТЫРИ+

# n = int(input("пиши число"))
# for a in range(1,n):
#     f = 0
#     f = f + 1
#     b = n + f
#     n = b
#     print(b)
#                ПЯТЬ-

# n = int(input("вшап")) 

# for a in range(0 , n):
#     g = g + 1
#     f = f + 1

#                     ШЕСТЬ+
# a = int(input("ведите первое число"))
# b = int(input("ведите второй число"))
# c = int(input("ведите третие число"))
# d = int(input("ведите четвертый число"))
# g = [a,b,c,d,]
# g.sort()
# print(g)


#                          СЕМЬ
# p = int(input("веди число"))
# primes = []

# for num in range(2, p + 1):
#     for i in range(2, num):
#         if num % i == 0:
#             break
#     else:
#         primes.append(num)

# print(primes)


#                           ВОСЕМ+
# a = input("пиши слово")
# b = len(a)
# print(b)


#                         деведть+

# a = input("ведите первое число")
# b = input("ведите второй число")
# c = input("ведите третие число")
# d = input("ведите четвертый число")
# g = [a,b,c,d,]
# g = g[:: -1]
# print(g)

#                       ДЕСЕТЬ

# a = input("ведите первое число")
# b = input("ведите второй число")
# c = input("ведите третие число")
# d = input("ведите четвертый число")
# g = [a,b,c,d,]
# print(f"ваш список до изменения{g}")

# g = set([a,b,c,d,])
# print(f"ваш список после изменения{g}")

#                         ОДИНАЦАТЬ


# a = input("ведите первое число")
# b = input("ведите второй число")
# c = input("ведите третие число(второй маси)")
# d = input("ведите четвертый число(второй маси)")
# g = [a,b,]
# h = [c,d,]

# ob = set(g).intersection(h)
# print(ob)



#                         двенацать 

# n = int(input("пиши число"))
# a = 0
# while a <= (n - 1):
#     a = a + 1
#     print(a) 
#                           тринацать


# n = int(input("пиши число"))
# a = 0
# h = 0
# while a <= (n - 1):
#     a = a + 1
#     h = a + h
#     print(a) 
# print(h)    
#                        ЧЕТЫРНАЦАТЬ
# password = "password"
# password = input("ведите пароль: ")
# while password != "password":
#     password = input("ведите пароль: ")
    
# print(f"пароль верный ваш пароль: {password}")

#                      ПЯТНАЦАТЬ

# a = 12
# h =[]
# while a != 0:
#     a = int(input("ведите чило: "))
#     h.append(a)
#     print(h)
# f = max(h)
# print(f"наиболшое число из веденых это {f}")    

#                       шестнацать
# class person:
#     def __init__(self,name,age): 
#         self.age = age
#         self.name = name
#     def intro(name,age): 
#         print(f"завут :{name} возраст: {age}")
# person.intro("dima", 19)

#                            СЕМНАДЦАТЬ

# class rectongle:
#     def __init__(self,width,hight):
#         self.width = width
#         self.hight = high
#     def perimetr(width,hight):
#         plosh = width *hight    
#         pirim = 2 * (width + hight)
#         print(f"пиримитр по вашим условиям {pirim}  а плошадь {plosh}")
# rectongle.perimetr(5,3)        

#                           ВОСЕМНАДЦАТЬ

# class student:
#     def __init__(self,name , grades):
#         self.name = name
#         self.grades = grades

# class graduates_S(student):
#     def __init__(self, name, grades, tittle):
#         super().__init__(name, grades) 
#         self,tittle = tittle 
#     def viv (name,grades,tittle):
#         print(f"имя студента: {name}  его град: {grades}  его титул: {tittle}")    

# graduates_S.viv("dime", "imba", "karolmira")

#                      ДЕВЕТНАЦАТЬ

# value = [1,1,1,3,4,5,6,787,768,5,3,2,1]

# for i in value:
#     if i <= 3:
#         print(i)
#     else:
#         pass     

#                   ДВАЦАТЬ

# a = [1,1,1,3,4,5,6,787,768,5,3,2,1]
# b = [1,32,435,25,345,42,23,12,1,2,3,4,5,6,7,9,0,]

# d = set(a + b)
# print(d)

#                 ДВАЦАТЬ ОДИН

# b = [1,32,435,25,345,42,23,12,1,2,3,4,5,6,7,9,0,]

# b.sort()
# print(b)


#                     не доделал
# my_di = {"d",2,3,4,623,200,34,"wsfd",324}

# for i in my_di:
#     d = 0
#     if i >= d:
#         print("dfgd")
#     else :
#         pass

#     d = i