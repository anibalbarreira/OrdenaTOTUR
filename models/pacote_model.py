from models.db import conectar

class Pacote:
    def __init__(self, Nome, Descricao, Preco_total, id=None):
        self.id = id
        self.Nome = Nome
        self.Descricao = Descricao
        self.Preco_total = Preco_total
      
    def salvar(self):
        conn = conectar()
        cursor = conn.cursor()

        if self.id is None:
            sql = "INSERT INTO Pacote (Nome, Descricao, Preco_total) VALUES (%s, %s, %s)"
            valores = (self.Nome, self.Descricao, self.Preco_total)
        else:
            sql = "UPDATE Pacote SET Nome=%s, Descricao=%s, Preco_total=%s WHERE id=%s"
            valores = (self.Nome, self.Descricao, self.Preco_total, self.id)

        cursor.execute(sql, valores)
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def buscar_todos():
        conn = conectar()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM pacote")
        resultados = cursor.fetchall()

        cursor.close()
        conn.close()
        return [Pacote(**r) for r in resultados]

    @staticmethod
    def buscar_por_id(id_Pacote):
        conn = conectar()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM Pacote WHERE id = %s", (id_Pacote,))
        resultado = cursor.fetchone()

        cursor.close()
        conn.close()

        return Pacote(**resultado) if resultado else None

    def deletar(self):
        if self.id is not None:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Pacote WHERE id = %s", (self.id,))
            conn.commit()
            cursor.close()
            conn.close()