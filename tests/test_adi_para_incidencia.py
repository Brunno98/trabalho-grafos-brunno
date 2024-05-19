# === ajustando importação ===
import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))
# ============================

import unittest
import numpy.testing as np
from parameterized import parameterized, param, parameterized_class
from src import tarefa_grupo_2
import json


class TestAdjParaIncidencia(unittest.TestCase):

    @parameterized.expand(
            param.explicit(kwargs=data) for data in json.load(open("tests/data/adjacencia_para_incidencia_data.json"))
    )
    def test_matriz_adjacencia_para_incidencia(self, matriz_adjacencia, direcionado, matriz_incidencia_esperada, vertices_esperados, arestas_esperadas):
        """
        Deve ser retornado uma matriz de incidencia baseada na matriz de adjencecia fornecida.
        Deve também retornar a quantidade de vertices e a quantidade de arestas da matriz.
        """
        matriz_incidencia, quantidade_vertices, quantidade_arestas = tarefa_grupo_2.adj_para_incidencia(matriz_adjacencia, direcionado)

        np.assert_array_equal(matriz_incidencia, matriz_incidencia_esperada)
        self.assertEqual(quantidade_vertices, vertices_esperados)
        self.assertEqual(quantidade_arestas, arestas_esperadas)


if __name__ == "__main__":
    unittest.main()