"""
Módulo de concatenação de dados
Este módulo demonstra diferentes formas de concatenar e formatar dados em Python
"""

def coletar_dados_pessoais():
    """Coleta informações pessoais do usuário"""
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    return nome, idade

def formatar_apresentacao(nome, idade):
    """Formata uma string de apresentação usando diferentes métodos"""
    # Usando f-string (método moderno)
    apresentacao1 = f"Olá, me chamo {nome} e tenho {idade} anos!"
    
    # Usando método format()
    apresentacao2 = "Prazer em conhecer {}, você tem {} anos.".format(nome, idade)
    
    # Usando concatenação tradicional
    apresentacao3 = "Seja bem-vindo(a) " + nome + "!"
    
    return [apresentacao1, apresentacao2, apresentacao3]

def criar_lista_info(nome, idade):
    """Cria uma lista com diferentes tipos de dados"""
    # Convertendo idade para inteiro para demonstração
    idade_num = int(idade)
    
    info = [
        nome,
        idade_num,
        f"{nome} {idade}",
        {"nome": nome, "idade": idade_num},
        (nome, idade_num)
    ]
    
    return info

def mostrar_resultados(apresentacoes, info):
    """Mostra os diferentes resultados de concatenação"""
    print("\nApresentações:")
    for i, apresentacao in enumerate(apresentacoes, 1):
        print(f"{i}. {apresentacao}")
    
    print("\nLista de informações em diferentes formatos:")
    for i, item in enumerate(info, 1):
        print(f"{i}. {item} (tipo: {type(item).__name__})")

if __name__ == "__main__":
    try:
        nome, idade = coletar_dados_pessoais()
        apresentacoes = formatar_apresentacao(nome, idade)
        info = criar_lista_info(nome, idade)
        mostrar_resultados(apresentacoes, info)
    except ValueError as e:
        print(f"Erro ao processar dados: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")