import csv
import json
import ast
from clinicaladmin.database import db, ApplicationDetails, ApplicationTagData, MethodDescription, Customers

db.drop_all()
db.create_all()


def set_simple_table(csv_file, model_class ):
    f=open(csv_file, 'rU')
    rdr = csv.reader(f, lineterminator = '\r')
    headers = rdr.next()
    reader = csv.DictReader( f, headers)
    out = json.dumps([ row for row in reader ], encoding = 'latin1')
    dict_list = ast.literal_eval(out)
    for line in dict_list:
        model = model_class()
        for key, val in line.items():
            model.__dict__[key] = val
        db.session.add(model)
        db.session.commit()

def set_price_table(csv_file): #Depends on Prices
    f=open(csv_file, 'rU')
    rdr = csv.reader(f, lineterminator = '\r')
    headers = rdr.next()
    reader = csv.DictReader( f, headers)
    out = json.dumps( [ row for row in reader ], encoding = 'latin1')
    dict_list = ast.literal_eval(out)
    for line in dict_list:
        model = ApplicationDetails()
        app_tag = line['application_tag']        
        app_tag_data = ApplicationTagData.query.filter_by(application_tag = app_tag).first()
        model.application_tag_data =  app_tag_data
        model.application_tag = app_tag_data.application_tag
        for key, val in line.items():
            model.__dict__[key] = val
        db.session.add(model)
        db.session.commit()


csv_file = '/tmp/application_tags.csv'
set_simple_table(csv_file, ApplicationTagData)

csv_file = '/tmp/methods.csv'
set_simple_table(csv_file, MethodDescription)

csv_file = '/tmp/custs.csv'
set_simple_table(csv_file, Customers)

csv_file = '/tmp/Invoice.csv'
set_simple_table(csv_file, Customers)

csv_file = '/tmp/prices.csv'
set_price_table(csv_file)




