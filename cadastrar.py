from armazenamento import carregar, salvar


def cadastrar(matricula, nome, curso):
    matricula, nome, curso = matricula.strip(), nome.strip(), curso.strip()
    if not all((matricula, nome, curso)):
        raise ValueError("Preencha matrícula, nome e curso.")
    alunos = carregar()
    if matricula in alunos:
        raise ValueError("Matrícula já cadastrada.")
    alunos[matricula] = {"nome": nome, "curso": curso}
    salvar(alunos)
