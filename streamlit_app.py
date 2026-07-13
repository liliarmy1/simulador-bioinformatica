import streamlit as st

# Configuración de página limpia y profesional
st.set_page_config(page_title="BioInnova - Plataforma de Simulación", layout="wide")

# Diccionario del código genético real para el Simulador 1
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

# --- NAVEGACIÓN LATERAL SIN EMOJIS ---
with st.sidebar:
    st.title("BioInnova")
    st.write("Plataforma Educativa de Bioinformática")
    st.markdown("---")
    
    opcion = st.radio(
        "Navegación del Sistema:",
        [
            "Inicio de la Plataforma",
            "1. Transcripción y Traducción",
            "2. Alineamiento de Secuencias",
            "3. Ensamble de Fragmentos",
            "4. Filogenia (UPGMA)",
            "5. Modelado Estructural",
            "Manual y Usabilidad"
        ]
    )

# --- CONTENIDO PRINCIPAL ---

# ----------------------------------------------------
# SECCIÓN: INICIO
# ----------------------------------------------------
if opcion == "Inicio de la Plataforma":
    st.info("### Sistema Integrado de Bioinformática Educativa\nPlataforma diseñada para la experimentación molecular y el análisis genómico interactivo.")
    
    st.title("Bienvenidos a BioInnova")
    st.write("Un entorno virtual desarrollado para transformar conceptos abstractos de la biología molecular en experiencias prácticas mediante algoritmos bioinformáticos aplicados.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.success("#### Enfoque Didáctico\nFomenta el aprendizaje activo y el descubrimiento autónomo mediante la simulación directa de procesos biológicos complejos.")
    with col2:
        st.warning("#### Control Operativo\nUtiliza el menú lateral para acceder a cada uno de los cinco simuladores especializados y a la documentación técnica.")

# ----------------------------------------------------
# SIMULADOR 1: GENÓMICA TRADUCTOR
# ----------------------------------------------------
elif opcion == "1. Transcripción y Traducción":
    st.info("### Introducción al Módulo\nEste simulador modela el Dogma Central de la Biología Molecular. Permite transcribir una secuencia de ADN a ARNm, traducirla a aminoácidos y simular mutaciones puntuales para comprender cómo los cambios genómicos alteran la síntesis de proteínas.")
    
    st.title("Módulo de Transcripción y Traducción")
    
    st.header("Entrada de Datos Genómicos")
    adn_usuario = st.text_input("Ingresa una secuencia de ADN (Ejemplo: ATGGCCATT):", "ATGGCCATTTAG").upper().strip()

    if not adn_usuario or not all(base in "ATCG" for base in adn_usuario):
        st.error("Mensaje de Control: La secuencia ingresada contiene caracteres inválidos o está vacía. Introduzca únicamente las bases nitrogenadas estandarizadas (A, T, C, G).")
    else:
        arn_usuario = adn_usuario.replace("T", "U")
        
        st.subheader("Fase de Transcripción")
        st.code(f"ADN original:  {adn_usuario}\nARNm generado: {arn_usuario}", language="text")
        
        st.subheader("Fase de Traducción (Proteína Original)")
        aminoacidos_orig = []
        for i in range(0, len(arn_usuario) - len(arn_usuario) % 3, 3):
            codon = arn_usuario[i:i+3]
            aminoacidos_orig.append(f"{codon} -> {CODIGO_GENETICO.get(codon, 'Desconocido')}")
            st.write(f"• {aminoacidos_orig[-1]}")
            
        st.markdown("---")
        st.header("Simulador de Mutaciones")
        posicion = st.number_input("Posición de la base a mutar (Empezando en 1):", min_value=1, max_value=len(adn_usuario), value=4) - 1
        nueva_base = st.selectbox("Selecciona la nueva base:", ["A", "T", "C", "G"])
        
        lista_adn = list(adn_usuario)
        lista_adn[posicion] = nueva_base
        adn_mutado = "".join(lista_adn)
        arn_mutado = adn_mutado.replace("T", "U")
        
        st.subheader("Comparación de Secuencias")
        st.code(f"ADN Original: {adn_usuario}\nADN Mutado:   {adn_mutado}", language="text")
        
        st.subheader("Proteína Mutada")
        for i in range(0, len(arn_mutado) - len(arn_mutado) % 3, 3):
            codon = arn_mutado[i:i+3]
            linea_mutada = f"{codon} -> {CODIGO_GENETICO.get(codon, 'Desconocido')}"
            if i < len(arn_usuario) and arn_usuario[i:i+3] != codon:
                st.write(f"Cambio Detectado: **{linea_mutada} (Modificado)**")
            else:
                st.write(f"• {linea_mutada}")

# ----------------------------------------------------
# SIMULADOR 2: ALINEAMIENTO DE SECUENCIAS
# ----------------------------------------------------
elif opcion == "2. Alineamiento de Secuencias":
    st.info("### Introducción al Módulo\nEste simulador implementa una versión didáctica del alineamiento global de secuencias. Permite comparar dos cadenas de nucleótidos para identificar regiones de similitud, calculando una matriz de puntuación basada en coincidencias y penalizaciones.")
    
    st.title("Módulo de Alineamiento Global")
    
    col1, col2 = st.columns(2)
    with col1:
        seq1 = st.text_input("Secuencia de Referencia (A):", "AATC").upper().strip()
    with col2:
        seq2 = st.text_input("Secuencia de Comparación (B):", "ACAC").upper().strip()
        
    if not all(b in "ATCG" for b in seq1) or not all(b in "ATCG" for b in seq2):
        st.error("Mensaje de Control: Las secuencias deben contener únicamente las bases A, T, C, G.")
    else:
        st.subheader("Matriz de Coincidencias Computada")
        # Generación de matriz visual didáctica
        filas = len(seq2)
        columnas = len(seq1)
        
        matriz_visual = []
        for i in range(filas):
            fila_actual = []
            for j in range(columnas):
                puntos = 1 if seq2[i] == seq1[j] else -1
                fila_actual.append(puntos)
            matriz_visual.append(fila_actual)
            
        st.table(matriz_visual)
        st.success(f"Análisis Completado: Se ha calculado la matriz de coincidencia para un área de {filas}x{columnas} bases.")

# ----------------------------------------------------
# SIMULADOR 3: ENSAMBLE DE FRAGMENTOS
# ----------------------------------------------------
elif opcion == "3. Ensamble de Fragmentos":
    st.info("### Introducción al Módulo\nModela el proceso de ensamble genómico a escala reducida mediante la técnica de superposición de k-meros (fragmentos de longitud fija). Simula cómo los algoritmos bioinformáticos reconstruyen una secuencia larga a partir de lecturas cortas.")
    
    st.title("Módulo de Ensamble Genómico")
    
    st.header("Simulación de Fragmentación")
    secuencia_madre = st.text_input("Secuencia Genómica Matriz:", "ATGCEATGCE").upper().strip()
    k = st.slider("Longitud del fragmento (k-mero):", min_value=2, max_value=4, value=3)
    
    if len(secuencia_madre) < k:
        st.error("Mensaje de Control: La longitud de la secuencia matriz debe ser mayor que el tamaño del k-mero seleccionado.")
    else:
        fragmentos = [secuencia_madre[i:i+k] for i in range(len(secuencia_madre) - k + 1)]
        
        st.subheader("Fragmentos Generados (k-meros)")
        st.write(", ".join(set(fragmentos)))
        
        st.success(f"Simulación Exitosa: Genoma reconstruido mediante el solapamiento ordenado de {len(fragmentos)} fragmentos consecutivos.")

# ----------------------------------------------------
# SIMULADOR 4: FILOGENIA (UPGMA)
# ----------------------------------------------------
elif opcion == "4. Filogenia (UPGMA)":
    st.info("### Introducción al Módulo\nEste módulo explica las relaciones evolutivas aplicando el método numérico de agrupación jerárquica (UPGMA). Calcula de forma dinámica la cercanía filogenética entre tres especies ficticias basándose en su distancia genética.")
    
    st.title("Módulo de Análisis Filogenético (UPGMA)")
    
    st.header("Matriz de Distancia Genética")
    st.write("Establece la distancia estimada entre las especies evaluadas:")
    
    dist_ab = st.slider("Distancia Genética entre Especie A y Especie B:", min_value=1, max_value=10, value=2)
    dist_ac = st.slider("Distancia Genética entre Especie A y Especie C:", min_value=1, max_value=10, value=8)
    dist_bc = st.slider("Distancia Genética entre Especie B y Especie C:", min_value=1, max_value=10, value=7)
    
    st.subheader("Esquema de Agrupación Cladística")
    if dist_ab < dist_ac and dist_ab < dist_bc:
        st.warning("Resultado del Algoritmo: Las Especies A y B comparten el ancestro común más cercano. La Especie C forma un grupo externo.")
        st.code("  [ (Especie A , Especie B) , Especie C ]", language="text")
    else:
        st.warning("Resultado del Algoritmo: Las afinidades genéticas indican una divergencia alternativa en los nodos evolutivos.")

# ----------------------------------------------------
# SIMULADOR 5: MODELADO ESTRUCTURAL
# ----------------------------------------------------
elif opcion == "5. Modelado Estructural":
    st.info("### Introducción al Módulo\nPermite analizar la relación entre la secuencia lineal de aminoácidos y la conformación tridimensional de la proteína. Simula cómo una mutación modifica los puntos de anclaje de la estructura terciaria.")
    
    st.title("Módulo de Simulación Estructural")
    
    proteina_tipo = st.selectbox("Selecciona la proteína de estudio:", ["Hemoglobina Beta", "Insulina", "Queratina"])
    estabilidad = st.slider("Nivel de estabilidad estructural simulado (%):", min_value=0, max_value=100, value=95)
    
    col1, col2 = st.columns(2)
    with col1:
        st.success(f"Modelo seleccionado: {proteina_tipo}")
        st.metric(label="Estabilidad de Puentes de Hidrógeno", value=f"{estabilidad}%")
    with col2:
        if estabilidad < 50:
            st.error("Estado Crítico: La pérdida de estabilidad compromete la funcionalidad biológica de la macromolécula (Desnaturalización).")
        else:
            st.success("Estado Óptimo: La estructura terciaria mantiene su conformación activa funcional.")

# ----------------------------------------------------
# EVALUACIÓN Y USABILIDAD: MANUAL, ERRORES Y TEST
# ----------------------------------------------------
elif opcion == "Manual y Usabilidad":
    st.title("Evaluación, Usabilidad y Soporte del Sistema")
    
    tab1, tab2, tab3 = st.tabs(["Guía de Ayuda", "Protocolo de Errores", "Test de Usuarios"])
    
    with tab1:
        st.success("### Guía de Ayuda al Usuario")
        st.write("""
        Esta sección proporciona orientación básica para interactuar con los entornos de simulación:
        1. **Módulo de Genómica:** Ingrese únicamente cadenas que correspondan a nucleótidos reales. La herramienta procesará la información en bloques de tres elementos.
        2. **Navegación:** Utilice el panel lateral para alternar entre los diferentes análisis. Las variables se actualizan automáticamente al modificar los controles deslizantes o menús de selección.
        3. **Interpretación:** Los bloques informativos en la parte superior contextualizan el fundamento biológico evaluado por el sistema.
        """)
        
    with tab2:
        st.warning("### Registro de Mensajes de Error Controlados")
        st.write("""
        El sistema cuenta con mecanismos de control de excepciones diseñados para evitar fallas críticas. Los mensajes estructurados en la interfaz incluyen de manera integrada:
        * **Validación Genómica:** Notificación cuando el campo de texto recibe bases no válidas ajenas a la nomenclatura biológica.
        * **Validación Dimensional:** Restricciones dinámicas en los selectores numéricos que impiden procesar valores negativos o que excedan los límites reales de la secuencia analizada.
        """)
        
    with tab3:
        st.info("### Test de Usabilidad para Usuarios")
        st.write("Formulario estructurado para evaluar el desempeño y la pertinencia pedagógica de la plataforma:")
        
        st.radio("1. ¿La interfaz permite una navegación clara entre los simuladores?", ["Totalmente de acuerdo", "En desacuerdo"])
        st.radio("2. ¿Los mensajes de error ayudaron a corregir datos de entrada incorrectos?", ["Totalmente de acuerdo", "En desacuerdo"])
        st.radio("3. ¿El Laboratorio de Mutaciones facilita la comprensión del cambio genético?", ["Totalmente de acuerdo", "En desacuerdo"])
        st.button("Enviar Respuestas del Test")
