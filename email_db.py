import sqlite3

conexao = sqlite3.connect('crud_email.db')

def gerir_id():
    conexao = sqlite3.connect('crud_email.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT seq FROM sqlite_sequence WHERE name='email'")
    next_id = cursor.fetchone()[0]
    return next_id + 1

def criar_email():
    try:
        conexao = sqlite3.connect('crud_email.db')
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO crud_email (email_jogadores) VALUES (?)")
        email_id = cursor.lastrowid
        conexao.commit()
        conexao.close()
        return email_id
    except Exception as Ex:
        print(Ex)
        return 0
    
def atualizar_email():
    try:
        conexao = sqlite3.connect('crud_email.db')
        cursor = conexao.cursor()
        cursor.execute("UPDATE crud_email SET email_jogadores = ? WHERE id_email = ?")
        conexao.commit()
        conexao.close()
        return True
    except Exception as Ex:
        print(Ex)
        return False  
    
def remover_email(id:int):
    try:
        conexao = sqlite3.connect('crud_email.db')
        cursor = conexao.cursor()
        sql_delete = "DELETE FROM crud_email WHERE id_email = ?"
        cursor.execute(sql_delete, (id, ))
        conexao.commit()
        conexao.close()
        return True
    except Exception as Ex:
        print(Ex)
        return False      
    
def retornar_email(id:int):
    try:
        if id == 0:
            return gerir_id(), ""   
        conexao = sqlite3.connect('crud_email.db')
        cursor = conexao.cursor()

        sql_select = "SELECT * FROM crud_email WHERE id_email = ?"
        cursor.execute(sql_select, (id, ))
        id, email_personagem = cursor.fetchone()
        conexao.close()
        return id, email_jogadores
    except:
        return False

def retornar_todos():
    try:
        conexao = sqlite3.connect('crud_email.db')
        cursor = conexao.cursor()
        sql_select = "SELECT * FROM crud_email"
        cursor.execute(sql_select)
        email_jogadores = cursor.fetchall()
        conexao.close()
        return email_jogadores
    except:
        return False    
           

#cursor = conexao.cursor()

#sql_insert = "INSERT INTO crud_email (email_jogadores) VALUES (?)"

#sql_select_varios = "SELECT * FROM crud_email"

#sql_update = "UPDATE crud_email SET email_jogadores = ? WHERE id_email = ?"

#sql_delete = "DELETE FROM crud_email WHERE id_email = ?"

