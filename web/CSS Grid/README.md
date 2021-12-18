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

# Grid: Alinhamento
---

Existem 6 propriedades de alinhamento:
1. `justify-content`
2. `align-content`
3. `justify-items`
4. `justify-self`
5. `align-self`

Separa-se em 2 grupos:
1. `justify` e `align`
2. `content`, `items` e `self`

---

## Justify e Align

Dimensões do grid:
1. **Eixo x**: posicionamento horizontalmente, da esquerda para direita
2. **Eixo y**: posicionamento vertical, de cima para baixo

---

## Content, Items e Self
Pode-se observar as propriedades ao juntar `Justify` e `Align`, com os elemetos:  `content`, `items` e `self`

---

### Content
`justify-content` e `align-content` nos permite alinhar o próprio grid, relativo ao espaço fora do grid e são normalmente usados quando o grid 
é menor que a área disponível que ele poderia ocupar.  

**7 valores** possíveis para `justify-content`:
1. start 
    - Alinha o grid com o "início", + à esquerda 
2. end 
    - Alinha o grid com o "fim", + à direita
3. center 
    - Alinha o grid no "centro", no meio 
4. stretch 
    - Padrão, semelhante ao start
5. space-between 
    - Alinha as colunas do grid, criando um espaço no meio: "Entre"
6. space-around 
    - Semelhante ao between, mas também cria um espaço ao redor 
7. space-evenly
    - Semelhante ao space-around, mas separa todas as colunas a uma mesma distância entre si e entre as colunas

*Obs. `align-content` funciona de forma semelhante ao `justify-content`, porém na vertical e no lugar de "colunas" utiliza linhas*

### Items

`justify-items` e `align-items` permite alinhar os items do grid dentro da célula que ele habita, quando há espaço disponível.


**4 valores** possíveis para `justify-items` e `align-items`:
1. start
    - Alinha o item no início da célula
2. end
    - Alinha o item no fim da célula
3. center
    - Alinha o item no centro da célula
4. stretch
    - Alinhamento padrão

*Obs. `justify-items` alinha os items horizontalmente, enquanto `align-items` alinha os items verticalmente*



