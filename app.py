# _*_ coding: utf-8 _*_
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
        'background': '#111111',
        'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(children='My First Dash App',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Dash: A Web Application Framework for Python.',
        style={
            'textAlign':'center',
            'color': colors['text']
        }
        ),

    dcc.Graph(
        id='example-graph',
        figure={
            'data':[
                {'x': [1, 2, 3, 4], 'y': [4, 1, 2, 3], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3, 4], 'y': [2, 4, 5, 7], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization',
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
