from models.db import conectar

class Atrativo_turistico:
    def _init_(self, Nome, Tipo, Cidade, Preco, id=None):
        self.id = id
        self.Nome = Nome
        self.Tipo = Tipo
        self.Cidade = Cidade
        self.Preco = Preco
        
    def salvar(self):
        conn = conectar()
        cursor = conn.cursor()

        if self.id is None:
            sql = "INSERT INTO Atrativo_turistico (Nome, Tipo, Cidade, Preco) VALUES (%s, %s, %s)"
            valores = (self.Nome, self.Tipo, self.Cidade, self.Preco)
        else:
            sql = "UPDATE Atrativo_turistico SET Nome=%s, Tipo=%s, Cidade=%s, Preco=%s WHERE id=%s"
            valores = (self.Nome, self.Tipo, self.Cidade, self.Preco, self.id)

        cursor.execute(sql, valores)
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def buscar_todos():
        conn = conectar()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM Atrativo_turistico")
        resultados = cursor.fetchall()

        cursor.close()
        conn.close()
        return [Atrativo_turistico(**r) for r in resultados]

    @staticmethod
    def buscar_por_id(id_Atrativo_turistico):
        conn = conectar()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM Atrativo_turistico WHERE id = %s", (id_Atrativo_turistico))
        resultado = cursor.fetchone()

        cursor.close()
        conn.close()

        return Atrativo_turistico(**resultado) if resultado else None

    def deletar(self):
        if self.id is not None:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Atrativo_turistico WHERE id = %s", (self.id,))
            conn.commit()
            cursor.close()
            conn.close()