import streamlit as st

# Configuración de la página (¡Esto le da el diseño ancho y limpio!)
st.set_page_config(page_title="BioInnova - Aula Virtual", layout="wide")

# Diccionario con el código genético para el Simulador 1
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
    for i in range(0, len(secuencia_arn) - len(secuencia_arn) % 3, 3):
        codon = secuencia_arn[i:i+3]
        resultado = CODIGO_GENETICO.get(codon, "Desconocido")
        aminoacidos.append(f"{codon} ➔ {resultado}")
    return aminoacidos

# --- MENÚ LATERAL (SIDEBAR) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3022/3022607.png", width=100)
    st.title("BioInnova Hub")
    st.write("Aula Interactiva de Bioinformática")
    st.markdown("---")
    
    # Aquí creamos el selector de espacios igual que tu compañero
    opcion = st.radio(
        "Selecciona un espacio del aula:",
        [
            "🏠 Inicio del Aula",
            "🧬 1. Transcripción y Traducción",
            "📊 2. Alineamiento de Secuencias",
            "🧩 3. Ensamble de Fragmentos",
            "🌳 4. Filogenia UPGMA",
            "🔬 5. Modelado Estructural"
        ]
    )

# --- CONTENIDO PRINCIPAL SEGÚN LA OPCIÓN SELECCIONADA ---

if opcion == "🏠 Inicio del Aula":
    # Banner llamativo de bienvenida
    st.info("### 💻 Sistema Central BioInnova v1.0\nSimuladores interactivos avanzados orientados a la educación secundaria.")
    
    st.title("🧬 Bienvenidos al Laboratorio Digital de Bioinformática")
    st.write("Esta plataforma integra herramientas computacionales y modelos biológicos diseñados para el aprendizaje activo y la experimentación genética.")
    
    # Crear tarjetas visuales organizadas
    col1, col2 = st.columns(2)
    with col1:
        st.success("#### 🧪 Propósito Pedagógico\nPermitir a los estudiantes manipular secuencias moleculares reales y simular fenómenos evolutivos y estructurales en tiempo real.")
    with col2:
        st.warning("#### 🤖 Asistente de Aula\nExplora cada módulo interactivo utilizando el menú de la izquierda para desplegar los algoritmos base.")

elif opcion == "🧬 1. Transcripción y Traducción":
    st.title("🧬 Módulo 1: Del Gen a la Proteína (Transcripción, Traducción y Mutaciones)")
    
    st.header("1. Entrada de la Secuencia de ADN")
    adn_usuario = st.text_input("Ingresa una secuencia de ADN (ej: ATGGCCATT):", "ATGGCCATTTAG").upper().strip()

    if not all(base in "ATCG" for base in adn_usuario):
        st.error("⚠️ Error: La secuencia contiene caracteres inválidos. Solo se permiten A, T, C y G.")
    else:
        arn_usuario = adn_usuario.replace("T", "U")
        
        st.subheader("📝 Proceso de Transcripción (ADN a ARNm)")
        st.code(f"Hebra de ADN:  {adn_usuario}\nCadena de ARNm: {arn_usuario}", language="text")
        
        st.subheader("🧪 Cadena de Aminoácidos (Proteína Original)")
        lista_proteina_original = traducir_arn(arn_usuario)
        for aminoacido in lista_proteina_original:
            st.write(f"• {aminoacido}")
            
        st.markdown("---")
        
        st.header("2. Laboratorio de Mutaciones")
        posicion = st.number_input("Elige la posición de la base que deseas cambiar (desde 1):", 
                                  min_value=1, max_value=len(adn_usuario), value=4) - 1
        
        nueva_base = st.selectbox("Selecciona la nueva base nitrogenada mutada:", ["A", "T", "C", "G"])
        
        lista_adn_mutado = list(adn_usuario)
        lista_adn_mutado[posicion] = nueva_base
        adn_mutado = "".join(lista_adn_mutado)
        arn_mutado = adn_mutado.replace("T", "U")
        
        st.subheader("🔄 Comparación de Secuencias Genómicas")
        st.code(f"ADN Original: {adn_usuario}\nADN Mutado:   {adn_mutado}", language="text")
        
        st.subheader("🧬 Nueva Cadena de Aminoácidos (Resultado de la Mutación)")
        lista_proteina_mutada = traducir_arn(arn_mutado)
        
        for idx, linea in enumerate(lista_proteina_mutada):
            if idx < len(lista_proteina_original) and lista_proteina_original[idx] != linea:
                st.write(f"🔴 **{linea} (¡CAMBIÓ POR LA MUTACIÓN!)**")
            else:
                st.write(f"• {linea}")

elif opcion == "📊 2. Alineamiento de Secuencias":
    st.title("📊 Módulo 2: Alineamiento de Secuencias")
    st.info("Próximamente: Constructor interactivo de la matriz de puntuación (Needleman-Wunsch).")

elif opcion == "🧩 3. Ensamble de Fragmentos":
    st.title("🧩 Módulo 3: Ensamble de Fragmentos")
    st.info("Próximamente: Simulador a escala reducida mediante Gráficos de De Bruijn.")

elif opcion == "🌳 4. Filogenia UPGMA":
    st.title("🌳 Módulo 4: Filogenia Interactiva")
    st.info("Próximamente: Construcción dinámica de árboles evolutivos basados en matrices de distancia.")

elif opcion == "🔬 5. Modelado Estructural":
    st.title("🔬 Módulo 5: Modelado Estructural de Proteínas")
    st.info("Próximamente: Simulación tridimensional del impacto de mutaciones puntuales.")
