import pyautogui
import clipboard
import threading
import keyboard
import os
import sys

# Instalar pip install pyautogui

#tempo para arrumar o programa

site1 = "https://nconsig4.fenixsoft.com.br/Margem/ConsultaMargem.aspx"
siteExpirado = "https://nconsig4.fenixsoft.com.br/ExpiredSession.aspx"
erroPagina ="Erro de Servidor no Aplicativo '/'."


entradas = input('Insira quantidade de elementos da planilia: ')
entradas2 = int(entradas)

def x():
   pyautogui.sleep(8)
   quantidadePlanilia = 0
   while quantidadePlanilia != entradas2 :
      
      pyautogui.keyDown('alt')
      pyautogui.sleep(0.5)
      pyautogui.press(['tab'])
      pyautogui.sleep(0.5)
      pyautogui.keyUp('alt')

      pyautogui.sleep(1)
      pyautogui.hotkey('ctrl', 's')
      pyautogui.sleep(1)
      pyautogui.hotkey('ctrl', 'c')
      pyautogui.press(['right'])


      pyautogui.keyDown('alt')
      pyautogui.sleep(0.5)
      pyautogui.press(['tab'])
      pyautogui.sleep(0.5)
      pyautogui.keyUp('alt')

      pyautogui.hotkey('ctrl','l')  #verificar quantidade de tab
      pyautogui.press('tab')
      pyautogui.press('tab')
      pyautogui.press('tab')
      pyautogui.press('tab')


      pyautogui.sleep(1)
      pyautogui.hotkey('ctrl', 'v')
      pyautogui.press(['tab'])

      pyautogui.keyDown('alt')
      pyautogui.sleep(0.5)
      pyautogui.press(['tab'])
      pyautogui.sleep(0.5)
      pyautogui.keyUp('alt')

      pyautogui.hotkey('ctrl', 'c')
      pyautogui.press(['right'])

      pyautogui.sleep(0.5)

      pyautogui.keyDown('alt')
      pyautogui.sleep(0.5)
      pyautogui.press(['tab'])
      pyautogui.sleep(0.5)
      pyautogui.keyUp('alt')

      pyautogui.sleep(1)

      pyautogui.hotkey('ctrl', 'v')

      pyautogui.sleep(1)
      
      pyautogui.moveTo(792, 574) # botao pesquisar
      pyautogui.sleep(0.5)
      pyautogui.click()
      pyautogui.sleep(2)


      pyautogui.hotkey('ctrl', 'shift', 'i')
      pyautogui.sleep(0.5)
      pyautogui.moveTo(1151,238)  ######################coordenada click inspecionar
      pyautogui.sleep(1)
      pyautogui.click() 
      pyautogui.sleep(0.5)
      pyautogui.hotkey('ctrl','f')
      pyautogui.write('erro')
      pyautogui.press('enter')
      pyautogui.moveTo(1006,293)   ###########coordenada string erro quando aperta enter
      pyautogui.sleep(0.5)    
      pyautogui.click()
      pyautogui.click()
      pyautogui.hotkey('ctrl','c')
      pyautogui.hotkey('ctrl', 'shift', 'i')
      pyautogui.sleep(0.5)
      quantidadePlanilia == entradas2

      erro = clipboard.paste()
      if erro == erroPagina:
        pyautogui.hotkey('alt', 'left')
        pyautogui.press(['tab'])

        pyautogui.keyDown('alt')
        pyautogui.sleep(0.5)
        pyautogui.press(['tab'])
        pyautogui.sleep(0.5)
        pyautogui.keyUp('alt')

        pyautogui.sleep(1)
        pyautogui.write('ERRO')

        pyautogui.sleep(1)
        pyautogui.hotkey('ctrl', 'left')
        pyautogui.press(['down'])

        pyautogui.keyDown('alt')
        pyautogui.sleep(0.5)
        pyautogui.press(['tab'])
        pyautogui.sleep(0.5)
        pyautogui.keyUp('alt') 
        sys.exit()
      else:
        pyautogui.sleep(0.5)

        pyautogui.hotkey('ctrl', 'l')
        pyautogui.sleep(1)
        pyautogui.hotkey('ctrl', 'c')
        site = clipboard.paste()
         
        if site == site1:               #nao contem (verificar o numero de tabs aqui (1 a mais ou um a menos))
            pyautogui.press(['tab'])
            pyautogui.press(['tab'])
            pyautogui.press(['tab'])      
            pyautogui.press(['tab'])      
            pyautogui.press('enter') 

            pyautogui.sleep(1)
            pyautogui.press(['tab']) 

            pyautogui.sleep(0.5)
            pyautogui.keyDown('alt')
            pyautogui.sleep(0.5)
            pyautogui.press(['tab'])
            pyautogui.sleep(0.5)
            pyautogui.keyUp('alt') 

            pyautogui.write('naocontem')
            pyautogui.hotkey('ctrl', 'left')
            pyautogui.press(['down'])

            pyautogui.sleep(0.5)
            pyautogui.keyDown('alt')
            pyautogui.sleep(0.5)
            pyautogui.press(['tab'])
            pyautogui.sleep(0.5)
            pyautogui.keyUp('alt')
        elif site == siteExpirado:
            pyautogui.sleep(1)
            pyautogui.hotkey('ctrl','l')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('tab')
            pyautogui.press('enter') 

            pyautogui.keyDown('alt')               
            pyautogui.sleep(0.5)
            pyautogui.press(['tab'])
            pyautogui.sleep(0.5)
            pyautogui.keyUp('alt')

    	
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.press('right')
            pyautogui.write("expirou")
            sys.exit()
        else:
            pyautogui.moveTo(586, 462)   #coordenada da margem 
            pyautogui.sleep(0.5)
            pyautogui.click()
            pyautogui.click()
            pyautogui.click()
            pyautogui.hotkey('ctrl', 'c')  #copiou a margem
            pyautogui.sleep(1)
         
            pyautogui.press(['tab']) 
            pyautogui.press('enter')  # voltou pra consulta

            pyautogui.sleep(1.5)


            pyautogui.keyDown('alt')
            pyautogui.sleep(0.5)
            pyautogui.press(['tab'])
            pyautogui.sleep(0.5)
            pyautogui.keyUp('alt')

            pyautogui.sleep(1)
            pyautogui.hotkey('ctrl','v')
            pyautogui.sleep(1)
            pyautogui.hotkey('ctrl','left')
            pyautogui.sleep(0.5)
            pyautogui.hotkey('ctrl','left')
            pyautogui.sleep(0.5)
            pyautogui.press('down')
            pyautogui.sleep(0.5)
            pyautogui.keyDown('alt')
            pyautogui.sleep(0.5)
            pyautogui.press(['tab'])
            pyautogui.sleep(0.5)
            pyautogui.keyUp('alt')            

      quantidadePlanilia += 1
   
   
      


# Função que para o programa caso clice na tecla especifica
def y():
   while(True):
      if keyboard.is_pressed('up'):
         pyautogui.hotkey('shift', 'alt')
         os._exit(0)
      
      
             
threading.Thread(target=x).start() ## Roda as duas funções ao mesmo tempo
threading.Thread(target=y).start() ## Roda as duas funções ao mesmo tempo


