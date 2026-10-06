from Classes.Banco import Banco
from Classes.Tempo import Tempo


class Horario:
    dic_tempo = Tempo.dados_santoangelo()

    @staticmethod
    def horarios_1():
        query = """
               select 
id_horario,
CASE EXTRACT(ISODOW FROM data_hora)
    WHEN 1 THEN 'Segunda'
    WHEN 2 THEN 'Terça'
    WHEN 3 THEN 'Quarta'
    WHEN 4 THEN 'Quinta'
    WHEN 5 THEN 'Sexta'
    WHEN 6 THEN 'Sábado'
    WHEN 7 THEN 'Domingo'
END AS dia_semana,
data_hora,
reservado
from horario 
where data_hora 
between current_date and current_date + interval '1 day'
ORDER BY data_hora
                """
        tabela = Banco.consulta(query)
        return tabela

    @staticmethod
    def horarios_2():
        query = """
        select 
id_horario,
CASE EXTRACT(ISODOW FROM data_hora)
    WHEN 1 THEN 'Segunda'
    WHEN 2 THEN 'Terça'
    WHEN 3 THEN 'Quarta'
    WHEN 4 THEN 'Quinta'
    WHEN 5 THEN 'Sexta'
    WHEN 6 THEN 'Sábado'
    WHEN 7 THEN 'Domingo'
END AS dia_semana,
data_hora,
reservado
from horario 
where data_hora 
between current_date + interval '1 day' and current_date + interval '2 day'
ORDER BY data_hora
        """
        tabela = Banco.consulta(query)
        return tabela

    @staticmethod
    def horarios_3():
        query = """
        select 
id_horario,
CASE EXTRACT(ISODOW FROM data_hora)
    WHEN 1 THEN 'Segunda'
    WHEN 2 THEN 'Terça'
    WHEN 3 THEN 'Quarta'
    WHEN 4 THEN 'Quinta'
    WHEN 5 THEN 'Sexta'
    WHEN 6 THEN 'Sábado'
    WHEN 7 THEN 'Domingo'
END AS dia_semana,
data_hora,
reservado
from horario 
where data_hora 
between current_date + interval '2 day' and current_date + interval '3 day'
ORDER BY data_hora
        """
        tabela = Banco.consulta(query)
        return tabela

    @staticmethod
    def horarios_4():
        query = """
        select 
id_horario,
CASE EXTRACT(ISODOW FROM data_hora)
    WHEN 1 THEN 'Segunda'
    WHEN 2 THEN 'Terça'
    WHEN 3 THEN 'Quarta'
    WHEN 4 THEN 'Quinta'
    WHEN 5 THEN 'Sexta'
    WHEN 6 THEN 'Sábado'
    WHEN 7 THEN 'Domingo'
END AS dia_semana,
data_hora,
reservado
from horario 
where data_hora 
between current_date + interval '3 day' and current_date + interval '4 day'
ORDER BY data_hora
        """
        tabela = Banco.consulta(query)
        return tabela

    @staticmethod
    def horarios_5():
        query = """
        select 
id_horario,
CASE EXTRACT(ISODOW FROM data_hora)
    WHEN 1 THEN 'Segunda'
    WHEN 2 THEN 'Terça'
    WHEN 3 THEN 'Quarta'
    WHEN 4 THEN 'Quinta'
    WHEN 5 THEN 'Sexta'
    WHEN 6 THEN 'Sábado'
    WHEN 7 THEN 'Domingo'
END AS dia_semana,
data_hora,
reservado
from horario 
where data_hora 
between current_date + interval '4 day' and current_date + interval '5 day'
ORDER BY data_hora
        """
        tabela = Banco.consulta(query)
        return tabela

    @staticmethod
    def consulta_horarios(id_horario):
        lista_parametros = []
        lista_parametros.append(id_horario)
        query = f"""
        select 
        *
        from horario
        where id_horario = %s
        """
        tabela = Banco.consulta_unica_parametros(query, lista_parametros)
        return tabela

    @staticmethod
    def reservar_horario(id_usuario, id_horario):
        lista_parametros = []
        lista_parametros.append(id_usuario)
        lista_parametros.append(id_horario)
        query = """
            update horario
                set reservado = True,
                    id_responsavel = %s
                where id_horario = %s
        """
        dic_status = Banco.salvar_dados_banco_parametros(query, lista_parametros)
        return dic_status

    @staticmethod
    def horarios_usuario(id_usuario):
        query = """
            select 
data_hora,
CASE EXTRACT(ISODOW FROM h.data_hora)
    WHEN 1 THEN 'Segunda'
    WHEN 2 THEN 'Terça'
    WHEN 3 THEN 'Quarta'
    WHEN 4 THEN 'Quinta'
    WHEN 5 THEN 'Sexta'
    WHEN 6 THEN 'Sábado'
    WHEN 7 THEN 'Domingo'
END AS dia_semana
from horario h
inner join usuario u on u.id_usuario = h.id_responsavel
where id_usuario = %s and data_hora > current_timestamp
        """
        tabela = Banco.consulta_varios_parametros(query, [id_usuario, ])
        return tabela

print(Horario.horarios_usuario(1))