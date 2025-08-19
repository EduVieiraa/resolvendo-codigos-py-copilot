"""
Módulo para verificação de números pares e ímpares
Este módulo demonstra o uso de condicionais e operador módulo em Python
"""

def obter_numero():
    """Solicita e valida um número inteiro do usuário"""
    while True:
        try:
            numero = int(input("Digite um número inteiro: "))
            return numero
        except ValueError:
            print("Por favor, digite apenas números inteiros!")

def verificar_par_impar(numero):
    """
    Verifica se um número é par ou ímpar usando o operador módulo
    Retorna True para par e False para ímpar
    """
    return numero % 2 == 0

def exibir_resultado(numero, eh_par):
    """Exibe o resultado da verificação de forma formatada"""
    resultado = "par" if eh_par else "ímpar"
    print(f"\nO número {numero} é {resultado}!")
    
    # Informação adicional sobre o número
    if numero > 0:
        print("Este é um número positivo")
    elif numero < 0:
        print("Este é um número negativo")
    else:
        print("Este é o número zero")

if __name__ == "__main__":
    print("=== Verificador de Números Pares e Ímpares ===")
    
    try:
        # Obtém o número do usuário
        numero = obter_numero()
        
        # Verifica se é par ou ímpar
        eh_par = verificar_par_impar(numero)
        
        # Exibe o resultado
        exibir_resultado(numero, eh_par)
        
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
