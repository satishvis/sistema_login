from app import app
from bottle import template, static_file, request

# static routes
@app.get('/<filename:re:.*\.css>')
def stylesheets(filename):
	return static_file(filename, root='app/static/css')

@app.get('/<filename:re:.*\.js>')
def javascripts(filename):
	return static_file(filename, root='app/static/js')

@app.get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
	return static_file(filename, root='app/static/img')

@app.get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
	return static_file(filename, root='app/static/fonts')


@app.route('/') # @get('/login') cai direto na página login
def login():
	return template('login')

# ir para page cadastro
@app.route('/cadastro')
def cadastro():
	return template('cadastro')	

@app.route('/cadastro', method='POST') # @post('/cadastro')
def acao_cadastro():
	username = request.forms.get('username')
	password = request.forms.get('password')
	insert_user(username, password)	
	return template('verificacao_cadastro', nome=username)

@app.route('/', method='POST') # @post('/login')
def acao_login():
	username = request.forms.get('username')
	password = request.forms.get('password')
	return template('verificacao_login', sucesso=True)

@app.error(404)
def error404(error):
	return template('pagina404')	