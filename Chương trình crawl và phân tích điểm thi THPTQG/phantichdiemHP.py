import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("diemthiHP.csv")

toan = df['Toan']
nguvan = df['Ngu van']
ngoaingu = df['Ngoai ngu']
ly = df['Ly']
hoa = df['Hoa']
sinh = df['Sinh']
su = df['Su']
dia = df['Dia']
gdcd = df['GDCD']

Toan = {'0':0, '0.2':0, '0.4':0, '0.6':0, '0.8':0, '1':0, '1.2':0, '1.4':0, '1.6':0, '1.8':0, '2':0, '2.2':0, '2.4':0, '2.6':0,
        '2.8':0, '3':0, '3.2':0, '3.4':0, '3.6':0, '3.8':0, '4':0, '4.2':0, '4.4':0, '4.6':0, '4.8':0, '5':0, '5.2':0, '5.4':0, '5.6':0,
        '5.8':0, '6':0, '6.2':0, '6.4':0, '6.6':0, '6.8':0, '7':0, '7.2':0, '7.4':0, '7.6':0, '7.8':0, '8':0, '8.2':0, '8.4':0, '8.6':0, 
        '8.8':0, '9':0, '9.2':0, '9.4':0, '9.6':0, '9.8':0, '10':0}
NgoaiNgu = {'0':0, '0.2':0, '0.4':0, '0.6':0, '0.8':0, '1':0, '1.2':0, '1.4':0, '1.6':0, '1.8':0, '2':0, '2.2':0, '2.4':0, '2.6':0,
        '2.8':0, '3':0, '3.2':0, '3.4':0, '3.6':0, '3.8':0, '4':0, '4.2':0, '4.4':0, '4.6':0, '4.8':0, '5':0, '5.2':0, '5.4':0, '5.6':0,
        '5.8':0, '6':0, '6.2':0, '6.4':0, '6.6':0, '6.8':0, '7':0, '7.2':0, '7.4':0, '7.6':0, '7.8':0, '8':0, '8.2':0, '8.4':0, '8.6':0, 
        '8.8':0, '9':0, '9.2':0, '9.4':0, '9.6':0, '9.8':0, '10':0}
Ly = Hoa = Sinh = Su = Dia = Gdcd = {'0':0, '0.25':0, '0.5':0, '0.75':0, '1':0, '1.25':0, '1.5':0, '1.75':0, '2':0, '2.25':0, '2.5':0, '2.75':0,
                                            '3':0, '3.25':0, '3.5':0, '3.75':0, '4':0, '4.25':0, '4.5':0, '4.75':0, '5':0, '5.25':0, '5.5':0, '5.75':0, 
                                            '6':0, '6.25':0, '6.5':0, '6.75':0, '7':0, '7.25':0, '7.5':0, '7.75':0, '8':0, '8.25':0, '8.5':0, '8.75':0, 
                                            '9':0, '9.25':0, '9.5':0, '9.75':0, '10':0}
NguVan = {'0':0, '0.25':0, '0.5':0, '0.75':0, '1':0, '1.25':0, '1.5':0, '1.75':0, '2':0, '2.25':0, '2.5':0, '2.75':0,
        '3':0, '3.25':0, '3.5':0, '3.75':0, '4':0, '4.25':0, '4.5':0, '4.75':0, '5':0, '5.25':0, '5.5':0, '5.6':0, '5.75':0, 
        '6':0, '6.25':0, '6.5':0, '6.75':0, '7':0, '7.25':0, '7.5':0, '7.6':0, '7.75':0, '8':0, '8.25':0, '8.5':0, '8.75':0, 
        '9':0, '9.25':0, '9.5':0, '9.75':0, '10':0}
