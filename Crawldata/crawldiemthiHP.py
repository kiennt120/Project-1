from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="chromedriver")

driver.get("https://tienphong.vn/tra-cuu-diem-thi.tpo")

file = open("data.csv", "a")

for i in range(1, 23565):
    print("Thi sinh thu:", i)
    x = f'{i}'
    if len(x) == 1:
        SBD = "0300000" + x
    elif len(x) == 2:
        SBD = "030000" + x
    elif len(x) == 3:
        SBD = "03000" + x
    elif len(x) == 4:
        SBD = "0300" + x
    else:
        SBD = "030" + x
    txtSBD = driver.find_element(By.ID, "txtkeyword")
    txtSBD.send_keys(SBD)
    txtSBD.send_keys(Keys.ENTER)
    sleep(0.25)
    point = driver.find_elements(By.CLASS_NAME, "point")

    try:
        sbd = point[1].text
        toan = point[2].text
        van = point[3].text
        ngoaingu = point[4].text
        ly = point[5].text
        hoa = point[6].text
        sinh = point[7].text
        su = point[8].text
        dia = point[9].text
        GDCD = point[10].text

        str = f"{sbd}, {toan}, {van}, {ngoaingu}, {ly}, {hoa}, {sinh}, {su}, {dia}, {GDCD}, \n"
    except:
        str = f"{SBD}, \n"
    file.write(str)
    print(str)
    driver.find_element(By.ID, "txtkeyword").clear()


driver.close()
file.close()