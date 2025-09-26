import frappe

def execute(filters=None):
    columns = [
        {"label": "INVENTARIO", "fieldname": "INVENTARIO", "fieldtype": "Data", "width": 'auto'},
        {"label": "TIPO_EQUIPO", "fieldname": "TIPO_EQUIPO", "fieldtype": "Data", "width": 'auto'},
        {"label": "MARCA", "fieldname": "MARCA", "fieldtype": "Data", "width": 'auto'},
        {"label": "MODELO", "fieldname": "MODELO", "fieldtype": "Data", "width": 'auto'},
        {"label": "SERIE", "fieldname": "SERIE", "fieldtype": "Data", "width": 'auto'},
        {"label": "CALIDAD_DE", "fieldname": "CALIDAD_DE", "fieldtype": "Data", "width": 'auto'},
        {"label": "FECHA_INICIO", "fieldname": "FECHA_INICIO", "fieldtype": "Date", "width": 'auto'},
        {"label": "FECHA_FIN", "fieldname": "FECHA_FIN", "fieldtype": "Date", "width": 'auto'},
        {"label": "ESTADO", "fieldname": "ESTADO", "fieldtype": "Data", "width": 'auto'},
        {"label": "TIPO_ASIGNACION", "fieldname": "TIPO_ASIGNACION", "fieldtype": "Data", "width": 'auto'},
    ]

    data = []
    if filters.get("colaborador"):
        data = frappe.db.sql("""
            SELECT
                e.numero_inventario AS INVENTARIO,
                e.tipo_equipo AS TIPO_EQUIPO,
                e.marca_equipo AS MARCA,
                e.modelo_equipo AS MODELO,
                e.numero_serie AS SERIE,
                e.calidad_de AS CALIDAD_DE,
                d.fecha_inicio AS FECHA_INICIO,
                d.fecha_fin AS FECHA_FIN,
                CASE
                    WHEN d.fecha_fin IS NULL THEN 'Asignación Activa'
                    WHEN e.activo_sistema = 0 THEN 'Equipo Inactivo'
                    ELSE 'Asignación Finalizada'
                END AS ESTADO,
                a.tipo_asignacion AS TIPO_ASIGNACION
            FROM `tabSOP-ASIGNACIONEQUIPODETALLE` d
            INNER JOIN `tabSOP-ASIGNACIONEQUIPO` a ON d.parent = a.name
            INNER JOIN `tabSOP-EQUIPO` e ON d.equipo = e.name
            WHERE d.parent in 
			(SELECT name FROM `tabSOP-ASIGNACIONEQUIPO` x where x.link_colaborador= %s)
            ORDER BY d.fecha_inicio DESC
        """, (filters.get("colaborador"),), as_dict=1)

    return columns, data
