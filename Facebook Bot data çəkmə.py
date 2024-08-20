from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from bs4 import BeautifulSoup

path = r'C:\Users\BAKU\Desktop\geckodriver-v0.35.0-win64\geckodriver.exe'
service = Service(executable_path=path)
driver = webdriver.Firefox(service=service)
driver.maximize_window()
wait = WebDriverWait(driver, 20)

try:
    driver.get("https://www.facebook.com/")
    sleep(1)
    email = wait.until(EC.presence_of_element_located((By.ID, "email"))).send_keys("login..") # Logini girin
    password = wait.until(EC.presence_of_element_located((By.ID, "pass"))).send_keys("password..") # Passwordu girin
    buton = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()
    sleep(1)
    driver.get("https://www.facebook.com/search/groups/?q=data%20analyst&sde=Abo6mQGTwumSH8ghiQqAvvjPX7NFviMO4wSBhxr6grIQwUayjg5k0ye5FNdIS2HCiLkkJOB-TfP5YV29lVJ9zt3H")
    sleep(2)  

    # Sehifeye getmek ve asagi surusdurmek
    last_page = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(2) 
        new_page = driver.execute_script("return document.body.scrollHeight")
        if new_page == last_page:
            break
        last_page = new_page
        
        # HTML cekme ve melumati isleme
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        
        data = soup.find_all("div", class_="x1yztbdb")
        for veri in data:
            basliq = veri.find("div", class_="xu06os2 x1ok221b")
            if basliq:
                elan = basliq.text
            uzvler = veri.find("span", class_="x1lliihq x6ikm8r x10wlt62 x1n2onr6")
            if uzvler:
                split = uzvler.text.split("·")[1]
                if split:
                    print(elan + " " + split)

except Exception as e:
    print(f"Umumi Xeta {e}")

finally:
    driver.quit()
