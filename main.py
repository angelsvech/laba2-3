#
#1
# a="1234"
# d=input("код")
# if a == d :
#     print ("подходит")
#     if d.isdigit():
#         print("Введены только цифры")
#     else:
#         print("Введено не только цифры")
# else:
#     print("повторите вход")

#2
# a = int(input("введите номер места"))
# if a in range(1, 56):
#     print("место найдено")
# else:
#     print("место не найдено")
# if a % 2 == 0:
#     print("место внизу")
# else:
#     print("местщ сверху")
# if a>36:
#     print("место сбоку")
# else:
#     print("место не сбоку")

#3
# a=int(input("введите год"))
# if a%4==0 and a%100!=0:
#     print(f"Год {a} высокосный")
# else:
#     print(f"Год {a} не высокосный")

# 4
#a=(input("введите1 цвет"))
#b=(input("введите2 цвет"))
#if a not in ["красный", "синий", "желтый"] or b not in ["красный", "синий", "желтый"]:
#    print ("другой цвет")
#else:
#    if a in ["красный"] and b in ["синий"]:
#        print("фиолетовый")
#    else:
#        if a in ["красный"] and b in ["желтый"]:
#            print("оранжевый")
#        else:
#            if b in ["красный"] and a in ["синий"]:
#               print("фиолетовый")
#            else:
#                if b in ["красный"] and a in ["желтый"]:
#                    print("оранжевый")
#                else:
#                    if a in ["желтый"] and b in ["синий"]:
#                        print("зеленый")
#                    else:
#                        if a in ["синий"] and b in ["желтый"]:
#                            print("зеленый")
#                        else:
#                            print("введите разные цвета")

# лаба 3
#1
#
# while True:
# words = []
# N = int(input("Введите колличество слов:"))
# for y in range(N):
#     w = input(("вводите слова{}: ".format(y+1)))
#     words.append(w)
# x = ' '.join(words)
# print(x)

#2
# q = ""
# while True:
#     word = input("Вводите слова через enter или 'stop' для завершения: ")
#     if word.lower() == 'stop':
#         break
#     q += word + " "
# q = q.strip()
# print("Получилась строка:", q)

#3
#w=input("введите слово")
#if 'ф' in w:
#    print("Ого! Это редкое слово!")
#else:
#    print("Эх, это не очень редкое слово...")

#4
# prav = 0
# net = 0
# while net < 3:
#     n1 = random.randint(1, 100)
#     n2 = random.randint(1, 100)
#     prav = n1+n2
#     otvet = int(input(f"{n1}+{n2}="))
#     if otvet == prav:
#         print("правильно!")
#         prav +=1
#     else:
#         print(" ответ неверный!")
#         net +=1
