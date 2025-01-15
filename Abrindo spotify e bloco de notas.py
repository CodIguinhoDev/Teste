import pyautogui as escolhe_opcao

opcao = escolhe_opcao.confirm('Clique no botão desejado',
             buttons=['Spotify', 'Notepad'])

if opcao == 'Spotify':

    escolhe_opcao.hotkey('win', 'r')#Clicando nas teclas windows + r

    #Delay de 2seg após abrir o windows r
    escolhe_opcao.sleep(2)

    #Escreve spotify
    escolhe_opcao.typewrite('Spotify')
    # Delay de 1seg
    escolhe_opcao.sleep(2)

    #Clica na tecla enter e acessa o spotify
    escolhe_opcao.press('Enter')

    #Espera até 10seg pro spotify abrir
    escolhe_opcao.sleep(10)
    escolhe_opcao.moveTo(x=548, y=27)
    escolhe_opcao.click()
    escolhe_opcao.sleep(3)
    #Na aba de pesquisa do spotify, procurou pelo artista Leall
    escolhe_opcao.typewrite('Leall')
    escolhe_opcao.sleep(3)
    escolhe_opcao.press('Enter')
    escolhe_opcao.sleep(2)

    #Clicou na primeira música que apareceu
    escolhe_opcao.moveTo(x=547, y=224)
    escolhe_opcao.click()

else:
    escolhe_opcao.hotkey('win', 'r')  # Clicando nas teclas windows + r

    # Delay de 2seg após abrir o windows r
    escolhe_opcao.sleep(2)

    # Escreve Bloco de notas
    escolhe_opcao.typewrite('Notepad')

    # Delay de 1seg
    escolhe_opcao.sleep(1)

    # Clica na tecla enter e acessa o bloco de notas
    escolhe_opcao.press('Enter')