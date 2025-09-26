import frappe

def execute(filters=None):
    columns = [
        {"label": "COLABORADOR", "fieldname": "COLABORADOR", "fieldtype": "Link", "options": "SOP-EQUIPO", "width": 'auto'},
        {"label": "UNIDAD", "fieldname": "UNIDAD", "fieldtype": "Data", "width": 'auto'},
        {"label": "FECHA_INICIO", "fieldname": "FECHA_INICIO", "fieldtype": "Date", "width": 'auto'},
        {"label": "FECHA_FIN", "fieldname": "FECHA_FIN", "fieldtype": "Date", "width": 'auto'},
        {"label": "ESTADO", "fieldname": "ESTADO", "fieldtype": "Data", "width": 'auto'},
        {"label": "TIPO_ASIGNACION", "fieldname": "TIPO_ASIGNACION", "fieldtype": "Data", "width": 'auto'},
    ]

    data = []
    if filters.get("equipo"):
        data = frappe.db.sql("""
            SELECT
                a.nombre_colaborador AS COLABORADOR,
                a.unidad_colaborador AS UNIDAD,
                d.fecha_inicio AS FECHA_INICIO,
                d.fecha_fin AS FECHA_FIN,
                CASE
                    WHEN d.fecha_fin IS NULL THEN 'Asignado'
                    WHEN e.activo_sistema = 0 THEN 'Equipo Inactivo'
                    ELSE 'Finalizado'
                END AS ESTADO,
                a.tipo_asignacion AS TIPO_ASIGNACION
            FROM `tabSOP-ASIGNACIONEQUIPODETALLE` d
            INNER JOIN `tabSOP-ASIGNACIONEQUIPO` a ON d.parent = a.name
            INNER JOIN `tabSOP-EQUIPO` e ON d.equipo = e.name
            WHERE d.equipo = %s
            ORDER BY d.fecha_inicio DESC
        """, (filters.get("equipo"),), as_dict=1)

    return columns, data
