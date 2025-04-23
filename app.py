import streamlit as st

# Função para calcular o desconto do INSS
def calcular_inss(salario_bruto):
    faixas = [
        (1412.00, 0.075),
        (2666.68, 0.09),
        (4000.03, 0.12),
        (7786.02, 0.14)
    ]
    inss = 0.0
    limite_anterior = 0.0

    for limite, aliquota in faixas:
        if salario_bruto > limite:
            inss += (limite - limite_anterior) * aliquota
            limite_anterior = limite
        else:
            inss += (salario_bruto - limite_anterior) * aliquota
            break
    return inss

# Função para calcular o desconto do IRRF
def calcular_irrf(salario_bruto, inss, dependentes):
    base_calculo = salario_bruto - inss - (dependentes * 189.59)
    if base_calculo <= 2259.20:
        return 0.0
    elif base_calculo <= 2826.65:
        return base_calculo * 0.075 - 169.44
    elif base_calculo <= 3751.05:
        return base_calculo * 0.15 - 381.44
    elif base_calculo <= 4664.68:
        return base_calculo * 0.225 - 662.77
    else:
        return base_calculo * 0.275 - 896.00

# Interface com Streamlit
st.title("Calculadora de Salário Líquido 2024")

salario_bruto = st.number_input("Informe o salário bruto (R$):", min_value=0.0, format="%.2f")
dependentes = st.number_input("Número de dependentes:", min_value=0, step=1)

if st.button("Calcular"):
    inss = calcular_inss(salario_bruto)
    irrf = calcular_irrf(salario_bruto, inss, dependentes)
    salario_liquido = salario_bruto - inss - irrf

    st.subheader("Resultado:")
    st.write(f"Salário Bruto: R$ {salario_bruto:.2f}")
    st.write(f"INSS: R$ {inss:.2f}")
    st.write(f"IRRF: R$ {irrf:.2f}")
    st.write(f"Salário Líquido: R$ {salario_liquido:.2f}")
