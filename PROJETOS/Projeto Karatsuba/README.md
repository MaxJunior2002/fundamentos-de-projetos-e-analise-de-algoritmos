# Algoritmo de Multiplicação de Karatsuba

O algoritmo de Karatsuba é um método utilizado para uma multiplicação mais eficiente de números inteiros grandes. Ao invés de utilizar a multiplicação tradicional ele utiliza uma abordagem recursiva reduzindo a complexidade de $O(n^2)$ para $O(n^{1.585})$, onde $n$ é o numero de dígitos. O algoritmo foi implementado no formato de uma função que recebe dois números foi preparada para trabalhar de forma recursiva, com uma condição de parada que valida se um dos números é menor que 5. Na sequencia é validado o tamanho dos números e preenchido o numero menor com zeros a esquerda, se for o caso. Em seguida são divididos os números em metades. Seguindo com as multiplicações que moldam o algoritmo e após isso é feita a subtração que resulta na soma dos produtos cruzados. Finalizando com a aplicação da formula que retorna o resultado final da multiplicação.

-----

### Como Executar o Projeto

Para rodar o algoritmo, siga estes passos:

1.  **Clone o repositório:** Abra o terminal ou prompt de comando e use o seguinte comando para clonar o projeto:

    ```bash
    git clone [URL_DO_REPOSITORIO]
    ```

2.  **Navegue até o diretório do projeto:**

    ```bash
    cd [PATH_DO_REPOSITORIO]
    ```

3.  **Execute o arquivo:** O código principal está em `main.py`. Use o comando a seguir para executá-lo:

    ```bash
    python main.py
    ```

O resultado da multiplicação será exibido na tela.

-----

### Relatório Técnico

#### Análise da Complexidade Ciclomática

A complexidade ciclomática mede o número de caminhos independentes no código.

  - **Grafo de Fluxo:**

      - **Nós (N):** 6
      - **Arestas (E):** 7
      - **Componentes Conexos (P):** 1

  - **Cálculo:** $M = E - N + 2P = 7 - 6 + 2 \* 1 = 3$

A complexidade é **3**, o que indica um fluxo de controle simples e de fácil manutenção.

-----

#### Análise da Complexidade Assintótica

Determina o comportamento do algoritmo com o aumento da entrada ($n$).

  - **Complexidade de Tempo ($O(n)$):** $O(n^{1.585})$

      - **Melhor Caso, Caso Médio e Pior Caso:** Todos mantêm a mesma complexidade, pois a estrutura recursiva é consistente.

  - **Complexidade de Espaço ($O(n)$):** $O(n)$

      - O espaço de memória é linear em relação ao número de dígitos, devido ao armazenamento das subpartes dos números nas chamadas recursivas da pilha de execução.