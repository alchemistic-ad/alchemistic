import frappe
from frappe.utils import getdate
from erpnext.accounts.doctype.journal_entry.journal_entry import JournalEntry


def autoname(doc: JournalEntry, action):
    if not doc.custom_prefix:
        return
    posting_date = getdate(doc.posting_date)
    year = str(posting_date.year)[-1]
    month = posting_date.strftime("%m")
    doc.naming_series = doc.custom_prefix + year + month + ".#"


def before_print(doc: JournalEntry, action, print_settings):
    doc.received_by = frappe.get_value("User", doc.owner, "full_name")
