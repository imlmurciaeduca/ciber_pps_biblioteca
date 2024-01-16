import psycopg2
from flask import Flask, request, jsonify

# Instanciamos Flask
app = Flask(__name__)

# Conectamos con nuestra BBDD
conn = psycopg2.connect(host = 'mi-postgres', port = '5432', database = 'pps_database', user = 'postgres', password = '1234')
cur = conn.cursor()

@app.route('/')
def index():
    return 'Aquí no hay nada que ver'

@app.route('/usuarios/listar')
def listar_usuarios():    
    cur.execute('SELECT * FROM usuarios')
    
    resultados = [{'nombre': nombre, 'email': email} for _, nombre, email in cur.fetchall()]
        
    return jsonify(resultados)
      
def insertar_usuario(nombre: str, email: str):
    cur.execute(f'INSERT INTO usuarios(nombre, email) VALUES(\'{nombre}\', \'{email}\')')
    conn.commit()

@app.route('/usuarios/add', methods = ['POST'])
def add_usuario():
    data = dict(request.get_json())
    nombre = data['nombre']
    email = data['email']
    insertar_usuario(nombre, email)
    return jsonify(success=True, nombre = nombre, email = email)

app.run(host='0.0.0.0')