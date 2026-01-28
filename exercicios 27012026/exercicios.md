# Lista de Exercícios: Estruturas Condicionais (if, elif, else)

**Objetivo:** Praticar a lógica de decisão e ramificação de código.
**Restrição:** Resolva os exercícios sem utilizar laços de repetição (while/for).

---

## Nível Básico

### 1. Positivo, Negativo ou Zero
Peça um número ao usuário e imprima se ele é "Positivo", "Negativo" ou "Zero".

### 2. Par ou Ímpar
Peça um número inteiro ao usuário e informe se ele é par ou ímpar.
*(Dica: Use o operador resto `%`)*

### 3. Maior de Dois
Peça dois números e imprima o maior deles. Se forem iguais, imprima "Números iguais".

### 4. Vogal ou Consoante
Peça ao usuário para digitar uma letra. Verifique se a letra é uma vogal (a, e, i, o, u) ou uma consoante.

---

## Nível Intermediário

### 5. Cálculo de Média Escolar
Peça duas notas parciais de um aluno. Calcule a média e exiba a situação:
*   Média >= 7: "Aprovado"
*   Média < 7 mas >= 5: "Recuperação"
*   Média < 5: "Reprovado"

### 6. Maior de Três
Peça três números ao usuário e mostre qual é o maior deles. Tente fazer isso apenas usando `if/else`, sem a função `max()`.

### 7. O Preço do Produto
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

### 8. Turno de Estudo
Pergunte em que turno você estuda. Peça para digitar **M** (matutino), **V** (vespertino) ou **N** (noturno). Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

---

## Nível Avançado (Desafios de Lógica)

### 9. Validação de Triângulo
Peça os 3 lados de uma forma geométrica.
1.  Primeiro, verifique se eles **podem** formar um triângulo (a soma de dois lados quaisquer deve ser maior que o terceiro).
2.  Se formarem um triângulo, diga se é:
    *   **Equilátero:** 3 lados iguais.
    *   **Isósceles:** 2 lados iguais.
    *   **Escaleno:** 3 lados diferentes.

### 10. Ano Bissexto
Peça um ano correspondente a um ano qualquer e informe se ele é ou não bissexto.
*   **Regra:** O ano deve ser divisível por 4.
*   **Exceção:** Se for divisível por 100, ele NÃO é bissexto...
*   **Exceção da exceção:** ...a menos que ele também seja divisível por 400.

### 11. O Detetive
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
1.  "Telefonou para a vítima?"
2.  "Esteve no local do crime?"
3.  "Mora perto da vítima?"
4.  "Devia para a vítima?"
5.  "Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime:
*   Se a pessoa responder positivo a 2 questões: "Suspeita".
*   Entre 3 e 4 questões: "Cúmplice".
*   5 questões: "Assassino".
*   Caso contrário: "Inocente".

### 12. Caixa Eletrônico
Faça um programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e informar quantas notas de cada valor serão fornecidas.
*   Notas disponíveis: R$ 100, R$ 50, R$ 10, R$ 5 e R$ 1.
*   Exemplo: Para sacar R$ 256, o programa fornece 2 notas de 100, 1 nota de 50, 1 nota de 5 e 1 nota de 1.
*(Dica: Use divisão inteira `//` e resto `%` para descobrir as quantidades)*
