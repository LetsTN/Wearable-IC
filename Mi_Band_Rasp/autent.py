
import struct
import time
import logging
import crc16
import os

from bluepy.btle import DefaultDelegate, Peripheral, ADDR_TYPE_RANDOM, BTLEException
from datetime import datetime
from Crypto.Cipher import AES
from Queue import Queue, Empty

from constantes import UUIDS, ESTADO_AUTENTICACAO, TIPOS_ALERTA, TIPO_FILA

class DelegaAutenticacao(DefaultDelegate):
	""" Essa classe herda de DefaultDelegate para lidar com o processo de autenticação """

	def __init__(self,dispositivo):
		DefaultDelegate.__init__(self)
		self.device = dispositivo

	def handleNotification(self, hnd, data):
		if hnd == self.device._char_auth.getHandle():

			if data[:3] == b'\x10\x01\x01':
				self.device._req_rdn()

			elif data[:3] == b'\x10\x01\x04':
				self.device.state = ESTADO_AUTENTICACAO.ENVIO_CHAVE_FALHOU

			elif data[:3] == b'\x10\x02\x01':
				# 16 bytes
				random_nr = data[3:]
				self.device._send_enc_rdn(random_nr)

			elif data[:3] == b'\x10\x02\x04':
				self.device.state = ESTADO_AUTENTICACAO.REQUISICAO_NA_FALHOU

			elif data[:3] == b'\x10\x03\x01':
				self.device.state = ESTADO_AUTENTICACAO.AUTENTICACAO_OK

			elif data[:3] == b'\x10\x03\x04':
				self.device.status = ESTADO_AUTENTICACAO.ENCRIPTACAO_CHAVE_FALHOU
				self.device._send_key()

			else:
				self.device.state = ESTADO_AUTENTICACAO.AUTENTICACAO_FALHOU

		elif hnd == self.device._char_heart_measure.getHandle():
			self.device.queue.put((TIPO_FILA.BATIMENTOS, data))

		elif hnd == 0x38:
			# Parece que não foi testado, mas n vou tirar isso daq n
			if len(data) == 20 and struct.unpack('b', data[0])[0] == 1:
				self.device.queue.put((TIPO_FILA.ACEL_BRUTA, data))

			elif len(data) == 16:
				self.device.queue.put((TIPO_FILA.BAT_BRUTO, data))

		else:
			self.device._log.error("Unhandled Response " + hex(hnd) + ": " + str(data.encode("hex")) + " len:" + str(len(data)))


class MiBand3(Peripheral):

	_KEY = b'\x01\x23\x45\x67\x89\x01\x22\x23\x34\x45\x56\x67\x78\x89\x90\x02'
	_send_key_cmd = struct.pack('<18s', b'\x01\x08' + _KEY)
	_send_rnd_cmd = struct.pack('<2s', b'\x02\x08')
	_send_enc_key = struct.pack('<2s', b'\x03\x08')

	def __init__(self, end_mac, timeout = 0.5, debug = False):
		