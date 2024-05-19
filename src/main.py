import numpy as np
from tarefa_grupo_2 import adj_para_incidencia, calcular_graus   

if __name__ == "__main__":
    # Exemplo de uma matriz de adjacências
    matriz_adj = [
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 0]
    ]
    
    matriz_incidencia, num_vertices, num_arestas = adj_para_incidencia(matriz_adj)
    graus = calcular_graus(matriz_adj)
    
    print("Matriz de Adjacência:")
    print(np.array(matriz_adj))
    print("\nMatriz de Incidência:")
    print(matriz_incidencia)
    print(f"\nNúmero de Vértices: {num_vertices}")
    print(f"Número de Arestas: {num_arestas}")
    print(f"Grau de cada Vértice: {graus}")