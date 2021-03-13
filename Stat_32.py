from openpyxl import load_workbook
import pendulum

# file_r = open('ats32.txt', 'r')
# file_w = open('ats32_edited.txt', 'w')
#
# # Вытаскивание из файла только строк с нужной информацией по транковым группам
# for x in file_r:
#     if x.find('      800    ') != -1:
#         file_w.write(x)
#
#     if x.find('      300    ') != -1:
#         file_w.write(x)
#
#     if x.find('      980    ') != -1:
#         file_w.write(x)
#     # Поиск данных для статистики по средам
#     if x.find('     USAGE   SEIZE   ANS     TERM    OUT     SYSTERM') != -1:
#         file_w.write(x)
#         for y in range(12):
#             file_w.write(file_r.readline())
#         # после первого выполнения условия if прекратить поиск, используем break
#         break
#
# file_r.close()
# file_w.close()

# Открытие файла Exel для добавления данных
name_file_exel = ('StatATS32_' + pendulum.today('Europe/Moscow').format('MMYY') + '.xlsx')
book = load_workbook(name_file_exel)
# Так как нумерация страниц начинается с единицы
# Надо ли приводить переменные к целочисленным значениям?!!!!!!!!!!!!!!!!!!


# Поставить защиту от ошибки если не существует нужного листа в книге
try:
    # Выбираем определенную страницу в книге
    # Номер странице в книге равняется сегодняшнему дню
    # sheet = book.worksheets[int(pendulum.today('Europe/Moscow').format('DD')) - 1]
    sheet = book.worksheets[1]

    file_r = open('ats32_edited.txt', 'r')

    # Привер рассположения данных
    # 1 (stroka[13:24:].strip())
    # 2 (stroka[24:35:].strip())
    # 3 (stroka[35:46:].strip())
    # 4 (stroka[46:57:].strip())
    # 5 (stroka[57:68:].strip())
    # 6 (stroka[68:len(stroka):])

    # Строка №1 800
    stroka = file_r.readline()
    # Извлечение нужных данных и присвоение переменным
    ISEIZE_800 = stroka[13:24:].strip()
    IANS_800 = stroka[57:68:].strip()

    # Строка №2 800
    stroka = file_r.readline()
    # Извлечение нужных данных и присвоение переменным
    OATTMPT_800 = stroka[13:24:].strip()
    OVFL_800 = stroka[35:46:].strip()
    OSEIZE_800 = stroka[46:57:].strip()
    OARR_800 = stroka[57:68:].strip()

    # Строка №3 800
    stroka = file_r.readline()
    # Извлечение нужных данных и присвоение переменным
    OANS_800 = stroka[13:24:].strip()
    TOTUSG_800 = stroka[24:35:].strip()
    IANSUSG_800 = stroka[46:57:].strip()
    OANSUSG_800 = stroka[57:68:].strip()

    # Строка №4 800
    stroka = file_r.readline()
    # Извлечение нужных данных и присвоение переменным
    ITRANSZ_800 = stroka[68:len(stroka):].strip()

    # Строка №5 800
    stroka = file_r.readline()
    # Извлечение нужных данных и присвоение переменным
    DBLSZR_800 = stroka[13:24:].strip()
    FCO_800 = stroka[68:len(stroka):].strip()

    # Строка №6 800
    stroka = file_r.readline()
    # Извлечение нужных данных и присвоение переменным
    SBBSY_800 = stroka[13:24:].strip()
    SBNANS_800 = stroka[24:35:].strip()

    # Строка №7 800
    stroka = file_r.readline()
    # Полезных данных нет в 7ой строке

    sheet['C6'] = ISEIZE_800
    sheet['D6'] = OSEIZE_800
    sheet['G6'] = ITRANSZ_800
    sheet['H6'] = IANSUSG_800
    sheet['I6'] = OANSUSG_800
    sheet['J6'] = int(TOTUSG_800) / 100
    sheet['L6'] = IANS_800
    sheet['M6'] = OANS_800
    sheet['O6'] = SBBSY_800
    sheet['P6'] = SBNANS_800
    sheet['Q6'] = OARR_800
    sheet['R6'] = OVFL_800
    sheet['S6'] = DBLSZR_800
    sheet['T6'] = FCO_800
    book.save(name_file_exel)
# _______________________________________________________________________________________

    # Строка №1 300
    stroka = file_r.readline()
    # Извлечение нужных данных и присвоение переменным
    ISEIZE_300 = stroka[13:24:].strip()
    IANS_300 = stroka[57:68:].strip()

    # Строка №2 300
    stroka = file_r.readline()
    # Извлечение нужных данных и присвоение переменным
    OATTMPT_300 = stroka[13:24:].strip()
    OVFL_300 = stroka[35:46:].strip()
    OSEIZE_300 = stroka[46:57:].strip()
    OARR_300 = stroka[57:68:].strip()

    # Строка №3 300
    stroka = file_r.readline()
    # Извлечение нужных данных и присвоение переменным
    OANS_300 = stroka[13:24:].strip()
    TOTUSG_300 = stroka[24:35:].strip()
    IANSUSG_300 = stroka[46:57:].strip()
    OANSUSG_300 = stroka[57:68:].strip()

    # Строка №4 300
    stroka = file_r.readline()
    # Извлечение нужных данных и присвоение переменным
    ITRANSZ_300 = stroka[68:len(stroka):].strip()

    # Строка №5 300
    stroka = file_r.readline()
    # Извлечение нужных данных и присвоение переменным
    DBLSZR_300 = stroka[13:24:].strip()
    FCO_300 = stroka[68:len(stroka):].strip()

    # Строка №6 300
    stroka = file_r.readline()
    # Извлечение нужных данных и присвоение переменным
    SBBSY_300 = stroka[13:24:].strip()
    SBNANS_300 = stroka[24:35:].strip()

    # Строка №7 300
    stroka = file_r.readline()
    # Полезных данных нет в 7ой строке
    sheet['C7'] = ISEIZE_300
    sheet['D7'] = OSEIZE_300
    sheet['G7'] = ITRANSZ_300
    sheet['H7'] = IANSUSG_300
    sheet['I7'] = OANSUSG_300
    sheet['J7'] = int(TOTUSG_300) / 100
    sheet['L7'] = IANS_300
    sheet['M7'] = OANS_300
    sheet['O7'] = SBBSY_300
    sheet['P7'] = SBNANS_300
    sheet['Q7'] = OARR_300
    sheet['R7'] = OVFL_300
    sheet['S7'] = DBLSZR_300
    sheet['T7'] = FCO_300
    book.save(name_file_exel)
