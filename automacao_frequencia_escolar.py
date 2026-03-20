import pyautogui
import time

# Pequena pausa entre ações para evitar erros
pyautogui.PAUSE = 0.1

# Lista com os percentuais de frequência dos alunos
frequencias = [
    84, 94, 75, 75, 89, 94,94, 99, 84, 82, 84, 99, 94, 94, 84, 82, 99, 99, 75, 75, 78, 82,90, 81, 99, 99, 99, 91, 77, 75, 86, 86, 81, 99, 72, 95, 99, 95, 81, 77, 75, 72, 99, 75, 99, 63, 
95, 75, 81, 72, 95, 77, 77, 81, 75, 90, 90, 86, 75, 68, 75, 90, 90, 99, 81, 99, 99, 75, 81, 75, 72, 95, 72, 81, 99, 75, 95, 72, 90, 75, 90, 81, 81, 81, 90, 68, 75, 63, 75, 95, 90, 
68,81, 86, 81, 99, 99, 75, 99, 68, 77, 86, 99, 75, 75, 75, 75, 75, 75, 75, 75, 90 
]

# Coordenadas dos campos onde será iniciado o preenchimento
campos_iniciais = [
    (1794, 559),
    (1794, 606),
    (1794, 655),
    (1794, 702),
    (1794, 750)
]

def navegar_ate_campos():
    """
    Navega até os campos corretos usando TAB
    """
    for _ in range(4):
        pyautogui.press('tab')


def preencher_duas_frequencias(freq1, freq2):
    """
    Preenche dois campos de frequência para o aluno
    """
    pyautogui.write(str(freq1))
    pyautogui.press('tab')
    pyautogui.write('3b')
    pyautogui.press('tab')

    pyautogui.write(str(freq2))
    pyautogui.press('tab')
    pyautogui.write('3b')
    pyautogui.press('tab')

    # Confirmação
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')


def executar_automacao():
    """
    Executa a automação completa de lançamento de frequência
    """
    indice = 0

    while indice < len(frequencias):
        for posicao in campos_iniciais:
            if indice >= len(frequencias):
                break

            # Primeira frequência
            freq1 = frequencias[indice]
            indice += 1

            # Segunda frequência (ou repete se não houver)
            if indice < len(frequencias):
                freq2 = frequencias[indice]
                indice += 1
            else:
                freq2 = freq1

            print(f"Inserindo frequências: {freq1} e {freq2}")

            time.sleep(1)
            pyautogui.click(posicao)
            time.sleep(1)

            navegar_ate_campos()
            preencher_duas_frequencias(freq1, freq2)

        # Avança para próxima página/lista
        time.sleep(1)
        pyautogui.click(1857, 836)
        time.sleep(1)


# Início da execução
executar_automacao()