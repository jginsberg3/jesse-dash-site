import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

layout = html.Div([

	html.Div([
		html.Div([
			html.H2('This is the awesome homepage!')
		], className='homepagetitle'),


		html.Div('''
                This is an example of a simple Dash app with
                local, customized CSS.
            ''', className="dummy"),

		html.Div([
			html.H5('Here are some awesome web apps to try:', )
		])

	], className='row'),


	html.Div([
		html.Div([
			dcc.Link('Go to App 1', href='/apps/app1')
		], className='six columns'),

		html.Div([
			dcc.Link('Go to App 2', href='/apps/app2')
		], className='six columns')
	], className='row'),


	html.Div([
		html.P('This is the footer.', className='footer')
	])

])

