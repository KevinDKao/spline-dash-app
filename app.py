from dash import Dash, html

app = Dash(__name__, title="My Cool Site")

url = 'https://my.spline.design/theshipwreck-8b30202962a589f6138c7f3ec2df5f0a/' # shipwreck
url = 'https://my.spline.design/abstractgradientbackground-800f4c0a1123415c428cfe8835cacb6e/' # Bubblegun

app.layout = html.Div([
    html.Iframe(
        src=url,
        style={
            'width': '100%',
            'height': '100vh',
            'border': 'none'
        }
    )
], style={
    'width': '100%',
    'height': '100vh',
    'margin': 0,
    'padding': 0
})

if __name__ == '__main__':
    app.run_server(debug=True, host='192.168.0.235', port=8050)