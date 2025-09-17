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

    # CSS estilo MagicUI (gradientes, brilhos, cartões)
    st.markdown(
        """
        <style>
        /* Fundo com gradiente sutil */
        .stApp {
            background: radial-gradient(1200px 600px at 10% 10%, #1a1f2e 0%, #0f1420 50%, #0a0d14 100%);
            color: #e6e9ef;
        }
        /* Título com gradiente */
        .gradient-text {
            background: linear-gradient(90deg, #8b5cf6 0%, #06b6d4 50%, #22d3ee 100%);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            filter: drop-shadow(0 2px 10px rgba(34, 211, 238, 0.25));
        }
        /* Linha divisória elegante */
        .nice-sep { height: 1px; background: linear-gradient(90deg, transparent, rgba(255,255,255,0.15), transparent); margin: 12px 0 22px; }
        /* Cartões */
        .glass-card {
            border-radius: 16px;
            background: linear-gradient(180deg, rgba(255,255,255,0.06), rgba(255,255,255,0.03));
            border: 1px solid rgba(255,255,255,0.08);
            box-shadow: 0 20px 35px -15px rgba(0,0,0,0.55), inset 0 1px 0 rgba(255,255,255,0.04);
            padding: 18px 16px;
        }
        /* Botão brilhante estilo Magic */
        .stButton > button {
            background: linear-gradient(90deg, #4f46e5, #06b6d4, #22d3ee);
            background-size: 200% 100%;
            color: #0b1020;
            border: 0;
            border-radius: 12px;
            padding: 10px 16px;
            font-weight: 700;
            transition: background-position 300ms ease, transform 120ms ease, box-shadow 120ms ease;
            box-shadow: 0 0 0 1px rgba(255,255,255,0.06) inset, 0 10px 25px -10px rgba(34, 211, 238, 0.6);
        }
        .stButton > button:hover {
            background-position: 100% 0;
            transform: translateY(-1px);
            box-shadow: 0 0 0 1px rgba(255,255,255,0.08) inset, 0 18px 35px -10px rgba(34, 211, 238, 0.8);
        }
        .stButton > button:active { transform: translateY(0); }
        /* Inputs */
        .stNumberInput input {
            background: rgba(255,255,255,0.06);
            border-radius: 10px !important;
            border: 1px solid rgba(255,255,255,0.08);
            color: #e6e9ef !important;
        }
        /* Cabeçalhos */
        h1, h2, h3, h4 { letter-spacing: 0.2px; }
        /* Footer links */
        .footer a { color: #7dd3fc; text-decoration: none; }
        .footer a:hover { text-decoration: underline; }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Título principal
    st.markdown("<h1 class='gradient-text'>🧮 Calculadora Python Web</h1>", unsafe_allow_html=True)
    st.markdown("<div class='nice-sep'></div>", unsafe_allow_html=True)

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
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)

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

        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.subheader("📊 Resultado")
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)

        # Botão para calcular
        if st.button("✨ Calcular", type="primary", use_container_width=True):
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

        st.markdown("</div>", unsafe_allow_html=True)

    # Informações adicionais
    st.markdown("<div class='nice-sep'></div>", unsafe_allow_html=True)

    # Expansor com informações sobre as operações
    with st.expander("ℹ️ Informações sobre as Operações"):
        st.markdown(
            """
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
            """
        )

    # Expansor com exemplos
    with st.expander("💡 Exemplos de Uso"):
        st.markdown(
            """
            **Exemplos de Cálculos:**
            - **Soma:** 5 + 3 = 8
            - **Potência:** 2^3 = 8
            - **Raiz Quadrada:** √16 = 4
            - **Seno:** sen(30°) = 0.5
            - **Fatorial:** 5! = 120
            - **Logaritmo:** ln(e) = 1
            """
        )

    # Rodapé
    st.markdown("<div class='nice-sep'></div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='footer'>**Desenvolvido com ❤️ usando Python e Streamlit** | "
        "💻 <a href='https://github.com/rubensliv/calculadora-python-web' target='_blank'>Código Fonte</a> | "
        "📧 <a href='mailto:contato@exemplo.com'>Contato</a></div>",
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()