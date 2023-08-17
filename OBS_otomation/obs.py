from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import cv2
from number_extract import extract

options=Options()
# options.add_experimental_option('detach',True)
browser = webdriver.Chrome(options=options)

def first_page():
    kontrol=True
    while kontrol:
        browser.get('https://obsogrenci.ktun.edu.tr/')
        username=browser.find_element(by=By.XPATH,value='//*[@id="emailaddress"]')
        password=browser.find_element(by=By.XPATH,value='//*[@id="password"]')
        checkbox1=browser.find_element(by=By.XPATH,value='//input[@id="checkbox3"]')
        checkbox2=browser.find_element(by=By.XPATH,value='//input[@id="checkbox4"]')
        login_button=browser.find_element(by=By.XPATH,value='/html/body/div[1]/div/div/div/form/div[6]/button')
        number_area=browser.find_element(by=By.XPATH,value='//input[@id="TxtCaptcha"]')

        numbers=browser.find_element(by=By.XPATH,value='//img[@id="Image1"]')
        numbers.screenshot('./numbers.png')
        imag=cv2.imread("numbers.png")
        extracted_numbers=extract(imag)

        username.send_keys("")
        password.send_keys("")
        browser.execute_script("arguments[0].click();", checkbox1)
        browser.execute_script("arguments[0].click()",checkbox2)
        number_area.send_keys(extracted_numbers)
        login_button.click()
        time.sleep(1)
        if browser.current_url == 'https://obsogrenci.ktun.edu.tr/Ogrenci/Anasayfa':
            kontrol=False
            time.sleep(1)

first_page()

def second_page():
    browser.get('https://obsogrenci.ktun.edu.tr/Ogrenci/NotDurumu')
    table_rows=browser.find_elements(By.XPATH,'//*[@id="wrapper"]/div[3]/div/div/div/div/div/div[2]/div/div/div/div[6]/table/tbody/tr')
    for row in table_rows:
        deneme=row.find_elements(By.XPATH,'.//td[@class="text-center"]')
        for i in range(len(deneme)):
            print(deneme[i].text)
        print("------------------")

second_page()




# browser.quit()