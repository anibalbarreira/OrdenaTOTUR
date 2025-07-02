from models.db import conectar

class Turista:
    def __init__(self, Nome, Email, Telefone, Cidade, Nacionalidade, id=None):
        self.id = id
        self.Nome = Nome
        self.Email = Email
        self.Cidade = Cidade
        self.Nacionalidade = Nacionalidade
        self.Telefone = Telefone

    def salvar(self):
        conn = conectar()
        cursor = conn.cursor()

        if self.id is None:
            sql = "INSERT INTO turista (Nome, Email, Telefone, Cidade, Nacionalidade) VALUES (%s, %s, %s, %s, %s)"
            valores = (self.Nome, self.Email, self.Telefone, self.Cidade, self.Nacionalidade)
        else:
            sql = "UPDATE turista SET Nome=%s, Email=%s, Telefone=%s, Cidade=%s, Nacionalidade=%s WHERE id=%s"
            valores = (self.Nome, self.Email, self.Telefone, self.Cidade, self.Nacionalidade, self.id)

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
        return [Turista(**r) for r in resultados]

    @staticmethod
    def buscar_por_id(id_turista):
        conn = conectar()
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM Turista WHERE id = %s", (id_turista,))
        resultado = cursor.fetchone()

        cursor.close()
        conn.close()

        return Turista(**resultado) if resultado else None

    def deletar(self):
        if self.id is not None:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Turista WHERE id = %s", (self.id,))
            conn.commit()
            cursor.close()
            conn.close()