## a) Liste e descreva o que são as 4 etapas do processo de compilação.

As etapas são préprocessamento, compilação, montagem e link. A etapa de pré-processamento remove coisas necessárias para a visualização e entendimento to código pelo usuário mas que são desnecessárias para o compilador como comentário, espaços, novas linhas, tabs, entre outros. A compilação transforma o código de uma linguagem de programação para assembly. Depois faz a montagem para a linguagem de máquina. Por fim, faz a união com as bibliotecas de código de máquinas usado no sistema.

## b) O compilador gcc permite fornecer parâmetros extras, que modificam desde a emissão de erros até o binário final, o otimizando para determinados comportamentos. Explique a função dos seguintes parâmetros:

i) -static: Gera um programa estaticamente, ou seja, não depende de bibliotecas dinâmicas para rodar.

ii) -g: Produz informações para debug

iii) -pendantic: Desabilita as extensões do GCC e gera mais avisos de acordo com a padronização, mesmo que não afete diretamente o desempenho ou qualidade do código.

iv) -Wall: habilita avisos

v) -Os: Habilita otimizações até o nível O2 desde que não aumente o tamanho do arquivo.

vi) -O3: Realiza otimizções no código. É possível passar as flags o1 e o2 tmb mas todas tem a mesma função de otmização. A diferença entre elas é que o nível de otimização varia entre de menor para maior de acordo com a numeração da flag.
