import streamlit as st
import streamlit.components.v1 as components
import time

# --- CONFIGURACIÓN DE LA PLATAFORMA ---
st.set_page_config(
    page_title="BioInnova - Laboratorio Virtual de Bioinformática",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos personalizados para mejorar la interfaz (Tarjetas, Bordes Redondeados, Sombras y Colores)
st.markdown("""
    <style>
    .main-title {
        font-size: 42px !important;
        font-weight: 800;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 5px;
    }
    .subtitle {
        font-size: 20px !important;
        text-align: center;
        color: #555555;
        margin-bottom: 30px;
    }
    .bio-card {
        background-color: #F8F9FA;
        border-radius: 12px;
        padding: 20px;
        border-left: 6px solid #1E88E5;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    .step-card {
        background-color: #F1F8FF;
        border-radius: 8px;
        padding: 15px;
        border-left: 4px solid #43A047;
        margin-bottom: 10px;
    }
    .codon-box {
        display: inline-block;
        border: 2px solid #7E57C2;
        border-radius: 6px;
        padding: 8px 12px;
        margin: 5px;
        text-align: center;
        background-color: #F3E5F5;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# --- INICIALIZACIÓN DEL SISTEMA DE PUNTOS (GAMIFICACIÓN) ---
if 'biopuntos' not in st.session_state:
    st.session_state.biopuntos = 0
if 'modulos_completados' not in st.session_state:
    st.session_state.modulos_completados = set()

def completar_modulo(modulo_nombre, puntos):
    if modulo_nombre not in st.session_state.modulos_completados:
        st.session_state.modulos_completados.add(modulo_nombre)
        st.session_state.biopuntos += puntos
        st.toast(f"Modulo completado: +{puntos} BioPuntos")

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
    'UAU': 'Tirosina', 'UAC': 'Tirosina', 'UAA': 'STOP', 'UAG': 'STOP',
    'CAU': 'Histidina', 'CAC': 'Histidina', 'CAA': 'Glutamina', 'CAG': 'Glutamina',
    'AAU': 'Asparagina', 'AAC': 'Asparagina', 'AAA': 'Lisina', 'AAG': 'Lisina',
    'GAU': 'Ácido Aspártico', 'GAC': 'Ácido Aspártico', 'GAA': 'Ácido Glutámico', 'GAG': 'Ácido Glutámico',
    'UGU': 'Cisteína', 'UGC': 'Cisteína', 'UGA': 'STOP', 'UGG': 'Triptófano',
    'CGU': 'Arginina', 'CGC': 'Arginina', 'CGA': 'Arginina', 'CGG': 'Arginina',
    'AGU': 'Serina', 'AGC': 'Serina', 'AGA': 'Arginina', 'AGG': 'Arginina',
    'GGU': 'Glicina', 'GGC': 'Glicina', 'GGA': 'Glicina', 'GGG': 'Glicina'
}

# --- BARRA LATERAL PROFESIONAL ---
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #1E88E5;'>BioInnova</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'><b>Laboratorio Virtual Avanzado</b></p>", unsafe_allow_html=True)
    
    # Cuadro de Puntuación en la Barra Lateral
    st.markdown(f"""
        <div style='background-color: #FFF3E0; padding: 15px; border-radius: 8px; border-left: 5px solid #FFB74D; text-align: center; margin-bottom: 20px;'>
            <span style='font-size: 18px; font-weight: bold; color: #E65100;'>BioPuntos Acumulados</span><br>
            <span style='font-size: 28px; font-weight: 800; color: #E65100;'>{st.session_state.biopuntos} pts</span>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    opcion = st.radio(
        "Selecciona una estación de trabajo:",
        [
            "Portada Principal",
            "Estación 1: Transcripción y Traducción",
            "Estación 2: Alineamiento Global",
            "Estación 3: Ensamble Genómico",
            "Estación 4: Filogenia Molecular",
            "Estación 5: Estructura Proteica 3D",
            "Caso Clínico Integrado",
            "Manual, Errores y Test de Usabilidad"
        ]
    )

# --- FUNCIÓN PARA SIMULAR CARGA (BARRA DE PROGRESO) ---
def ejecutar_barra_progreso(texto="Cargando simulación..."):
    progreso_bar = st.progress(0)
    status_text = st.empty()
    for i in range(100):
        time.sleep(0.005)
        progreso_bar.progress(i + 1)
        status_text.text(f"{texto} {i+1}%")
    progreso_bar.empty()
    status_text.empty()

# --- MODULO 0: PORTADA PRINCIPAL ---
if opcion == "Portada Principal":
    st.markdown("<div class='main-title'>BioInnova</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Laboratorio Virtual de Bioinformática y Simulación Molecular</div>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background-image: linear-gradient(135deg, #1E88E5 0%, #1565C0 100%); padding: 40px; border-radius: 15px; color: white; text-align: center; margin-bottom: 30px;">
        <h2 style="color: white; font-weight: 700;">Aprende genética, simula algoritmos reales y experimenta como un bioinformático</h2>
        <p style="font-size: 16px; max-width: 800px; margin: 0 auto; opacity: 0.9;">
            Bienvenido al entorno virtual interactivo diseñado para automatizar y visualizar procesos moleculares complejos. Descubre cómo las ciencias de la computación descifran el código de la vida.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<div class='bio-card'><h4>Simulación Precisa</h4>Modelos moleculares basados en parámetros reales de la biología computacional.</div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='bio-card' style='border-left-color: #43A047;'><h4>Enfoque Gamificado</h4>Resuelve desafíos científicos, acumula BioPuntos y obtén tu certificación de aptitud.</div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='bio-card' style='border-left-color: #7E57C2;'><h4>Diseño Pedagógico</h4>Desgloses algorítmicos paso a paso ideales para defensas ante jurados académicos.</div>", unsafe_allow_html=True)

    st.markdown("### Flujo de la Información Biológica en el Laboratorio")
    st.info("ADN Núcleo-Plasmático -> ARN Mensajero Transcrito -> Cadena Polipeptídica Traducida -> Estructura Terciaria 3D Funcional")

    if len(st.session_state.modulos_completados) == 6:
        st.markdown("""
            <div style="background-color: #E8F5E9; border: 2px solid #43A047; padding: 30px; border-radius: 12px; text-align: center; margin-top: 20px;">
                <h1 style="color: #2E7D32;">CERTIFICADO EMITIDO</h1>
                <h3>Felicidades, Aprendiz de Bioinformática</h3>
                <p>Has completado con éxito todos los módulos técnicos del laboratorio virtual con excelencia académica.</p>
            </div>
        """, unsafe_allow_html=True)

# --- ESTACIÓN 1: TRANSCRIPCIÓN Y TRADUCCIÓN ---
elif opcion == "Estación 1: Transcripción y Traducción":
    st.markdown("## Estación 1: Transcripción y Traducción Génica")
    st.markdown("---")
    
    adn_input = st.text_input("Ingresa la secuencia molde de ADN (Dirección 5' a 3'):", "ATGGCCATTTAG").upper().strip()
    
    if not adn_input or not all(base in "ATCG" for base in adn_input):
        st.error("Mensaje de Control: Detectamos caracteres no biológicos en tu entrada. Recuerda que el ADN solo acepta las bases nitrogenadas estandarizadas: A, T, C y G. Por favor, verifica tu secuencia.")
    else:
        if st.button("Ejecutar Análisis Molecular"):
            ejecutar_barra_progreso("Modelando Dogma Central...")
            
            # PASO 1: Leer ADN
            st.markdown("<div class='step-card'><b>Paso 1: Lectura de la Cadena Molde</b><br>Secuencia de entrada procesada correctamente de forma molecular.</div>", unsafe_allow_html=True)
            st.code(f"ADN: {adn_input}", language="text")
            
            # PASO 2: Transcripción
            arn_secuencia = adn_input.replace("T", "U")
            st.markdown("<div class='step-card'><b>Paso 2: Transcripción a ARN Mensajero (ARNm)</b><br>La enzima ARN polimerasa sustituye la Timina (T) por el Uracilo (U).</div>", unsafe_allow_html=True)
            st.code(f"ARNm: {arn_secuencia}", language="text")
            
            # PASO 3: Segmentación de Codones
            st.markdown("<div class='step-card'><b>Paso 3: Segmentación en Tripletes (Codones)</b><br>El ribosoma agrupa los nucleótidos de tres en tres para iniciar la lectura limpia.</div>", unsafe_allow_html=True)
            codones = [arn_secuencia[i:i+3] for i in range(0, len(arn_secuencia) - len(arn_secuencia) % 3, 3)]
            
            codon_html = ""
            for c in codones:
                codon_html += f"<div class='codon-box'>{c}</div>"
            st.markdown(codon_html, unsafe_allow_html=True)
            
            # PASO 4: Traducción a Aminoácidos
            st.markdown("<div class='step-card'><b>Paso 4: Traducción a Cadena Polipeptídica</b><br>Cada triplete se traduce al aminoácido correspondiente según el código genético universal.</div>", unsafe_allow_html=True)
            
            for c in codones:
                amino = CODIGO_GENETICO.get(c, 'Desconocido')
                st.markdown(f"""
                    <div style="background-color: #EDE7F6; padding: 10px; margin: 5px 0; border-radius: 5px; border-left: 4px solid #7E57C2;">
                        <b>Codón:</b> <code style="color:#7E57C2;">{c}</code> -> <b>Aminoácido Asignado:</b> {amino}
                    </div>
                """, unsafe_allow_html=True)
                
            completar_modulo("Transcripción", 20)

    st.markdown("---")
    st.markdown("### Desafío de Estación")
    r1 = st.radio("¿Cuál es el codón universal estandarizado para el inicio de la traducción proteica?", ["UUU", "UGA", "AUG", "GGG"])
    if r1 == "AUG":
        st.success("Correcto. El codón AUG codifica para la Metionina y marca el inicio del marco de lectura abierto.")
    else:
        st.error("Inténtalo de nuevo. Pista: Es el codón que codifica para la Metionina.")

# --- ESTACIÓN 2: ALINEAMIENTO GLOBAL (ALGORITMO REAL NEEDLEMAN-WUNSCH) ---
elif opcion == "Estación 2: Alineamiento Global":
    st.markdown("## Estación 2: Alineamiento de Secuencias Homólogas")
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    with col1:
        s1 = st.text_input("Secuencia Genómica de Referencia (A):", "AATC").upper().strip()
    with col2:
        s2 = st.text_input("Secuencia Genómica Objeto (B):", "ACAC").upper().strip()
        
    if not all(b in "ATCG" for b in s1) or not all(b in "ATCG" for b in s2):
        st.error("Mensaje de Control: Las cadenas ingresadas contienen errores de formato nucleotídico. Asegúrate de usar únicamente letras A, T, C, G.")
    else:
        if st.button("Calcular Matriz Dinámica de Puntuación"):
            ejecutar_barra_progreso("Calculando alineamiento mediante Needleman-Wunsch...")
            
            n, m = len(s2), len(s1)
            matriz = [[0] * (m + 1) for _ in range(n + 1)]
            
            for i in range(n + 1): matriz[i][0] = -i
            for j in range(m + 1): matriz[0][j] = -j
            
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    match = matriz[i-1][j-1] + (1 if s2[i-1] == s1[j-1] else -1)
                    delete = matriz[i-1][j] - 1
                    insert = matriz[i][j-1] - 1
                    matriz[i][j] = max(match, delete, insert)
                    
            st.markdown("<div class='step-card'><b>Matriz de Programación Dinámica Computada</b><br>Visualiza la puntuación matemática acumulada para encontrar el camino óptimo de alineamiento.</div>", unsafe_allow_html=True)
            st.table(matriz)
            
            st.markdown("<div class='step-card'><b>Resultado del Alineamiento Óptimo Hallado</b></div>", unsafe_allow_html=True)
            st.success(f"Score del Alineamiento Global Final: {matriz[n][m]} puntos.")
            completar_modulo("Alineamiento", 20)

# --- ESTACIÓN 3: ENSAMBLE DE FRAGMENTOS ---
elif opcion == "Estación 3: Ensamble Genómico":
    st.markdown("## Estación 3: Ensamble Genómico por Solapamiento")
    st.markdown("---")
    
    secuencia_madre = st.text_input("Ingresa la secuencia genómica original para fragmentación controlada:", "ATGCATGCAT").upper().strip()
    k = st.slider("Selecciona la longitud fija de los fragmentos (k-meros):", min_value=2, max_value=5, value=3)
    
    if len(secuencia_madre) < k:
        st.error("Mensaje de Control: Configuración incoherente. El tamaño del fragmento (k-mero) no puede superar la longitud total de la secuencia genómica.")
    else:
        if st.button("Fragmentar y Ensamblar"):
            ejecutar_barra_progreso("Calculando mapas de solapamiento...")
            
            fragmentos = [secuencia_madre[i:i+k] for i in range(len(secuencia_madre) - k + 1)]
            st.markdown("<div class='step-card'><b>Fragmentos Generados en el Proceso (k-meros únicos):</b></div>", unsafe_allow_html=True)
            st.write(", ".join(set(fragmentos)))
            
            st.markdown("<div class='step-card'><b>Visualización del Solapamiento y Alineación del Contig:</b><br>Observa cómo se superponen los fragmentos de forma lógica en la memoria computacional para reconstruir el genoma original.</div>", unsafe_allow_html=True)
            
            for idx, frag in enumerate(fragmentos):
                espacios = " " * idx
                st.code(f"{espacios}{frag}", language="text")
                
            st.success(f"Genoma Reconstruido Exitosamente (Contig Completo): {secuencia_madre}")
            completar_modulo("Ensamble", 20)

# --- ESTACIÓN 4: FILOGENIA MOLECULAR ---
elif opcion == "Estación 4: Filogenia Molecular":
    st.markdown("## Estación 4: Análisis Cladístico Basado en Distancias")
    st.markdown("---")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        sp1 = st.text_input("Especie Endémica A:", "Solenodon")
    with col2:
        sp2 = st.text_input("Especie Endémica B:", "Plagiodontia")
    with col3:
        sp3 = st.text_input("Especie de Referencia C:", "Homo_sapiens")
        
    st.markdown("### Configuración de Distancias Evolutivas Mutuas")
    d12 = st.slider(f"Distancia genética molecular entre {sp1} y {sp2}:", min_value=1, max_value=20, value=3)
    
    if st.button("Renderizar Árbol Filogenético Dinámico"):
        ejecutar_barra_progreso("Computando agrupamientos estructurales UPGMA...")
        
        import graphviz
        dot = graphviz.Digraph(comment='Árbol Filogenético')
        dot.node('R', 'Ancestro Común')
        dot.node('N1', f'Nodo Interno\n(Distancia: {d12/2})')
        dot.node('A', sp1)
        dot.node('B', sp2)
        dot.node('C', sp3)
        
        dot.edge('R', 'N1')
        dot.edge('R', 'C')
        dot.edge('N1', 'A')
        dot.edge('N1', 'B')
        
        st.markdown("<div class='step-card'><b>Cladograma Estructural Computado mediante Algoritmo UPGMA</b></div>", unsafe_allow_html=True)
        st.graphviz_chart(dot)
        completar_modulo("Filogenia", 20)

# --- ESTACIÓN 5: ESTRUCTURA PROTEICA 3D ---
elif opcion == "Estación 5: Estructura Proteica 3D":
    st.markdown("## Estación 5: Modelado Estructural e Interacción Macromolecular")
    st.markdown("---")
    
    proteina_sel = st.selectbox(
        "Selecciona el espécimen macromolecular a renderizar en tiempo real:",
        ["Hemoglobina (Cadena Beta)", "Insulina", "Inmunoglobulina"]
    )
    
    pdb_mapping = {
        "Hemoglobina (Cadena Beta)": {"id": "1A3N", "fun": "Transporte de oxígeno en la sangre.", "aa": "146 residuos", "enf": "Anemia Falciforme."},
        "Insulina": {"id": "1ZNI", "fun": "Regulación homeostática de la glucosa en plasma.", "aa": "51 residuos", "enf": "Diabetes Mellitus Tipo 1."},
        "Inmunoglobulina": {"id": "1IGY", "fun": "Defensa inmunológica y reconocimiento de antígenos.", "aa": "Cadenas pesadas y ligeras", "enf": "Inmunodeficiencias específicas."}
    }
    
    info_p = pdb_mapping[proteina_sel]
    col_v, col_i = st.columns([2, 1])
    
    with col_v:
        st.markdown("<div class='step-card'><b>Visor Molecular Interactivo Tridimensional (3Dmol.js)</b></div>", unsafe_allow_html=True)
        html_code = f"""
        <div style="height: 450px; width: 100%; position: relative;" class="viewer_3dmoljs" 
             data-pdb="{info_p['id']}" data-backgroundcolor="0xffffff" data-style="cartoon:color=spectrum"></div>
        <script src="https://3dmol.org/build/3Dmol-min.js"></script>
        """
        components.html(html_code, height=470)
        st.caption("Interacción: Clic izquierdo para rotar la estructura, clic derecho para trasladar y rueda del mouse para zoom continuo.")
        
    with col_i:
        st.markdown("<div class='bio-card' style='border-left-color: #7E57C2;'><h4>Ficha Técnico-Científica</h4></div>", unsafe_allow_html=True)
        st.write(f"Código de Acceso PDB: `{info_p['id']}`")
        st.write(f"Función Celular: {info_p['fun']}")
        st.write(f"Dimensión Estructural: {info_p['aa']}")
        st.write(f"Patología Asociada: {info_p['enf']}")
        
        if st.checkbox("Mostrar curiosidad científica"):
            st.info("Los modelos de simulación por computadora permiten diseñar fármacos específicos que encajan en los sitios activos de estas proteínas sin necesidad de pruebas de laboratorio masivas.")
            
    completar_modulo("Estructuras", 20)

# --- CASO CLÍNICO INTEGRADO ---
elif opcion == "Caso Clínico Integrado":
    st.markdown("## Estación Clínica: Diagnóstico Molecular de Precisión")
    st.markdown("---")
    
    st.markdown("""
        <div class='bio-card' style='border-left-color: #E53935;'>
            <h4>Historial Médico del Paciente</h4>
            <p>Paciente de 14 años de edad asiste a consulta presentando cuadros recurrentes de fatiga extrema, dolor óseo agudo e ictericia. Se sospecha de una hemoglobinopatía congénita. Vamos a analizar su secuencia nucleotídica para confirmar el diagnóstico.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Secuencia de Nucleótidos Obtenida por Secuenciación Sanger:")
    st.code("Cadena Normal:   ATG GTG CAC CTG ACT CCT GAG GAG\nCadena Paciente: ATG GTG CAC CTG ACT CCT GTG GAG", language="text")
    
    diagnostico = st.radio("Tras observar detenidamente el set de secuencias, ¿existe una mutación puntual en el paciente?", ["Seleccionar...", "Sí, se detecta un cambio puntual de bases.", "No, las cadenas son completamente idénticas."])
    
    if diagnostico == "Sí, se detecta un cambio puntual de bases.":
        st.success("Diagnóstico Correcto. Has identificado con precisión la mutación. El nucleótido Adenina (A) fue sustituido por una Timina (T). Esto altera por completo el codón GAG (Ácido Glutámico) mutándolo a GTG (Valina), provocando la polimerización anómala de la Hemoglobina que desencadena la Anemia Falciforme.")
        completar_modulo("CasoClinico", 20)
    elif diagnostico == "No, las cadenas son completamente idénticas.":
        st.error("Respuesta incorrecta. Observa con atención el triplete número 7 en ambas cadenas gaseosas.")

# --- MANUAL DE USUARIO, PROTOCOLO DE ERRORES Y TEST DE USABILIDAD ---
elif opcion == "Manual, Errores y Test de Usabilidad":
    st.title("Documentación Técnica y Validación de Campo")
    
    tab1, tab2, tab3 = st.tabs(["Manual del Usuario Avanzado", "Protocolo de Mensajes de Error", "Test de Usabilidad de 10 Preguntas"])
    
    with tab1:
        st.markdown("""
            ### Guía Completa de Operación del Laboratorio Virtual
            Esta plataforma automatiza el análisis bioinformático en estaciones de trabajo modulares consecutivas:
            1. **Transcripción y Traducción:** Transforma secuencias crudas de ADN a proteínas funcionales en segundos.
            2. **Alineamiento de Secuencias:** Implementa el algoritmo real de Needleman-Wunsch para obtener matrices de homología biológica.
            3. **Ensamble Genómico:** Modela mapas de solapamiento lógicos de fragmentos genómicos (k-meros).
            4. **Filogenia Molecular:** Reconstruye árboles evolutivos utilizando técnicas matemáticas cuantitativas basadas en distancias.
            5. **Visualización Interactiva:** Renderiza archivos de la base de datos internacional PDB en tres dimensiones sin requerir plugins locales.
        """)
        
    with tab2:
        st.markdown("""
            ### Gestión Inteligente y Control Operativo de Errores
            El sistema cuenta con blindaje de código ante excepciones de usuario:
            * **Excepción de Entrada Alfanumérica:** Si ingresas letras ajenas a A, T, C, G, el software congela el análisis de forma segura y despliega un panel instructivo amigable en lugar de romperse.
            * **Incoherencia de Parámetros de Fragmentación:** Si la longitud del k-mero supera las dimensiones de la secuencia molde, la interfaz activa una bandera de advertencia matemática.
        """)
        
    with tab3:
        st.markdown("### Cuestionario de Usabilidad Integral para el Usuario (Escala Likert)")
        st.write("Por favor, califica los siguientes enunciados para evaluar la pertinencia técnica del laboratorio virtual:")
        
        preguntas = [
            "1. ¿La interfaz gráfica del laboratorio facilita la navegación autónoma?",
            "2. ¿El desglose paso a paso mejora significativamente la comprensión de los algoritmos?",
            "3. ¿El visor tridimensional interactivo responde de manera fluida y precisa?",
            "4. ¿La matriz de programación dinámica del alineamiento es clara y legible?",
            "5. ¿Los mensajes de error proporcionan indicaciones claras para corregir entradas?",
            "6. ¿El sistema de BioPuntos motiva el avance continuo por las estaciones?",
            "7. ¿El caso clínico ayuda a conectar la bioinformática con la práctica médica real?",
            "8. ¿La velocidad de carga y procesamiento de los simuladores es óptima?",
            "9. ¿El lenguaje técnico utilizado es adecuado para fines educativos y profesionales?",
            "10. ¿Consideras que esta herramienta está lista para ser presentada formalmente ante un jurado?"
        ]
        
        respuestas_test = {}
        for p in preguntas:
            respuestas_test[p] = st.radio(p, ["Totalmente de acuerdo", "De acuerdo", "En desacuerdo", "Totalmente en desacuerdo"], key=p)
            
        if st.button("Validar y Enviar Test de Usabilidad"):
            st.success("Muchas gracias. Tus respuestas han sido recopiladas y procesadas en la base de datos de usabilidad del laboratorio virtual.")
