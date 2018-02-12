from app import app
@app.route('/')
@app.route('/index')
def index():
     user = {'username', 'bryan623'}
     return '''
     <html>
        <head>
            <title>Home - NFSNation</title>
        </head>
        <body>
        </body
    </html>
