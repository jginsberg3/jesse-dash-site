import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

layout = html.Div([
	html.Div([
		html.H3('This is the awesome homepage!')
	]),
	html.Div([
		dcc.Link('Go to App 1', href='/apps/app1')
	]),
	html.Div([
		dcc.Link('Go to App 2', href='/apps/app2')
	])
])