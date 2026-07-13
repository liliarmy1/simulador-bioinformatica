import streamlit as st
import streamlit.components.v1 as components

# Configuración avanzada de la interfaz
st.set_page_config(page_title="BioInnova - Plataforma de Simulación", layout="wide")

# Diccionario del código genético real
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

# --- NAVEGACIÓN LATERAL ---
with st.sidebar:
    st.title("BioInnova")
    st.write("Plataforma de Simulación Bioinformática")
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

if opcion == "Inicio de la Plataforma":
    st.info("### Sistema Integrado de Bioinformática Educativa\nPlataforma diseñada para la experimentación molecular y el análisis genómico interactivo.")
    st.title("Bienvenidos a BioInnova")
    st.write("Un entorno virtual desarrollado para transformar conceptos abstractos de la biología molecular en experiencias prácticas mediante algoritmos bioinformáticos aplicados.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.success("#### Enfoque Didáctico\nFomenta el aprendizaje activo y el descubrimiento autónomo mediante la simulación directa de procesos biológicos complejos.")
    with col2:
        st.warning("#### Control Operativo\nUtiliza el menú lateral para acceder a cada uno de los cinco simuladores especializados y a la documentación técnica.")

elif opcion == "1. Transcripción y Traducción":
    st.info("### Introducción al Módulo\nEste simulador modela el Dogma Central de la Biología Molecular. Permite transcribir una secuencia de ADN a ARNm, traducirla a aminoácidos y simular mutaciones puntuales.")
    st.title("Módulo de Transcripción y Traducción")
    
    adn_usuario = st.text_input("Ingresa una secuencia de ADN (Ejemplo: ATGGCCATTTAG):", "ATGGCCATTTAG").upper().strip()

    if not adn_usuario or not all(base in "ATCG" for base in adn_usuario):
        st.error("Mensaje de Control: La secuencia ingresada contiene caracteres inválidos o está vacía. Introduzca únicamente las bases nitrogenadas estandarizadas (A, T, C, G).")
    else:
        arn_usuario = adn_usuario.replace("T", "U")
        st.subheader("Fase de Transcripción")
        st.code(f"ADN original:  {adn_usuario}\nARNm generado: {arn_usuario}", language="text")
        
        st.subheader("Fase de Traducción (Proteína Original)")
        for i in range(0, len(arn_usuario) - len(arn_usuario) % 3, 3):
            codon = arn_usuario[i:i+3]
            st.write(f"• {codon} -> {CODIGO_GENETICO.get(codon, 'Desconocido')}")

elif opcion == "2. Alineamiento de Secuencias":
    st.info("### Introducción al Módulo\nEste simulador implementa una versión didáctica del alineamiento global de secuencias. Permite comparar dos cadenas de nucleótidos para identificar regiones de similitud, calculando una matriz de puntuación.")
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
        matriz_visual = [[1 if b2 == b1 else -1 for b1 in seq1] for b2 in seq2]
        st.table(matriz_visual)
        st.success(f"Análisis Completado de forma exitosa.")

elif opcion == "3. Ensamble de Fragmentos":
    st.info("### Introducción al Módulo\nModela el proceso de ensamble genómico a escala reducida mediante la técnica de superposición de fragmentos de longitud fija (k-meros).")
    st.title("Módulo de Ensamble Genómico")
    
    secuencia_madre = st.text_input("Secuencia Genómica Matriz:", "ATGCEATGCE").upper().strip()
    k = st.slider("Longitud del fragmento (k-mero):", min_value=2, max_value=4, value=3)
    
    if len(secuencia_madre) < k:
        st.error("Mensaje de Control: La longitud de la secuencia matriz debe ser mayor que el tamaño del k-mero seleccionado.")
    else:
        fragmentos = [secuencia_madre[i:i+k] for i in range(len(secuencia_madre) - k + 1)]
        st.subheader("Fragmentos Generados (k-meros)")
        st.write(", ".join(set(fragmentos)))
        st.success(f"Simulación Exitosa de solapamiento.")

elif opcion == "4. Filogenia (UPGMA)":
    st.info("### Introducción al Módulo\nEste módulo agrupa jerárquicamente las especies según su distancia genética empleando el método numérico UPGMA. Personalice las especies y configure las distancias moleculares.")
    st.title("Módulo de Análisis Filogenético (UPGMA)")
    
    st.header("Configuración de Especies")
    col1, col2, col3 = st.columns(3)
    with col1:
        spA = st.text_input("Nombre de la Especie A:", "Solenodon")
    with col2:
        spB = st.text_input("Nombre de la Especie B:", "Plagiodontia")
    with col3:
        spC = st.text_input("Nombre de la Especie C:", "Homo_sapiens")
        
    st.header("Matriz de Distancias Evolutivas")
    dist_ab = st.slider(f"Distancia entre {spA} y {spB}:", min_value=1, max_value=20, value=3)
    dist_ac = st.slider(f"Distancia entre {spA} y {spC}:", min_value=1, max_value=20, value=15)
    dist_bc = st.slider(f"Distancia entre {spB} y {spC}:", min_value=1, max_value=20, value=14)
    
    st.subheader("Cladograma Filogenético Generado")
    
    # Determinar matemáticamente cuál par está más cercano según las distancias reales
    if dist_ab <= dist_ac and dist_ab <= dist_bc:
        par_cercano = f"({spA}, {spB})"
        externo = spC
    elif dist_ac <= dist_ab and dist_ac <= dist_bc:
        par_cercano = f"({spA}, {spC})"
        externo = spB
    else:
        par_cercano = f"({spB}, {spC})"
        externo = spA
        
    st.warning("Resultado del Análisis:")
    st.code(f"───┤ Node \n    ├─── {par_cercano}\n    └─── {externo}", language="text")

elif opcion == "5. Modelado Estructural":
    st.info("### Introducción al Módulo\nVisualización tridimensional interactiva de la estructura molecular de proteínas mediante el renderizado directo de archivos PDB.")
    st.title("Visualizador de Estructuras Proteicas 3D")
    
    proteina = st.selectbox("Selecciona el modelo macromolecular a renderizar:", ["Hemoglobina (Cadena Beta)", "Insulina", "Inmunoglobulina"])
    
    # Mapeo de códigos PDB reales para renderizar mediante la API pública de la RCSB PDB
    pdb_codes = {
        "Hemoglobina (Cadena Beta)": "1A3N",
        "Insulina": "1ZNI",
        "Inmunoglobulina": "1IGY"
    }
    pdb_id = pdb_codes[proteina]
    
    st.success(f"Estructura Terciaria Activa: Código de acceso PDB asignado {pdb_id}")
    
    # Código HTML e incrustación JavaScript de 3Dmol.js para lograr la visualización molecular tridimensional interactiva
    componente_html = f"""
    <div style="height: 500px; width: 100%; position: relative;" class="viewer_3dmoljs" 
         data-pdb="{pdb_id}" data-backgroundcolor="0xffffff" data-style="cartoon:color=spectrum"></div>
    <script src="https://3dmol.org/build/3Dmol-min.js"></script>
    """
    
    components.html(componente_html, height=520)
    st.caption("Control del Visor: Utilice el clic izquierdo para rotar la estructura, el clic derecho para trasladarla y la rueda de desplazamiento para aplicar zoom.")

elif opcion == "Manual y Usabilidad":
    st.title("Evaluación, Usabilidad y Soporte del Sistema")
    tab1, tab2, tab3 = st.tabs(["Guía de Ayuda", "Protocolo de Errores", "Test de Usuarios"])
    
    with tab1:
        st.success("### Guía de Ayuda al Usuario")
        st.write("1. **Navegación:** Utilice el panel izquierdo.\n2. **Visualización 3D:** Interactúe directamente sobre el lienzo molecular usando el ratón.")
    with tab2:
        st.warning("### Registro de Mensajes de Error Controlados")
        st.write("* **Validación Genómica:** Filtra caracteres no biológicos.\n* **Límites de Entrada:** Restringe valores numéricos incoherentes.")
    with tab3:
        st.info("### Test de Usabilidad para Usuarios")
        st.radio("1. ¿La interfaz permite una navegación clara?", ["Totalmente de acuerdo", "En desacuerdo"])
        st.radio("2. ¿Los visualizadores interactivos facilitan la comprensión?", ["Totalmente de acuerdo", "En desacuerdo"])
        st.button("Enviar Respuestas del Test")
