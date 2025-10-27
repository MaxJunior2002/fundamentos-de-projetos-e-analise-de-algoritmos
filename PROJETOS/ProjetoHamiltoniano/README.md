# [span_0](start_span)Implementação do Algoritmo para Caminho Hamiltoniano[span_0](end_span)

## Descrição do Projeto

[span_1](start_span)Este projeto consiste no desenvolvimento de um programa em Python que implementa o algoritmo para encontrar um **Caminho Hamiltoniano** em um grafo orientado ou não orientado[span_1](end_span).

[span_2](start_span)Um **Caminho Hamiltoniano** em um grafo é um caminho que visita cada vértice exatamente uma vez[span_2](end_span). [span_3](start_span)Encontrar esse caminho é um problema clássico na teoria dos grafos e está associado a problemas de alta complexidade computacional, como o Problema do Caixeiro Viajante[span_3](end_span). [span_4](start_span)O objetivo do algoritmo implementado é determinar se um Caminho Hamiltoniano existe em um grafo e, em caso afirmativo, encontrá-lo[span_4](end_span).

[span_5](start_span)A abordagem utilizada, sugerida nas dicas[span_5](end_span), é o algoritmo de **Backtracking** (retrocesso), que é uma técnica de busca exaustiva baseada em tentativa e erro e é ideal para problemas de combinação e arranjo.

### Lógica da Implementação (`main.py`)

A implementação utiliza uma **lista de adjacência** (dicionário Python) para representar o grafo. O mesmo código funciona para grafos orientados e não orientados.

-   **`encontrar_caminho_hamiltoniano(grafo)`**:
    -   É a função principal que itera sobre todos os vértices, tentando iniciar a busca pelo Caminho Hamiltoniano a partir de **cada vértice** (`for vertice_inicial...`).
    -   Se a função recursiva encontrar um caminho que visita todos os $N$ vértices, este é o Caminho Hamiltoniano e é retornado imediatamente.

-   **`_backtracking_caminho_hamiltoniano(grafo, num_vertices, caminho_atual)`**:
    -   **Caso Base (Sucesso)**: Verifica se o comprimento de `caminho_atual` é igual a `num_vertices`. Se for, a solução foi encontrada e o caminho é retornado.
    -   **Passo Recursivo**: O algoritmo considera o último vértice do caminho (`vertice_u`) e itera sobre todos os seus vizinhos (`vertice_v`).
    -   **Condição de Continuação**: Garante que o `vertice_v` ainda **não** foi visitado, verificando se ele está no `caminho_atual`.
    -   **Tentativa e Retrocesso (Backtracking)**:
        1.  Adiciona `vertice_v` ao caminho.
        2.  Chama a função recursivamente.
        3.  Se a chamada recursiva falhar (retornar `None`), remove `vertice_v` do caminho (`caminho_atual.pop()`) e tenta o próximo vizinho, realizando o retrocesso.

---

## [span_6](start_span)Como Executar o Projeto[span_6](end_span)

Para rodar o projeto localmente, siga os passos abaixo:

1.  **Clone o repositório:** Abra o terminal ou prompt de comando e use o seguinte comando para clonar o projeto:

    ```bash
    git clone [https://github.com/MaxJunior2002/fundamentos-de-projetos-e-analise-de-algoritmos.git](https://github.com/MaxJunior2002/fundamentos-de-projetos-e-analise-de-algoritmos.git)
    ```

2.  **Navegue até o diretório do projeto:**

    ```bash
    cd PROJETOS/ProjetoHamiltoniano
    ```

3.  **[span_7](start_span)Execute o arquivo:** O código principal está em `main.py`[span_7](end_span). Use o comando a seguir para executá-lo:

    ```bash
    python main.py
    ```
    O programa executará os exemplos de teste e exibirá o Caminho Hamiltoniano encontrado (ou a informação de que ele não existe).

---

## [span_8](start_span)Relatório Técnico[span_8](end_span)

### [span_9](start_span)Análise da Complexidade Computacional[span_9](end_span)

#### [span_10](start_span)Classes P, NP, NP-Completo e NP-Difícil[span_10](end_span)

[span_11](start_span)O problema de encontrar (ou determinar a existência de) um Caminho Hamiltoniano se enquadra nas seguintes classes de complexidade[span_11](end_span):

