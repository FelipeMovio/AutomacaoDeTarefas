# passo 5 - Repetir para todos os produtos 
import time
import pandas 
import pyautogui
# pyautogui.press - apertar uma tecla
# pyautogui.write - escrever algo
# pyautogui.click - clicar em algum lugar


pyautogui.PAUSE = 0.5  # configuração de tempo entre execuçoes


# passo 1 - Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(2)

# passo 2 - Fazer login 
pyautogui.press("tab")      
pyautogui.write("email@email.com")
pyautogui.press("tab")
pyautogui.write("senhasuperfacil")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(2)

# passo 3 - importar base de dados 
tabela = pandas.read_csv("./produtos.csv")

# passo 4 - cadastrar um produto 
for linha in tabela.index:
    pyautogui.press("tab")

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    precoUnitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(precoUnitario)
    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.press("enter")

    pyautogui.scroll(10000)

