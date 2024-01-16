import psycopg2

def listar_usuarios():
    print('##########################################')
    print('### Lista de usuarios de la Biblioteca ###')
    print('##########################################')
    print()
    
    cur.execute('SELECT * FROM usuarios')
    
    for usuario in cur.fetchall():
        _, nombre, email = usuario
        print(f'Nombre: {nombre}. Email: {email}')
        
    print()
        
        
def insertar_usuario(nombre: str, email: str):
    cur.execute(f'INSERT INTO usuarios(nombre, email) VALUES(\'{nombre}\', \'{email}\')')
    conn.commit()
    print(f'Insertado {nombre} con email {email}')
    print()
    

with psycopg2.connect(host = 'localhost', port = '5432', database = 'pps_database', user = 'postgres', password = '1234') as conn:
    cur = conn.cursor()
    
    while True:
        listar_usuarios()
        
        nombre, email = input('Introduce nombre#email: ').split('#')
        
        insertar_usuario(nombre, email)