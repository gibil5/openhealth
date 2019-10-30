# Open Health - ODOO 9 MODULE - PYTHON

## Version 7.0

## Description
Object Oriented Module for Odoo. 
Odoo is an ERP system for small companies. 
Inherits OeHealth. 
Contains ALL the Data Model. 
Business logic is in classes and libraries.


## Author
Javier Revilla

## Website
http://jrevilla.com

## Category
- Object Oriented,
- Service Oriented, 
- Medical Services


## History
- Created: 11 Sep 2016
- Last updated: 29 Oct 2019

## Database
Postgres

## Contains
- All External Dependencies,
- All Models,
- All Users,
- All Views,
- All Security,
- All Data.


## External modules
- Spanish translation,
- Oehealth,
- Base multi image,
- Web Export View, 
- Accounting and Finance. Adjust tax to zero.


## Python Libs
- Numpy, Num2words, Pandas, QrCode, 
- Unidecode - dep
- pysftp - dep


## For PDF Reporting (tickets)
- Install wkhtmltopdf (0.12.2 v). Other versions will not work.


## For Tickets (right button printing)
- On Chrome, install extension: PDF Viewer. Link it to Adobe Reader. 


## Deprecated services
- Ooor, 
- Testcafe, 
- Auto-backup, 
- Inventory. 


## Remember Robert C. Martin
- Respect the Law of Demeter: avoid Train Wreckages. When you see more than two dots, this needs fixing.
- Do not mix the Data Model and Business Rules. Encapsulate Business Rules in a separate module. 
- Use Three layered model: Odoo Active Data - Customized Class with BR - General purpose Library.
- Handle Exceptions.
- The Database should not contain Business rules. Remove computes.


## Always clean your System
- Remove Procurement Orders, 
- Remove Stock Moves,
- Remove Products Consumables,
- Remove Computes.


## Depends': 
- base
- oehealth
- base_multi_image





## Services provided

### Products 

### Users and Groups

### Sales

### Security 

### Configurators

### Actions 

### Product Selector

### Accounting 

### Marketing 

### Management 

### Reports

### Counters 

### Companies 

### EMR

### Physicians 

### Patients 

### Containers 

### Partners

### Menus 

### Static - Style Css 
