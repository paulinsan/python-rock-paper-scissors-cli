# 🎮 Pedra, Papel ou Tesoura

Um jogo de **Pedra, Papel ou Tesoura** desenvolvido em Python para praticar conceitos fundamentais de programação, como funções, estruturas condicionais, loops, tratamento de erros e dicionários.

> 🚧 **Status:** Em desenvolvimento

---

## 📌 Sobre o projeto

Este projeto foi desenvolvido como parte dos meus estudos em **Python**, com o objetivo de colocar em prática conceitos de programação através de um jogo simples e interativo executado no terminal.

O jogador escolhe entre **Pedra, Papel ou Tesoura**, enquanto o computador realiza uma escolha aleatória.

A cada rodada, o programa verifica o resultado, atualiza o placar e permite que o jogador continue ou encerre a partida.

---

## 🎮 Como funciona

O jogador escolhe uma das três opções:

```text
[1] Pedra ⛰️
[2] Papel 📄
[3] Tesoura ✂️
```

O computador escolhe uma opção aleatoriamente.

As regras são:

* ⛰️ Pedra vence ✂️ Tesoura
* 📄 Papel vence ⛰️ Pedra
* ✂️ Tesoura vence 📄 Papel
* Escolhas iguais resultam em empate

---

## ✨ Funcionalidades

* 🎮 Escolha entre Pedra, Papel ou Tesoura
* 🤖 Escolha aleatória do computador
* 🔄 Sistema de múltiplas rodadas
* 🏆 Contador de pontos
* 👀 Contador de empates
* 🔢 Contador de rodadas
* 📊 Exibição do placar durante a partida
* 🏁 Exibição do resultado final
* 🔁 Opção para jogar novamente
* ❌ Validação de entradas inválidas
* 🛡️ Tratamento de erros com `try/except`
* 🧩 Organização do código utilizando funções
* 📚 Utilização de dicionário para armazenar o placar

---

## 🧠 Conceitos de Python utilizados

Durante o desenvolvimento foram utilizados diversos conceitos importantes da linguagem:

### Variáveis

Utilizadas para armazenar informações do jogo.

```python
computador = random.choice(opcoes)
```

### Listas

Utilizadas para armazenar as opções disponíveis:

```python
opcoes = ["Pedra ⛰️", "Papel 📄", "Tesoura ✂️"]
```

### Estruturas condicionais

Utilizadas para verificar as escolhas e determinar o resultado:

```python
if resultado == "empate":
    ...
elif resultado == "jogador":
    ...
else:
    ...
```

### Laço `while`

Utilizado para manter o jogo funcionando enquanto o jogador desejar continuar:

```python
while True:
    ...
```

### Funções

O código foi dividido em funções para facilitar a organização e reutilização:

```python
def escolher_opcao():
    ...

def jogar_novamente():
    ...

def verificar_vencedor(jogador, computador):
    ...

def mostrar_placar(placar):
    ...

def mostrar_resultado_final(placar):
    ...
```

### Dicionários

O placar é armazenado em um dicionário:

```python
placar = {
    "jogador": 0,
    "computador": 0,
    "empates": 0,
    "rodadas": 0
}
```

### Tratamento de erros

O `try/except` impede que o programa seja encerrado quando o jogador digita algo que não seja um número:

```python
try:
    jogador = int(input(...))

except ValueError:
    print("❌ Opção inválida!")
```

---

## 📊 Sistema de pontuação

O jogo mantém quatro informações principais:

| Informação   | Descrição                           |
| ------------ | ----------------------------------- |
| `jogador`    | Pontos conquistados pelo jogador    |
| `computador` | Pontos conquistados pelo computador |
| `empates`    | Quantidade de rodadas empatadas     |
| `rodadas`    | Quantidade total de rodadas         |

Exemplo:

```text
===== PLACAR =====
Você:       4
Computador: 2
Empates:    1
Rodadas:    7
```

Ao final da partida, o programa compara a pontuação do jogador com a do computador e informa se o jogador:

* 🏆 Venceu
* 😓 Perdeu
* 👀 Empatou

---

## 🗂️ Estrutura das funções

### `escolher_opcao()`

Responsável por receber e validar a escolha do jogador.

### `jogar_novamente()`

Pergunta se o jogador deseja iniciar outra rodada e aceita apenas `S` ou `N`.

### `verificar_vencedor()`

Compara a escolha do jogador com a escolha do computador e retorna:

```text
"jogador"
"computador"
"empate"
```

### `mostrar_placar()`

Exibe os dados armazenados no dicionário `placar`.

### `mostrar_resultado_final()`

Compara a pontuação final e informa o resultado da partida.

---

## ▶️ Como executar

### 1. Clone o repositório

```bash
git clone URL_DO_SEU_REPOSITORIO
```

### 2. Acesse a pasta do projeto

```bash
cd nome-do-projeto
```

### 3. Execute o programa

```bash
python nome_do_arquivo.py
```

---

## 🛠️ Tecnologias utilizadas

* 🐍 Python
* 🎲 Biblioteca `random`
* 💻 Terminal

---

## 🚧 Próximos passos

Este projeto ainda está em desenvolvimento. Algumas melhorias que podem ser implementadas futuramente:

* [ ] Melhorar a interface do terminal
* [ ] Criar um menu inicial
* [ ] Adicionar histórico das partidas
* [ ] Criar níveis de dificuldade
* [ ] Separar o projeto em diferentes arquivos Python
* [ ] Criar uma versão com interface gráfica utilizando Tkinter

---

## 📚 Objetivo de aprendizado

O principal objetivo deste projeto é praticar programação em Python através de uma aplicação simples, evoluindo o código gradualmente e aplicando novos conceitos conforme o aprendizado.

O projeto começou com uma estrutura simples de Pedra, Papel ou Tesoura e foi sendo aprimorado com:

```text
Jogo básico
    ↓
Múltiplas rodadas
    ↓
Sistema de pontuação
    ↓
Funções
    ↓
Dicionário
    ↓
Placar completo
    ↓
Resultado final
```

---

## 👨‍💻 Autor

**Paulo Henrique dos Santos**

Estudante de **Análise e Desenvolvimento de Sistemas (ADS)**.

🔗 GitHub: [@paulinsan](https://github.com/paulinsan)
