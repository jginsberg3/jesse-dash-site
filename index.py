import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from app import server # jg added this - needed for testing with local flask server
  # also, just makes the gunicorn call more straightforward
from apps import app1, app2, homepage


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
      return homepage.layout
    if pathname == '/apps/app1':
      return app1.layout
    elif pathname == '/apps/app2':
      return app2.layout
    else:
      return homepage.layout

#if __name__ == '__main__':
#    app.run_server(debug=True)