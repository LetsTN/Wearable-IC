import sys
from autent import MiBand3
from cursesmenu import *
from cursesmenu.items import *
from constants import ALERT_TYPES
import time
import os 


''' Biblioteca com as principais funcionalidades para a 
aplicação wearable do MI Band no projeto com os bombeiros '''


### RODAR PELO TERMINAL COM O SEGUINTE COMANDO <$ python3 main.py "00:00:00:00:00" --init> ###
### "00:00:00:00:00" É O ENDEREÇO MAC DA MI BAND, PODE SER PEGO PELO COMANDO <$ sudo hcitool lescan> ###
### SE ISSO DER ERRO, REINICIE O BLUETOOTH COM <$ sudo hciconfig hci0 reset> ###



def ligar():
	time.sleep(1)
	band.send_alert(TIPOS_ALERTA.TELEFONE)

def msg():
	time.sleep(1)
	band.send_alert(TIPOS_ALERTA.MENSAGEM)

def info():
	print('MiBand')
	print('Soft revision:',band.get_revision())
	print('Hardware revision:',band.get_hrdw_revision())
	print('Serial:',band.get_serial())
	print('Battery:', band.get_battery_info())
	print('Time:', band.get_current_time())
	print('Steps:', band.get_steps())
	a =input('Aperte ENTER para continuar')

def msg_custom():
	band.send_custom_alert(5)

def liga_custom():
	band.send_custom_alert(3)

def ligacao_perdida_custom():
	band.send_custom_alert(4)

def l(x):
	print('Realtime heart BPM:', x)

def batimentos():
	band.start_raw_data_realtime(heart_measure_callback=l)
	raw_input('Aperte ENTER para continuar')

def mudar_data():
	band.change_date()

MAC_ADDR = sys.argv[1]
print('Tentando se contctar com ', MAC_ADDR)

def atualizar_firmware():
	fileName = input('Coloque o nome do arquivo com extensão\n')
	band.dfuUpdate(fileName)

band = MiBand3(MAC_ADDR, debug=True)
band.setSecurityLevel(level = "medium")

# Autenticar o endereço da  MiBand
if len(sys.argv) > 2:
	if band.initialize():
		print("Inicialidado...")
	band.disconnect()
	sys.exit(0)
else:
	band.authenticate()

menu = CursesMenu("MiBand MAC: " + MAC_ADDR, "Escolha uma opção")
menu_info = FunctionItem("Ver informações do dispositivo", info)
menu_ligar = FunctionItem("Mandar uma ligação de alta prioridade", ligar)
menu_msg = FunctionItem("Mandar uma mensagem de média prioridade", msg)
menu_msg_c = FunctionItem("Mandar uma notificação de mensagem", msg_custom)
menu_liga_c = FunctionItem("Mandar uma notificação de ligação", liga_custom)
menu_liga_p = FunctionItem("Mandar uma notificação de ligação perdida", ligacao_perdida_custom)
menu_data = FunctionItem("Mudar a data e a hora", mudar_data)
menu_bate = FunctionItem("Ler batimentos", batimentos)
menu_firm = FunctionItem("Atualizar o Firmware", atualizar_firmware)

menu.append_item(menu_info)
menu.append_item(menu_ligar)
menu.append_item(menu_msg)
menu.append_item(menu_msg_c)
menu.append_item(msg_liga_c)
menu.append_item(menu_liga_p)
menu.append_item(menu_data)
menu.append_item(menu_bate)
menu.append_item(menu_firm)
menu.show()
