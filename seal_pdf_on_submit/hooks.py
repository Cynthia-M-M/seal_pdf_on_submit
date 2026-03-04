app_name = "seal_pdf_on_submit"
app_title = "Seal Pdf On Submit"
app_publisher = "Cynthia Moraa"
app_description = "Creates a PDF when a document is submitted in ERPNext"
app_icon = "octicon octicon-file-pdf"
app_color = "#DB2B39"
app_email = "cynthia@stelden.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "seal_pdf_on_submit",
# 		"logo": "/assets/seal_pdf_on_submit/logo.png",
# 		"title": "Seal Pdf On Submit",
# 		"route": "/seal_pdf_on_submit",
# 		"has_permission": "seal_pdf_on_submit.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/seal_pdf_on_submit/css/seal_pdf_on_submit.css"
# app_include_js = "/assets/seal_pdf_on_submit/js/seal_pdf_on_submit.js"

# include js, css files in header of web template
# web_include_css = "/assets/seal_pdf_on_submit/css/seal_pdf_on_submit.css"
# web_include_js = "/assets/seal_pdf_on_submit/js/seal_pdf_on_submit.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "seal_pdf_on_submit/public/scss/website"

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

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "seal_pdf_on_submit/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "seal_pdf_on_submit.utils.jinja_methods",
# 	"filters": "seal_pdf_on_submit.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "seal_pdf_on_submit.install.before_install"
# after_install = "seal_pdf_on_submit.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "seal_pdf_on_submit.uninstall.before_uninstall"
# after_uninstall = "seal_pdf_on_submit.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "seal_pdf_on_submit.utils.before_app_install"
# after_app_install = "seal_pdf_on_submit.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "seal_pdf_on_submit.utils.before_app_uninstall"
# after_app_uninstall = "seal_pdf_on_submit.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "seal_pdf_on_submit.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"seal_pdf_on_submit.tasks.all"
# 	],
# 	"daily": [
# 		"seal_pdf_on_submit.tasks.daily"
# 	],
# 	"hourly": [
# 		"seal_pdf_on_submit.tasks.hourly"
# 	],
# 	"weekly": [
# 		"seal_pdf_on_submit.tasks.weekly"
# 	],
# 	"monthly": [
# 		"seal_pdf_on_submit.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "seal_pdf_on_submit.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "seal_pdf_on_submit.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "seal_pdf_on_submit.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "seal_pdf_on_submit.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["seal_pdf_on_submit.utils.before_request"]
# after_request = ["seal_pdf_on_submit.utils.after_request"]

# Job Events
# ----------
# before_job = ["seal_pdf_on_submit.utils.before_job"]
# after_job = ["seal_pdf_on_submit.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"seal_pdf_on_submit.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

