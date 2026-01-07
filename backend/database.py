import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), 'vagas.db')

def conectar_db():

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def criar_tabelas():
    
    conn = conectar_db()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vagas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            plataforma TEXT NOT NULL,
            preco TEXT NOT NULL,
            descricao TEXT NOT NULL,
            data TEXT NOT NULL,
            link TEXT,
            criada_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

def obter_todas_vagas():
    
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM vagas ORDER BY data DESC')
    vagas = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return vagas

def inserir_vaga(titulo, plataforma, preco, descricao, data, link=None):
    
    conn = conectar_db()
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO vagas (titulo, plataforma, preco, descricao, data, link)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (titulo, plataforma, preco, descricao, data, link))
    
    conn.commit()
    conn.close()

def limpar_vagas():
    
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM vagas')
    conn.commit()
    conn.close()


criar_tabelas()