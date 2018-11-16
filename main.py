from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from App.route import route

app = Flask(__name__)
app.register_blueprint(route, url_prefix='/api/v1')
app.config.from_object('config.DefaultConfig')
db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)