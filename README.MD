# Non-Deterministic-Turing-Machine

## Entrada

### Na primeira linha, recebe uma lista de estados. Na segunda linha, o alfabeto de entrada. Na terceira linha, o alfabeto da fita. Na quarta linha, o símbolo especial que limita a fita à esquerda. Na quinta linha, o símbolo branco da fita. Na sexta linha, o número total n de transições. Para cada uma das n linhas seguintes, há uma quíntupla <a, b, c, d, e> onde ‘a’ é o estado de origem, ‘b’ é o caractere a ser lido, ‘c’ é o estado de destino, ‘d’ é o símbolo a ser escrito e, por fim, ‘e’ é a direção, imóvel (I), esquerda (E) e direita (D). Em seguida, recebe um caractere informando o estado inicial. Em seguida, há uma lista de estados finais. Por fim, há uma lista de palavras de teste a ser reconhecida. Os itens da listas serão separados por espaço em branco. A palavra vazia é representada por *.

## Saída

#### O algoritmo imprime, para cada palavra de teste, ‘S’ se a MTND reconhece a palavra ou ‘N’ caso contrário.
#### Os arquivos .in são exemplos de entrada.