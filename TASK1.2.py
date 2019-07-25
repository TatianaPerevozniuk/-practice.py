# 2) создать словарь из произвольного кол-ва элементов, где ключ - страна, значение - столица.
#     создать список из рандомных стран. С помощью оператора in проверить на условие вхождения
# значения со списка в ключи словаря, если истинно, тогда выводим столицу.
dict_countries = {'Ukraine':'Kyiv',
                  'UK':'London',
                  'USA':'Washington',
                  'Russia':'Moscow',
                  'Brasil':'Brasilia'}
list_countries = ['Ukraine','Brasil','Belarus','Hungary','Russia','Moldova']
for c in list_countries:
    if c in dict_countries:
        print(dict_countries[c])