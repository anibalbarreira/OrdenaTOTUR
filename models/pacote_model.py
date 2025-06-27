from models.db import conectar

class Pacote:
    def _init_(self, Nome, Descricao, Preco_total, id=None):
        self.id = id
        self.Nome = Nome
        self.Descricao = Descricao
        self.Preco_total = Preco_total
      
    def salvar(self):
        conn = conectar()
        cursor = conn.cursor()

        if self.id is None:
            sql = "INSERT INTO turista (Nome, Descricao, Preco_total) VALUES (%s, %s, %s)"
            valores = (self.Nome, self.Descricao, self.Preco_total)
        else:
            sql = "UPDATE turista SET Nome=%s, Email=%s, Telefone=%s, Cidade=%s, Nacionalidade=%s WHERE id=%s"
            valores = (self.Nome, self.Descricao, self.Preco_total, self.id)

        cursor.execute(sql, valores)
        conn.commit()
        cursor.close()
        conn.close()

    @staticmethod
    def buscar_todos():
        conn = conectar()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM turista")
        resultados = cursor.fetchall()

        cursor.close()
        conn.close()
        return [Pacote(**r) for r in resultados]

    @staticmethod
    def buscar_por_id(id_Pacote):
        conn = conectar()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM pacote WHERE id = %s", (id_Pacote,))
        resultado = cursor.fetchone()

        cursor.close()
        conn.close()

        return Pacote(**resultado) if resultado else None

    def deletar(self):
        if self.id is not None:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM pacote WHERE id = %s", (self.id,))
            conn.commit()
            cursor.close()
            conn.close()