import streamlit as st

# Diccionario con el código genético real para la traducción
CODIGO_GENETICO = {
    'UUU': 'Fenilalanina', 'UUC': 'Fenilalanina', 'UUA': 'Leucina', 'UUG': 'Leucina',
    'CUU': 'Leucina', 'CUC': 'Leucina', 'CUA': 'Leucina', 'CUG': 'Leucina',
    'AUU': 'Isoleucina', 'AUC': 'Isoleucina', 'AUA': 'Isoleucina', 'AUG': 'Metionina (INICIO)',
    'GUU': 'Valina', 'GUC': 'Valina', 'GUA': 'Valina', 'GUG': 'Valina',
    'UCU': 'Serina', 'UCC': 'Serina', 'UCA': 'Serina', 'UCG': 'Serina',
    'CCU': 'Prolina', 'CCC': 'Prolina', 'CCA': 'Prolina', 'CCG': 'Prolina',
    'ACU': 'Treonina', 'ACC': 'Treonina', 'ACA': 'Treonina', 'ACG': 'Treonina',
    'GCU': 'Alanina', 'GCC': 'Alanina', 'GCA': 'Alanina', 'GCG': 'Alanina',
    'UAU': 'Tirosina', 'UAC': 'Tirosina', 'UAA': 'STOP (Parada)', 'UAG': 'STOP (Parada)',
    'CAU': 'Histidina', 'CAC': 'Histidina', 'CAA': 'Glutamina', 'CAG': 'Glutamina',
    'AAU': 'Asparagina', 'AAC': 'Asparagina', 'AAA': 'Lisina', 'AAG': 'Lisina',
    'GAU': 'Ácido Aspártico', 'GAC': 'Ácido Aspártico', 'GAA': 'Ácido Glutámico', 'GAG': 'Ácido Glutámico',
    'UGU': 'Cisteína', 'UGC': 'Cisteína', 'UGA': 'STOP (Parada)', 'UGG': 'Triptófano',
    'CGU': 'Arginina', 'CGC': 'Arginina', 'CGA': 'Arginina', 'CGG': 'Arginina',
    'AGU': 'Serina', 'AGC': 'Serina', 'AGA': 'Arginina', 'AGG': 'Arginina',
    'GGU': 'Glicina', 'GGC': 'Glicina', 'GGA': 'Glicina', 'GGG': 'Glicina'
}

def traducir_arn(secuencia_arn):
    aminoacidos = []
    # Lee la secuencia recorriendo de 3 en 3 letras (codones)
    for i in range(0, len(secuencia_arn) - len(secuencia_arn) % 3, 3):
        codon = secuencia_arn[i:i+3]
        resultado = CODIGO_GENETICO.get(codon, "Desconocido")
        aminoacidos.append(f"{codon} ➔ {resultado}")
    return aminoacidos

# --- INTERFAZ GRÁFICA DE LA APLICACIÓN WEB ---
st.title("🧬 Simulador 1: Transcripción y Traducción de ADN")
st.write("Módulo interactivo diseñado para visualizar la síntesis de proteínas y el impacto de las mutaciones.")

st.header("1. Entrada de la Secuencia de ADN")
# Secuencia predeterminada para que el usuario entienda el formato (múltiplo de 3)
adn_usuario = st.text_input("Ingresa una secuencia de ADN (ej: ATGGCCATT):", "ATGGCCATTTAG").upper().strip()

# Validación pedagógica de la entrada
if not all(base in "ATCG" for base in adn_usuario):
    st.error("⚠️ Error: La secuencia contiene caracteres inválidos. Solo se permiten las bases nitrogenadas A, T, C y G.")
else:
    # PROCESO 1: Transcripción (Sustituir Timina por Uracilo)
    arn_usuario = adn_usuario.replace("T", "U")
    
    st.subheader("📝 Proceso de Transcripción (ADN a ARNm)")
    st.code(f"Hebra de ADN:  {adn_usuario}\nCadena de ARNm: {arn_usuario}", language="text")
    
    # PROCESO 2: Traducción Original
    st.subheader("🧪 Cadena de Aminoácidos (Proteína Original)")
    lista_proteina_original = traducir_arn(arn_usuario)
    for aminoacido in lista_proteina_original:
        st.write(f"• {aminoacido}")
        
    st.markdown("---")
    
    # PROCESO 3: Simulación Dinámica de Mutaciones Puntuales
    st.header("2. Laboratorio de Mutaciones")
    st.write("Modifica una única base nitrogenada de la secuencia original para comprobar experimentalmente su efecto.")
    
    # Control interactivo para elegir la posición exacta de la mutación
    posicion = st.number_input("Elige la posición de la base que deseas cambiar (desde 1):", 
                              min_value=1, max_value=len(adn_usuario), value=4) - 1
    
    nueva_base = st.selectbox("Selecciona la nueva base nitrogenada mutada:", ["A", "T", "C", "G"])
    
    # Construcción de la secuencia mutada
    lista_adn_mutado = list(adn_usuario)
    lista_adn_mutado[posicion] = nueva_base
    adn_mutado = "".join(lista_adn_mutado)
    arn_mutado = adn_mutado.replace("T", "U")
    
    st.subheader("🔄 Comparación de Secuencias Genómicas")
    st.code(f"ADN Original: {adn_usuario}\nADN Mutado:   {adn_mutado}", language="text")
    
    # Traducción de la secuencia mutada y comparación en tiempo real
    st.subheader("🧬 Nueva Cadena de Aminoácidos (Resultado de la Mutación)")
    lista_proteina_mutada = traducir_arn(arn_mutado)
    
    for idx, linea in enumerate(lista_proteina_mutada):
        # Si el aminoácido mutado cambió respecto al original, lo resaltamos en rojo
        if idx < len(lista_proteina_original) and lista_proteina_original[idx] != linea:
            st.write(f"🔴 **{linea} (¡CAMBIÓ POR LA MUTACIÓN!)**")
        else:
            st.write(f"• {linea}")
