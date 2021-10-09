from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = r"C:\Users\Gustavo Afonso\Desktop\ChromeDriver\chromedriver.exe"
INSTAGRAM_LOGIN_URL = "https://www.instagram.com/"
user_name = "Your instagram login"
password = "Your instagram password"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(INSTAGRAM_LOGIN_URL)
