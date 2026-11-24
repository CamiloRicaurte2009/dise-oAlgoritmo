import sqlite3
from modelos import Paquete
class Repositorio:
    def __init__(self, ruta):
        self.con = sqlite3.connect(ruta)
        self.con.execute("CREATE TABLE IF NOT EXISTS paquete (viajes INTEGER UNIQUE)")
        self.con.execute("CREATE TABLE IF NOT EXISTS consulta (n INT, algoritmo TEXT, minimo INT, paquetes TEXT)")
    def insertar(self, v): self.con.execute("INSERT OR IGNORE INTO paquete VALUES (?)", (v,))
    def listar(self): return [Paquete(f[0]) for f in self.con.execute("SELECT viajes FROM paquete")]
    def guardar(self, n, alg, m, p): self.con.execute("INSERT INTO consulta VALUES (?,?,?,?)", (n, alg, m, str(p))); self.con.commit()
