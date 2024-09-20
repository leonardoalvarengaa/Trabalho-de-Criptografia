# Projeto: Criptografia com Cifras de César e Vigenère

Este projeto implementa dois algoritmos de criptografia clássicos: a **Cifra de César** e a **Cifra de Vigenère**. O programa oferece um menu interativo que permite ao usuário escolher entre criptografar ou descriptografar uma mensagem usando uma das cifras.

## Funcionalidades

1. **Cifra de César**:
   - A Cifra de César é uma técnica de substituição de caracteres em que cada letra da mensagem é deslocada por um número fixo de posições no alfabeto.
   - O usuário pode escolher entre criptografar ou descriptografar a mensagem, fornecendo uma chave (número) para o deslocamento.

2. **Cifra de Vigenère**:
   - A Cifra de Vigenère usa uma palavra-chave para determinar o deslocamento de cada letra da mensagem. A chave é repetida ou truncada para combinar com o tamanho da mensagem.
   - O usuário pode escolher entre criptografar ou descriptografar a mensagem, fornecendo uma chave (palavra) que será usada para o processo de codificação ou decodificação.

## Como o programa funciona

O programa inicia com um **menu** onde o usuário pode escolher entre:

1. Cifra de César  
2. Cifra de Vigenère  
0. Sair

Dependendo da escolha, o programa solicita a mensagem e a chave necessária, além de perguntar se o usuário deseja criptografar ou descriptografar. 

Após a seleção, o programa retorna o resultado da operação.

### Cifra de César
- **Entrada**: Mensagem e chave (número para deslocamento).
- **Modos**:
  - `C`: Criptografar
  - `D`: Descriptografar

### Cifra de Vigenère
- **Entrada**: Mensagem e chave (palavra).
- **Modos**:
  - `C`: Criptografar
  - `D`: Descriptografar

## Exemplo de Uso

### Cifra de César
- Mensagem: `HELLO`
- Chave: `3`
- Modo: `C` (Criptografar)
- **Resultado**: `KHOOR`

### Cifra de Vigenère
- Mensagem: `HELLO`
- Chave: `KEY`
- Modo: `C` (Criptografar)
- **Resultado**: `RIJVS`

## Autores

- **Tallis Teixeira** - *Desenvolvedor* - [GitHub](https://github.com/tallismelo07)
- **Leonardo Alvarega** - *Desenvolvedor* - [GitHub](https://github.com/leonardoalvarengaa)
- **Gabriel Frade** - *Desenvolvedor* - [GitHub](https://github.com/gabrfrade01)
- **Marcos Rezende** - *Desenvolvedor* - [GitHub](https://github.com/marcosjrzz)


 
