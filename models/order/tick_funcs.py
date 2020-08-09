# -*- coding: utf-8 -*-
"""
	Ticket Funcs
	Encapsulate Ticket Business Rules

	Created: 			29 Aug 2019
	Last up: 	 		09 Aug 2020
"""
import datetime
import math
try:
	from num2words import num2words
except (ImportError, IOError) as err:
	_logger.debug(err)


# ---------------------------------------------------- Ticket - tools -------------
def get_company(self, tag):
	"""
	Used by Ticket
	openhealth.report_ticket_receipt_electronic
	"""
	options = {
		'name' : self.configurator.company_name,
		'ruc' : self.configurator.ticket_company_ruc,
		'address' : self.configurator.ticket_company_address,
		'phone' : self.configurator.company_phone,
		'note' : self.configurator.ticket_note,
		'description' : self.configurator.ticket_company_address,
		'warning' : self.configurator.ticket_warning,
		'website' : self.configurator.company_website,
		'email' : self.configurator.company_email,
	}
	return options[tag]
