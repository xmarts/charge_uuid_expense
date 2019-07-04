# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import tempfile
import base64
import os
from lxml import etree, objectify
from xml.etree import ElementTree as ET

class HRExpense(models.Model):
	_inherit = "hr.expense"

	xml_file = fields.Binary(string="Archivo XML")
	xml_filename = fields.Char('File Name')
	xml_uuid = fields.Char(string="Folio Fiscal")

	@api.onchange('xml_file')
	def onchange_read_xml_uuid(self):
		if self.xml_file:
			result = self.xml_file.encode('utf-8')
			data = base64.decodestring(result)
			fobj = tempfile.NamedTemporaryFile(delete=False)
			fname = fobj.name
			fobj.write(data)
			fobj.close()
			file_xml = open(fname,"r")
			tree = objectify.fromstring(file_xml.read().encode())
			if self._get_stamp_data(tree) == None:
				self.xml_uuid = 'Error en archivo XML'
			else:
				tfd = self._get_stamp_data(tree)
				self.xml_uuid = tfd.get('UUID')
		else: 
			self.xml_uuid = 'XML no cargado'



	@api.model
	def _get_stamp_data(self, cfdi):
		self.ensure_one()
		if not hasattr(cfdi, 'Complemento'):
			return None
		attribute = 'tfd:TimbreFiscalDigital[1]'
		namespace = {'tfd': 'http://www.sat.gob.mx/TimbreFiscalDigital'}
		node = cfdi.Complemento.xpath(attribute, namespaces=namespace)
		return node[0] if node else None