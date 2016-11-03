from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin import BaseView, expose
from flask_admin.base import MenuLink, Admin, BaseView, expose
from clinicaladmin.database import db, app, ApplicationDetails, ApplicationTagData, MethodDescription, Customers, Invoice

class PriceView(ModelView):
    column_list = (['application_tag', 'version', 'date_valid_from', 'standard_price', 'priority_price', 'express_price', 'research_price', 'accredited', 'description','comment', 'percent_charged_to_kth'])
    column_searchable_list = (['application_tag'])
    column_default_sort = 'date_valid_from'

class MethodDescriptionView(ModelView):
    column_searchable_list = (['method', 'method_nr'])
    column_default_sort = 'method_nr'

class CustView(ModelView):
    column_searchable_list = (['customer_number', 'customer_name', 'agreement_date', 'primary_contact_name', 'primary_contact_email', 'primary_contact_delivery_name', 'primary_contact_delivery_email', 'access_to_scout', 'uppmax_account', 'agreement_diarie_number', 'clinical_genomics_project_account_KI', 'clinical_genomics_project_account_KTH', 'organisation_number', 'invoicing_address', 'invoicing_reference', 'invoicing_contact_person', 'invoicing_email'])
    column_default_sort = 'customer_number'


class AppTagView(ModelView):
    column_searchable_list = (['application_tag', 'created_at', 'minimum_order', 'sequencing_depth', 'sample_amount', 'sample_volume', 'sample_concentration', 'turnaround_time', 'priority_processing'])
    column_default_sort = 'application_tag'

class InvoiceView(ModelView):
    column_searchable_list = (['invoice_id','customer', 'invoice_date'])
    column_default_sort = 'invoice_date'



@app.route('/')
def index():
    return '<a href="/AppTags">The Application Tag Database</a>'


def main():
    admin_db = Admin(app, name='AppTags', template_mode='bootstrap3', url='/AppTags')
    admin_db.add_link(MenuLink(name='Back Home', url='/'))

    admin_db.add_view(AppTagView(ApplicationTagData, db.session , endpoint ='ApplicationTagData' , name = "Application Tags" ))     #category = "List"
    admin_db.add_view(PriceView(ApplicationDetails, db.session,  endpoint ='Details', name = "Details"))                            #category = "List"
    admin_db.add_view(MethodDescriptionView(MethodDescription, db.session , endpoint ='MethodDescription' , name = "Method Descriptions" ))
    admin_db.add_view(CustView(Customers, db.session , endpoint ='Customers' , name = "Customers" ))
    admin_db.add_view(InvoiceView(Invoice, db.session , endpoint ='Invoices' , name = "Invoices" ))

    # Adding filter list
#    admin_db.add_link(MenuLink(name='WGS research', category='Filters', url='http://localhost:5000/AppTags/InvoiceData/?flt0_0=res&flt2_7=whol'))
#    admin_db.add_link(MenuLink(name='WGS clinical', category='Filters', url='http://localhost:5000/AppTags/InvoiceData/?flt0_0=cl&flt1_7=whol'))

    app.secret_key = 'mayapapaya'
    app.run(debug=True)




if __name__ == "__main__":
    main()






