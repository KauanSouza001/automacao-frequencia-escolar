import pyautogui
import time

print("Mova o mouse até o local desejado...")
time.sleep(5)

x, y = pyautogui.position()
print(f"Coordenadas capturadas: X={x}, Y={y}")