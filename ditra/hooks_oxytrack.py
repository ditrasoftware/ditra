from . import __version__ as app_version
from frappe import __version__ as frappe_version
from frappe import _

app_name = "oxytrack"
app_title = "Oxytrack"
app_publisher = "Ditra Software"
app_description = "Medical products supply-chain management platform"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@oxytrack.io"
app_license = "Ditra Software License"
# app_logo_url = "/assets/oxytrack/images/oxytrack-favicon.svg"
app_logo_url = "/assets/oxytrack/images/oxytrack-logo.png"
guest_title = app_title

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/css/oxytrack.css"
app_include_js = ["/assets/js/oxytrack.min.js"]

# include js, css files in header of web template
web_include_css = ["/assets/css/oxytrack-web.css", "/assets/css/oxytrack.css"]
web_include_js = ["/assets/js/oxytrack.min.js", "/assets/js/control.min.js", "/assets/js/dialog.min.js", "/assets/js/oxytrack-web.min.js"]

# include custom scss in every website theme (without file extension ".scss")
website_theme_scss = "oxytrack/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"
home_page = "landing"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }
role_home_page = {
	"Customer": "features"
}

# on_session_creation = [
# 	"oxytrack.oxytrack.custom.address.address.override",
# ]

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

website_context = {
	"brand_html": "<img class='navbar-icon' src='/assets/oxytrack/images/oxytrack-favicon.svg' />&nbsp;OxyTrack",
	# brand_html = '<div><img src="oxytrack-logo.png"> OxyTrack</div>'
	"favicon": 	"/assets/oxytrack/images/oxytrack-favicon.svg",
	# "favicon": "/assets/frappe_theme/img/favicon.ico",
	"splash_image": "/assets/oxytrack/images/oxytrack-logo.svg",
	# "top_bar_items": [
	# 	{"label": "Videos", "url": "/videos", "right": 1},
	# 	{"label": "Knowledge Base", "url": "https://kb.erpnext.com", "right": 1, "target": 'target="_blank"'},
	# ],
	# "hide_login": 1,
	"include_search": 1,
	# "page_titles": {
	# 	"kb": "ERPNext Manual"
	# },
	"js_globals": {
		"search_path": "/search"
	},
	"custom_footer": """<div class="text-extra-muted manual-feedback" style="padding-bottom: 70px;">
		<a class="underline" href="https://beta.oxytrack.io" target="_blank">
			Have questions? Ask us.</a></div>""",
}

email_brand_image = "/assets/oxytrack/images/oxytrack-logo.png"

default_mail_footer = """
	<span>
		Sent via
		<a class="text-muted" href="https://beta.oxytrack.io?source=via_email_footer" target="_blank">
			OxyTrack
		</a>
	</span>
"""


# website_route_rules = [
# 	{"from_route": "/addresses", "to_route": "Addresses"},
# 	{"from_route": "/addresses/<path:name>", "to_route": "addresses",
# 		"defaults": {
# 			"doctype": "Address",
# 			"parents": [{"label": _("Home"), "route": "features"}, {"label": _("Addresses"), "route": "addresses"}]
# 		}
# 	}
# ]

# standard_portal_menu_items = [
# 	{"title": _("Addresses"), "route": "/addresses", "reference_doctype": "Address"},
# ]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "oxytrack.utils.jinja_methods",
# 	"filters": "oxytrack.utils.jinja_filters"
# }
jenv = {
	"methods": [
		"get_address_display:frappe.contacts.doctype.address.address.get_address_display"
	]
}

# Installation
# ------------

# before_install = "oxytrack.install.before_install"
# after_install = "oxytrack.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "oxytrack.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

