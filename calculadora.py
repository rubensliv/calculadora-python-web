#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculadora em Python
Uma calculadora simples com operações básicas e avançadas
"""

import math
import sys


def exibir_menu():
    """Exibe o menu principal da calculadora"""
    print("\n" + "="*50)
    print("           CALCULADORA PYTHON")
    print("="*50)
    print("1. Soma (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    print("5. Potência (^)")
    print("6. Raiz Quadrada (√)")
    print("7. Seno")
    print("8. Cosseno")
    print("9. Tangente")
    print("10. Logaritmo")
    print("11. Fatorial")
    print("0. Sair")
    print("="*50)


def obter_numero(mensagem):
    """Obtém um número válido do usuário"""
    while True:
        try:
            numero = float(input(mensagem))
            return numero
        except ValueError:
            print("❌ Erro: Digite um número válido!")
        except KeyboardInterrupt:
            print("\n\n👋 Calculadora encerrada pelo usuário.")
            sys.exit(0)


def obter_numero_positivo(mensagem):
    """Obtém um número positivo válido do usuário"""
    while True:
        numero = obter_numero(mensagem)
        if numero >= 0:
            return numero
        print("❌ Erro: O número deve ser positivo!")


def somar(numero_a, numero_b):
    """Realiza a operação de soma"""
    return numero_a + numero_b


def subtrair(numero_a, numero_b):
    """Realiza a operação de subtração"""
    return numero_a - numero_b


def multiplicar(numero_a, numero_b):
    """Realiza a operação de multiplicação"""
    return numero_a * numero_b


def dividir(numero_a, numero_b):
    """Realiza a operação de divisão"""
    if numero_b == 0:
        raise ValueError("❌ Erro: Divisão por zero não é permitida!")
    return numero_a / numero_b


def potencia(base, expoente):
    """Calcula a potência"""
    return base ** expoente


def raiz_quadrada(numero):
    """Calcula a raiz quadrada"""
    if numero < 0:
        raise ValueError("❌ Erro: Não é possível calcular raiz quadrada de número negativo!")
    return math.sqrt(numero)


def seno(angulo_graus):
    """Calcula o seno de um ângulo em graus"""
    return math.sin(math.radians(angulo_graus))


def cosseno(angulo_graus):
    """Calcula o cosseno de um ângulo em graus"""
    return math.cos(math.radians(angulo_graus))


def tangente(angulo_graus):
    """Calcula a tangente de um ângulo em graus"""
    return math.tan(math.radians(angulo_graus))


def logaritmo(numero):
    """Calcula o logaritmo natural"""
    if numero <= 0:
        raise ValueError("❌ Erro: Logaritmo só é definido para números positivos!")
    return math.log(numero)


def fatorial(numero):
    """Calcula o fatorial de um número"""
    if numero < 0:
        raise ValueError("❌ Erro: Fatorial não é definido para números negativos!")
    if not numero.is_integer():
        raise ValueError("❌ Erro: Fatorial só é definido para números inteiros!")
    return math.factorial(int(numero))


def executar_operacao_basica(escolha):
    """Executa operações básicas que precisam de dois números"""
    numero_a = obter_numero("Digite o primeiro número: ")
    numero_b = obter_numero("Digite o segundo número: ")

    if escolha == 1:  # Soma
        resultado = somar(numero_a, numero_b)
        print(f"✅ Resultado: {numero_a} + {numero_b} = {resultado}")
    elif escolha == 2:  # Subtração
        resultado = subtrair(numero_a, numero_b)
        print(f"✅ Resultado: {numero_a} - {numero_b} = {resultado}")
    elif escolha == 3:  # Multiplicação
        resultado = multiplicar(numero_a, numero_b)
        print(f"✅ Resultado: {numero_a} × {numero_b} = {resultado}")
    elif escolha == 4:  # Divisão
        resultado = dividir(numero_a, numero_b)
        print(f"✅ Resultado: {numero_a} ÷ {numero_b} = {resultado}")


def executar_operacao_avancada(escolha):
    """Executa operações avançadas"""
    if escolha == 5:  # Potência
        base = obter_numero("Digite a base: ")
        expoente = obter_numero("Digite o expoente: ")
        resultado = potencia(base, expoente)
        print(f"✅ Resultado: {base}^{expoente} = {resultado}")
    elif escolha == 6:  # Raiz quadrada
        numero = obter_numero_positivo("Digite o número: ")
        resultado = raiz_quadrada(numero)
        print(f"✅ Resultado: √{numero} = {resultado}")
    elif escolha == 7:  # Seno
        angulo = obter_numero("Digite o ângulo em graus: ")
        resultado = seno(angulo)
        print(f"✅ Resultado: sen({angulo}°) = {resultado}")
    elif escolha == 8:  # Cosseno
        angulo = obter_numero("Digite o ângulo em graus: ")
        resultado = cosseno(angulo)
        print(f"✅ Resultado: cos({angulo}°) = {resultado}")
    elif escolha == 9:  # Tangente
        angulo = obter_numero("Digite o ângulo em graus: ")
        resultado = tangente(angulo)
        print(f"✅ Resultado: tan({angulo}°) = {resultado}")
    elif escolha == 10:  # Logaritmo
        numero = obter_numero_positivo("Digite o número: ")
        resultado = logaritmo(numero)
        print(f"✅ Resultado: ln({numero}) = {resultado}")
    elif escolha == 11:  # Fatorial
        numero = obter_numero("Digite um número inteiro: ")
        resultado = fatorial(numero)
        print(f"✅ Resultado: {int(numero)}! = {resultado}")


def executar_operacao(escolha):
    """Executa a operação selecionada"""
    try:
        if 1 <= escolha <= 4:
            executar_operacao_basica(escolha)
        elif 5 <= escolha <= 11:
            executar_operacao_avancada(escolha)

    except ValueError as error:
        print(str(error))
    except ArithmeticError as error:
        print(f"❌ Erro matemático: {error}")


def main():
    """Função principal da calculadora"""
    print("🚀 Bem-vindo à Calculadora Python!")

    while True:
        try:
            exibir_menu()
            escolha = input("\nEscolha uma opção (0-11): ").strip()

            if escolha == '0':
                print("\n👋 Obrigado por usar a Calculadora Python!")
                break
            if escolha.isdigit() and 1 <= int(escolha) <= 11:
                executar_operacao(int(escolha))
            else:
                print("❌ Opção inválida! Escolha um número de 0 a 11.")

            input("\n⏸️  Pressione Enter para continuar...")

        except KeyboardInterrupt:
            print("\n\n👋 Calculadora encerrada pelo usuário.")
            break
        except (ValueError, ArithmeticError) as error:
            print(f"❌ Erro: {error}")
            input("\n⏸️  Pressione Enter para continuar...")


if __name__ == "__main__":
    main()
