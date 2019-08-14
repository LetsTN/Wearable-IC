
___all__ = ['UUIDS']


class Imutavel(type):

	# "Tipo" imutável

	def __call__(*args):

		raise Exception("Você não pode instanciar um objeto imutável")

	def __setattr__(*args):
		
		raise Exception("Você não pode modificar um objeto imutável")


class UUIDS(object):

	# Serviços e especificações do smartwatch

	__metaclass__ = Imutavel

	BASE = "0000%s-0000-1000-8000-00805f9b34fb"

	SERVICO_MIBAND1 = BASE % 'fee0'
	SERVICO_MIBAND2 = BASE % 'fee1'

	SERVICO_ALERTA = BASE % '1802'
	SERVICO_ALERTA_NOTIFICACAO = BASE % '1811'
	SERVICO_FREQ_CARD = BASE % '180d'
	SERVICO_INFO_DISPOSITIVO = BASE % '180a'

	CARACTERISTICA_HZ = "00000002-0000-3512-2118-0009af100700"
	CARACTERISTICA_SENSOR = "00000001-0000-3512-2118-0009af100700"
	CARACTERISTICA_AUTH = "00000009-0000-3512-2118-0009af100700"
	CARACTERISTICA_FREQ_CARD_MEDICAO = "00002a37-0000-1000-8000-00805f9b34fb"
	CARACTERISTICA_FREQ_CARD_CONTROLE = "00002a39-0000-1000-8000-00805f9b34fb"
	CARACTERISTICA_ALERTA = "00002a06-0000-1000-8000-00805f9b34fb"
	CARACTERISTICA_CUSTOM_ALERTA = "00002a46-0000-1000-8000-00805f9b34fb"
	CARACTERISTICA_BATERIA = "00000006-0000-3512-2118-0009af100700"
	CARACTERISTICA_PASSOS = "00000007-0000-3512-2118-0009af100700"
	CARACTERISTICA_LE_PARAMS = BASE % "FF09"
	CARACTERISTICA_REVISAO = 0x2a28
	CARACTERISTICA_SERIAL = 0x2a25
	CARACTERISTICA_HRDW_REVISAO = 0x2a27
	CARACTERISTICA_CONFIG = "00000003-0000-3512-2118-0009af100700"
	CARACTERISTICA_DEVICEEVENT = "00000010-0000-3512-2118-0009af100700"

	CARACTERISTICA_HORA_ATUAL = BASE % '2A2B'
	CARACTERISTICA_IDADE = BASE % '2A80'
	CARACTERISTICA_CONFIG_USUARIO = "00000008-0000-3512-2118-0009af100700"

	NOTIFICACAO_DESCRICAO = 0x2902

	# Update do firmaware
	### Tem q hackear essa parte depois para personalizar o smartwatch para nosso uso pessoal

	SERVICO_DFU_FIRMWARE = "00001530-0000-3512-2118-0009af100700"
	CARACTERISTICA_DFU_FIRMWARE = "00001531-0000-3512-2118-0009af100700"
	CARACTERISTICA_DFU_FIRMWARE_ESCREVER = "00001532-0000-3512-2118-0009af100700"

class ESTADO_AUTENT(object):

	# Relacionado à autenticação

	__metaclass__ = Imutavel

	AUTENT_OK = "Autenticação ok"
	AUTENT_FALHA = "Autenticação falhou"
	FALHA_ENCRIPTACAO_CHAVE = "Autenticação da encriptação da chave falhou, enviando uma nova"
	FALHA_ENVIO_CHAVE = "Falha do envio da chave"
	FALHA_REQU_NUMALE = "Aconteceu algo errado na requisição do nṹmero aleatório"


class TIPO_ALERTA(object):

	# Possíveis alertas

	__metaclass__ = Imutavel

	NEHUM = '\x00'
	MENSAGEM = '\x01'
	TELEFONE = '\x02'

class TIPO_FILA(object):

	# Objetos tipo fila do smartwatch

	__metaclass__ = Imutavel

	BATIMENTO = 'heart'
	RAW_ACEL = 'raw_accel'
	RAW_BATIMENTO = 'raw_heart'