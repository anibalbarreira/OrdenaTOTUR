from models.db import conectar

class Pacote_atrativo:
    def _init_(self, Nome, Descricao, Preco, id=None):
        self.id = id
        self.Nome = Nome
        self.Descricao = Descricao
        self.Preco = Preco
      
    def salvar(self):
        conn = conectar()
        cursor = conn.cursor()

        if self.id is None:
            sql = "INSERT INTO Pacote_atrativo (Nome, Descricao, Preco) VALUES (%s, %s, %s)"
            valores = (self.Nome, self.Descricao, self.Preco)
        else:
            sql = "UPDATE Pacote_atrativo SET Nome=%s, Descricao=%s, Preco=%s WHERE id=%s"
            valores = (self.Nome, self.Descricao, self.Preco, self.id)

        cursor.execute(sql, valores)
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def buscar_todos():
        conn = conectar()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM Pacote_atrativo")
        resultados = cursor.fetchall()

        cursor.close()
        conn.close()
        return [Pacote_atrativo(**r) for r in resultados]

    @staticmethod
    def buscar_por_id(id_Pacote_atrativo):
        conn = conectar()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM pacote WHERE id = %s", (id_Pacote_atrativo,))
        resultado = cursor.fetchone()

        cursor.close()
        conn.close()

        return Pacote_atrativo**resultado) if resultado else None

    def deletar(self):
        if self.id is not None:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Pacote_atrativo WHERE id = %s", (self.id,))
            conn.commit()
            cursor.close()
            conn.close()