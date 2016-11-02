from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import (Column, Integer, String, DateTime, Text, Enum,
                        ForeignKey, UniqueConstraint, Numeric, Date)
from sqlalchemy.orm import relationship, backref
from clinicaladmin.config import DEMULTIPLEX_DATABASE_URI

import os



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DEMULTIPLEX_DATABASE_URI
db = SQLAlchemy(app)

class Customers(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    customer_number = db.Column(db.String(500), unique=False) 
    customer_name = db.Column(db.String(500), unique=False)
    agreement_date = db.Column(db.String(500), unique=False)    
    primary_contact_name = db.Column(db.String(500), unique=False)
    primary_contact_email = db.Column(db.String(500), unique=False)
    primary_contact_delivery_name = db.Column(db.String(500), unique=False)
    primary_contact_delivery_email = db.Column(db.String(500), unique=False)
    access_to_scout = db.Column(db.String(500), unique=False)
    uppmax_account = db.Column(db.String(500), unique=False)
    agreement_diarie_number = db.Column(db.String(500), unique=False)
    clinical_genomics_project_account_KI = db.Column(db.String(500), unique=False)
    clinical_genomics_project_account_KTH = db.Column(db.String(500), unique=False)
    organisation_number = db.Column(db.String(500), unique=False)
    invoicing_address = db.Column(db.String(500), unique=False)
    invoicing_reference = db.Column(db.String(500), unique=False)
    invoicing_contact_person = db.Column(db.String(500), unique=False)
    invoicing_email = db.Column(db.String(500), unique=False)

class ApplicationDetails(db.Model):
    __tablename__ = 'details'
    id = db.Column(db.Integer, primary_key=True)
    #application_tag = db.Column(db.String(500), unique=False)
    version = db.Column(db.String(500), unique=False)
    application_tag = db.Column(db.String(500), unique=False) #db.Column(db.String(50), db.ForeignKey('application_tags.application_tag'))
    application_tag_id = db.Column(db.ForeignKey('application_tags.id'), nullable=False)
    application_tag_data = relationship('ApplicationTagData', backref=backref('details'))
    date_valid_from = db.Column(db.String(500), unique=False)
    express_price = db.Column(db.String(500), unique=False)
    standard_price = db.Column(db.String(500), unique=False)
    priority_price = db.Column(db.String(500), unique=False)
    research_price = db.Column(db.String(500), unique=False)
    accredited = db.Column(db.String(500), unique=False)
    description = db.Column(db.String(500), unique=False)
    comment = db.Column(db.String(500), unique=False)


    def __repr__(self):
        return '{} v{}'.format(self.application_tag, self.version)

#(u"{self.application_tag_data.application_tag}: {self.application_tag_data.application_tag_version}"
                #.format(self=self))


class ApplicationTagData(db.Model):
    __tablename__ = 'application_tags'
    id = db.Column(db.Integer, primary_key=True)
#    details_id = db.Column(db.ForeignKey('details.id'))
#    details = relationship('ApplicationDetails', cascade='all,delete', backref='application')
    application_tag = db.Column(db.String(50), unique=False)
    created_at = db.Column(db.String(500), unique=False)
    minimum_order = db.Column(db.String(500), unique=False)
    sequencing_depth = db.Column(db.String(500), unique=False)
    sample_amount = db.Column(db.String(500), unique=False)
    sample_volume = db.Column(db.String(500), unique=False)
    sample_concentration = db.Column(db.String(500), unique=False)
    turnaround_time = db.Column(db.String(500), unique=False)
    priority_processing = db.Column(db.String(500), unique=False)
    

    def __repr__(self):
        return self.application_tag

class MethodDescription(db.Model):
    __tablename__ = 'methods'
    id = db.Column(db.Integer, primary_key=True)
    method = db.Column(db.String(500), unique=False)
    method_nr = db.Column(db.String(500), unique=False)
    information = db.Column(db.String(500), unique=False)
    limitations = db.Column(db.String(500), unique=False)
    version = db.Column(db.String(500), unique=False)




