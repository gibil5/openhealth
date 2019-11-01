# Open Health - Odoo 9 Module - Python 

## Version 7.0

## Description
Object Oriented Module for the Odoo9 Python Platform. 
Odoo is an open-source ERP (Enterprise Ressource Planning) system for small companies. 
Odoo is designed to be easily extended by the addition of custom modules that replicate the Business Logic of a company. 
It also provides a high level of configuration. 

Back-end software is written in Python. Front-end software is written using XML and Javascript. We use a Postgres Database on Linux Centos7. 

Odoo's data is available from the outside for external analysis or integration with other tools. 
The model API is available over XML-RPC. JSON is used for data encapsulation. 

All data can be exported to the Excel format. 
Reporting is generated in the PDF format.


I have developed this module for a highly specialized Medical Clinic in Lima. 
It inherits a high-end third-party Medical module.


## Author
Javier Revilla 
jrevilla55@gmail.com


## Categories
- Medical Services
- Open source
- ERP
- Object Oriented
- Service Oriented
- XML-RPC
- JSON
- Javascript
- XML
- Postgres
- Linux 
- Centos7


## History
- Created: 11 Sep 2016
- Last updated: 1 Nov 2019

## Database
Postgres

## Contains
- All External Dependencies
- All Models
- All Users
- All Views
- All Security
- All Data


## Dependencies 

### External Odoo modules
- Oehealth
- Base multi image
- Web Export View 
- Accounting and Finance


### Python Libs
- Numpy
- Num2words
- Pandas
- QrCode


## For PDF Reporting (tickets)
- Install wkhtmltopdf (0.12.2 v). Other versions will not work.


## For Tickets (right button printing)
- On Chrome, install extension: PDF Viewer. Link it to Adobe Reader. 


## Deprecated services
- Ooor
- Testcafe
- Auto-backup
- Inventory


## Remember Robert C. Martin
- Respect the Law of Demeter: avoid Train Wreckages. When you see more than two dots, this needs fixing.
- Do not mix the Data Model and Business Rules. Encapsulate Business Rules in a separate module. 
- Use Three layered model: Odoo Active Data - Customized Class with BR - General purpose Library.
- Handle Exceptions.
- The Database should not contain Business rules. Remove computes.




## Classes that have been extended

- Products 

- Users and Groups

- Sales

- Security 

- Reports

- Companies 

- Physicians 

- Patients 

- Partners

- Menus 



## Classes that have been developed from scratch

- Containers 

- Configurators

- Product Selector

- Electronic Accounting 

- Marketing 

- Management 

- Counters 


## Static 
- Style in CSS 






