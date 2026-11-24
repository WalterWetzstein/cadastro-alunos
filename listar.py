from armazenamento import carregar


def listar():
    return sorted(carregar().items(), key=lambda item: item[1]["nome"].casefold())
