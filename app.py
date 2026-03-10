#conexão com mysql
from flask import Flask, render_template, request, redirect,url_for
import mysql.connector
app = Flask(__name__)
# Configurações do banco de dados
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='sistemacontas'
    )
# Rota para exibir a página inicial
@app.route('/')
def index():
    try:
        conn = get_db_connection()
        cursor=conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM despesas")
        dados = cursor.fetchall()
        # soma
        cursor.execute("SELECT SUM(valor) AS total FROM despesas")
        total = cursor.fetchone()
        total_geral= total['total'] if total['total']else 0
        # A pagar
        # cursor.execute("SELECT total - pago AS restante FROM despesas")
        # restante=cursor.fetchone()
        # totalFinal=restante['restante']if restante['restante'] else 0

        # soma por categoria
        cursor.execute("SELECT categoria, SUM(valor) AS total_categoria FROM despesas GROUP BY categoria")
        total_por_categoria = {row['categoria']: row['total_categoria'] for row in cursor.fetchall()}
    

        cursor.close()
        conn.close()
        return render_template('index.html', despesas=dados, total_geral=total_geral, total_por_categoria=total_por_categoria)
    except Exception as e :
        print("Erro ao conectar ao banco de dados:", e)
        return render_template('index.html',despesas=[])
    


#rota para salvar
@app.route('/salvar_despesa',methods=['POST'])
def salvar():
    descricao= request.form['descricao']
    valor= request.form['valor']
    categoria=request.form['categoria']
    dataVencimento=request.form['dataVencimento']
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO despesas (descricao, valor, categoria, dataVencimento) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (descricao, valor, categoria, dataVencimento))
        conn.commit()
        print("LOG: Despesa salva com sucesso!")
    except mysql.connector.Error as err:
        print(f"Erro ao salvar a despesa:", err)
    finally:
        if 'cursor' in locals():
            cursor.close()
            conn.close()
        
    return redirect(url_for('index'))


#exibir a página de despesas
def exibir ():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM depesas")
    dados = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', despesas=dados)

@app.route('/editar_despesa', methods=['POST'])
def editar_despesa():
    id = request.form['id']
    descricao = request.form['descricao']
    valor = request.form['valor']
    categoria = request.form['categoria']
    dataVencimento = request.form['dataVencimento']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "UPDATE despesas SET descricao = %s, valor = %s, categoria = %s, dataVencimento = %s WHERE id = %s"
    cursor.execute(sql, (descricao, valor, categoria, dataVencimento, id))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

@app.route('/excluir_despesa', methods=['POST'])
def excluir_despesa():
    id = request.form.get('id')
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM despesas WHERE id = %s"
    cursor.execute(sql, (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True)