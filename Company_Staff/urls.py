from django.urls import path
from . import views

urlpatterns = [
    # -------------------------------Company section--------------------------------
    path('Company/Dashboard',views.company_dashboard,name='company_dashboard'),
    path('Company/Staff-Request',views.company_staff_request,name='company_staff_request'),
    path('Company/Staff-Request/Accept/<int:pk>',views.staff_request_accept,name='staff_request_accept'),
    path('Company/Staff-Request/Reject/<int:pk>',views.staff_request_reject,name='staff_request_reject'),
    path('Company/All-Staffs',views.company_all_staff,name='company_all_staff'),
    path('Company/Staff-Approval/Cancel/<int:pk>',views.staff_approval_cancel,name='staff_approval_cancel'),
    path('Company/Profile',views.company_profile,name='company_profile'),
    path('Company/Profile-Editpage',views.company_profile_editpage,name='company_profile_editpage'),
    path('Company/Profile/Edit/Basicdetails',views.company_profile_basicdetails_edit,name='company_profile_basicdetails_edit'),
    path('Company/Password_Change',views.company_password_change,name='company_password_change'),
    path('Company/Profile/Edit/Companydetails',views.company_profile_companydetails_edit,name='company_profile_companydetails_edit'),
    path('Company/Module-Editpage',views.company_module_editpage,name='company_module_editpage'),
    path('Company/Module-Edit',views.company_module_edit,name='company_module_edit'),
    path('Company/Renew/Payment_terms',views.company_renew_terms,name='company_renew_terms'),
   
    







    # -------------------------------Staff section--------------------------------
    path('Staff/Dashboard',views.staff_dashboard,name='staff_dashboard'),
    path('Staff/Profile',views.staff_profile,name='staff_profile'),
    path('Staff/Profile-Editpage',views.staff_profile_editpage,name='staff_profile_editpage'),
    path('Staff/Profile/Edit/details',views.staff_profile_details_edit,name='staff_profile_details_edit'),
    path('Staff/Password_Change',views.staff_password_change,name='staff_password_change'),



    # -------------------------------Zoho Modules section--------------------------------
    #---------------------------------Payroll employee-----------------------------------
    path('Company/payroll_employee_create',views.payroll_employee_create,name='payroll_employee_create'),
    path('Company/payroll_employee_list',views.employee_list,name='employee_list'),
    path('Company/payroll_employee_overview/<int:pk>',views.employee_overview,name='employee_overview'),
    path('Company/create_employee',views.create_employee,name='create_employee'),
    path('Company/payroll_employee_edit/<int:pk>',views.payroll_employee_edit,name='payroll_employee_edit'),
    path('Company/do_payroll_edit/<int:pk>',views.do_payroll_edit,name='do_payroll_edit'),
    path('Company/add_comment/<int:pk>',views.add_comment,name='add_comment'),
    path('Company/delete_comment/<int:pk>/<int:pi>',views.delete_commet,name='delete_comment'),
    path('Company/delete_employee/<int:pk>',views.delete_employee,name='delete_employee'),
    path('Company/employee_status/<int:pk>',views.employee_status,name='employee_status'),
    path('Company/add_blood',views.add_blood,name='add_blood'),
    path('company/import_payroll_excel',views.import_payroll_excel,name='import_payroll_excel'),
    path('Company/add_file/<int:pk>',views.add_file,name='add_file'),
    
    
]