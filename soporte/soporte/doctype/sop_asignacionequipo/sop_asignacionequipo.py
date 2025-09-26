# Copyright (c) 2025, jesus flores and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import today

class SOPASIGNACIONEQUIPO(Document):
	pass

@frappe.whitelist()
def get_available_equipment(doctype, txt, searchfield, start, page_len, filters):
	fecha_actual = filters.get("fecha_actual") or today()

	# Selecciona equipos activos que no estén en una asignación activa
	return frappe.db.sql("""
		SELECT eq.name, eq.numero_inventario
		FROM `tabSOP-EQUIPO` eq
		WHERE eq.activo_sistema = 1
		AND NOT EXISTS (
			SELECT 1
			FROM `tabSOP-ASIGNACIONEQUIPODETALLE` det
			WHERE det.equipo = eq.name
				AND (det.fecha_fin IS NULL OR det.fecha_fin >= %(fecha_actual)s)
		)
		AND eq.{searchfield} LIKE %(txt)s
		ORDER BY eq.name
		LIMIT %(start)s, %(page_len)s
	""".format(searchfield=searchfield), {
		"txt": "%%%s%%" % txt,
		"start": start,
		"page_len": page_len,
		"fecha_actual": fecha_actual
	})

@frappe.whitelist()
def get_available_equipment_count():
    disponibles = frappe.db.sql("""
        SELECT COUNT(*) 
        FROM `tabSOP-EQUIPO` e
        WHERE e.activo_sistema = 1
        AND NOT EXISTS (
            SELECT 1 FROM `tabSOP-ASIGNACIONEQUIPODETALLE` d
            WHERE d.equipo = e.name
              AND (d.fecha_fin IS NULL OR d.fecha_fin > %(hoy)s)
        )
    """, {"hoy": today()})[0][0]
    return disponibles