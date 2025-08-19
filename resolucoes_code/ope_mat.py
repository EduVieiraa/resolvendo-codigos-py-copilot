"""
Módulo de operações matemáticas
Este módulo contém funções para realizar diferentes operações matemáticas entre números
"""

def solicitar_numeros():
    """Solicita dois números ao usuário"""
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        return num1, num2
    except ValueError:
        raise ValueError("Por favor, digite apenas números válidos")

def calcular_operacoes(num1, num2):
    """Realiza operações matemáticas básicas entre dois números"""
    soma = num1 + num2
    subtracao = num1 - num2
    multiplicacao = num1 * num2
    divisao = num1 / num2 if num2 != 0 else "Não é possível dividir por zero"
    
    return {
        "soma": soma,
        "subtracao": subtracao,
        "multiplicacao": multiplicacao,
        "divisao": divisao
    }

def mostrar_resultados(resultados):
    """Mostra os resultados das operações"""
    print("\nResultados:")
    for operacao, resultado in resultados.items():
        print(f"{operacao.capitalize()}: {resultado}")

if __name__ == "__main__":
    try:
        num1, num2 = solicitar_numeros()
        resultados = calcular_operacoes(num1, num2)
        mostrar_resultados(resultados)
    except ValueError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")