# _______________________________________________________________________________________
    # Строка №1 980
    stroka = file_r.readline()
    # Извлечение нужных данных и присвоение переменным
    ISEIZE_980 = stroka[13:24:].strip()
    IANS_980 = stroka[57:68:].strip()

    # Строка №2 980
    stroka = file_r.readline()
    # Извлечение нужных данных и присвоение переменным
    OATTMPT_980 = stroka[13:24:].strip()
    OVFL_980 = stroka[35:46:].strip()
    OSEIZE_980 = stroka[46:57:].strip()
    OARR_980 = stroka[57:68:].strip()

    # Строка №3 980
    stroka = file_r.readline()
    # Извлечение нужных данных и присвоение переменным
    OANS_980 = stroka[13:24:].strip()
    TOTUSG_980 = stroka[24:35:].strip()
    IANSUSG_980 = stroka[46:57:].strip()
    OANSUSG_980 = stroka[57:68:].strip()

    # Строка №4 980
    stroka = file_r.readline()
    # Извлечение нужных данных и присвоение переменным
    ITRANSZ_980 = stroka[68:len(stroka):].strip()

    # Строка №5 980
    stroka = file_r.readline()
    # Извлечение нужных данных и присвоение переменным
    DBLSZR_980 = stroka[13:24:].strip()
    FCO_980 = stroka[68:len(stroka):].strip()

    # Строка №6 980
    stroka = file_r.readline()
    # Извлечение нужных данных и присвоение переменным
    SBBSY_980 = stroka[13:24:].strip()
    SBNANS_980 = stroka[24:35:].strip()

    # Строка №7 980
    stroka = file_r.readline()
    # Полезных данных нет в 7ой строке
    sheet['C8'] = ISEIZE_980
    sheet['D8'] = OSEIZE_980
    sheet['G8'] = ITRANSZ_980
    sheet['H8'] = IANSUSG_980
    sheet['I8'] = OANSUSG_980
    sheet['J8'] = int(TOTUSG_980) / 100
    sheet['L8'] = IANS_980
    sheet['M8'] = OANS_980
    sheet['O8'] = SBBSY_980
    sheet['P8'] = SBNANS_980
    sheet['Q8'] = OARR_980
    sheet['R8'] = OVFL_980
    sheet['S8'] = DBLSZR_980
    sheet['T8'] = FCO_980
    book.save(name_file_exel)

# _______________________________________________________________________________________
    # Заполение вычислительных ячеек
    sheet['C9'] = (int(ISEIZE_800) + int(ISEIZE_300) + int(ISEIZE_980))
    sheet['D9'] = (int(OSEIZE_800) + int(OSEIZE_300) + int(OSEIZE_980))
    sheet['G9'] = (int(ITRANSZ_800) + int(ITRANSZ_300) + int(ITRANSZ_980))
    sheet['H9'] = (int(IANSUSG_800) + int(IANSUSG_300) + int(IANSUSG_980))
    sheet['I9'] = (int(OANSUSG_800) + int(OANSUSG_300) + int(OANSUSG_980))
    sheet['J9'] = (int(TOTUSG_800) / 100 + int(TOTUSG_300) / 100 + int(TOTUSG_980) / 100)
    sheet['E6'] = (int(ISEIZE_800) + int(OSEIZE_800))
    sheet['E7'] = (int(ISEIZE_300) + int(OSEIZE_300))
    sheet['E8'] = (int(ISEIZE_980) + int(OSEIZE_980))
    sheet['N6'] = (int(IANS_800) + int(OANS_800))
    sheet['N7'] = (int(IANS_300) + int(OANS_300))
    sheet['N8'] = (int(IANS_980) + int(OANS_980))
    sheet['U6'] = (int(OARR_800) + int(OVFL_800) + int(DBLSZR_800) + int(FCO_800))
    sheet['U7'] = (int(OARR_300) + int(OVFL_300) + int(DBLSZR_300) + int(FCO_300))
    sheet['U8'] = (int(OARR_980) + int(OVFL_980) + int(DBLSZR_980) + int(FCO_980))


    book.save(name_file_exel)
# _______________________________________________________________________________________
    # Строка №1 для "среды"
    stroka = file_r.readline()
    stroka = file_r.readline()
    # Извлечение нужных данных и присвоение переменным
    TERM = stroka[32:40:].strip()
    sheet['F6'] = TERM
    book.save(name_file_exel)

except IndexError:
    print('Не найдена страница ' + str(pendulum.today('Europe/Moscow').format('DD.MM')) +
          ' в книге ' + name_file_exel)
# except:
#     print('Ошибка при открытии страницы в книге')

book.close()
