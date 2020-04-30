# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 16:36:46 2020

Simple template for creating invoices.

@author: George
"""
import os
from datetime import date,timedelta
from InvoiceGenerator.api import Invoice, Item, Client, Provider, Creator
from InvoiceGenerator.pdf import SimpleInvoice

########## A modifier

client_name = 'Tech_Camp'
items = []
# units, cost per unit etc.
items.append(Item(40,20,description = 'Tutoring Pygame',unit = 'hours'))
items.append(Item(1,300,description = 'Course Design Pygame'))

##########

os.environ["INVOICE_LANG"] = "en"

client = Client(client_name)
provider = Provider('George Ruck Data Science', bank_account='22076047', bank_code='40-06-21')
creator = Creator('George Ruck')

inv_num = open(r'invoice_num.txt','r+')
num = inv_num.read()
inv_num.close()
os.remove('invoice_num.txt')
file = open('invoice_num.txt','w')
file.write(str(int(num) + 1))
file.close()

invoice = Invoice(client, provider, creator)
invoice.currency_locale = 'en_GB.UTF-8'
invoice.currency = '£'
invoice.date = date.today()
invoice.payback = date.today() + timedelta(days = 14)
invoice.number = int(num)

for item in items:
    invoice.add_item(item)

invoice.title = "Freelance Tech Camp - Python"

pdf = SimpleInvoice(invoice)
os.chdir(r'C:\Users\George\Documents\Invoices')
pdf.gen('{}_RUCK_{}.pdf'.format(num,client_name),generate_qr_code = True)