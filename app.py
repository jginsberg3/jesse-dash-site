import dash
import dash_auth

from helpers.get_logins import *

# read in names-passwords
# passwords should be saved in the same path as app.py
password_file_name = 'logins'
login_list = return_login_info(password_file_name)

# create the app
app = dash.Dash()

# add the app authentication
auth = dash_auth.BasicAuth(
    app,
    login_list
)

# define the app's server
server = app.server

# for dev only
app.config.suppress_callback_exceptions = True

# add Boostrap CSS
#app.css.append_css({'external_url':'https://codepen.io/chriddyp/pen/bWLwgP.css'}). # plotly official css
app.css.append_css({'external_url':'https://codepen.io/jginsberg3/pen/zJPVBq.css'}) # jg fork of the plotly official css
