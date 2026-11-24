from cadastrar import cadastrar
from listar import listar
from consultar import consultar
from excluir import excluir


def main():
    while True:
        print("\nCADASTRO DE ALUNOS — 1.0.0")
        print("1 - Cadastrar aluno\n2 - Listar alunos\n3 - Consultar aluno\n4 - Excluir aluno\n0 - Sair")
        opcao = input("Escolha: ").strip()
        try:
            if opcao == "1":
                matricula = input("Matrícula: ")
                nome = input("Nome: ")
                curso = input("Curso: ")
                cadastrar(matricula, nome, curso)
                print("Aluno cadastrado.")
            elif opcao == "2":
                alunos = listar()
                if not alunos:
                    print("Nenhum aluno cadastrado.")
                for matricula, aluno in alunos:
                    print(f"{matricula} | {aluno['nome']} | {aluno['curso']}")
            elif opcao == "3":
                aluno = consultar(input("Matrícula: "))
                if aluno:
                    print(f"Nome: {aluno['nome']} | Curso: {aluno['curso']}")
                else:
                    print("Aluno não encontrado.")
            elif opcao == "4":
                matricula = input("Matrícula: ")
                if input("Confirmar exclusão? (s/n): ").strip().lower() == "s":
                    print("Aluno excluído." if excluir(matricula) else "Aluno não encontrado.")
                else:
                    print("Exclusão cancelada.")
            elif opcao == "0":
                print("Sistema encerrado.")
                break
            else:
                print("Opção inválida.")
        except (ValueError, OSError) as erro:
            print(f"Não foi possível concluir: {erro}")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nSistema encerrado.")
