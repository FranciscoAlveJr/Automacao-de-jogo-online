from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from time import sleep
from bs4 import BeautifulSoup as bs
from tkinter import messagebox
from tkinter import Tk


url_metamask = 'chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#restore-vault'
url_pegaxy = 'https://play.pegaxy.io/renting?tab=fee&sortBy=price&sortType=ASC'

options = Options()
# Caminho dos dados do chrome
options.add_argument("user-data-dir=C:/Users/junio/AppData/Local/Google/Chrome/User Data/")

driver = Chrome(service=Service(ChromeDriverManager().install()), options=options)
sleep(1)

# Acessa o metamask
driver.get(url_metamask)

wa = WebDriverWait(driver, 10)
wa.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div/form/div[1]/div/input')))

# Digita a frase no campo indicado
frase = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div/form/div[1]/div/input')
frase.send_keys('region similar author round between winner traffic glance arrow forest tree frozen')

# Digita a senha no campo indicado
senha = driver.find_element(By.ID, 'password')
senha.send_keys('eraldo213243122334')

# Digita a mesma senha para confirmar
confirm = driver.find_element(By.ID, 'confirm-password')
confirm.send_keys('eraldo213243122334')

# Clica em restaurar
restaurar = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/div/form/button')
restaurar.click()

# Acessa a página do Pegaxy
driver.get(url_pegaxy)

wa.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[1]/div[1]/div/div/ul/li[5]')))

# Clica em conectar
connect = driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/div/div/ul/li[5]')
connect.click()

wa.until(
    EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div/div[2]/div/div[2]/div[2]/div[2]/span[2]')))

# Clica em connect
con_metamask = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div[2]/div/div[2]/div[2]/div[2]/span[2]')
con_metamask.click()

sleep(2)

# Muda para a janela do metamask
janelas = driver.window_handles
driver.switch_to.window(janelas[1])

wa.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div[3]/div[2]/button[2]')))

# Clica em próximo
proximo = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div[3]/div[2]/button[2]')
proximo.click()

wa.until(EC.presence_of_element_located(
    (By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]')))

# Clica em conectar
conectar = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]')
conectar.click()

wa.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div[3]/button[2]')))

# Clica em assinar
assinar = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[3]/button[2]')
assinar.click()

driver.switch_to.window(janelas[0])

sleep(1.5)

alugar = False

# Loop para separar e printar os dados de cada pegasus
while not alugar:
    try:
        wa.until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/div/div/div/div[2]')))

        html = driver.page_source
        soup = bs(html, 'html.parser')

        # Acha os dados de cada pegasus e põe em listas
        energias = soup.find_all('div', {'class': 'list-enegy'})
        titles = soup.find_all('div', {'class': 'item-info-title'})
        valores = soup.find_all('span', {'class': 'content-name-title'})
        tempos = soup.find_all('div', {'class': 'content-name-title'})
        btn = driver.find_elements(By.CLASS_NAME, 'action-button')

        for i in range(len(energias)):
            title = titles[i].text
            energia = int(energias[i].text[:2])
            valor = float(valores[i].text)
            tempo = int(tempos[i].text[5:7])

            if energia >= 1 and valor <= 60 and tempo == 1:
                print(title)
                print(f'\tEnergia = {energia}')
                print(f'\tValor = {valor}')
                print(f'\tTempo = {tempo}')

                print(btn[i])
                btn[i].click()

                wa.until(EC.presence_of_element_located(
                    (By.XPATH, '/html/body/div[3]/div/div/div/div[2]/div[2]/div[1]/div/div[2]')))
                aprove = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div[2]/div[2]/div[1]/div/div[2]')
                aprove.click()
                alugar = True
                break

        if not alugar:
            driver.refresh()
    except:
        continue

try:
    janelas2 = driver.window_handles
    driver.switch_to.window(janelas2[1])

    wa.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div[5]/footer/button[2]')))
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[5]/footer/button[2]').click()
    driver.switch_to.window(janelas2[0])
except IndexError:
    pass

wa.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div/div[2]/div[2]/div[2]')))

rent = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div[2]/div[2]/div[2]')

rec = False
while not rec:
    try:
        rent.click()

        sleep(3)

        janelas3 = driver.window_handles
        driver.switch_to.window(janelas3[1])

        wa.until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[1]/div/div[2]/div/div[4]/div[3]/footer/button[2]')))
        rec = True
    except:
        continue

confirm2 = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[4]/div[3]/footer/button[2]')
# confirm2.click()

# root = Tk()
# root.destroy()
# messagebox.showinfo('Pegaxy', 'Cavalo alugado com sucesso!')


sleep(6000)
# driver.quit()