1.  **Classe NP (Nondeterministic Polynomial Time)**: O problema pertence à classe **NP**. [span_12](start_span)Uma solução (o caminho) pode ser verificada em tempo polinomial[span_12](end_span).

2.  **[span_13](start_span)Classe NP-Completo (NP-C)**: O problema do Caminho Hamiltoniano (decisão) é **NP-Completo**[span_13](end_span).
    * **Justificativa**: Por ser um problema de decisão, ele se enquadra na classe NP. [span_14](start_span)É considerado NP-Completo, pois é um dos problemas fundamentais para os quais todos os outros problemas em NP podem ser reduzidos em tempo polinomial[span_14](end_span).

3.  **Relação com o Problema do Caixeiro Viajante (TSP)**:
    * [span_15](start_span)O problema do Caminho Hamiltoniano está diretamente associado ao Problema do Caixeiro Viajante[span_15](end_span). Ambos são problemas NP-Completos. [span_16](start_span)O Ciclo Hamiltoniano é um caso particular do TSP onde se busca um ciclo com um limite de custo específico, o que reforça a classificação de NP-Completo[span_16](end_span).

4.  **[span_17](start_span)Classe NP-Difícil**: Por ser NP-Completo, o problema do Caminho Hamiltoniano também é **NP-Difícil**[span_17](end_span).

#### [span_18](start_span)Análise da Complexidade Assintótica de Tempo[span_18](end_span)

1.  **Determinação da Complexidade Temporal**:
    * A complexidade temporal do algoritmo de Backtracking implementado, no pior caso, é **$O(N!)$**, onde $N$ é o número de vértices.

2.  **Explicação do Método**:
    * [span_19](start_span)O método utilizado para determinar a complexidade é a **contagem de operações** baseada na árvore de recursão[span_19](end_span).
    * No pior caso, o algoritmo deve explorar um número de caminhos que pode se aproximar do número total de permutações de $N$ vértices (que é $N!$). A busca recursiva tenta estender o caminho $N$ vezes, e em cada nível, o número de opções de ramificação pode ser até $N, N-1, N-2, \ldots, 1$.
    * O crescimento fatorial do espaço de busca domina o tempo de execução no pior cenário.

#### [span_20](start_span)Aplicação do Teorema Mestre[span_20](end_span)

1.  **Verificação de Aplicabilidade**:
    * **[span_21](start_span)Não é possível** aplicar o Teorema Mestre para analisar a complexidade do algoritmo de Backtracking para o Caminho Hamiltoniano no pior caso[span_21](end_span).

2.  **Justificativa**:
    * [span_22](start_span)O Teorema Mestre é projetado para relações de recorrência do tipo **divisão e conquista** na forma $T(n) = aT(n/b) + f(n)$[span_22](end_span).
    * [span_23](start_span)A recorrência do Backtracking, no pior caso ($T(N) \approx N \cdot T(N-1) + O(1)$), não se ajusta a este modelo, pois o problema não é dividido em subproblemas de tamanhos iguais e fixos, mas sim em subproblemas que dependem da estrutura do grafo e reduzem o tamanho do problema em 1 a cada passo[span_23](end_span).

#### [span_24](start_span)Análise dos Casos de Complexidade[span_24](end_span)

1.  **Explicação das Diferenças**:

| Caso de Complexidade | Descrição |
| :--- | :--- |
| **Pior Caso** | Ocorre quando o algoritmo explora o maior número de caminhos antes de encontrar a solução ou confirmar que ela não existe. Exemplo: A solução é a última testada, ou o grafo é denso, mas não tem caminho. |
| **Melhor Caso** | [span_25](start_span)Ocorre quando o algoritmo encontra o Caminho Hamiltoniano imediatamente, geralmente na primeira tentativa de busca[span_25](end_span). |
| **Caso Médio** | O desempenho médio ao longo de todas as possíveis entradas de grafo. [span_26](start_span)É difícil de determinar analiticamente[span_26](end_span). |

2.  **Impacto no Desempenho do Algoritmo**:
    * A diferença entre o **Pior Caso** ($O(N!)$) e o **Melhor Caso** ($O(N)$) é a principal razão pela qual o problema é considerado intratável.
    * [span_27](start_span)O crescimento fatorial do pior caso significa que o algoritmo é impraticável para grafos com um número moderado de vértices ($N > 20$), sendo o tempo de execução sensível à estrutura do grafo[span_27](end_span).
