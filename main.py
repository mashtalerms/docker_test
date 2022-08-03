from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)
app.config['SQL_ALCHEMY_DATABASE-URI'] = 'postgresql://flask_app:flask_app_password'

db = SQLAlchemy(app)

@app.route('/')
def index():
    test = None
    test = db.session.execute(text("SELECT 'TEST' ")).scalar()
    return f'ITS WORKING {test}'


if __name__=='__main__':
    app.run(host='0.0.0.0', port=8080)
