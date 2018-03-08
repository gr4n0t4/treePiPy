### This class defines the frontend and calls to the backend
from flask import Flask, render_template
from flask_reverse_proxy import ReverseProxied
app = Flask(__name__)
app.wsgi_app = ReverseProxied(app.wsgi_app)

@app.route('/')
def index():
   return render_template('index.html')

if __name__ == '__main__':
   app.run(host='0.0.0.0',debug = True)






