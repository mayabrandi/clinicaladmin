from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose
from flask_admin.base import MenuLink, Admin, BaseView, expose
from clinicaladmin.database import db, app, ApplicationDetails, ApplicationTagData, MethodDescription, Customers

class PriceView(ModelView):
    column_searchable_list = (['application_tag'])
    column_default_sort = 'date_valid_from'
    column_filters = (['application_tag'])

class MethodDescriptionView(ModelView):
    column_list = ('method', 'version', 'method_nr', 'information', 'limitations')
    column_searchable_list = (['method', 'method_nr'])

class CustView(ModelView):
    column_searchable_list = (['customer_name', 'customer_number'])

class AppTagView(ModelView):
    #column_list = ('application_tag', 'created_at', 'minimum_order', )
    column_searchable_list = (['application_tag'])
    column_default_sort = 'application_tag'

# Flask views
@app.route('/')
def index():
    return '<a href="/AppTags">The Application Tag Database</a>'


def main():
    invoice = Admin(app, name='AppTags', template_mode='bootstrap3', url='/AppTags')
    invoice.add_link(MenuLink(name='Back Home', url='/'))


    invoice.add_view(AppTagView(ApplicationTagData, db.session , endpoint ='ApplicationTagData' , name = "Application Tags" )) #category = "List"
    invoice.add_view(PriceView(ApplicationDetails, db.session,  endpoint ='Details', name = "Details")) #category = "List"


    invoice.add_view(MethodDescriptionView(MethodDescription, db.session , endpoint ='MethodDescription' , name = "Method Descriptions" ))

    invoice.add_view(CustView(Customers, db.session , endpoint ='Customers' , name = "Customers" ))

    # Adding filter list
#    invoice.add_link(MenuLink(name='WGS research', category='Filters', url='http://localhost:5000/AppTags/InvoiceData/?flt0_0=res&flt2_7=whol'))
#    invoice.add_link(MenuLink(name='WGS clinical', category='Filters', url='http://localhost:5000/AppTags/InvoiceData/?flt0_0=cl&flt1_7=whol'))

    app.secret_key = 'mayapapaya'
    app.run(debug=True)




if __name__ == "__main__":
    main()






