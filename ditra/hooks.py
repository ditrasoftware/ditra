from . import __version__ as app_version

app_name = "ditra"
app_title = "Ditra"
app_publisher = "Ditra Software Srl"
app_description = "Digital Transformation Platform"
app_email = "admin@ditra.io"
app_license = "Proprietary"
required_apps = ["erpnext", "healthcare"]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/ditra/css/ditra.css"
# app_include_js = "/assets/ditra/js/ditra.js"

# include js, css files in header of web template
# web_include_css = "/assets/ditra/css/ditra.css"
# web_include_js = "/assets/ditra/js/ditra.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "ditra/public/scss/website"

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

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "ditra.utils.jinja_methods",
#	"filters": "ditra.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "ditra.install.before_install"
# after_install = "ditra.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "ditra.uninstall.before_uninstall"
# after_uninstall = "ditra.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ditra.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"ditra.tasks.all"
#	],
#	"daily": [
#		"ditra.tasks.daily"
#	],
#	"hourly": [
#		"ditra.tasks.hourly"
#	],
#	"weekly": [
#		"ditra.tasks.weekly"
#	],
#	"monthly": [
#		"ditra.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "ditra.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "ditra.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "ditra.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"ditra.auth.validate"
# ]

fixtures = [
	# {
    # 	"dt": "Module Def", 
    # 	"filters": [["name", "in", ['Ditra']]]
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
    # {
    # 	"dt": "Custom Script"
	# },
	{
		"dt": "Role", 
    	# "filters": [["name", "in", ["Customer"]]]
    },
	{
		"dt": "Custom DocPerm", 
    	# "filters": [["role", "in", ["Customer"]]]
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
    	# "or_filters": [["name", "like", "TERGAS%"], ["name", "like", "MAGALDI%"]]
    },
	{
		"dt": "Contact", 
		# "or_filters": [["name", "like", "TERGAS%"], ["name", "like", "MAGALDI%"]]
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
    	"dt": "E Commerce Settings"
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
    {
    	"dt": "Website Item"
	},
	{
    	"dt": "Item Price"
	}
]
