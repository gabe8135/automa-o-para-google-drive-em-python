#importando a biblioteca de automação de comandos teclado/mouse/monitor
import pyautogui
#importando biblioteca de tempo para as pausas feitas no decorrer do programa
import time

#mensagem de alerta no inicio
pyautogui.alert("ATENÇÂO codigo em execução no mexa em nada")

#um comando para intervalo de cada comando
pyautogui.PAUSE = 1.5

#pressione a tecla do windows
pyautogui.press('winleft')

#escreva crome no teclado
pyautogui.write('chrome')

#aperte enter
pyautogui.press('enter')

#usar um tempo maior de espera para digitar o endereço do google drive
time.sleep(1)

#digite na barra de pesquisa o comnado para ir ao google drive
pyautogui.write("https://drive.google.com/drive/u/0/my-drive")

#aperte enter no teclado novamente
pyautogui.press('enter')

#deixar a tela cheia
pyautogui.hotkey('win','up')

#pressione as teclas de atalho para area de trabalho win+d
pyautogui.hotkey('winleft','d')

#tempo de espera
time.sleep(1)

#colocando a posiçaõ do mouse sob o arquivo em questão
pyautogui.moveTo(26, 57)

#tempo de espera
time.sleep(2)

#clicar com o mouse
pyautogui.mouseDown()

#arrastando o arquivo para onde eu quero
pyautogui.moveTo(538, 551)

#pressionar as teclas alt + tab para ir para a janela do drive aberta  
pyautogui.hotkey('alt','tab')


#esperar um tempo de 5 seg para a pagina carregar toda
time.sleep(5)

#soltar o botao pressionado do mouse
pyautogui.mouseUp()

#exibir caixa de mensagem para saber que o programa funcionou
pyautogui.alert("arquivo enviado para a nuvem com exito!")