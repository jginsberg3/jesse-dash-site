import dash
import dash_auth

from helpers.get_logins import *

# read in names-passwords
# passwords should be saved in the same path as app.py
password_file_name = 'logins'
login_list = return_login_info(password_file_name)

app = dash.Dash()
auth = dash_auth.BasicAuth(
    app,
    login_list
)
server = app.server
app.config.suppress_callback_exceptions = True

