import frappe
from frappe.utils import getdate
from erpnext.accounts.doctype.payment_entry.payment_entry import PaymentEntry


def autoname(doc: PaymentEntry, action):
    posting_date = getdate(doc.posting_date)
    year = str(posting_date.year)[-1]
    month = posting_date.strftime("%m")
    prefix = "PV"
    doc.naming_series = prefix + year + month + ".#"


def before_print(doc: PaymentEntry, action, print_settings):
    doc.received_by = frappe.get_value("User", doc.owner, "full_name")
