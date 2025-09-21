# Algoritmo de Seleção Simultânea (MaxMin Select)

## Descrição do Projeto

Este projeto consiste na implementação do algoritmo **MaxMin Select** em Python. O objetivo do algoritmo é encontrar, de forma simultânea e eficiente, o maior e o menor elemento em uma sequência de números. A abordagem utilizada é a de **divisão e conquista**, que reduz o número total de comparações em relação a uma busca sequencial simples.

A lógica do algoritmo recursivo é a seguinte:
1.  **Divisão**: O problema de encontrar o mínimo e o máximo em uma lista de `n` elementos é continuamente dividido em dois subproblemas de tamanho `n/2`.
2.  **Conquista**: A recursão continua até que os subproblemas atinjam um tamanho trivial (um ou dois elementos), que são os nossos **casos base**:
    * Se a lista tem um único elemento, ele é ao mesmo tempo o mínimo e o máximo.
    * Se a lista tem dois elementos, uma única comparação determina qual é o mínimo e qual é o máximo.
3.  **Combinação**: Após as chamadas recursivas retornarem o mínimo e o máximo de suas respectivas metades, os resultados são combinados. São necessárias apenas duas comparações adicionais para determinar o mínimo e o máximo globais:
    * O mínimo global é o menor entre os mínimos das duas metades.
    * O máximo global é o maior entre os máximos das duas metades.

### Lógica da Implementação (`main.py`)

-   **Linhas 10-12**: O primeiro caso base verifica se a lista (`arr`) contém apenas um elemento. Se sim, ele é retornado como mínimo e máximo.
-   **Linhas 15-19**: O segundo caso base trata de listas com dois elementos. Uma comparação determina e retorna o par (mínimo, máximo).
-   **Linha 22**: Para listas maiores, o índice do meio é calculado para dividir a lista.
-   **Linhas 25-26**: Duas chamadas recursivas são feitas: uma para a metade esquerda (`arr[:meio]`) e outra para a metade direita (`arr[meio:]`). Cada chamada retorna o par (mínimo, máximo) de sua respectiva sub-lista.
-   **Linhas 29-32**: Esta é a etapa de combinação. O mínimo final é encontrado comparando `min_esq` com `min_dir`, e o máximo final é encontrado comparando `max_esq` com `max_dir`.
-   **Linha 34**: O par (menor_final, maior_final) é retornado.

-----

### Como Executar o Projeto

Para rodar o algoritmo, siga estes passos:

1.  **Clone o repositório:** Abra o terminal ou prompt de comando e use o seguinte comando para clonar o projeto:

    ```bash
    git clone https://github.com/MaxJunior2002/fundamentos-de-projetos-e-analise-de-algoritmos.git
    ```

2.  **Navegue até o diretório do projeto:**

    ```bash
    cd PROJETOS/ProjetoMaxMin
    ```

3.  **Execute o arquivo:** O código principal está em `main.py`. Use o comando a seguir para executá-lo:

    ```bash
    python main.py
    ```

O resultado da análise, mostrando o menor e o maior elemento da lista de exemplo, será exibido na tela.

-----

### Relatório Técnico

#### Análise da Complexidade Assintótica (Método de Contagem de Operações)

A eficiência do MaxMin Select é medida pelo número de comparações que ele realiza.

1.  **Casos Base:**
    * Para uma lista com **n = 1**, são feitas **0** comparações.
    * Para uma lista com **n = 2**, é feita **1** comparação.

2.  **Passo Recursivo (n > 2):**
    * O algoritmo divide a lista em duas metades de tamanho `n/2`.
    * Ele resolve os dois subproblemas recursivamente. O custo para isso é $2 \cdot T(n/2)$.
    * Na etapa de combinação, ele realiza **2** comparações: uma para achar o mínimo global e outra para achar o máximo global.

    A relação de recorrência para o número de comparações $C(n)$ é:
    $$ C(n) = 2 \cdot C(n/2) + 2 $$

    Resolvendo a recorrência (para $n$ sendo uma potência de 2):
    $C(n) = 2(2C(n/4) + 2) + 2 = 4C(n/4) + 4 + 2$
    $C(n) = 4(2C(n/8) + 2) + 6 = 8C(n/8) + 8 + 6$
    ...
    $C(n) = 2^k C(n/2^k) + \sum_{i=1}^{k} 2^i$

    A recursão para quando $n/2^k = 2$, ou seja, $k = \log_2(n) - 1$.
    $C(n) = 2^{\log_2(n)-1} \cdot C(2) + 2(2^{\log_2(n)-1} - 1)$
    $C(n) = (n/2) \cdot 1 + n - 2 = n/2 + n - 2 = \frac{3n}{2} - 2$

    O número total de comparações é aproximadamente $\frac{3n}{2}$, o que nos leva a uma complexidade de tempo **$O(n)$**.

#### Análise da Complexidade Assintótica (Aplicação do Teorema Mestre)

A recorrência para a complexidade de tempo do MaxMin Select é:
$$ T(n) = 2T(n/2) + O(1) $$

Onde:
* $T(n)$ é o tempo para resolver o problema de tamanho `n`.
* $2T(n/2)$ representa as duas chamadas recursivas em subproblemas de tamanho `n/2`.
* $O(1)$ representa o custo constante da etapa de combinação (duas comparações).

Vamos aplicar o Teorema Mestre à fórmula $T(n) = aT(n/b) + f(n)$.

1.  **Identificação dos valores:**
    * $a = 2$ (número de subproblemas)
    * $b = 2$ (fator de redução do tamanho do problema)
    * $f(n) = O(1)$ (custo externo, que é constante)

2.  **Cálculo de $log_b a$:**
    * $p = \log_2 2 = 1$

3.  **Determinação do Caso do Teorema Mestre:**
    * Precisamos comparar $f(n)$ com $n^{\log_b a} = n^1$.
    * Temos que $f(n) = O(1)$. Como $f(n)$ cresce mais lentamente que $n^1$, a recorrência se enquadra no **Caso 1** do Teorema Mestre.
    * O Caso 1 se aplica se $f(n) = O(n^{\log_b a - \epsilon})$ para algum $\epsilon > 0$. No nosso caso, para $\epsilon = 1$, temos $O(n^{1-1}) = O(n^0) = O(1)$, o que satisfaz a condição.

4.  **Solução Assintótica:**
    * Pelo Caso 1, a solução da recorrência é $T(n) = \Theta(n^{\log_b a})$.
    * Portanto, a complexidade assintótica do algoritmo MaxMin Select é **$\Theta(n)$**.

Ambos os métodos confirmam que o algoritmo possui uma complexidade de tempo linear.