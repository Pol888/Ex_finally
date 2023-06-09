from MyExceptions import LessDataError, MoreDataError, NameError, DateError, GenderError, TelError
import re

def main():

    data_input = input("Введите ФИО(с большой буквы), дату рождения(dd.mm.yyyy), пол(f or m) и телефон(4566665455) "
                       "в произвольном порядке через пробел.\n\n").split()
    #data_input = '89994568883 Kemidovich Pavel Anatolievich 23.08.1988 m'.split()
    try:
        if len(data_input) > 6:
            raise MoreDataError
        elif len(data_input) < 6:
            raise LessDataError
        else:
            names = r"^[A-Z][a-z]{0,}$"
            date = r"^\d{2}\.\d{2}\.\d{4}$"
            gender = r'^[f m]$'
            tel = r"[0-9]{4,22}"
            count_Name = [0, []]
            c_date = 0
            c_gender = 0
            c_tel = 0
            for i in data_input:
                if re.search(names, i):
                    count_Name[0] += 1
                    count_Name[1].append(i)
                elif re.search(date, i):
                    c_date += 1
                elif re.search(gender, i):
                    c_gender += 1
                elif re.search(tel, i):
                    c_tel += 1


            if count_Name[0] < 3:
                raise NameError
            elif c_date != 1:
                raise DateError
            elif c_gender != 1:
                raise GenderError
            elif c_tel != 1:
                raise TelError
            elif count_Name[0] == 3 and c_date == 1 and c_gender == 1 and c_tel == 1:
                with open(count_Name[1][0] + '.txt', 'a', encoding='utf-8') as file_append:
                    file_append.write(' '.join(data_input) + '\n')

                with open(input('Введите имя файла для чтения\n'), "r", encoding='utf-8') as file_read:
                    print(file_read.readline())


    except MoreDataError as e:
        print('Слишком много данных')
    except LessDataError as e:
        print('Слишком мало данных')
    except NameError as e:
        print('Некорректно введены данные о имени, фамилии или отчестве')
    except DateError as e:
        print('Некорректно введены данные даты')
    except GenderError as e:
        print('Некорректно введены данные о половом признаке')
    except TelError as e:
        print('Некорректно введены данные о номере телефона')
    except FileNotFoundError as e:
        print('файл не существует')





if __name__ == '__main__':
    main()