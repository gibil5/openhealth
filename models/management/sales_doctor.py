# -*- coding: utf-8 -*-
"""
    Sales Doctor - Strategy

    SRP
        Responsibility of this class:
		Encapsulates a strategy for resolving a problem (business logic).

    Interface

    Created:             11 dec 2020
    Last up:             12 dec 2020
"""
from __future__ import print_function
from lib import mgt_funcs, prod_funcs, mgt_db
from physician import Physician
from mgt_order_line import MgtOrderLine

from management_db import ManagementDb

# ------------------------------------------------------------------- Class -----------------------
class SalesDoctor(object):
    """
    SalesDoctor
    """

    def __init__(self, management, date_begin, date_end, doctor_line, total_amount):
        """
        Init
        """
        print()
        print('SalesDoctor - init')

        self.management = management
        self.date_begin = date_begin
        self.date_end = date_end
        self.doctor_line = doctor_line
        self.total_amount = total_amount

# ----------------------------------------------- Update Sales -----------------
    def update(self):
        """
        Update sales by doctor
        """
        print()
        print('SalesDoctor - update')

        # Clean - Important
        self.doctor_line.unlink()

        # Init vars
        total_amount = 0
        total_count = 0
        total_tickets = 0

        # Get - Should be static method
        doctors = Physician.get_doctors(self.management)
        print(doctors)


        # Create Sales - By Doctor - All
        for doctor in doctors:
            #print(doctor.name)
            #print(doctor.active)

            # Get Orders - Must include Credit Notes
            orders, count = ManagementDb.get_orders_filter_by_doctor(self.management, self.date_begin, self.date_end, doctor.name)
            #print(orders)
            #print(count)

            if count > 0:
                self.create_doctor_data(doctor.name, orders)

    # update_sales_by_doctor

# ----------------------------------------------------------- Create Doctor Data ------------
    def create_doctor_data(self, doctor_name, orders):
        """
        Create doctor data
        """
        print()
        print('** Create Doctor Data')

        # Init Loop
        amount = 0
        count = 0
        #tickets = 0

        # Create
        doctor = self.doctor_line.create({
                                            'name': doctor_name,
                                            'management_id': self.management.id,
                                        })

        # Loop
        for order in orders:

            # For loop
            #tickets = tickets + 1

            # Filter Block
            if not order.x_block_flow:

                # For loop
                amount = amount + order.amount_total

                # State equal to Sale
                if order.state in ['sale']:

                    # Order Lines
                    for line in order.order_line:

                        # For loop
                        count = count + 1

                        # Create- Should be a class method
                        #print('*** Create Doctor Order Line !')
                        order_line = MgtOrderLine.create_oh(order, line, doctor, self.management)

                    # Line Analysis Sale - End
                # Conditional State Sale - End
                # Conditional State - End
            # Filter Block - End
        # Loop - End

        # Stats
        doctor.amount = amount
        doctor.x_count = count

        # Percentage
        if self.total_amount != 0:
            doctor.per_amo = (doctor.amount / self.total_amount)

    # create_doctor_data
