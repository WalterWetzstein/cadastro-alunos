from armazenamento import carregar


def consultar(matricula):
    return carregar().get(matricula.strip())
