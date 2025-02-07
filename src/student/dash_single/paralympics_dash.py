# Imports for Dash and Dash.html
from dash import Dash, html
import dash_bootstrap_components as dbc

meta_tags = [
    {"name": "viewport", "content": "width=device-width, initial-scale=1"},
]
# Variable that contains the external_stylesheet to use, in this case Bootstrap styling from dash bootstrap components (dbc)
external_stylesheets = [dbc.themes.BOOTSTRAP]
app = Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags)

row_one = dbc.Row([
    dbc.Col(children=[
        html.H1("Paralympics Data Analytics"),
        html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent congue luctus elit nec gravida.")]),
])
r2_c1 = dbc.Select(
    options=[
        {"label": "Events", "value": "events"},  # The value is in the format of the column heading in the data
        {"label": "Sports", "value": "sports"},
        {"label": "Countries", "value": "countries"},
        {"label": "Athletes", "value": "participants"},
    ],
    value="events",  # The default selection
    id="dropdown-input",  # id uniquely identifies the element, will be needed later for callbacks
)
r2_c2 = html.Div(
    [
        dbc.Label("Select the Paralympic Games type"),
        dbc.Checklist(
            options=[
                {"label": "Summer", "value": "summer"},
                {"label": "Winter", "value": "winter"},
            ],
            value=["summer"],  # Values is a list as you can select 1 AND 2
            id="checklist-input",
        ),
    ]
)
r3_c1 = html.Img(src=app.get_asset_url('line-chart-placeholder.png'), className="img-fluid")
r3_c2 = html.Img(src=app.get_asset_url('bar-chart-placeholder.png'), className="img-fluid")
r4_c1 = html.Img(src=app.get_asset_url('map-placeholder.png'), className="img-fluid")

r4_c2 = dbc.Card([
    dbc.CardImg(src=app.get_asset_url("logos/2022_Beijing.jpg"),top=True),
    dbc.CardBody([html.H4("Beijing 2022", className="card-title"),
        html.P("Number of athletes: XX", className="card-text", ),
        html.P("Number of events: XX", className="card-text", ),
        html.P("Number of countries: XX", className="card-text", ),
        html.P("Number of sports: XX", className="card-text", ),
    ]),
],
    style={"width": "18rem"},

)

row_two = dbc.Row([
    dbc.Col(children=[r2_c1], width=4),
    dbc.Col(children=[r2_c2], width={"size": 4, "offset": 2}),
    # 2 'empty' columns between this and the previous column
])
row_three = dbc.Row([
    dbc.Col([
        dbc.Row(children=['6 clolumns']),
        dbc.Row(children=[r3_c1])
    ]),
    dbc.Col([
        dbc.Row(children=['6 columns']),
        dbc.Row(children=[r3_c2])
    ])

])
row_four = dbc.Row([
    dbc.Col([
        dbc.Row(children=['World map']),
        dbc.Row(children=[r4_c1])
    ]),
    dbc.Col([
        dbc.Row(children=['8 columns']),
        dbc.Row(children=[r4_c2])
    ])
])
# Pass the stylesheet and meta_tag variables to the Dash app constructor

app.layout = dbc.Container([
    row_one,
    row_two,
    row_three,
    row_four
])

if __name__ == '__main__':
    app.run(debug=True)