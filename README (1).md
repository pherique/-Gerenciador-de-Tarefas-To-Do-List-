
# 🗂️ Gerenciador de Tarefas (To-Do List)

Um projeto simples em Python que permite gerenciar tarefas pelo terminal. Você pode adicionar, listar, marcar como concluída e excluir tarefas. As tarefas são salvas em um arquivo `.json`, então continuam disponíveis mesmo após fechar o programa.

---

## 🚀 Funcionalidades

- Adicionar tarefas com título, descrição e data
- Listar tarefas salvas
- Marcar tarefas como concluídas
- Excluir tarefas
- Salvamento automático em arquivo `.json`

---

## 🧠 O que você aprende com esse projeto

- Listas e dicionários em Python
- Funções e modularização
- Entrada e saída de dados
- Estruturas de controle (if, while, for)
- Manipulação de arquivos (`open`, `json`)
- Tratamento básico de erros com `try/except`

---

## 📝 Explicação do código (linha por linha)

### `import json`  
Importa o módulo `json`, que permite salvar e carregar dados no formato JSON (formato leve, legível e compatível com várias linguagens).

### `import os`  
Importa o módulo `os`, que permite verificar se um arquivo existe.

---

### `tarefas = []`  
Cria uma lista vazia para armazenar as tarefas.

### `ARQUIVO = "tarefas.json"`  
Define o nome do arquivo onde as tarefas serão salvas.

---

### `def carregar_tarefas():`  
Função que carrega as tarefas do arquivo JSON (se ele existir).

#### `os.path.exists(ARQUIVO)`  
Verifica se o arquivo já existe no sistema.

#### `with open(...) as f:`  
Abre o arquivo para leitura. O `with` garante que o arquivo será fechado depois.

#### `json.load(f)`  
Converte o conteúdo do arquivo JSON em lista de dicionários (tarefas).

---

### `def salvar_tarefas():`  
Função que salva as tarefas atuais no arquivo JSON.

#### `json.dump(tarefas, f, indent=4, ensure_ascii=False)`  
Converte a lista de tarefas para texto JSON e escreve no arquivo, formatando com indentação e aceitando acentos/caracteres especiais.

---

### `def adicionar_tarefa():`  
Função que adiciona uma nova tarefa.

- Usa `input()` para coletar o título, descrição e data
- Cria um dicionário com esses dados e `"concluida": False`
- Adiciona esse dicionário à lista `tarefas`
- Chama `salvar_tarefas()` para salvar a nova tarefa

---

### `def listar_tarefas():`  
Função que mostra todas as tarefas.

- Verifica se há tarefas; se não, exibe mensagem.
- Usa `enumerate()` para mostrar o número de cada tarefa.
- Mostra status (✅ concluída ou ❌ pendente), título e data.

---

### `def concluir_tarefa():`  
Permite marcar uma tarefa como concluída.

- Mostra todas as tarefas com `listar_tarefas()`
- Pede ao usuário o índice da tarefa
- Altera `"concluida"` para `True`
- Salva novamente com `salvar_tarefas()`

#### `try/except`  
Evita erro caso o usuário digite algo inválido.

---

### `def excluir_tarefa():`  
Permite remover uma tarefa.

- Mostra todas as tarefas com `listar_tarefas()`
- Pede índice da tarefa a ser removida
- Remove da lista com `pop()`
- Salva novamente com `salvar_tarefas()`

---

### `def menu():`  
Cria o menu interativo do programa.

- Roda um `while True` para repetir o menu até o usuário sair
- Mostra opções numeradas
- Usa `input()` para capturar a escolha
- Chama a função correspondente a cada opção

---

### `tarefas = carregar_tarefas()`  
Carrega as tarefas do arquivo ao iniciar o programa.

---

### `menu()`  
Inicia o programa executando o menu interativo.

---

## ▶️ Como rodar o projeto

1. Certifique-se de ter o Python instalado.
2. Salve o código em um arquivo chamado `gerenciador_tarefas.py`
3. No terminal, execute:

```bash
python gerenciador_tarefas.py
```

---

## 📂 Estrutura esperada do projeto

```
📁 seu_projeto/
├── gerenciador_tarefas.py
├── tarefas.json  # (criado automaticamente)
└── README.md
```

---

## 📌 Melhorias futuras

- Interface gráfica com `tkinter` ou web com `Flask`
- Prioridades ou categorias de tarefa
- Filtro de tarefas por status ou data
- Validação de datas com `datetime`

---

## 📚 Créditos

Projeto didático para iniciantes em Python, com foco em lógica, estrutura e boas práticas.
