#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculadora Web em Python com Streamlit
Uma calculadora interativa com interface web moderna
"""

import streamlit as st
import math


def calcular_soma(numero_a, numero_b):
    """Realiza a operação de soma"""
    return numero_a + numero_b


def calcular_subtracao(numero_a, numero_b):
    """Realiza a operação de subtração"""
    return numero_a - numero_b


def calcular_multiplicacao(numero_a, numero_b):
    """Realiza a operação de multiplicação"""
    return numero_a * numero_b


def calcular_divisao(numero_a, numero_b):
    """Realiza a operação de divisão"""
    if numero_b == 0:
        raise ValueError("❌ Erro: Divisão por zero não é permitida!")
    return numero_a / numero_b


def calcular_potencia(base, expoente):
    """Calcula a potência"""
    return base ** expoente


def calcular_raiz_quadrada(numero):
    """Calcula a raiz quadrada"""
    if numero < 0:
        raise ValueError("❌ Erro: Não é possível calcular raiz quadrada de número negativo!")
    return math.sqrt(numero)


def calcular_seno(angulo_graus):
    """Calcula o seno de um ângulo em graus"""
    return math.sin(math.radians(angulo_graus))


def calcular_cosseno(angulo_graus):
    """Calcula o cosseno de um ângulo em graus"""
    return math.cos(math.radians(angulo_graus))


def calcular_tangente(angulo_graus):
    """Calcula a tangente de um ângulo em graus"""
    return math.tan(math.radians(angulo_graus))


def calcular_logaritmo(numero):
    """Calcula o logaritmo natural"""
    if numero <= 0:
        raise ValueError("❌ Erro: Logaritmo só é definido para números positivos!")
    return math.log(numero)


def calcular_fatorial(numero):
    """Calcula o fatorial de um número"""
    if numero < 0:
        raise ValueError("❌ Erro: Fatorial não é definido para números negativos!")
    if not numero.is_integer():
        raise ValueError("❌ Erro: Fatorial só é definido para números inteiros!")
    return math.factorial(int(numero))


def main():
    """Função principal da aplicação Streamlit"""
    # Configuração da página
    st.set_page_config(
        page_title="Calculadora Python",
        page_icon="🧮",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Título principal
    st.title("🧮 Calculadora Python Web")
    st.markdown("---")
    
    # Sidebar com seleção de operação
    st.sidebar.header("🔢 Escolha a Operação")
    
    operacao = st.sidebar.selectbox(
        "Selecione uma operação:",
        [
            "Soma (+)",
            "Subtração (-)",
            "Multiplicação (×)",
            "Divisão (÷)",
            "Potência (^)",
            "Raiz Quadrada (√)",
            "Seno",
            "Cosseno",
            "Tangente",
            "Logaritmo Natural (ln)",
            "Fatorial (!)"
        ]
    )
    
    # Container principal
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📝 Entrada de Dados")
        
        # Operações que precisam de dois números
        if operacao in ["Soma (+)", "Subtração (-)", "Multiplicação (×)", "Divisão (÷)", "Potência (^)"]:
            numero_a = st.number_input("Primeiro número:", value=0.0, step=0.1, format="%.6f")
            numero_b = st.number_input("Segundo número:", value=0.0, step=0.1, format="%.6f")
            
        # Operações que precisam de um número
        elif operacao in ["Raiz Quadrada (√)", "Logaritmo Natural (ln)", "Fatorial (!)"]:
            numero = st.number_input("Digite o número:", value=0.0, step=0.1, format="%.6f")
            
        # Operações trigonométricas
        elif operacao in ["Seno", "Cosseno", "Tangente"]:
            angulo = st.number_input("Digite o ângulo em graus:", value=0.0, step=0.1, format="%.6f")
    
    with col2:
        st.subheader("📊 Resultado")
        
        # Botão para calcular
        if st.button("🚀 Calcular", type="primary", use_container_width=True):
            try:
                if operacao == "Soma (+)":
                    resultado = calcular_soma(numero_a, numero_b)
                    st.success(f"✅ **{numero_a} + {numero_b} = {resultado}**")
                    
                elif operacao == "Subtração (-)":
                    resultado = calcular_subtracao(numero_a, numero_b)
                    st.success(f"✅ **{numero_a} - {numero_b} = {resultado}**")
                    
                elif operacao == "Multiplicação (×)":
                    resultado = calcular_multiplicacao(numero_a, numero_b)
                    st.success(f"✅ **{numero_a} × {numero_b} = {resultado}**")
                    
                elif operacao == "Divisão (÷)":
                    resultado = calcular_divisao(numero_a, numero_b)
                    st.success(f"✅ **{numero_a} ÷ {numero_b} = {resultado}**")
                    
                elif operacao == "Potência (^)":
                    resultado = calcular_potencia(numero_a, numero_b)
                    st.success(f"✅ **{numero_a}^{numero_b} = {resultado}**")
                    
                elif operacao == "Raiz Quadrada (√)":
                    resultado = calcular_raiz_quadrada(numero)
                    st.success(f"✅ **√{numero} = {resultado}**")
                    
                elif operacao == "Seno":
                    resultado = calcular_seno(angulo)
                    st.success(f"✅ **sen({angulo}°) = {resultado}**")
                    
                elif operacao == "Cosseno":
                    resultado = calcular_cosseno(angulo)
                    st.success(f"✅ **cos({angulo}°) = {resultado}**")
                    
                elif operacao == "Tangente":
                    resultado = calcular_tangente(angulo)
                    st.success(f"✅ **tan({angulo}°) = {resultado}**")
                    
                elif operacao == "Logaritmo Natural (ln)":
                    resultado = calcular_logaritmo(numero)
                    st.success(f"✅ **ln({numero}) = {resultado}**")
                    
                elif operacao == "Fatorial (!)":
                    resultado = calcular_fatorial(numero)
                    st.success(f"✅ **{int(numero)}! = {resultado}**")
                    
            except ValueError as error:
                st.error(str(error))
            except ArithmeticError as error:
                st.error(f"❌ **Erro matemático:** {error}")
            except Exception as error:
                st.error(f"❌ **Erro inesperado:** {error}")
    
    # Informações adicionais
    st.markdown("---")
    
    # Expansor com informações sobre as operações
    with st.expander("ℹ️ Informações sobre as Operações"):
        st.markdown("""
        **Operações Básicas:**
        - **Soma (+):** Adiciona dois números
        - **Subtração (-):** Subtrai o segundo número do primeiro
        - **Multiplicação (×):** Multiplica dois números
        - **Divisão (÷):** Divide o primeiro número pelo segundo
        
        **Operações Avançadas:**
        - **Potência (^):** Eleva o primeiro número à potência do segundo
        - **Raiz Quadrada (√):** Calcula a raiz quadrada de um número
        - **Seno/Cosseno/Tangente:** Funções trigonométricas (ângulo em graus)
        - **Logaritmo Natural (ln):** Logaritmo na base e
        - **Fatorial (!):** Produto de todos os inteiros positivos até o número
        """)
    
    # Expansor com exemplos
    with st.expander("💡 Exemplos de Uso"):
        st.markdown("""
        **Exemplos de Cálculos:**
        - **Soma:** 5 + 3 = 8
        - **Potência:** 2^3 = 8
        - **Raiz Quadrada:** √16 = 4
        - **Seno:** sen(30°) = 0.5
        - **Fatorial:** 5! = 120
        - **Logaritmo:** ln(e) = 1
        """)
    
    # Rodapé
    st.markdown("---")
    st.markdown(
        "**Desenvolvido com ❤️ usando Python e Streamlit** | "
        "💻 [Código Fonte](https://github.com/rubensliv/calculadora-python-web) | "
        "📧 [Contato](mailto:contato@exemplo.com)"
    )


if __name__ == "__main__":
    main()