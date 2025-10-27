# main.py

def encontrar_caminho_hamiltoniano(grafo):
    num_vertices = len(grafo)
    
    for vertice_inicial in range(num_vertices):
        caminho_atual = [vertice_inicial]
        
        caminho_encontrado = _backtracking_caminho_hamiltoniano(
            grafo, 
            num_vertices, 
            caminho_atual
        )
        
        if caminho_encontrado:
            return caminho_encontrado
            
    return None

def _backtracking_caminho_hamiltoniano(grafo, num_vertices, caminho_atual):
    if len(caminho_atual) == num_vertices:
        return caminho_atual
    
    vertice_u = caminho_atual[-1]
    
    for vertice_v in grafo.get(vertice_u, []):
        
        if vertice_v not in caminho_atual:
            
            caminho_atual.append(vertice_v)
            
            resultado = _backtracking_caminho_hamiltoniano(
                grafo, 
                num_vertices, 
                caminho_atual
            )
            
            if resultado:
                return resultado
            
            caminho_atual.pop()
            
    return None

def criar_grafo(arestas, orientado=False):
    grafo = {}
    
    todos_vertices = set()
    for u, v in arestas:
        todos_vertices.add(u)
        todos_vertices.add(v)
        
    for v in todos_vertices:
        grafo[v] = []

    for u, v in arestas:
        if v not in grafo[u]:
            grafo[u].append(v)
        
        if not orientado:
            if u not in grafo[v]:
                grafo[v].append(u)
    
    return grafo

if __name__ == '__main__':
    
    arestas_nao_orientado = [
        (0, 1), (0, 2),
        (1, 2), (1, 3), 
        (2, 4), 
        (3, 4), (3, 5),
        (4, 5)
    ]
    grafo_nao_orientado = criar_grafo(arestas_nao_orientado, orientado=False)
    
    caminho_nao_orientado = encontrar_caminho_hamiltoniano(grafo_nao_orientado)
    
    if caminho_nao_orientado:
        print("Caminho Hamiltoniano (Não Orientado):", " -> ".join(map(str, caminho_nao_orientado)))
    else:
        print("Caminho Hamiltoniano (Não Orientado) não existe.")
        
    
    arestas_orientado = [
        (0, 1),
        (1, 2)
    ]
    grafo_orientado = criar_grafo(arestas_orientado, orientado=True)
    
    caminho_orientado = encontrar_caminho_hamiltoniano(grafo_orientado)
    
    if caminho_orientado:
        print("Caminho Hamiltoniano (Orientado):", " -> ".join(map(str, caminho_orientado)))
    else:
        print("Caminho Hamiltoniano (Orientado) não existe.")
