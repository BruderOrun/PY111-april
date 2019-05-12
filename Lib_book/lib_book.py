import os
import shutil
from itertools import count
import re
import subprocess

list_for_analysis = [] #todo Временное хранение списка на разбор и добавление
directory_choice = '/home/bruder/PycharmProjects/PY111-april/Lib_book/the_choice'  #todo  директория хранящая файлы на разбор и добавление
# file_added_books = '/Users/norunov/Documents/python/politech/PY111-april/Lib_book/the_added_books/added_books.txt'  #todo
directory_added_books = '/home/bruder/PycharmProjects/PY111-april/Lib_book/the_added_books' #todo директория хранения файлов бибилиотеки
list_added_books = []  #todo Временное хранение списка бибилиотеки


def view(directory, listt):  #todo  вывод списка библиотеки или списка на разбор
    files = os.listdir(directory)
    files = sorted(files, reverse=True)
    for i in range(len(files)):
        if files[i].endswith('.txt') or files[i].endswith('.doc'):
            listt.append(files[i])
            print(f'{i+1}. {files[i]}')
    return listt


def view_filt(fil):
    for i in range(len(fil)):
        print(f'{i+1}. {fil(list_for_analysis, a)[i]}')



def number_book():
    selected_book_number = int(input('Впишите НОМЕР книги, с которой произвести действие \n'))
    return selected_book_number


def transfer_file_to_lib(book, d_c, d_a_b):  #todo добавление в библиотеку
    directory_file_choice = f'{d_c}/{book}'
    directory_file_added = f'{d_a_b}/{book}'
    if os.path.isfile(directory_file_added) is True:
        print('Такая книга уже есть в биюлиотеке')
    else:
        shutil.move(directory_file_choice, directory_file_added)
    # with open(file_added_books, "a+") as myfile:
    #     if os.path.isfile(directory_file_added) is True:
    #         print('Такая книга уже есть в биюлиотеке')
    #     else:
    #         myfile.write(f'{book} \n')



def read(ft,dir):
    file = f'{dir}/{ft}'
    with open(file, "r") as myfile:
        for line in myfile.readlines():
            print(line)

        # my = myfile.readlines()
        # print(my[4])4
        # for i in myfile:
        #     print(i)
#     print('Ваша библиотека содержит следующие книги')
#     with open(f_a_b, "r") as myfile:
#         for i in myfile:
#             print(i)
#read
#
# def pars_name(f_a_b):
#     a = input('Выберите параметр фильтрации: '
#               'Название книги - 1, ФИО автора - 2, Год издания - 3, Расширение файла - 4 ')
#     b = input('Введите данные для поиска.')
#     with open(f_a_b, "r") as myfile:
#         for i in myfile:
#             a = i.split('_')
#             b = a[2].split('.')
#             book_name = a[0]
#             autor_name = a[1]
#             year_publishing = b[0]
#             file_extension = b[1]
#             if b == book_name or autor_name or year_publishing or file_extension:
#                 print(i)
#             else:
#                 print("Что то пошло не так")
#                 continue
# def vi():
#     view(directory_added_books, list_added_books)
# def vi_0():
#     view(directory_choice, list_for_analysis)
# def t_f_t():
#     transfer_file_to_lib(list_for_analysis[number_book() - 1], directory_choice, directory_added_books)
# def switch_case(case):
#     return "You entered " + {
#     '1' : vi(),
#     '2' : vi_0(),
#     '3' : t_f_t()
#     }.get(case, "an out of range number")
def fil(lstt, a):
    filt = list(filter(lambda x: a in x, lstt))
    return filt

if __name__ == '__main__':

    for i in count():
        num = input("Главное меню, что необходимо сделать ?\n"
                    "1 - Показать список книг в библиотеке\n"
                    "2 - Показать книги 'На добавление'\n"
                    "3 - Добавление в библиотеку'\n"
                    "4 - Почитаем")
        print()

        if num == '1':
            view(directory_added_books, list_added_books)
            print()
            print('Нужно ли отфильтровать список, (y,n)')
            vb = input('Введите (y,n)')
            if vb == 'n':
                continue
            else:
                a = input('Введите данные для фильтрации')
                if fil(list_added_books, a) == []:
                    print(fil(list_added_books, a))
                    print('Совпадений не найдено')
                    print()
                    continue
                else:
                    print(fil(list_added_books, a))

        if num == '2':
            view(directory_choice, list_for_analysis)
            print()
            print('Нужно ли отфильтровать список, (y,n)')
            vb_2 = input('Введите (y,n)')
            if vb_2 == 'n':
                continue
            else:
                a = input('Введите данные для фильтрации')
                fil(list_for_analysis, a)
                print(fil(list_for_analysis, a))
                if fil(list_for_analysis, a) == []:
                    print('Совпадений не найдено')
                    print()
                    continue
        if num == '3':
            view(directory_choice, list_for_analysis)
            print()
            print('Нужно ли отфильтровать список, (y,n)')
            vb_2 = input('Введите (y,n)')
            if vb_2 == 'n':
                continue
            else:
                a = input('Введите данные для фильтрации')
                for i in range(len(fil(list_for_analysis, a))):
                    print(f'{i + 1}. {fil(list_for_analysis, a)[i]}', end='\n')
                if fil(list_for_analysis, a) == []:
                    print('Совпадений не найдено')
                    print()
                    continue
                else:
                    transfer_file_to_lib(fil(list_for_analysis, a)[number_book() - 1], directory_choice, directory_added_books)
        if num == '4':
            view(directory_added_books, list_added_books)
            print()
            print('Нужно ли отфильтровать список, (y,n)')
            vb_2 = input('Введите (y,n)')
            if vb_2 == 'n':
                continue
            else:
                a = input('Введите данные для фильтрации')
                for i in range(len(fil(list_added_books, a))):
                    print(f'{i + 1}. {fil(list_added_books, a)[i]}', end='\n')
                if fil(list_added_books, a) == []:
                    print('Совпадений не найдено')
                    print()
                    continue
                else:
                    read(fil(list_added_books, a)[number_book() - 1], directory_added_books)
                    # transfer_file_to_lib(fil(list_for_analysis, a)[number_book() - 1], directory_choice,
                    #                      directory_added_books)


    # for i in count():
    #     view(directory_added_books, list_added_books)
    #     # view(directory_choice, list_for_analysis)
    #     transfer_file_to_lib(list_for_analysis[number_bo1ok() - 1], directory_choice, directory_added_books)
    #     print(list_added_books)
    #
    #     # pars_name(file_added_books)
    #     # list_of_books_lib(file_added_books)


