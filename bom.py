from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\muham\\OneDrive\\Kerja\\Bot Whatsapp\\Spam\\chromedriver.exe")
chrome_options = Options()
chrome_options.add_argument("user-data-dir=selenium") 
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://web.whatsapp.com/')

# name = input('MASUKAN NAMA TARGET : ')
msg = input('ISI PESAN CINTA MU : ')
count = int(input('JUMLAH PESAN : '))

input('klik enter untuk bom dia ')

# user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
# user.click()

msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
    button.click()
    time.sleep(0.5)