DiembanA00 = DiembanC00 = DiembanA01 = DiembanD01 = {'<=1':0, '<=2':0, '<=3':0, '<=4':0, '<=5':0, '<=6':0, '<=7':0, '<=8':0, '<=9':0, '<=10':0, '<=11':0, '<=12':0, '<=13':0, '<=14':0, '<=15':0, '<=16':0, 
            '<=17':0, '<=18':0, '<=19':0, '<=20':0, '<=21':0, '<=22':0, '<=23':0, '<=24':0, '<=25':0, '<=26':0, '<=27':0, '<=28':0, '<=29':0, '<=30':0}

for i in range(0, 23564):
    if toan[i] != ' ' and toan[i] is not np.nan:
        Toan[toan[i]] += 1
    if nguvan[i] != ' ' and nguvan[i] is not np.nan:
        NguVan[nguvan[i]] += 1
    if ngoaingu[i] != ' ' and ngoaingu[i] is not np.nan:
        NgoaiNgu[ngoaingu[i]] += 1
    if ly[i] != ' ' and ly[i] is not np.nan:
        Ly[ly[i]] += 1
    if hoa[i] != ' ' and hoa[i] is not np.nan:
        Hoa[hoa[i]] += 1
    if sinh[i] != ' ' and sinh[i] is not np.nan:
        Sinh[sinh[i]] += 1
    if su[i] != ' ' and su[i] is not np.nan:
        Su[su[i]] += 1 
    if dia[i] != ' ' and dia[i] is not np.nan:
        Dia[dia[i]] += 1
    if gdcd[i] != ' ' and gdcd[i] is not np.nan:
        Gdcd[gdcd[i]] += 1 

    if toan[i] != ' ' and ly[i] != ' ' and hoa[i]  != ' ' and (toan[i] is not np.nan) and (ly[i] is not np.nan) and (hoa[i] is not np.nan):
        diem = float(toan[i]) + float(ly[i]) + float(hoa[i])
        if diem <= 1.0:
            DiembanA00['<=1'] += 1
        elif diem <= 2.0:
            DiembanA00['<=2'] += 1
        elif diem <= 3.0:
            DiembanA00['<=3'] += 1
        elif diem <= 4.0:
            DiembanA00['<=4'] += 1
        elif diem <= 5.0:
            DiembanA00['<=5'] += 1
        elif diem <= 6.0:
            DiembanA00['<=6'] += 1
        elif diem <= 7.0:
            DiembanA00['<=7'] += 1
        elif diem <= 8.0:
            DiembanA00['<=8'] += 1
        elif diem <= 9.0:
            DiembanA00['<=9'] += 1
        elif diem <= 10.0:
            DiembanA00['<=10'] += 1
        elif diem <= 11.0:
            DiembanA00['<=11'] += 1
        elif diem <= 12.0:
            DiembanA00['<=12'] += 1
        elif diem <= 13.0:
            DiembanA00['<=13'] += 1
        elif diem <= 14.0:
            DiembanA00['<=14'] += 1
        elif diem <= 15.0:
            DiembanA00['<=15'] += 1
        elif diem <= 16.0:
            DiembanA00['<=16'] += 1
        elif diem <= 17.0:
            DiembanA00['<=17'] += 1
        elif diem <= 18.0:
            DiembanA00['<=18'] += 1
        elif diem <= 19.0:
            DiembanA00['<=19'] += 1
        elif diem <= 20.0:
            DiembanA00['<=20'] += 1
        elif diem <= 21.0:
            DiembanA00['<=21'] += 1
        elif diem <= 22.0:
            DiembanA00['<=22'] += 1
        elif diem <= 23.0:
            DiembanA00['<=23'] += 1
        elif diem <= 24.0:
            DiembanA00['<=24'] += 1
        elif diem <= 25.0:
            DiembanA00['<=25'] += 1
        elif diem <= 26.0:
            DiembanA00['<=26'] += 1
        elif diem <= 27.0:
            DiembanA00['<=27'] += 1
        elif diem <= 28.0:
            DiembanA00['<=28'] += 1      
        elif diem <= 29.0:
            DiembanA00['<=29'] += 1
        else:
            DiembanA00['<=30'] += 1

    if nguvan[i] != ' ' and su[i] != ' ' and dia[i]  != ' ' and (nguvan[i] is not np.nan) and (su[i] is not np.nan) and (dia[i] is not np.nan):
        diem = float(nguvan[i]) + float(su[i]) + float(dia[i])
        if diem <= 1.0:
            DiembanC00['<=1'] += 1
        elif diem <= 2.0:
            DiembanC00['<=2'] += 1
        elif diem <= 3.0:
            DiembanC00['<=3'] += 1
        elif diem <= 4.0:
            DiembanC00['<=4'] += 1
        elif diem <= 5.0:
            DiembanC00['<=5'] += 1
        elif diem <= 6.0:
            DiembanC00['<=6'] += 1
        elif diem <= 7.0:
            DiembanC00['<=7'] += 1
        elif diem <= 8.0:
            DiembanC00['<=8'] += 1
        elif diem <= 9.0:
            DiembanC00['<=9'] += 1
        elif diem <= 10.0:
            DiembanC00['<=10'] += 1
        elif diem <= 11.0:
            DiembanC00['<=11'] += 1
        elif diem <= 12.0:
            DiembanC00['<=12'] += 1
        elif diem <= 13.0:
            DiembanC00['<=13'] += 1
        elif diem <= 14.0:
            DiembanC00['<=14'] += 1
        elif diem <= 15.0:
            DiembanC00['<=15'] += 1
        elif diem <= 16.0:
            DiembanC00['<=16'] += 1
        elif diem <= 17.0:
            DiembanC00['<=17'] += 1
        elif diem <= 18.0:
            DiembanC00['<=18'] += 1
        elif diem <= 19.0:
            DiembanC00['<=19'] += 1
        elif diem <= 20.0:
            DiembanC00['<=20'] += 1
        elif diem <= 21.0:
            DiembanC00['<=21'] += 1
        elif diem <= 22.0:
            DiembanC00['<=22'] += 1
        elif diem <= 23.0:
            DiembanC00['<=23'] += 1
        elif diem <= 24.0:
            DiembanC00['<=24'] += 1
        elif diem <= 25.0:
            DiembanC00['<=25'] += 1
        elif diem <= 26.0:
            DiembanC00['<=26'] += 1
        elif diem <= 27.0:
            DiembanC00['<=27'] += 1
        elif diem <= 28.0:
            DiembanC00['<=28'] += 1      
        elif diem <= 29.0:
            DiembanC00['<=29'] += 1
        else:
            DiembanC00['<=30'] += 1

    if toan[i] != ' ' and ly[i] != ' ' and ngoaingu[i]  != ' ' and (toan[i] is not np.nan) and (ly[i] is not np.nan) and (ngoaingu[i] is not np.nan):
        diem = float(toan[i]) + float(ly[i]) + float(ngoaingu[i])
        if diem <= 1.0:
            DiembanA01['<=1'] += 1
        elif diem <= 2.0:
            DiembanA01['<=2'] += 1
        elif diem <= 3.0:
            DiembanA01['<=3'] += 1
        elif diem <= 4.0:
            DiembanA01['<=4'] += 1
        elif diem <= 5.0:
            DiembanA01['<=5'] += 1
        elif diem <= 6.0:
            DiembanA01['<=6'] += 1
        elif diem <= 7.0:
            DiembanA01['<=7'] += 1
        elif diem <= 8.0:
            DiembanA01['<=8'] += 1
        elif diem <= 9.0:
            DiembanA01['<=9'] += 1
        elif diem <= 10.0:
            DiembanA01['<=10'] += 1
        elif diem <= 11.0:
            DiembanA01['<=11'] += 1
        elif diem <= 12.0:
            DiembanA01['<=12'] += 1
        elif diem <= 13.0:
            DiembanA01['<=13'] += 1
        elif diem <= 14.0:
            DiembanA01['<=14'] += 1
        elif diem <= 15.0:
            DiembanA01['<=15'] += 1
        elif diem <= 16.0:
            DiembanA01['<=16'] += 1
        elif diem <= 17.0:
            DiembanA01['<=17'] += 1
        elif diem <= 18.0:
            DiembanA01['<=18'] += 1
        elif diem <= 19.0:
            DiembanA01['<=19'] += 1
        elif diem <= 20.0:
            DiembanA01['<=20'] += 1
        elif diem <= 21.0:
            DiembanA01['<=21'] += 1
        elif diem <= 22.0:
            DiembanA01['<=22'] += 1
        elif diem <= 23.0:
            DiembanA01['<=23'] += 1
        elif diem <= 24.0:
            DiembanA01['<=24'] += 1
        elif diem <= 25.0:
            DiembanA01['<=25'] += 1
        elif diem <= 26.0:
            DiembanA01['<=26'] += 1
        elif diem <= 27.0:
            DiembanA01['<=27'] += 1
        elif diem <= 28.0:
            DiembanA01['<=28'] += 1      
        elif diem <= 29.0:
            DiembanA01['<=29'] += 1
        else:
            DiembanA01['<=30'] += 1

    if toan[i] != ' ' and nguvan[i] != ' ' and ngoaingu[i]  != ' ' and (toan[i] is not np.nan) and (nguvan[i] is not np.nan) and (ngoaingu[i] is not np.nan):
        diem = float(toan[i]) + float(nguvan[i]) + float(ngoaingu[i])
        if diem <= 1.0:
            DiembanD01['<=1'] += 1
        elif diem <= 2.0:
            DiembanD01['<=2'] += 1
        elif diem <= 3.0:
            DiembanD01['<=3'] += 1
        elif diem <= 4.0:
            DiembanD01['<=4'] += 1
        elif diem <= 5.0:
            DiembanD01['<=5'] += 1
        elif diem <= 6.0:
            DiembanD01['<=6'] += 1
        elif diem <= 7.0:
            DiembanD01['<=7'] += 1
        elif diem <= 8.0:
            DiembanD01['<=8'] += 1
        elif diem <= 9.0:
            DiembanD01['<=9'] += 1
        elif diem <= 10.0:
            DiembanD01['<=10'] += 1
        elif diem <= 11.0:
            DiembanD01['<=11'] += 1
        elif diem <= 12.0:
            DiembanD01['<=12'] += 1
        elif diem <= 13.0:
            DiembanD01['<=13'] += 1
        elif diem <= 14.0:
            DiembanD01['<=14'] += 1
        elif diem <= 15.0:
            DiembanD01['<=15'] += 1
        elif diem <= 16.0:
            DiembanD01['<=16'] += 1
        elif diem <= 17.0:
            DiembanD01['<=17'] += 1
        elif diem <= 18.0:
            DiembanD01['<=18'] += 1
        elif diem <= 19.0:
            DiembanD01['<=19'] += 1
        elif diem <= 20.0:
            DiembanD01['<=20'] += 1
        elif diem <= 21.0:
            DiembanD01['<=21'] += 1
        elif diem <= 22.0:
            DiembanD01['<=22'] += 1
        elif diem <= 23.0:
            DiembanD01['<=23'] += 1
        elif diem <= 24.0:
            DiembanD01['<=24'] += 1
        elif diem <= 25.0:
            DiembanD01['<=25'] += 1
        elif diem <= 26.0:
            DiembanD01['<=26'] += 1
        elif diem <= 27.0:
            DiembanD01['<=27'] += 1
        elif diem <= 28.0:
            DiembanD01['<=28'] += 1      
        elif diem <= 29.0:
            DiembanD01['<=29'] += 1
        else:
            DiembanD01['<=30'] += 1

    
      
