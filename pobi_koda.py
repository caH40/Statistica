from openpyxl import load_workbook
import pendulum

file_r = open('ats32.txt', 'r')
file_w = open('ats32_edited.txt', 'w')
file_wsreda = open('ats32_edited_sreda.txt', 'w')

# Вытаскивание из файла только строк с нужной информацией по транковым группам
for x in file_r:
    # Поиск данных для статистики по средам
    if x.find('   OP TRFMR OFFSUM                                  PART 1 OF 8') != -1:
        for y in range(25):
            file_wsreda.write(file_r.readline())



file_r.close()
file_w.close()
file_wsreda.close()

