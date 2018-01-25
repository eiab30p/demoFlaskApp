"""
Configuration File.

The Configuration is simply going to set up your basic needs. For this example
we are going to enable cross-site request forgery or CSRF. This helps with
prevention of unauthorized commands to be transmitted from the app.

The SECRET_KEY is in fact redicoulse for a reason but it is only needed when
CSRF is enabled, and is used to create a cryptographic token that is used to
validate a form.

"""

WTF_CSRF_ENABLED = True
SECRET_KEY = 'MS8%rZuzrbEKuhF63e!!a^HuL'
