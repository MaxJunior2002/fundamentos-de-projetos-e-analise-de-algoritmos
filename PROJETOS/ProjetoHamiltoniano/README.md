# Implementação do Algoritmo para Caminho Hamiltoniano

## Descrição do Projeto

Este projeto consiste no desenvolvimento de um programa em Python que implementa o algoritmo para encontrar um **Caminho Hamiltoniano** em um grafo orientado ou não orientado.

Um **Caminho Hamiltoniano** em um grafo é um caminho que visita cada vértice exatamente uma vez. Encontrar esse caminho é um problema clássico na teoria dos grafos e está associado a problemas de alta complexidade computacional, como o Problema do Caixeiro Viajante. O objetivo do algoritmo implementado é determinar se um Caminho Hamiltoniano existe em um grafo e, em caso afirmativo, encontrá-lo.

A abordagem utilizada é o algoritmo de **Backtracking** (retrocesso).

### Lógica da Implementação (`main.py`)

O programa contém a implementação do algoritmo em `main.py`, utilizando uma **lista de adjacência** (dicionário Python) para representar o grafo.

-   **`encontrar_caminho_hamiltoniano(grafo)`**:
    -   Função principal que itera sobre todos os vértices, tentando iniciar a busca pelo Caminho Hamiltoniano a partir de **cada vértice**.
    -   Se a função recursiva encontrar um caminho que visita todos os $N$ vértices, este é o Caminho Hamiltoniano e é retornado.

-   **`_backtracking_caminho_hamiltoniano(grafo, num_vertices, caminho_atual)`**:
    -   **Caso Base (Sucesso)**: Retorna o caminho se o seu comprimento for igual a `num_vertices`.
    -   **Passo Recursivo**: Considera o último vértice (`vertice_u`) e itera sobre seus vizinhos (`vertice_v`).
    -   **Condição de Continuação**: Garante que o `vertice_v` ainda **não** foi visitado.
    -   **Tentativa e Retrocesso (Backtracking)**:
        1.  Adiciona `vertice_v` ao caminho.
        2.  Chama a função recursivamente.
        3.  Se falhar, remove `vertice_v` do caminho (`caminho_atual.pop()`) e tenta o próximo vizinho, realizando o retrocesso.

---

## Como Executar o Projeto

Instruções para rodar o código no ambiente local.

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/MaxJunior2002/fundamentos-de-projetos-e-analise-de-algoritmos.git
    ```

2.  **Navegue até o diretório do projeto:**
    ```bash
    cd PROJETOS/ProjetoHamiltoniano
    ```

3.  **Execute o arquivo:**
    ```bash
    python main.py
    ```
    O programa executará os exemplos de teste e exibirá o Caminho Hamiltoniano encontrado (ou a informação de que ele não existe).

---

## Relatório Técnico

### Análise da Complexidade Computacional

#### Classes P, NP, NP-Completo e NP-Difícil

1.  **Enquadramento do Problema do Caminho Hamiltoniano**

    * **Classe NP (Nondeterministic Polynomial Time)**: O problema pertence a **NP**, pois a validade de uma solução (caminho) pode ser verificada em tempo polinomial.
    * **Classe NP-Completo (NP-C)**: O problema do Caminho Hamiltoniano é **NP-Completo**.
    * **Classe NP-Difícil**: Por ser NP-Completo, o problema também é **NP-Difícil**.
    * **Classe P (Polynomial Time)**: O problema **não** pertence à classe P, a menos que se prove que P=NP.

2.  **Justificativa**

    O problema do Caminho Hamiltoniano (decisão) é reconhecido como **NP-Completo**. Ele está intimamente ligado ao **Problema do Caixeiro Viajante** (TSP), que também é NP-Completo. O Ciclo Hamiltoniano é um caso particular do TSP, e o fato de o problema do Caminho Hamiltoniano poder ser reduzido a um problema NP-Completo estabelece sua classificação.

#### Análise da Complexidade Assintótica de Tempo

1.  **Complexidade Temporal do Algoritmo**
    * A complexidade temporal do algoritmo de Backtracking implementado, no pior caso, é **$O(N!)$**, onde $N$ é o número de vértices.

2.  **Determinação da Complexidade**
    * O método utilizado é a **contagem de operações** baseada na árvore de recursão. No pior caso (como em um grafo completo), o algoritmo deve explorar um número de caminhos que pode se aproximar do total de permutações de N vértices (o que é N!). A natureza recursiva do backtracking, que tenta estender o caminho $N$ vezes, resulta em um crescimento fatorial.

#### Aplicação do Teorema Mestre

* **Aplicabilidade do Teorema Mestre**
    * **Não é possível** aplicar o Teorema Mestre para determinar a complexidade do algoritmo de Backtracking para o Caminho Hamiltoniano no pior caso.

* **Justificativa**
    * O Teorema Mestre se aplica a relações de recorrência do tipo **divisão e conquista** na forma T(n) = aT(n/b) + f(n).
    * A recorrência do Backtracking, no pior caso (T(N) \approx N \cdot T(N-1) + O(1)), não se ajusta a este modelo, pois o problema não é dividido em subproblemas de tamanhos iguais e fixos, sendo, portanto, inaplicável.

#### Análise dos Casos de Complexidade

1.  **Diferenças entre Casos de Complexidade**

| Caso de Complexidade | Descrição |
| :--- | :--- |
| **Pior Caso** | Ocorre quando o algoritmo é forçado a explorar a maioria das possíveis permutações de vértices antes de encontrar a solução ou determinar que ela não existe. Isso leva à complexidade O(N!). |
| **Melhor Caso** | Ocorre quando o Caminho Hamiltoniano é encontrado imediatamente, na primeira sequência de vizinhos testada. A complexidade de tempo é próxima de O(N). |
| **Caso Médio** | O desempenho médio ao longo de todas as possíveis entradas de grafo. É significativamente melhor que o pior caso, mas ainda é exponencial para grafos densos. |

2.  **Impacto no Desempenho do Algoritmo**
    * O desempenho é drasticamente impactado pela diferença entre o **Pior Caso** O(N!) e o **Melhor Caso** O(N). O crescimento fatorial do pior caso significa que o algoritmo é **intratável** para grafos com um número moderado de vértices (N > 20), tornando-o inadequado para grandes entradas. O tempo de execução é extremamente sensível à estrutura do grafo.
