import frappe
from frappe.utils import getdate, in_words
from erpnext.accounts.doctype.journal_entry.journal_entry import JournalEntry
from erpnext import get_company_currency


def autoname(doc: JournalEntry, action):
    if not doc.custom_prefix:
        return
    posting_date = getdate(doc.posting_date)
    year = str(posting_date.year)[-1]
    month = posting_date.strftime("%m")
    doc.naming_series = doc.custom_prefix + year + month + ".#"


def before_print(doc: JournalEntry, action, print_settings):
    doc.received_by = frappe.get_value("User", doc.owner, "full_name")
    doc.total_debit_in_words = (
        get_company_currency(doc.company) + " " + in_words(doc.total_debit)
    )
    doc.empty_rows = max(0, 7 - len([x for x in doc.accounts if x.user_remark]))

    for d in doc.accounts:
        if d.debit_in_account_currency > 0:
            d.amount = d.debit_in_account_currency
        else:
            d.amount = d.credit_in_account_currency
