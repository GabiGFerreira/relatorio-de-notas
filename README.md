# Sistema de Relatório de Alunos

Este projeto em Python realiza o cálculo da média de notas de alunos e verifica sua situação de aprovação.

## Funcionalidades

- Armazena dados de alunos
- Calcula média das notas
- Verifica aprovação ou reprovação
- Gera relatório formatado no terminal


# Estrutura dos Dados

Cada aluno é representado por um dicionário contendo:

```python
{
    "matricula": 1,
    "nome": "Israel",
    "notas": [6.5, 9, 8]
}
```

A lista `alunos_notas` contém todos os alunos cadastrados.

---

# Funções

## `calcular_media(notas)`

Calcula a média das notas de um aluno.

### Parâmetros

- `notas (list[float])`: lista de notas do aluno

### Retorno

- `float`: média das notas

---

## `verificar_aprovacao(media, media_minima=7.0)`

Verifica se o aluno foi aprovado.

### Parâmetros

- `media (float)`: média do aluno
- `media_minima (float)`: média mínima para aprovação

### Retorno

- `"Aprovado"` ou `"Reprovado"`

---

## `gerar_relatorios(alunos)`

Exibe um relatório contendo:

- Nome do aluno
- Média das notas
- Situação de aprovação

### Parâmetros

- `alunos (list[dict])`: lista de alunos

---

# Exemplo de Saída

```text
Nome | Média | Situação
Israel 7.8 Aprovado
Felipe 4.5 Reprovado
Nathan 7.8 Aprovado
```

---

# Como Executar

1. Instale o Python
2. Salve o código em um arquivo `.py`
3. Execute no terminal:

```bash
python nome_do_arquivo.py
```

---

# Tecnologias Utilizadas

- Python 3

---

# Objetivo

Este projeto foi desenvolvido para praticar:

- Funções
- Listas e dicionários
- Estruturas condicionais
- Laços de repetição
- Documentação com docstrings