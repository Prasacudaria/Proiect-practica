print("Scriptul a pornit.")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

# Creează și pornește browserul
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Accesează Google
driver.get("https://www.google.com")

# Așteaptă 5 secunde să se încarce tot
time.sleep(5)

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

# Extrage titlurile rezultatelor
titluri = driver.find_elements(By.CSS_SELECTOR, "h3")

# Pregătește lista pentru DataFrame
date_rezultate = []
for titlu in titluri:
    text = titlu.text
    if text:  # evită titluri goale
        date_rezultate.append({"Titlu": text})

# Salvează într-un fișier Excel
df = pd.DataFrame(date_rezultate)
df.to_excel("rezultate_google.xlsx", index=False)

print(f"Am salvat {len(date_rezultate)} titluri în 'rezultate_google.xlsx'.")

# Închide browserul
driver.quit()
