# Passo 1: Entrar no sistema da Empresa
#     Link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2: Fazer login
# Passo 3: Pegar/Importar a base de dados
# Passo 4: Cadastrar um produto
# Passo 5: Repetir o passo 4 até cadastrar todos os produtos

# pip install pyautogui
# pip install pandas openpyxl numpy

import pyautogui
import time
# pyautogui.click - clicar com o mouse
# pyautogui.write - escrever um texto
# pyautogui.press - apertar 1 tecla
# pyautogui.hotkey - combinação de teclas (Exemplo: Crtl C)
# pyautogui.scroll - rolar a tela para cima ou para baixo

pyautogui.PAUSE = 0.5 # P/ cada comando doafelipe.pereira@hotmail.com pyautogui

# ______________________________________________________________
### Passo 1: Entrar no sistema da Empresa
# Abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3) # Será somente para este local

# ______________________________________________________________
### Passo 2: Fazer login
pyautogui.click(x=785, y=385)
## pyautogui.hotkey("crtl", "a")
pyautogui.write("felipe.pereira@hotmail.com")
# passar para o campo de senha
pyautogui.press("tab")
pyautogui.write("123456@#$%")
# Para entrar
pyautogui.click(x=919, y=536)

time.sleep(3)

# ______________________________________________________________
### Passo 3: Pegar/Importar a base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")

print(tabela)

# ______________________________________________________________
### Passo 4: Cadastrar um produto
# para cada linha da minha tabela:
for linha in tabela.index:
    # codigo
    pyautogui.click(x=708, y=262)

    codigo = str(tabela.loc[linha, "codigo"]) #transformando em texto
    pyautogui.write(codigo)

    # marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    pyautogui.write(marca)

    # tipo
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    pyautogui.write(tipo)

    # categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.press("tab")
    pyautogui.write(categoria)

    # preco_unitario
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.press("tab")
    pyautogui.write(preco)

    # custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.press("tab")
    pyautogui.write(custo)

    # obs
    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    #clicar no botão de enviar
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000) # P/ subir a tela

# ______________________________________________________________
### Passo 5: Repetir o passo 4 até cadastrar todos os produtos