
__all__ = ['UUIDS']

class Imutavel(type):
	""" Classe que definte o tipo imutável para um objeto """

	def __call__(*args):
		raise Exception('Você não pode instanciar um objeto imutável')

	def __setattr__(*args):
		raise Exception('Você não pode modificar um objeto imutável')


class UUIDS(object):
	""" Classe de objetos que define os identificadores únicos universais do Mi Band """

	__metaclass__ = Imutavel

	BASE = "0000%s-0000-1000-8000-00805f9b34fb" # Base 
	
	# Serviços gerais do Mi Band
	SERVICO_MIBAND1 = BASE % 'fee0'
	SERVICO_MIBAND2 = BASE % 'fee1'

	# Serviços que o Mi Band oferece
	SERVICO_ALERTA = BASE % '1802'
	SERVICO_ALERTA_NOTIFICACAO = BASE % '1811'
	SERVICO_BATIMENTOS_CARDIACOS = BASE % '180d'
	SERVICO_INFORMACOES_DISPOSITIVO = BASE % '180a'

	# Características relacionadas ao dispositivo
	CARACTERISTICA_HZ = "00000002-0000-3512-2118-0009af100700" # Frequência 
	CARACTERISTICA_SENSOR = "00000001-0000-3512-2118-0009af100700"
	CARACTERISTICA_AUTENT = "00000009-0000-3512-2118-0009af100700" # Autenticação
	CARACTERISTICA_MEDICAO_BATIMENTOS = "00002a37-0000-1000-8000-00805f9b34fb"
	CARACTERISTICA_CONTROLE_BATIMENTOS = "00002a39-0000-1000-8000-00805f9b34fb"
	CARACTERISTICA_ALERTA = "00002a06-0000-1000-8000-00805f9b34fb"
	CARACTERISTICA_ALERTA_CUSTOMIZADO = "00002a46-0000-1000-8000-00805f9b34fb"
	CARACTERISTICA_BATERIA = "00000006-0000-3512-2118-0009af100700"
	CARACTERISTICA_PASSOS = "00000007-0000-3512-2118-0009af100700" # Quantidade de passos
	CARACTERISTICA_LE_PARAMS =  BASE % "FF09" # Não entendi pra que que serve (mas n tirei daqui)
	CARACTERISTICA_REVISAO = 0x2a28
	CARACTERISTICA_SERIAL = 0x2a25
	CARACTERISTICA_REVISAO_HARDWARE = 0x2a27
	CARACTERISTICA_CONFIGURACAO = "00000003-0000-3512-2118-0009af100700"
	CARACTERISTICA_DEVICEEVENT = "00000010-0000-3512-2118-0009af100700" # Também não entendi pra que serve, mas ok

	# Características relacionadas ao usuário
	CARACTERISTICA_HORA_ATUAL = BASE % '2A2B'
	CARACTERISTICA_IDADE = BASE % '2A80'
	CARACTERISTICA_CONFIGURACOES_USUARIO = "00000008-0000-3512-2118-0009af100700"

	DESCRICAO_NOTIFICACAO = 0x2902

	# Atualizações do Firmware do dispositivo
	SERVICO_AFD_FIRMWARE = "00001530-0000-3512-2118-0009af100700"
	CARACTERISTICA_AFD_FIRMWARE = "00001531-0000-3512-2118-0009af100700"
	CARACTERISTICA_AFD_FIRMWARE_ESCREVER = "00001532-0000-3512-2118-0009af100700"


class ESTADO_AUTENTICACAO(object):
	""" Classe que define os estados de autenticação do Mi Band """

	__metaclass__ = Imutavel

	AUTENTICACAO_OK = "Autenticação ok"
	AUTENTICACAO_FALHOU = "Autenticação falhou"
	ENCRIPTACAO_CHAVE_FALHOU = "Autenticação da chave de encriptação falhou, enviando uma nova chave"
	ENVIO_CHAVE_FALHOU = "Envio da chave falhou"
	REQUISICAO_NA_FALHOU = "Erro ao requisitar um número aleatório" # NA = Número Aleatório


class TIPOS_ALERTA(object):
	""" Classe que define os tipos de alerta possíveis para o Mi Band """

	__metaclass__ = Imutavel

	NENHUM = '\x00'
	MENSAGEM = '\x01'
	TELEFONE = '\x02'


class TIPO_FILA(object):
	""" Classe que define os objetos de tipo fila da medição dos batimentos cardíacos """

	__metaclass__ = Imutavel

	BATIMENTOS = 'batimetnos'
	ACEL_BRUTA = 'acel_bruta' # Aceleração bruta
	BAT_MRUTO = 'bat_bruto' # Batimento bruto