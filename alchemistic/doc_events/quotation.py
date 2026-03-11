import frappe
from frappe.utils import getdate
from erpnext.selling.doctype.quotation.quotation import Quotation


def autoname(doc: Quotation, action):
    transaction_date = getdate(doc.transaction_date)
    year = str(transaction_date.year)[-1]
    month = transaction_date.strftime("%m")
    prefix = doc.party_name[0].upper()
    doc.naming_series = prefix + year + month + ".#"
