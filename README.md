# Cadastro de alunos

Projeto e Engenharia de Software — Walter Matias Wetzstein

Sistema simples em Python, executado no terminal. Permite cadastrar, listar,
consultar pela matrícula e excluir alunos com confirmação.
Os dados são salvos em `alunos.json` e permanecem disponíveis ao reabrir o programa.
Cada aluno possui matrícula única, nome e curso.

## Executar

Com Python 3 instalado, abra um terminal na pasta do projeto:

```sh
python3 main.py
```

No Windows, pode usar `python main.py` ou `py main.py`.
Não é necessário instalar bibliotecas.

## Branches e integração

As quatro branches partiram do mesmo commit inicial e receberam alterações
independentes em arquivos separados:

- `feature/cadastrar-alunos`: cadastro e validação de matrícula.
- `feature/listar-alunos`: listagem em ordem alfabética.
- `feature/consultar-alunos`: consulta pela matrícula.
- `feature/excluir-alunos`: exclusão pela matrícula.

Cada funcionalidade recebeu um commit. As branches foram integradas à `main`
com commits de merge. Depois foi adicionado o menu que utiliza as quatro funções.
A tag `1.0.0` identifica a primeira versão completa.

Para verificar o histórico:

```sh
git log --graph --oneline --all
git branch --list
git show 1.0.0
```

## Testar

```sh
python3 -m unittest -v
```

Os testes usam arquivos temporários e não alteram os cadastros do usuário.
