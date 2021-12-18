# CSS Grid

## Grid

- Bidimensional
- Página é dividida em linhas e colunas
- Pode-se colocar elementos onde quiser nessa divisão

## Grid vs Flexbox

- Grid: 2 dimensões (linhas e colunas)
- Flexbox: 1 dimensão (linha ou coluna)
- Podem ser usados juntos, pois um pode complementar o outro
---
## Propriedades
São separadas em 2 grupos:
`containers` e `items`
### Containers

- display:grid;
- grid-template-columns;
- grid-template-rows;
- grid-gap
    - grid-row-gap
    - grid-column-gap
- grid-template-areas;

... Há + 4 propriedades e **alinhamento**

O template das colunas (grid-template-columns) pode ser definido
por meio de "frações de tela" de tamanho k, ou seja, k-fr. 

Exemplo:

1. 3 colunas, grid-template-columns: 1fr 2fr 1fr
    - 1fr que corresponderia a primeira fração: 25% da largura total
    - 2fr que corresponderia a segunda fração: 50% da largura total
    - 1fr que corresponderia a tecerira fração: 25% da largura total

2. 2 colunas, grid-template-columns: 1fr 1fr
    - 1fr que corresponderia a primeira fração: 50% da largura total
    - 1fr que corresponderia a segunda fração: 50% da largura total

3. 2 colunas, sendo a 2ª maior, grid-template-columns: 1fr 3fr
    - 1fr que corresponderia a primeira fração: 25% da largura total
    - 3fr que corresponderia a segunda fração: 75% da largura total 

De forma semelhante, pode-se definir o tamanho das linhas utilizando
o grid-template-rows, em que altura de cada linha pode ser definida, 
por exemplo, pela view port.

Exemplo:

1. 3 linhas:
    - grid-template-rows: 20vh 70vh 10vh

Note que os items dentro de  um container com esses propriedades não 
devem ter altura ou largura definida de forma fixa, já que essas serão
definidas automaticamente pela propriedade display.

### Items

- grid-column
    - grid-column-start
    - grid-column-end
- grid-row
    - grid-row-start
    - grid-row-end
- grid-area

... e mais 2 propriedades de **alinhamento**

