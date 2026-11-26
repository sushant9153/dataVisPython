from dash import Dash, dcc, html, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px

# Step 1: Load Iris dataset
df = px.data.iris()

# Step 2: Initialize Dash application
app = Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])

# Step 3: Create dashboard layout
app.layout = html.Div([

    html.H1("Iris Flower Dashboard Analysis"),

    html.Label("Select Flower Species"),

    dcc.Dropdown(
        id="species_dropdown",
        options=[
            {"label": "Setosa", "value": "setosa"},
            {"label": "Versicolor", "value": "versicolor"},
            {"label": "Virginica", "value": "virginica"}
        ],
        value="setosa",
        clearable=False
    ),

    dcc.Graph(id="iris_graph")

])

# Step 4: Create callback
@app.callback(
    Output("iris_graph", "figure"),
    Input("species_dropdown", "value")
)

def update_graph(selected_species):

    # Filter dataset
    filtered_df = df[
        df["species"] == selected_species
    ]

    # Generate graph
    fig = px.scatter(
        filtered_df,
        x="sepal_width",
        y="sepal_length",
        color="species",
        title=f"Iris Analysis: {selected_species}"
    )

    return fig


# Step 5: Run application
if __name__ == "__main__":
    app.run(debug=True)