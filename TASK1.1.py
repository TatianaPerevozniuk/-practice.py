#1) с помощью функции range (в диапазоне от 0 до 100) и циклов создать список парных значений.
"VARIANT1"
def new_spisok (my_list):
    count = []
    for i in my_list:
        if i % 2 == 0:
            count.append(i)
    return count

l = new_spisok(range(100))

print(l)


"VARIANT2"
# my_list = [i for i in range(100) if i % 2 == 0]
# print(my_list)