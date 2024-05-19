import numpy as np
from tarefa_grupo_2 import adj_para_incidencia, calcular_graus   

if __name__ == "__main__":
    # Exemplo de uma matriz de adjacências
                #    A  B  C  D
    matriz_adj =   [[0, 1, 2, 0], #A  (A->B),(A->C),(A->C)
                    [0, 0, 0, 1], #B  (B->D)
                    [0, 0, 0, 0], #C
                    [0, 0, 1, 0]] #D  (D->C)
    
    direcionado = True  # Defina como True se o grafo for direcionado

    matriz_incidencia, num_vertices, num_arestas = adj_para_incidencia(matriz_adj, direcionado)
    graus = calcular_graus(matriz_adj, direcionado)
    
    print("Matriz de Adjacência:")
    print(np.array(matriz_adj))
    print("\nMatriz de Incidência:")
    print(matriz_incidencia)
    print(f"\nNúmero de Vértices: {num_vertices}")
    print(f"Número de Arestas: {num_arestas}")
    
    if direcionado:
        graus_saida, graus_entrada = graus
        print(f"Grau de Saída de cada Vértice: {graus_saida}")
        print(f"Grau de Entrada de cada Vértice: {graus_entrada}")
    else:
        print(f"Grau de cada Vértice: {graus}")