import time
import pyautogui

def clicar_botao(imagem):
    try:
        # Localize as coordenadas do botão na tela com uma tolerância maior
        x, y = pyautogui.locateCenterOnScreen(imagem, confidence=0.8) 
        pyautogui.click(x, y)
        print(f"Botão '{imagem}' clicado!")
    except Exception as e:
        print(f"Erro ao clicar no botão '{imagem}': {e}")

def pular_abertura():
    clicar_botao('pularabertura.png')

def pular_ending():
    clicar_botao('pularending.png')

# Loop principal
while True:
    pular_abertura()
    pular_ending()
    time.sleep(0.3)
