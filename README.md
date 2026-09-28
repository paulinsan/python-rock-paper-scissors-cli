# 🎮 Pedra, Papel ou Tesoura

Jogo de **Pedra, Papel ou Tesoura** desenvolvido em Python para praticar conceitos fundamentais de programação, organização de código e criação de uma aplicação interativa executada no terminal.

> ✅ **Status: Concluído**

---

## 📌 Sobre o projeto

Este projeto foi desenvolvido como parte dos meus estudos em **Python**, com o objetivo de transformar conceitos aprendidos durante os estudos em uma aplicação prática.

O jogador escolhe entre **Pedra, Papel ou Tesoura**, enquanto o computador realiza uma escolha aleatória. A cada rodada, o programa verifica o resultado, atualiza o placar e permite que o jogador continue jogando ou encerre a partida.

Ao finalizar, o jogo apresenta o **placar final** e informa se o jogador venceu, perdeu ou terminou empatado.

---

## 🎮 Como jogar

Ao iniciar o jogo, são apresentadas três opções:

```text
[1] Pedra ⛰️
[2] Papel 📄
[3] Tesoura ✂️
```

O jogador deve informar o número correspondente à sua escolha.

O computador realiza sua escolha automaticamente.

### Regras

* ⛰️ **Pedra** vence **Tesoura**
* 📄 **Papel** vence **Pedra**
* ✂️ **Tesoura** vence **Papel**
* Escolhas iguais resultam em **empate**

---

## ✨ Funcionalidades

* 🎮 Escolha entre Pedra, Papel ou Tesoura
* 🤖 Escolha aleatória do computador
* 🔄 Sistema de múltiplas rodadas
* 🏆 Sistema de pontuação
* 👀 Contador de empates
* 🔢 Contador de rodadas
* 📊 Exibição do placar atual
* 🏁 Exibição do placar final
* 🏆 Identificação do resultado final da partida
* 🔁 Opção de jogar novamente
* ❌ Validação de entradas inválidas
* 🛡️ Tratamento de erros com `try/except`
* 🧩 Código organizado em funções
* 📚 Utilização de dicionário para gerenciamento do placar

---

## 🧠 Conceitos de Python praticados

Durante o desenvolvimento do projeto foram utilizados diferentes conceitos da linguagem Python.

### 📋 Listas

As opções disponíveis no jogo são armazenadas em uma lista:

```python
opcoes = ["Pedra ⛰️", "Papel 📄", "Tesoura ✂️"]
```

### 🎲 Biblioteca `random`

O computador utiliza `random.choice()` para escolher uma opção aleatoriamente:

```python
computador = random.choice(opcoes)
```

### 🔀 Estruturas condicionais

As estruturas `if`, `elif` e `else` são utilizadas para verificar os resultados das partidas e validar as escolhas do jogador.

### 🔁 Estruturas de repetição

O `while` mantém o jogo funcionando enquanto o jogador desejar continuar.

### 🧩 Funções

O projeto foi dividido em funções para organizar melhor as responsabilidades do programa:

```python
def escolher_opcao():
    ...

def verificar_vencedor(jogador, computador):
    ...

def mostrar_placar(placar):
    ...

def jogar_novamente():
    ...

def mostrar_resultado_final(placar):
    ...
```

### 📚 Dicionários

O sistema de pontuação utiliza um dicionário para armazenar as informações da partida:

```python
placar = {
    "jogador": 0,
    "computador": 0,
    "empates": 0,
    "rodadas": 0
}
```

Dessa forma, todas as informações relacionadas ao placar ficam organizadas em uma única estrutura.

### 🛡️ Tratamento de exceções

O `try/except` é utilizado para impedir que o programa seja encerrado quando o jogador informa algo que não pode ser convertido para inteiro:

```python
try:
    jogador = int(input(...))

except ValueError:
    print("❌ Opção inválida!")
```

---

## 📊 Sistema de pontuação

O dicionário `placar` controla quatro informações:

| Informação   | Descrição                           |
| ------------ | ----------------------------------- |
| `jogador`    | Pontos conquistados pelo jogador    |
| `computador` | Pontos conquistados pelo computador |
| `empates`    | Quantidade de rodadas empatadas     |
| `rodadas`    | Quantidade total de rodadas         |

Exemplo de placar:

```text
===== PLACAR ATUAL =====

Rodadas:    7
Você:       4
Computador: 2
Empates:    1
```

---

## 🏁 Resultado final

Quando o jogador decide encerrar a partida, o programa compara as pontuações finais.

Se o jogador tiver mais pontos:

```text
🏆 Você venceu a partida! 🏆
```

Se o computador tiver mais pontos:

```text
😓 Você perdeu a partida! 😓
```

Se ambos tiverem a mesma pontuação:

```text
👀 A partida terminou empatada! 👀
```

---

## 🗂️ Organização das funções

### `escolher_opcao()`

Responsável por receber e validar a escolha do jogador.

### `verificar_vencedor(jogador, computador)`

Compara as escolhas e retorna o resultado da rodada:

```text
"jogador"
"computador"
"empate"
```

### `mostrar_placar(placar)`

Exibe as informações armazenadas no dicionário de pontuação.

### `jogar_novamente()`

Pergunta se o jogador deseja continuar jogando e valida as respostas `S` e `N`.

### `mostrar_resultado_final(placar)`

Compara a pontuação final e informa o resultado da partida.

---

## ▶️ Como executar

### 1. Clone o repositório

```bash
git clone URL_DO_SEU_REPOSITORIO
```

### 2. Entre na pasta do projeto

```bash
cd nome-do-projeto
```

### 3. Execute o programa

```bash
python nome_do_arquivo.py
```

---

## 🛠️ Tecnologias utilizadas

* 🐍 **Python**
* 🎲 **Random**
* 💻 **Terminal**

---

## 📈 Evolução do projeto

O projeto foi desenvolvido de forma gradual, adicionando novos conceitos conforme o aprendizado:

```text
Jogo básico
     ↓
Múltiplas rodadas
     ↓
Sistema de pontuação
     ↓
Validação de entradas
     ↓
Tratamento de erros
     ↓
Organização em funções
     ↓
Dicionário para o placar
     ↓
Contador de rodadas e empates
     ↓
Placar atual e final
     ↓
Resultado final da partida
     ↓
Projeto concluído ✅
```

---

## 🎯 Objetivo de aprendizado

O principal objetivo deste projeto foi praticar **Python através de uma aplicação simples**, desenvolvendo o código gradualmente e aplicando conceitos de programação de maneira prática.

Além de funcionar como um jogo, o projeto serviu para praticar a organização e evolução de um código, passando de uma estrutura inicial simples para uma aplicação mais organizada utilizando **funções, estruturas condicionais, loops, tratamento de exceções e dicionários**.

---

## 👨‍💻 Autor

**Paulo Henrique dos Santos**

Estudante de **Análise e Desenvolvimento de Sistemas (ADS)**.

🔗 GitHub: [@paulinsan](https://github.com/paulinsan)
