import openpyxl
import pyperclip
import pyautogui
import time

#def executar_automacao():
# entrar na planilha
workbook = openpyxl.load_workbook(r'C:\Users\User\projetos\Freela\Nfs-e.xlsx')
sheet_teste = workbook['teste']

def executar_automacao():

        # copiar as informações e colar no lugar correspondente
        for linha in sheet_teste.iter_rows(min_row=2):

                cliente = linha[0].value
                pyautogui.click(740,229,duration=1)
                pyperclip.copy(cliente)
                pyautogui.hotkey('ctrl', 'v')
                
                cpf_cnpj = linha[1].value
                pyautogui.click(756,276,duration=1) 
                pyperclip.copy(cpf_cnpj) 
                pyautogui.hotkey('ctrl', 'v')

                cep = linha[2].value
                pyautogui.click(763,321,duration=1)
                pyperclip.copy(cep)
                pyautogui.hotkey('ctrl', 'v')

                endereco = linha[3].value
                pyautogui.click(765,367,duration=1)
                pyperclip.copy(endereco)
                pyautogui.hotkey('ctrl', 'v')

                bairro = linha[4].value
                pyautogui.click(769,415,duration=1)
                pyperclip.copy(bairro)
                pyautogui.hotkey('ctrl', 'v')

                municipio = linha[5].value
                pyautogui.click(770,461,duration=1)
                pyperclip.copy(municipio)
                pyautogui.hotkey('ctrl', 'v')

                uf = linha[6].value
                pyautogui.click(772,509,duration=1)
                pyperclip.copy(uf)
                pyautogui.hotkey('ctrl', 'v')

                inscricao_estadual = linha[7].value
                pyautogui.click(790,557,duration=1)
                pyperclip.copy(inscricao_estadual)
                pyautogui.hotkey('ctrl', 'v')

                descricao = linha[8].value
                pyautogui.click(792,604,duration=1)
                pyperclip.copy(descricao)
                pyautogui.hotkey('ctrl', 'v')

                quantidade = linha[9].value
                pyautogui.click(796,652,duration=1)
                pyperclip.copy(quantidade)
                pyautogui.hotkey('ctrl', 'v')
                
                valor_unitario = linha[10].value
                pyautogui.click(798,701,duration=1)
                pyperclip.copy(valor_unitario)
                pyautogui.hotkey('ctrl', 'v')
                
                valor_total = linha[11].value
                pyautogui.click(800,746,duration=1)
                pyperclip.copy(valor_total)
                pyautogui.hotkey('ctrl', 'v')

                # clicar no botão de gerar nf
                pyautogui.click(801,799,duration=1)

