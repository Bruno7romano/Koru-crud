from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__, static_url_path='/static', static_folder='static', template_folder='templates')


db = ["fork@teste.com","korao@example.com", "koruzim@example.com", "koruzito@gmail.com", "koru@yahoo.com", "superkoru@hotmail.com", "korukoru@outlook.com"]

usuarios = {}

adms = {
    1: {
        "nome" : "Rafael Muniz",
        "email" : "rafaelmuniz@gmail.com"
    },
    2: {
        "nome" : "Cléber Santos",
        "email" : "clebersantos@gmail.com"
    },
    3: {
        "nome" : "Leonardo Taian",
        "email" : "leonardotaian@gmail.com"
    }
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/verificar_email', methods=['POST'])
def verificar_email():
    email = request.form.get('email')

    if email in db:
        mensagem = "E-mail já inscrito."
    else:
        db.append(email)
        mensagem = "Inscrito com sucesso!"

    return render_template('index.html', mensagem=mensagem)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'koru' and password == 'koru':
            return render_template('adm.html', emails=db)
        else:
            mensagem = 'User não autorizado'
            return render_template('login.html', mensagem=mensagem)

    return render_template('login.html')



@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        usuarios[email] = {
        'nome' : nome,
        'email' : email,
        'senha' : senha
    }
    return render_template('cadastro.html')

@app.route("/admns")
def administradores():
    return render_template('adms.html', adms = adms)






if __name__ == '__main__':
    app.run(debug=True)

# alt to push
