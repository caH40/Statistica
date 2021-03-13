
file_r = open('ats33.txt', 'r')
file_w = open('ats33_edited.txt', 'w')


for x in file_r:
    if x.find('      200    ') != -1:
        file_w.write(x)

    if x.find('      803    ') != -1:
        file_w.write(x)

    if x.find('      800    ') != -1:
        file_w.write(x)

file_r.close()
file_w.close()

file_r = open('ats33_edited.txt', 'r')
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
ISEIZE = stroka[13:24:].strip()
IANS = stroka[57:68:].strip()

# Строка №2 800
stroka = file_r.readline()
# Извлечение нужных данных и присвоение переменным
OATTMPT = stroka[13:24:].strip()
OVFL = stroka[35:46:].strip()
OSEIZE = stroka[46:57:].strip()
OARR = stroka[57:68:].strip()

# Строка №3 800
stroka = file_r.readline()
# Извлечение нужных данных и присвоение переменным
OANS = stroka[13:24:].strip()
TOTUSG = stroka[24:35:].strip()
IANSUSG = stroka[46:57:].strip()
OANSUSG = stroka[57:68:].strip()

# Строка №4 800
stroka = file_r.readline()
# Извлечение нужных данных и присвоение переменным
ITRANSZ = stroka[68:len(stroka):].strip()

# Строка №5 800
stroka = file_r.readline()
# Извлечение нужных данных и присвоение переменным
DBLSZR = stroka[13:24:].strip()
FCO = stroka[68:len(stroka):].strip()

# Строка №6 800
stroka = file_r.readline()
# Извлечение нужных данных и присвоение переменным
SBBSY = stroka[13:24:].strip()
SBNANS = stroka[24:35:].strip()

# Строка №7 800
stroka = file_r.readline()
# Полезных данных нет в 7ой строке
print(ISEIZE,IANS,OATTMPT,OVFL,OSEIZE,OARR,OANS,TOTUSG,IANSUSG,OANSUSG,ITRANSZ,DBLSZR,FCO,SBBSY,SBNANS)

# Строка №1 300
stroka = file_r.readline()
# Извлечение нужных данных и присвоение переменным
ISEIZE = stroka[13:24:].strip()
IANS = stroka[57:68:].strip()

# Строка №2 300
stroka = file_r.readline()
# Извлечение нужных данных и присвоение переменным
OATTMPT = stroka[13:24:].strip()
OVFL = stroka[35:46:].strip()
OSEIZE = stroka[46:57:].strip()
OARR = stroka[57:68:].strip()

# Строка №3 300
stroka = file_r.readline()
# Извлечение нужных данных и присвоение переменным
OANS = stroka[13:24:].strip()
TOTUSG = stroka[24:35:].strip()
IANSUSG = stroka[46:57:].strip()
OANSUSG = stroka[57:68:].strip()

# Строка №4 300
stroka = file_r.readline()
# Извлечение нужных данных и присвоение переменным
ITRANSZ = stroka[68:len(stroka):].strip()

# Строка №5 300
stroka = file_r.readline()
# Извлечение нужных данных и присвоение переменным
DBLSZR = stroka[13:24:].strip()
FCO = stroka[68:len(stroka):].strip()

# Строка №6 300
stroka = file_r.readline()
# Извлечение нужных данных и присвоение переменным
SBBSY = stroka[13:24:].strip()
SBNANS = stroka[24:35:].strip()

# Строка №7 300
stroka = file_r.readline()
# Полезных данных нет в 7ой строке
print(ISEIZE,IANS,OATTMPT,OVFL,OSEIZE,OARR,OANS,TOTUSG,IANSUSG,OANSUSG,ITRANSZ,DBLSZR,FCO,SBBSY,SBNANS)

# Строка №1 980
stroka = file_r.readline()
# Извлечение нужных данных и присвоение переменным
ISEIZE = stroka[13:24:].strip()
IANS = stroka[57:68:].strip()

# Строка №2 980
stroka = file_r.readline()
# Извлечение нужных данных и присвоение переменным
OATTMPT = stroka[13:24:].strip()
OVFL = stroka[35:46:].strip()
OSEIZE = stroka[46:57:].strip()
OARR = stroka[57:68:].strip()

# Строка №3 980
stroka = file_r.readline()
# Извлечение нужных данных и присвоение переменным
OANS = stroka[13:24:].strip()
TOTUSG = stroka[24:35:].strip()
IANSUSG = stroka[46:57:].strip()
OANSUSG = stroka[57:68:].strip()

# Строка №4 980
stroka = file_r.readline()
# Извлечение нужных данных и присвоение переменным
ITRANSZ = stroka[68:len(stroka):].strip()

# Строка №5 980
stroka = file_r.readline()
# Извлечение нужных данных и присвоение переменным
DBLSZR = stroka[13:24:].strip()
FCO = stroka[68:len(stroka):].strip()

# Строка №6 980
stroka = file_r.readline()
# Извлечение нужных данных и присвоение переменным
SBBSY = stroka[13:24:].strip()
SBNANS = stroka[24:35:].strip()

# Строка №7 980
stroka = file_r.readline()
# Полезных данных нет в 7ой строке
print(ISEIZE,IANS,OATTMPT,OVFL,OSEIZE,OARR,OANS,TOTUSG,IANSUSG,OANSUSG,ITRANSZ,DBLSZR,FCO,SBBSY,SBNANS)



