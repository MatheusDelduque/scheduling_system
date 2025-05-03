// Copyright (c) 2025, Matheus Delduque and contributors
// For license information, please see license.txt

frappe.views.calendar["Appointment"] = {
    // Mapeia as propriedades do evento para os seus campos
    field_map: {
      id:      "name",        // id do evento       → primary key
      start:   "start_date",  // início do evento    → seu campo start_date
      end:     "end_date",    // fim do evento       → seu campo end_date
      title:   "name", // título do evento    → seu campo client_name
    },
    get_events_method: "frappe.desk.calendar.get_events",
  };
  