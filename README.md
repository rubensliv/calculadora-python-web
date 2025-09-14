# 🧮 Calculadora Python Web

Uma calculadora interativa desenvolvida em Python com interface web moderna usando Streamlit.

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## ✨ Funcionalidades

### Operações Básicas
- ➕ **Soma** - Adiciona dois números
- ➖ **Subtração** - Subtrai o segundo número do primeiro
- ✖️ **Multiplicação** - Multiplica dois números
- ➗ **Divisão** - Divide o primeiro número pelo segundo

### Operações Avançadas
- 🔢 **Potência** - Eleva um número à potência de outro
- √ **Raiz Quadrada** - Calcula a raiz quadrada de um número
- 📐 **Funções Trigonométricas** - Seno, Cosseno e Tangente (ângulos em graus)
- 📊 **Logaritmo Natural** - Logaritmo na base e
- ! **Fatorial** - Produto de todos os inteiros positivos até o número

## 🚀 Como Executar

### Pré-requisitos
- Python 3.7 ou superior
- pip (gerenciador de pacotes do Python)

### Instalação

1. **Clone o repositório**
   ```bash
   git clone https://github.com/rubensliv/calculadora-python-web.git
   cd calculadora-python-web
   ```

2. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute a aplicação**
   ```bash
   streamlit run calculadora_web.py
   ```

4. **Acesse no navegador**
   - A aplicação será aberta automaticamente em `http://localhost:8501`
   - Se não abrir automaticamente, acesse manualmente o endereço

## 📱 Interface

A aplicação possui uma interface moderna e responsiva com:

- **Sidebar** para seleção de operações
- **Campos de entrada** intuitivos
- **Botão de cálculo** destacado
- **Exibição de resultados** com formatação clara
- **Tratamento de erros** com mensagens informativas
- **Seções informativas** com exemplos e explicações

## 🛠️ Tecnologias Utilizadas

- **Python 3.x** - Linguagem de programação
- **Streamlit** - Framework para aplicações web
- **Math** - Biblioteca padrão do Python para operações matemáticas

## 📁 Estrutura do Projeto

```
calculadora-python-web/
├── calculadora.py          # Versão console da calculadora
├── calculadora_web.py      # Versão web com Streamlit
├── requirements.txt        # Dependências do projeto
└── README.md              # Este arquivo
```

## 🔧 Desenvolvimento

### Executar em modo de desenvolvimento
```bash
streamlit run calculadora_web.py --server.runOnSave true
```

### Adicionar novas operações
1. Crie uma nova função de cálculo
2. Adicione a opção no selectbox da sidebar
3. Implemente a lógica no botão de cálculo

## 📝 Exemplos de Uso

### Operações Básicas
- **Soma:** 5 + 3 = 8
- **Subtração:** 10 - 4 = 6
- **Multiplicação:** 7 × 8 = 56
- **Divisão:** 15 ÷ 3 = 5

### Operações Avançadas
- **Potência:** 2^8 = 256
- **Raiz Quadrada:** √64 = 8
- **Seno:** sen(30°) = 0.5
- **Fatorial:** 5! = 120
- **Logaritmo:** ln(e) = 1

## 🐛 Tratamento de Erros

A aplicação possui tratamento robusto de erros para:
- Divisão por zero
- Raiz quadrada de números negativos
- Logaritmo de números não positivos
- Fatorial de números negativos ou não inteiros
- Entradas inválidas

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir novas funcionalidades
- Enviar pull requests
- Melhorar a documentação

## 📧 Contato

Para dúvidas ou sugestões, entre em contato através do email: contato@exemplo.com

---

**Desenvolvido com ❤️ usando Python e Streamlit**

🔗 **Link do Repositório:** [https://github.com/rubensliv/calculadora-python-web](https://github.com/rubensliv/calculadora-python-web)