x_toan = list(Toan.keys())
y_toan = list(Toan.values())
x_nv = list(NguVan.keys())
y_nv = list(NguVan.values())
x_nn = list(NgoaiNgu.keys())
y_nn = list(NgoaiNgu.values())
x_ly = list(Ly.keys())
y_ly = list(Ly.values())
x_hoa = list(Hoa.keys())
y_hoa = list(Hoa.values())
x_sinh = list(Sinh.keys())
y_sinh = list(Sinh.values())
x_su = list(Su.keys())
y_su = list(Su.values())
x_dia = list(Dia.keys())
y_dia = list(Dia.values())
x_gdcd = list(Gdcd.keys())
y_gdcd = list(Gdcd.values())
x_a00 = list(DiembanA00.keys())
y_a00 = list(DiembanA00.values())
x_c00 = list(DiembanC00.keys())
y_c00 = list(DiembanC00.values())
x_a01 = list(DiembanA01.keys())
y_a01 = list(DiembanA01.values())
x_d01 = list(DiembanD01.keys())
y_d01 = list(DiembanD01.values())

# # Mon ngoai ngu
# plt.figure(figsize = (12, 6.5))
# y_pos = np.arange(len(x_nn))
# plt.xticks(y_pos, x_nn, rotation=90)
# for i in range (len(y_nn)):
#     plt.text(i, y_nn[i] + 15, y_nn[i], ha='center', rotation=90)
# plt.xlabel('Diem thi')
# plt.ylabel('So thi sinh')
# plt.title('Pho diem mon ngoai ngu')
# plt.bar(y_pos, y_nn, width=0.4)
# plt.show()

