"""
Módulo para verificação de palíndromos
Este módulo demonstra manipulação de strings e verificação de palíndromos
"""

def obter_palavra():
    """Solicita uma palavra do usuário"""
    while True:
        palavra = input("Digite uma palavra ou frase: ").strip()
        if palavra:  # Verifica se não está vazia
            return palavra
        print("Por favor, digite algo!")

def limpar_texto(texto):
    """Remove espaços e caracteres especiais, converte para minúsculas"""
    # Remove espaços e converte para minúsculas
    texto = texto.lower()
    # Remove caracteres especiais e espaços
    caracteres_validos = [c for c in texto if c.isalnum()]
    return ''.join(caracteres_validos)

def verificar_palindromo(texto):
    """
    Verifica se o texto é um palíndromo
    Retorna True se for palíndromo, False caso contrário
    """
    texto = limpar_texto(texto)
    return texto == texto[::-1]

def exibir_resultado(texto_original, eh_palindromo):
    """Exibe o resultado da verificação"""
    print("\n=== Resultado ===")
    print(f"Texto analisado: {texto_original}")
    
    if eh_palindromo:
        print("✨ É um palíndromo! ✨")
        print("Lido da esquerda para a direita ou da direita para a esquerda, permanece igual.")
    else:
        print("Não é um palíndromo.")
        texto_limpo = limpar_texto(texto_original)
        print(f"Normal:   {texto_limpo}")
        print(f"Invertido: {texto_limpo[::-1]}")

def mostrar_exemplos():
    """Mostra alguns exemplos de palíndromos"""
    print("\nExemplos de palíndromos:")
    exemplos = [
        "Ovo",
        "Arara",
        "Rir",
        "A base do teto desaba",
        "A torre da derrota"
    ]
    for exemplo in exemplos:
        print(f"- {exemplo}")

if __name__ == "__main__":
    print("=== Verificador de Palíndromos ===")
    print("Um palíndromo é uma palavra ou frase que se lê igual de trás para frente!")
    
    try:
        # Mostra exemplos para o usuário
        mostrar_exemplos()
        
        print("\nAgora é sua vez!")
        # Obtém o texto do usuário
        texto = obter_palavra()
        
        # Verifica se é palíndromo
        eh_palindromo = verificar_palindromo(texto)
        
        # Exibe o resultado
        exibir_resultado(texto, eh_palindromo)
        
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
