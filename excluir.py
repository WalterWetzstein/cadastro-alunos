from armazenamento import carregar, salvar


def excluir(matricula):
    alunos = carregar()
    matricula = matricula.strip()
    if matricula not in alunos:
        return False
    del alunos[matricula]
    salvar(alunos)
    return True
