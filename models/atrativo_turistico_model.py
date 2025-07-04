from models.db import conectar

class Atrativo_turistico:
    def __init__(self, Nome, Tipo, Cidade, Preco, id_Pacote, id=None):
        self.id = id
        self.Nome = Nome
        self.Tipo = Tipo
        self.Cidade = Cidade
        self.Preco = Preco
        self.id_Pacote = id_Pacote
        
    def salvar(self):
        conn = conectar()
        cursor = conn.cursor()

        if self.id is None:
            sql = "INSERT INTO atrativo_turistico (Nome, Tipo, Cidade, Preco, id_Pacote) VALUES (%s, %s, %s, %s, %s)"
            valores = (self.Nome, self.Tipo, self.Cidade, self.Preco, self.id_Pacote)
        else:
            sql = "UPDATE atrativo_turistico SET Nome=%s, Tipo=%s, Cidade=%s, Preco=%s, id_Pacote=%s, WHERE id_Atrativo=%s"
            valores = (self.Nome, self.Tipo, self.Cidade, self.Preco, self.id_Pacote, self.id)

        cursor.execute(sql, valores)
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def buscar_todos():
        conn = conectar()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM atrativo_turistico")
        resultados = cursor.fetchall()

        cursor.close()
        conn.close()
        return [Atrativo_turistico(**r) for r in resultados]

    @staticmethod
    def buscar_por_id(id_Atrativo_turistico):
        conn = conectar()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM atrativo_turistico WHERE id_Atrativo = %s", (id_Atrativo_turistico,))
        resultado = cursor.fetchone()

        cursor.close()
        conn.close()

        return Atrativo_turistico(**resultado) if resultado else None

    def deletar(self):
        if self.id is not None:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM atrativo_turistico WHERE id_Atrativo = %s", (self.id,))
            conn.commit()
            cursor.close()
            conn.close()