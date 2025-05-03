// Copyright (c) 2025, Matheus Delduque and contributors
// For license information, please see license.txt// arquivo: public/js/doctype/appointment/appointment.js

frappe.ui.form.on('Appointment', {
	start_date: _update_end_date,
	duration:   _update_end_date
  });
  
  function _update_end_date(frm) {
	const sd = frm.doc.start_date;
	const du = frm.doc.duration;
	if (!sd || !du) {
	  frm.set_value('end_date', null);
	  return;
	}
  
	// Quebra "HH:MM:SS" em horas, minutos e segundos
	const [h, m, s] = du.split(':').map(n => parseInt(n, 10) || 0);
  
	// Cria um objeto moment a partir do ISO string
	const end_moment = moment(sd)
	  .add(h, 'hours')
	  .add(m, 'minutes')
	  .add(s, 'seconds');
  
	// Formata de volta para "YYYY-MM-DD HH:mm:ss"
	const new_end = end_moment.format('YYYY-MM-DD HH:mm:ss');
  
	// Atualiza o campo end_date
	frm.set_value('end_date', new_end);
  }
  