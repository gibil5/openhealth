# -*- coding: utf-8 -*-
"""
	ticket_line.py
	TicketLine Class

	Created: 			24 Jul 2020
	Last up: 	 		24 Jul 2020
"""

class TicketLine(object):
	"""
	Used by Order.
	Contains the formatting rules. For all entries.
	Does not use Bootstrap classed. Is much more robust than the previous approach.
	Allows for easy font size config.
	"""

	def __init__(self, tag, value):
		#print 'Ticket - init'
		self.tag = tag
		self.value = value

	def format_line_items(self):
		"""
		Format Line Items
		"""
		_size_font = '2'

		# Items header
		if self.tag in ['items'] and self.value in ['header']:

			line = "<tr>\
						<td>\
							<font size='2'>\
								<b>Desc</b>\
							</font>\
						</td>\
						<td>\
							<font size='2'>\
								<b>Cnt</b>\
							</font>\
						</td>\
						<td>\
							<font size='2'>\
								<b>PUnit</b>\
							</font>\
						</td>\
						<td>\
							<font size='2'>\
								<b>Total</b>\
							</font>\
						</td>\
					</tr>"
			return line

	def get_line_items(self):
		"""
		Get Line Items
		"""
		line = self.format_line_items()
		return line

	def get_line(self):
		"""
		Get Line
		"""
		line = self.format_line_lean()
		return line

	def format_line_lean(self):
		"""
		Abstraction.
		Lean version (not bold)
		"""
		line = "<tr>\
					<td>\
						<font size='2'>" + self.tag + "</font>\
					</td>\
					<td>\
						<font size='2'>" + self.value + "</font>\
					</td>\
				</tr>"
		return line
