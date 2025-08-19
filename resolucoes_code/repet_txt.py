"""
Módulo de manipulação e repetição de texto
Este módulo demonstra diferentes operações com strings e padrões de repetição
"""

def coletar_texto():
    """Coleta um texto e um número de repetições do usuário"""
    texto = input("Digite um texto: ")
    try:
        repeticoes = int(input("Digite quantas vezes deseja repetir: "))
        if repeticoes < 0:
            raise ValueError("O número de repetições não pode ser negativo")
        return texto, repeticoes
    except ValueError as e:
        raise ValueError("Por favor, digite um número inteiro válido para repetições")

def repetir_texto(texto, repeticoes):
    """Cria diferentes padrões de repetição com o texto"""
    # Repetição simples
    padrao1 = (texto + " ") * repeticoes
    
    # Repetição com numeração
    padrao2 = "".join(f"{i+1}. {texto}\n" for i in range(repeticoes))
    
    # Repetição com separador
    padrao3 = " | ".join(texto for _ in range(repeticoes))
    
    return [padrao1, padrao2, padrao3]

def aplicar_transformacoes(texto):
    """Aplica diferentes transformações no texto"""
    transformacoes = {
        "Maiúsculas": texto.upper(),
        "Minúsculas": texto.lower(),
        "Capitalizado": texto.capitalize(),
        "Título": texto.title(),
        "Invertido": texto[::-1],
        "Sem espaços": texto.replace(" ", "")
    }
    return transformacoes

def mostrar_resultados(padroes, transformacoes):
    """Mostra os diferentes padrões e transformações"""
    print("\nPadrões de repetição:")
    for i, padrao in enumerate(padroes, 1):
        print(f"\nPadrão {i}:")
        print(padrao)
    
    print("\nTransformações do texto:")
    for nome, resultado in transformacoes.items():
        print(f"{nome}: {resultado}")

if __name__ == "__main__":
    try:
        texto, repeticoes = coletar_texto()
        padroes = repetir_texto(texto, repeticoes)
        transformacoes = aplicar_transformacoes(texto)
        mostrar_resultados(padroes, transformacoes)
    except ValueError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")