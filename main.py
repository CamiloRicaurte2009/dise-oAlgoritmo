from repositorio import Repositorio
from solucionadores import DP, Greedy
repo = Repositorio("recargas.db")
for v in (1, 3, 4): repo.insertar(v)
print("Tabla n=0..10:", [DP(repo.listar()).resolver(i)[0] for i in range(11)])
for n in (6, 10):
    for nombre, clase in (("DP", DP), ("Greedy", Greedy)):
        m, p = clase(repo.listar()).resolver(n)
        repo.guardar(n, nombre, m, p)
        print(n, nombre, m, p)
