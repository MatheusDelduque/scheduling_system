# Copyright (c) 2025, Matheus Delduque and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import timedelta
from frappe.utils import get_datetime

class Appointment(Document):
    
    def autoname(self):
        """Define o name como '<Seller Full Name> -- <Client Name>'."""
        # seller é a chave (email), vamos buscar o nome completo
        seller_key = self.seller or ""
        seller_name = frappe.db.get_value("User", seller_key, "full_name") or seller_key

        client = self.client_name or "UnknownClient"
        self.name = f"Seller: {seller_name} - Client: {client}"

    def validate(self):
        # sempre recalcula antes de salvar
        self.calculate_end_date()
        self.check_conflicts()

    def calculate_end_date(self):
        if self.start_date and self.duration:
            # converte a string para datetime
            start = get_datetime(self.start_date)

            # quebra o duration "HH:MM:SS"
            h, m, s = (int(x) for x in self.duration.split(":"))
            delta = timedelta(hours=h, minutes=m, seconds=s)

            # soma corretamente
            self.end_date = start + delta

    def check_conflicts(self):
        if self.seller and self.start_date and self.end_date:
            conflict = frappe.db.exists("Appointment", {
                "seller": self.seller,
                "start_date": ("<", self.end_date),
                "end_date":   (">", self.start_date),
                "name":       ("!=", self.name)
            })
            if conflict:
                frappe.throw("This seller already has an overlapping appointment.")