# # Mon Toan
plt.figure(figsize = (12, 6.5))
y_pos = np.arange(len(x_toan))
plt.xticks(y_pos, x_toan, rotation=90)
for i in range (len(y_toan)):
    plt.text(i, y_toan[i] + 15, y_toan[i], ha='center', rotation=90)
plt.xlabel('Diem thi')
plt.ylabel('So thi sinh')
plt.title('Pho diem mon toan')
plt.bar(y_pos, y_toan, width=0.4)
plt.show()

# # Ban A00
# plt.figure(figsize = (9, 6.5))
# y_pos = np.arange(len(x_a00))
# plt.xticks(y_pos, x_a00, rotation=90)
# for i in range (len(y_a00)):
#     plt.text(i, y_a00[i] + 28, y_a00[i], ha='center', rotation=90)
# plt.xlabel('Diem thang 30')
# plt.ylabel('So thi sinh')
# plt.title('Pho diem ban A00')
# plt.bar(y_pos, y_a00, width=0.5)
# plt.show()

# #Ban C00
# plt.figure(figsize = (9, 6.5))
# y_pos = np.arange(len(x_c00))
# plt.xticks(y_pos, x_c00, rotation=90)
# for i in range (len(y_c00)):
#     plt.text(i, y_c00[i] + 28, y_c00[i], ha='center', rotation=90)
# plt.xlabel('Diem thang 30')
# plt.ylabel('So thi sinh')
# plt.title('Pho diem ban C00')
# plt.bar(y_pos, y_c00, width=0.5)
# plt.show()

# # Ban D01 - tuong doi
# plt.figure(figsize = (9, 6.5))
# y_pos = np.arange(len(x_d01))
# plt.xticks(y_pos, x_d01, rotation=90)
# for i in range (len(y_d01)):
#     plt.text(i, y_d01[i] + 28, y_d01[i], ha='center', rotation=90)
# plt.xlabel('Diem thang 30')
# plt.ylabel('So thi sinh')
# plt.title('Pho diem ban D01 - tuong doi')
# plt.bar(y_pos, y_d01, width=0.5)
# plt.show()

# # Ban A01 - tuong doi
# plt.figure(figsize = (9, 6.5))
# y_pos = np.arange(len(x_a01))
# plt.xticks(y_pos, x_a01, rotation=90)
# for i in range (len(y_a01)):
#     plt.text(i, y_a01[i] + 28, y_a01[i], ha='center', rotation=90)
# plt.xlabel('Diem thang 30')
# plt.ylabel('So thi sinh')
# plt.title('Pho diem ban A01 - tuong doi')
# plt.bar(y_pos, y_a01, width=0.5)
# plt.show()