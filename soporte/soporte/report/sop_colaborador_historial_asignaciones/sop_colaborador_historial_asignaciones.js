// Copyright (c) 2025, jesus flores and contributors
// For license information, please see license.txt

frappe.query_reports["SOP-COLABORADOR-HISTORIAL-ASIGNACIONES"] = {
	"filters": [
        {
            fieldname: "colaborador",
            label: __("Colaborador"),
            fieldtype: "Link",
            options: "SOP-COLABORADOR",
            reqd: 1
        }
    ]
};
