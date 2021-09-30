#pip install flask
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


#Sempre inserir o código abaixo para iniciar a página
if __name__ == '__main__':
    app.run(debug=True)

#PAREI EM 13 MINUTOS