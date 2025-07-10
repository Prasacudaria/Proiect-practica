print("Scriptul a pornit.")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Creează și pornește browserul
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Accesează Google
driver.get("https://www.google.com")

# Așteaptă 10 secunde să se încarce tot
time.sleep(10)

# Încearcă să dai click pe butonul de accept cookies dacă apare
try:
    accept_btn = driver.find_element(By.XPATH, "//div[contains(text(),'Accept') or contains(text(),'Sunt de acord') or contains(text(),'Accept all')]")
    accept_btn.click()
    print("Am închis fereastra de cookies.")
    time.sleep(1)
except:
    print("Nu a apărut fereastra de cookies.")

# Găsește bara de căutare și caută orice doresti
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Luceafarul")
search_box.send_keys(Keys.RETURN)

# Așteaptă să se încarce rezultatele
time.sleep(100)

print("Căutarea a fost trimisă cu succes.")