# -*- coding: utf-8 -*-
"""
	ticket_line.py
    TicketLine Class

	Created: 			24 Jul 2020
	Last up: 	 		24 Jul 2020
"""

class TicketLine(object):

    def __init__(self, tag, value):
    	print('Ticket - init')
        self.tag = tag 
        self.value = value 

    def get_line(self): 
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
