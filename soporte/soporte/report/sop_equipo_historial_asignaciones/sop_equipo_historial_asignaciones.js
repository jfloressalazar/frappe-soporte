frappe.query_reports["SOP-EQUIPO-HISTORIAL-ASIGNACIONES"] = {
    "filters": [
        {
            fieldname: "equipo",
            label: __("Equipo"),
            fieldtype: "Link",
            options: "SOP-EQUIPO",
            reqd: 1
        }
    ]
};