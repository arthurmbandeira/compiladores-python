# Implementação de um compilador para a linguagem CMM
Este repositório contem o trabalho de implementação da disciplina Implmentação de Linguagens de Programação.

CMM é o acrônimo de C-Mais-ou-Menos, uma linguagem mais ou menos parecida com C.

## Execução
 - Instalar a ferramenta PLY com o comando ``` pip install ply ```
 - Estar no diretório ``` compiladores-python ```
 - Para executar somente o analisador léxico: 
   - Descomentar a linha 150 do arquivo ``` lexer.py ```
   - ``` python src/lexer.py -f test/< arquivo_de_teste.cmm > ```
 - Para execução do analisador sintático:
   - ``` python src/parser.py -f test/< arquivo_de_teste.cmm > ```

 #### Arthur Manuel Bandeira
 #### Carlos Henrique Paisca
