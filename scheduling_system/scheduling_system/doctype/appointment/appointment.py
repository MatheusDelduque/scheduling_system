# Copyright (c) 2025, Matheus Delduque and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import get_datetime
from datetime import timedelta
from frappe.model.rename_doc import rename_doc

class Appointment(Document):

    def get_title(self):
        """Gera o título padrão: 'Seller: X — Client: Y'."""
        seller_key  = self.seller or ""
        seller_name = frappe.db.get_value("User", seller_key, "full_name") or seller_key
        client      = self.client_name or ""
        return f"Seller: {seller_name} — Client: {client}"
        
    def validate(self):
        """Antes de salvar, recalcula end_date e verifica conflitos."""
        self.calculate_end_date()
        self.check_conflicts()

    def on_update(self):
        """Após salvar: renomeia se o título (name) mudou."""
        new_name = self.get_title()
        if self.name != new_name:
            rename_doc(self.doctype, self.name, new_name)
            # atualiza self.name no objeto para manter o form consistente
            self.name = new_name

        if self.name != new_name:
            # Renomeia o documento no banco de dados
            rename_doc(self.doctype, self.name, new_name)
            # Atualiza o atributo name em memória para manter o form consistente
            self.name = new_name

    def calculate_end_date(self):
        """Define end_date = start_date + duration."""
        if self.start_date and self.duration:
            start_dt = get_datetime(self.start_date)
            h, m, s = (int(x) for x in self.duration.split(":"))
            delta = timedelta(hours=h, minutes=m, seconds=s)
            self.end_date = start_dt + delta

    def check_conflicts(self):
        """Evita sobreposição de compromissos para o mesmo seller."""
        if self.seller and self.start_date and self.end_date:
            conflict = frappe.db.exists("Appointment", {
                "seller": self.seller,
                "start_date": ("<", self.end_date),
                "end_date":   (">", self.start_date),
                "name":       ("!=", self.name)
            })
            if conflict:
                frappe.throw("This seller already has an overlapping appointment.")