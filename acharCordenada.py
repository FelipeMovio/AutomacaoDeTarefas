import pyautogui
import time

print("Mova o mouse para a posição desejada e pressione Ctrl+C para obter as coordenadas.")
try:
    while True:
        x, y = pyautogui.position()
        positionStr = f'X: {x} Y: {y}'
        print(positionStr, end='\r') # Imprime na mesma linha
        time.sleep(0.1) # Uma pequena pausa para não sobrecarregar a CPU
except KeyboardInterrupt:
    print('\nCoordenadas capturadas!')
