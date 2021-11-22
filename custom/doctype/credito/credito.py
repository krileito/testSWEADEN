# Copyright (c) 2021, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from __future__ import unicode_literals
import frappe
from frappe.utils import getdate
from frappe.utils import today
from frappe.utils import (flt, getdate, get_first_day, get_last_day, date_diff,
    add_months, add_days, formatdate, cint)
from frappe import _
from frappe.model.document import Document

class credito(Document):
	def before_insert(self):
		if len(self.ci) <=9:
			frappe.throw('numero de cedula del socio es menor a 10 caracteres')


		if len(self.ci_conyuge) <=9 :
			frappe.throw('numero de cedula del garante es menor a 10 caracteres')


		if int(formatdate(self.fecha_de_nacimiento,'yyyy')) < 2003 :
			frappe.throw('es menor de edad')

		if int(formatdate(self.fecha_de_nacimiento_conyugue,'yyyy')) < 2003 :
			frappe.throw('es menor de edad el garante')