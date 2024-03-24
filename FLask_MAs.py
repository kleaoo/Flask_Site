from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/contacts/')
def contacts():
    developer_name = 'Сигма Сигмович'
    developer_nomer = '84957237420'
    developer_adres = 'ул. Гузовского, 30, Чебоксары этаж 1'
    return render_template('contacts.html', name=developer_name, adres=developer_adres, phone=developer_nomer)

@app.route("/info/")
def info():
    return render_template('info.html')

@app.route("/history/")
def history():
    return render_template('history.html')

if __name__ == "__main__":
    app.run(debug=True)
