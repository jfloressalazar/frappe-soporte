// Copyright (c) 2025, jesus flores and contributors
// For license information, please see license.txt

frappe.ui.form.on("SOP-ASIGNACIONEQUIPO", {
    refresh: function (frm) {

        frm.set_query("link_colaborador", function () {
            return {
                filters: {
                    activo_sistema: 1,
                },
            };
        });
    },

    refresh: function(frm) {
        frm.fields_dict["tbl_detalleasignacion"].grid.get_field("equipo").get_query = function(doc, cdt, cdn) {
            return {
                filters: {
                    activo_sistema: 1
                }
            };
        };
    }
});