has_website_permission = {
	# "Sales Order": "erpnext.controllers.website_list_for_contact.has_website_permission",
	# "Quotation": "erpnext.controllers.website_list_for_contact.has_website_permission",
	# "Sales Invoice": "erpnext.controllers.website_list_for_contact.has_website_permission",
	# "Supplier Quotation": "erpnext.controllers.website_list_for_contact.has_website_permission",
	# "Purchase Order": "erpnext.controllers.website_list_for_contact.has_website_permission",
	# "Purchase Invoice": "erpnext.controllers.website_list_for_contact.has_website_permission",
	# "Material Request": "erpnext.controllers.website_list_for_contact.has_website_permission",
	# "Delivery Note": "erpnext.controllers.website_list_for_contact.has_website_permission",
	# "Issue": "erpnext.support.doctype.issue.issue.has_website_permission",
	# "Timesheet": "erpnext.controllers.website_list_for_contact.has_website_permission",
	# "Lab Test": "erpnext.healthcare.web_form.lab_test.lab_test.has_website_permission",
	# "Patient Encounter": "erpnext.healthcare.web_form.prescription.prescription.has_website_permission",
	# "Patient Appointment": "erpnext.healthcare.web_form.patient_appointments.patient_appointments.has_website_permission",
	# "Patient": "erpnext.healthcare.web_form.personal_details.personal_details.has_website_permission",
	"Address": "oxytrack.oxytrack.web_form.address.address.has_website_permission",  # WFC
	"Contact": "oxytrack.oxytrack.web_form.contact.contact.has_website_permission",  # WFC
	"Pharmacy Settings": "oxytrack.oxytrack.web_form.pharmacy_settings.pharmacy_settings.has_website_permission"  # WFC
}

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }
override_doctype_class = {
	# 'Address': 'erpnext.accounts.custom.address.ERPNextAddress'
	'Address': ['oxytrack.oxytrack.custom.address.address.OxytrackAddress'],
	'Contact': ['oxytrack.oxytrack.custom.contact.contact.OxytrackContact'],
	'Patient': ['oxytrack.oxytrack.custom.patient.patient.OxytrackPatient'],
	'Web Form': ['oxytrack.oxytrack.web_form.web_form.web_form.OxytrackWebForm']
}

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }
doc_events = {
	'Address': {
		'validate': [
			'oxytrack.utils.update_address_links',
		],
	},
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"oxytrack.tasks.all"
# 	],
# 	"daily": [
# 		"oxytrack.tasks.daily"
# 	],
# 	"hourly": [
# 		"oxytrack.tasks.hourly"
# 	],
# 	"weekly": [
# 		"oxytrack.tasks.weekly"
# 	]
# 	"monthly": [
# 		"oxytrack.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "oxytrack.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "oxytrack.event.get_events"
# }
#
override_whitelisted_methods = {
	"frappe.website.doctype.web_form.web_form.get_in_list_view_fields": "oxytrack.whitelisted.get_in_list_view_fields"
}
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "oxytrack.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"oxytrack.auth.validate"
# ]

# fixtures = [
#     {
#         "dt": ("Custom Field", "Custom Script", "Property Setter"), 
#         "filters": [["dt", "in", ("Item", "Maintenance Visit Purpose", "Quotation", "Customer")]]
#     }
# ]

fixtures = [
	# {
    # 	"dt": "Module Def", 
    # 	"filters": [["name", "in", ['Oxytrack']]]
    # },
	# {
    # 	"dt": "Doctype", 
    # 	"filters": [["name", "in", ['Product','Product Transaction', 'Product Pickup']]]
    # },
    {
		"dt": "Custom Field", 
    	"filters": [["dt", "in", ["Item", "Patient", "Customer", "Supplier", "Address", "Contact", "Product", "Product Transaction", "Prescription", "Prescription Item"]]]
    },
	{
		"dt": "Property Setter", 
    	"filters": [["doc_type", "in", ["Item", "Patient", "Customer", "Supplier", "Address", "Contact", "Product", "Product Transaction", "Prescription", "Prescription Item"]]]
    },
	{
		"dt": "Role", 
    	"filters": [["name", "in", ["Customer"]]]
    },
	{
		"dt": "Custom DocPerm", 
    	"filters": [["role", "in", ["Customer"]]]
    },
	{
    	"dt": "Supplier Group", 
    },
	{
    	"dt": "Supplier", 
    },
	{
    	"dt": "Customer Group"
	},
	{
		"dt": "Address", 
    	"or_filters": [["name", "like", "TERGAS%"], ["name", "like", "MAGALDI%"]]
    },
	{
		"dt": "Contact", 
		"or_filters": [["name", "like", "TERGAS%"], ["name", "like", "MAGALDI%"]]
    },
	{
    	"dt": "User Group"
	},
	{
    	"dt": "Web Template"
	},
	{
    	"dt": "Website Settings"
	},
	{
    	"dt": "Portal Settings"
	},
	{
    	"dt": "Healthcare Settings"
	},
	{
    	"dt": "Domain Settings"
	},
	{
    	"dt": "Item Group", 
    	# "filters": [["name", "in", ['Gas Tank','Liquid Tank']]]
    },
	{
    	"dt": "Item"
	},
	# {
    # 	"dt": "Item Price"
	# }
]

# global_search_doctypes = {
# 	"Default": [
# 		{"doctype": "Customer", "index": 0},
# 		{"doctype": "Supplier", "index": 1},
# 		{"doctype": "Item", "index": 2},
# 		{"doctype": "Patient", "index": 3},
# 		{"doctype": "Product", "index": 4},
# 		{"doctype": "Address", "index": 5},
# 		{"doctype": "Contact", "index": 6}
# 	]		
# }

