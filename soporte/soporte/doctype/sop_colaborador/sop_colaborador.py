# Copyright (c) 2025, jesus flores and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class SOPCOLABORADOR(Document):

	def before_insert(self):
		self.nombre_colaborador=" ".join([self.nombres_colaborador, self.apellidos_colaborador])

	def before_save(self):
		self.nombre_colaborador=" ".join([self.nombres_colaborador, self.apellidos_colaborador])