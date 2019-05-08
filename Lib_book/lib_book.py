import os
import shutil
from itertools import count
import re
import subprocess

list_for_analysis = [] #todo Временное хранение списка на разбор и добавление
directory_choice = '/Users/norunov/Documents/python/politech/PY111-april/Lib_book/the_choice'  #todo  директория хранящая файлы на разбор и добавление
# file_added_books = '/Users/norunov/Documents/python/politech/PY111-april/Lib_book/the_added_books/added_books.txt'  #todo
directory_added_books = '/Users/norunov/Documents/python/politech/PY111-april/Lib_book/the_added_books' #todo директория хранения файлов бибилиотеки
list_added_books = []  #todo Временное хранение списка бибилиотеки

def view(directory, listt):  #todo  вывод списка библиотеки или списка на разбор
    files = os.listdir(directory)
    files = sorted(files, reverse=True)
    for i in range(len(files)):
        if files[i].endswith('.txt') or files[i].endswith('.doc'):
            listt.append(files[i])
            print(f'{i+1}. {files[i]}')
    return listt


def number_book():
    selected_book_number = int(input('Впишите НОМЕР книги. Для добавления в библиотеку \n'))
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



# def list_of_books_lib(f_a_b):
#     print('Ваша библиотека содержит следующие книги')
#     with open(f_a_b, "r") as myfile:
#         for i in myfile:
#             print(i)
#
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


if __name__ == '__main__':

    for i in count():
        num = input("Главное меню, что необходимо сделать ?\n"
                    "1 - Показать список книг в библиотеке\n"
                    "2 - Показать книги 'На добавление'\n"
                    "3 - Добавление в библиотеку"
                    "4 - Почитаем")
        print()

        if num == '1':
            view(directory_added_books, list_added_books)
            print()
            print('Нужно ли отфильтровать список, (Y,N)')
            vb = input('Введите (Y,N)')
            if vb == 'N':
                continue
            else:
                a = input('Введите данные для фильтрации')
                pass

        if num == '2':
            view(directory_choice, list_for_analysis)
            print()
            print('Нужно ли отфильтровать список, (Y,N)')
            vb_2 = input('Введите (Y,N)')
            if vb_2 == 'N':
                continue
            else:
                pass
        if num == '3':
            view(directory_choice, list_for_analysis)
            transfer_file_to_lib(list_for_analysis[number_book() - 1], directory_choice, directory_added_books)
            print()

    # for i in count():
    #     view(directory_added_books, list_added_books)
    #     # view(directory_choice, list_for_analysis)
    #     transfer_file_to_lib(list_for_analysis[number_bo1ok() - 1], directory_choice, directory_added_books)
    #     print(list_added_books)
    #
    #     # pars_name(file_added_books)
    #     # list_of_books_lib(file_added_books)


