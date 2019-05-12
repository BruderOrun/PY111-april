
f = '/home/bruder/PycharmProjects/PY111-april/Lib_book/the_added_books/1ри мушкетера_Александр Дюма_1985 — копия.txt'

def read(f):

    with open(f, "r") as myfile:
        for line in myfile.readlines():
            print(line)
read(f)
# def y_b():
#     vb = input('Введите (y,n)')
#     a = input('Введите данные для фильтрации')
#     return vb, a
#
# y_b()[1]
#
# y_b()[1]
# lst = ['1Ври мушкетера_Александр Дюма_1985 — копия.txt']
# a = input('aaa')
# def fil(lstt, a):
#     filt = list(filter(lambda x: a in x, lstt))
#     return filt
#
# print(fil(lst, a))

# def zero():
#     return "zero"
# def one():
#     return "one"
# def two():
#     return "two"
# switcher = {
#         0: zero,
#         1: one,
#         2: two
#     }
# def numbers_to_strings(argument):
#     # Get the function from switcher dictionary
#     func = switcher.get(argument, "nothing")
#     # Execute the function
#     return func()
#
# print(numbers_to_strings(2))
#
#
#
# def switch_case(case):
#     return  {
#     '1' : "vi",
#     '2' : "vi_0",
#     '3' : "t_f_t()"
#     }.get(case, "an out of range number")
#
# print(switch_case(str(2)))
# book = "Три мушкетера_Александр Дюма_2017.txt"
# def pars_name(book):
#     a = book.split('_')
#     b = a[2].split('.')
#     book_name = a[0]
#     autor_name = a[1]
#     year_publishing = b[0]
#     file_extension = b[1]
#     return book_name, autor_name, year_publishing, file_extension
#
# print(pars_name(book)[0])
# print(pars_name(book)[1])
# print(pars_name(book)[2])
# print(pars_name(book)[3])
# print('_'.join(pars_name(book)[::-1]))
#
#
#
# def name_preparation(book, d_c, d_a_b):
#     book_name = []
#     directory_file_choice = f'{d_c}/{book}'
#     print(book)
#     a = input('Если Вас устраивает наименование книги в указанном виде, нажмите 1 если нет 2')
#     for i in range(1):
#         if a == 1:
#             return  directory_file_choice
#         else:
#             book_name[0] = input('Введите название книги')
#             book_name[1] = input('Введите Фамилию и автора книги, через пробел')
#             book_name[2] = input('Напишите год издания в формате гггг' )
#             book_name[3] = input('Укажите расширение')
#         print('_'.join(book_name))
#         b = input('Если формат соответствует "Три мушкетера_Александр Дюма_2017.txt", нажмите 1, если нет 2')
#         if b != 1:
#             continue
#
# listt = (filter(lambda x: x.endswith('.txt'), files))
