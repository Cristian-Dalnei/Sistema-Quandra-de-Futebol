from flask import Flask, render_template, request, redirect, session
from Classes.Banco import Banco
from Classes.Horarios import Horario

app = Flask(__name__)
app.secret_key = 'minha_key'
def usuario_logado(session):
    if 'usuario' not in session:
        return redirect('/')
@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def fazer_login():
    email = request.form['email']
    senha = request.form['senha']
    id_usuario = Banco.verificar_login(email, senha)
    if id_usuario:
        session['usuario'] = id_usuario
        return redirect('/menu')
    return redirect('/')

@app.route('/sobre')
def sobre():
    resposta = usuario_logado(session)
    if resposta:
        return resposta
    return render_template('sobre.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/cadastro', methods=['POST'])
def cadastrar_cadastro():
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    email = request.form['email']
    senha = request.form['senha']
    dia = request.form['dia']
    mes = request.form['mes']
    ano = request.form['ano']
    #dic_status['cadastrado'] e ['erro']
    dic_status = Banco.cadastrar_usuario(nome, sobrenome, email, senha, ano, mes, dia)
    if dic_status['cadastrado'] == True:
        return redirect('/menu')
    else:
        erro = dic_status['erro']
        return render_template('erro_cadastro.html', erro=erro)

@app.route('/menu')
def menu():
    resposta = usuario_logado(session)
    if resposta:
        return resposta
    horario = Horario.horarios_usuario(session['usuario'])
    return render_template('menu.html', horarios=horario)

@app.route('/horarios')
def horarios():
    resposta = usuario_logado(session)
    if resposta:
        return resposta
    horario_1 = Horario.horarios_1()
    horario_2 = Horario.horarios_2()
    horario_3 = Horario.horarios_3()
    horario_4 = Horario.horarios_4()
    horario_5 = Horario.horarios_5()
    tempo_horarios = Horario.dic_tempo
    return render_template('horarios.html',
                           horario_1=horario_1,
                           horario_2=horario_2,
                           horario_3=horario_3,
                           horario_4=horario_4,
                           horario_5=horario_5,
                           tempo=tempo_horarios)

@app.route('/cadastra_horario/<int:horario_id>')
def cadastrar_horario(horario_id):
    resposta = usuario_logado(session)
    if resposta:
        return resposta
    horario = Horario.consulta_horarios(horario_id)
    info_usuario = Banco.informações_usuario(session['usuario'])
    return render_template('cadastro_horario.html', horario=horario, usuario=info_usuario)

@app.route('/confirmar_horario/<int:horario_id>', methods=['POST'])
def confirmar_horario(horario_id):
    resposta = usuario_logado(session)
    if resposta:
        return resposta
    dic_status = Horario.reservar_horario(session['usuario'], horario_id)
    return render_template('horario_reserva.html', horario=dic_status)


if __name__ == '__main__':
    app.run(debug=True)