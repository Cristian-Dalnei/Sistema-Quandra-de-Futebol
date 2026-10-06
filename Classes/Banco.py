import psycopg2
import bcrypt
from psycopg2.extras import RealDictCursor


class Banco:
    @staticmethod
    def conectar():
        conn = psycopg2.connect(
            host="localhost",
            database="arenafutebol",
            user="postgres",
            password="zmaddoxxbr18",
            port="5432"
        )
        return conn

    @staticmethod
    def fechar_conn(cur, conn):
        if cur:
            cur.close()
        if conn:
            conn.close()

    @staticmethod
    def consulta(query):
        tabela = None
        cur = None
        conn = None
        try:
            conn = Banco.conectar()
            cur = conn.cursor(cursor_factory=RealDictCursor)
            cur.execute(query)
            tabela = cur.fetchall()
        except Exception as e:
            print(e)
        finally:
            Banco.fechar_conn(cur, conn)
        return tabela

    @staticmethod
    def consulta_unica(query):
        tabela = None
        cur = None
        conn = None
        try:
            conn = Banco.conectar()
            cur = conn.cursor(cursor_factory=RealDictCursor)
            cur.execute(query)
            tabela = cur.fetchone()
        except Exception as e:
            print(e)
        finally:
            Banco.fechar_conn(cur, conn)
        return tabela

    @staticmethod
    def consulta_unica_parametros(query, parametros):
        tabela = None
        cur = None
        conn = None
        try:
            conn = Banco.conectar()
            cur = conn.cursor(cursor_factory=RealDictCursor)
            cur.execute(query, parametros)
            tabela = cur.fetchone()
        except Exception as e:
            print(e)
        finally:
            Banco.fechar_conn(cur, conn)
        return tabela

    @staticmethod
    def consulta_varios_parametros(query, parametros):
        tabela = None
        cur = None
        conn = None
        try:
            conn = Banco.conectar()
            cur = conn.cursor(cursor_factory=RealDictCursor)
            cur.execute(query, parametros)
            tabela = cur.fetchall()
        except Exception as e:
            print(e)
        finally:
            Banco.fechar_conn(cur, conn)
        return tabela


    @staticmethod
    def salvar_dados_banco_parametros(query, parametros):
        cur = None
        conn = None
        dic_status = {
            'cadastrado': False
        }
        try:
            conn = Banco.conectar()
            cur = conn.cursor(cursor_factory=RealDictCursor)
            cur.execute(query, parametros)
            conn.commit()
            dic_status['cadastrado'] = True
        except Exception as e:
            print(e)
        finally:
            Banco.fechar_conn(cur, conn)
        return dic_status

    @staticmethod
    def verificar_login(email, senha):
        query = f"SELECT id_usuario, hash_senha FROM usuario WHERE email = '{email}'"
        tabela = Banco.consulta_unica(query)
        if tabela:
            hash_senha = tabela['hash_senha']
            if bcrypt.checkpw(senha.encode(), hash_senha.encode()):
                return tabela['id_usuario']
            else:
                return None

    @staticmethod
    def email_existe(email):
        query = f"SELECT email FROM usuario WHERE email = '{email}'"
        tabela = Banco.consulta_unica(query)
        if tabela:
            return True
        return False


    @staticmethod
    def informações_usuario(id_usuario):
        query = f"SELECT id_usuario, nome, sobrenome, email, nascimento FROM usuario WHERE id_usuario = '{id_usuario}'"
        tabela = Banco.consulta_unica(query)
        return tabela

    @staticmethod
    def cadastrar_usuario(nome, sobrenome, email, senha, ano, mes, dia):
        query = """insert into usuario(nome, sobrenome, email, hash_senha, nascimento) 
                    values(%s, %s, %s, %s, %s)"""
        nascimento = f"{ano}-{mes}-{dia}"
        hash_senha = bcrypt.hashpw(senha.encode(), bcrypt.gensalt()).decode()
        cur = None
        conn = None
        dic_status = {
            'cadastrado': False,
            'erro': ''
                      }
        email_existe = Banco.email_existe(email)
        if email_existe:
            dic_status['cadastrado'] = False
            dic_status['erro'] = 'Email não disponivel.'
            return dic_status

        try:
            conn = Banco.conectar()
            cur = conn.cursor()
            cur.execute(query, (nome, sobrenome, email, hash_senha ,nascimento))
            conn.commit()
            dic_status['cadastrado'] = True
            return dic_status
        except Exception as e:
            print(e)
        finally:
            Banco.fechar_conn(cur, conn)
        dic_status['cadastrado'] = False
        return dic_status

