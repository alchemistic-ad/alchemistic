import frappe
from erpnext.projects.doctype.project.project import Project


def autoname(doc: Project, action):
    doc.naming_series = doc.project_name[0].upper() + ".###"
