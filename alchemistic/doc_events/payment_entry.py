import frappe


def before_print(doc, action, print_settings):
    doc.received_by = frappe.get_value("User", doc.owner, "full_name")
