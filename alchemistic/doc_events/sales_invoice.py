import frappe
from frappe.utils import getdate
from erpnext.accounts.doctype.sales_invoice.sales_invoice import SalesInvoice


def autoname(doc: SalesInvoice, action):
    posting_date = getdate(doc.posting_date)
    year = str(posting_date.year)[-1]
    month = posting_date.strftime("%m")
    prefix = doc.customer[0].upper()
    if doc.project:
        prefix = doc.project[0].upper()
    doc.naming_series = prefix + year + month + ".#"
