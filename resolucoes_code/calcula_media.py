"""
Módulo para cálculo de média de notas
Este módulo demonstra o uso de operadores aritméticos e manipulação de entrada do usuário
"""

def obter_nota(numero_nota):
    """
    Solicita e valida uma nota do usuário
    Retorna a nota como float se estiver entre 0 e 10
    """
    while True:
        try:
            nota = float(input(f"Digite a {numero_nota}ª nota (0-10): "))
            if 0 <= nota <= 10:
                return nota
            else:
                print("A nota deve estar entre 0 e 10!")
        except ValueError:
            print("Por favor, digite um número válido!")

def calcular_media(notas):
    """Calcula a média aritmética das notas"""
    return sum(notas) / len(notas)

def determinar_situacao(media):
    """Determina a situação do aluno com base na média"""
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"

def exibir_resultado(notas, media, situacao):
    """Exibe o resultado final com todas as informações"""
    print("\n=== Resultado ===")
    for i, nota in enumerate(notas, 1):
        print(f"Nota {i}: {nota:.1f}")
    print(f"\nMédia final: {media:.1f}")
    print(f"Situação: {situacao}")

if __name__ == "__main__":
    print("=== Calculadora de Média de Notas ===")
    
    try:
        # Coleta as três notas
        notas = []
        for i in range(1, 4):  # Coletar 3 notas
            nota = obter_nota(i)
            notas.append(nota)
        
        # Calcula a média
        media = calcular_media(notas)
        
        # Determina a situação do aluno
        situacao = determinar_situacao(media)
        
        # Exibe o resultado
        exibir_resultado(notas, media, situacao)
        
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
