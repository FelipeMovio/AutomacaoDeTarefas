# passo 1 - Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
                                           #  exemplo qualquer de site
# passo 2 - Fazer login 
# passo 3 - importar base de dados 
# passo 4 - cadastrar um produto 
# passo 5 - Repetir para todos os produtos 

import pyautogui
# pyautogui.press - apertar uma tecla
# pyautogui.write - escrever algo
# pyautogui.click - clicar em algum lugar

pyautogui.PAUSE = 0.5  # configuração de tempo entre execuçoes


# passo 1
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
pyautogui.sleep(2)

# passo 2
pyautogui.press("tab")
pyautogui.write("email@email.com")
pyautogui.press("tab")
pyautogui.write("1234")
