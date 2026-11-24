import json
from pathlib import Path

ARQUIVO = Path(__file__).with_name("alunos.json")


def carregar():
    if not ARQUIVO.exists():
        return {}
    with ARQUIVO.open(encoding="utf-8") as arquivo:
        alunos = json.load(arquivo)
    if not isinstance(alunos, dict) or any(
        not isinstance(a, dict) or not all(isinstance(a.get(c), str) for c in ("nome", "curso"))
        for a in alunos.values()
    ):
        raise ValueError("Arquivo de alunos inválido.")
    return alunos


def salvar(alunos):
    temporario = ARQUIVO.with_suffix(".tmp")
    temporario.write_text(json.dumps(alunos, ensure_ascii=False, indent=2), encoding="utf-8")
    temporario.replace(ARQUIVO)
