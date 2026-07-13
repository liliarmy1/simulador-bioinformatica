import streamlit as st
import streamlit.components.v1 as components
import time

# --- CONFIGURACIÓN DE LA PLATAFORMA ---
st.set_page_config(
    page_title="BioInnova - Laboratorio Virtual de Bioinformática",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos personalizados avanzados (Tarjetas, Bordes Redondeados, Sombras y Colores)
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
        margin-bottom: 15px;
    }
    .align-seq-box {
        font-family: 'Courier New', Courier, monospace;
        font-size: 22px;
        font-weight: bold;
        letter-spacing: 6px;
        background-color: #263238;
        color: #00E676;
        padding: 12px;
        border-radius: 6px;
        text-align: center;
        box-shadow: inset 0 2px 4px rgba(0,0,0,0.3);
        margin: 5px 0;
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

# --- INICIALIZACIÓN DEL SISTEMA DE PUNTOS ---
if 'biopuntos' not in st.session_state:
    st.session_state.biopuntos = 0
if 'modulos_completados' not in st.session_state:
    st.session_state.modulos_completados = set()

def completar_modulo(modulo_nombre, puntos):
    if modulo_nombre not in st.session_state.modulos_completados:
        st.session_state.modulos_completados.add(modulo_nombre)
        st.session_state.biopuntos += puntos
        st.toast(f"Módulo completado: +{puntos} BioPuntos")

# Diccionario del código genético universal
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

# --- BARRA LATERAL ---
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #1E88E5; margin-bottom: 2px;'>Laboratorio Virtual</h1>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    
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
            "Manual, Errores y Evaluación Técnica"
        ]
    )

def ejecutar_barra_progreso(texto="Cargando simulación..."):
    progreso_bar = st.progress(0)
    status_text = st.empty()
    for i in range(100):
        time.sleep(0.005)
        progreso_bar.progress(i + 1)
        status_text.text(f"{texto} {i+1}%")
    progreso_bar.empty()
    status_text.empty()

# --- MÓDULO 0: PORTADA PRINCIPAL ---
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
            
            st.markdown("<div class='step-card'><b>Paso 1: Lectura de la Cadena Molde</b><br>Secuencia de entrada procesada correctamente de forma molecular.</div>", unsafe_allow_html=True)
            st.code(f"ADN: {adn_input}", language="text")
            
            arn_secuencia = adn_input.replace("T", "U")
            st.markdown("<div class='step-card'><b>Paso 2: Transcripción a ARN Mensajero (ARNm)</b><br>La enzima ARN polimerasa sustituye la Timina (T) por el Uracilo (U).</div>", unsafe_allow_html=True)
            st.code(f"ARNm: {arn_secuencia}", language="text")
            
            st.markdown("<div class='step-card'><b>Paso 3: Segmentación en Tripletes (Codones)</b><br>El ribosoma agrupa los nucleótidos de tres en tres para iniciar la lectura limpia.</div>", unsafe_allow_html=True)
            codones = [arn_secuencia[i:i+3] for i in range(0, len(arn_secuencia) - len(arn_secuencia) % 3, 3)]
            
            codon_html = ""
            for c in codones:
                codon_html += f"<div class='codon-box'>{c}</div>"
            st.markdown(codon_html, unsafe_allow_html=True)
            
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
    r1 = st.radio("¿Cuál es el codón universal estandarizado para el inicio de la traducción proteica?", ["UUU", "UGA", "AUG", "GGG"], index=None)
    if r1 == "AUG":
        st.success("Correcto. El codón AUG codifica para la Metionina y marca el inicio del marco de lectura abierto.")
    elif r1 is not None:
        st.error("Inténtalo de nuevo. Pista: Es el codón que codifica para la Metionina.")

# --- ESTACIÓN 2: ALINEAMIENTO GLOBAL ---
elif opcion == "Estación 2: Alineamiento Global":
    st.markdown("## Estación 2: Alineamiento de Secuencias Homólogas")
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    with col1:
        s1 = st.text_input("Secuencia Genómica de Referencia (Secuencia 1):", "ATGCA").upper().strip()
    with col2:
        s2 = st.text_input("Secuencia Genómica Objeto (Secuencia 2):", "ATCCA").upper().strip()
        
    st.markdown("### Parámetros de Puntuación (Algoritmo Needleman-Wunsch)")
    c1, c2, c3 = st.columns(3)
    with c1: match_val = st.number_input("Coincidencia (Match)", value=1.0)
    with c2: mismatch_val = st.number_input("Diferencia (Mismatch)", value=-1.0)
    with c3: gap_val = st.number_input("Gap", value=-2.0)
        
    if not all(b in "ATCG" for b in s1) or not all(b in "ATCG" for b in s2):
        st.error("Mensaje de Control: Las cadenas ingresadas contienen errores de formato nucleotídico. Asegúrate de usar únicamente letras A, T, C, G.")
    else:
        if st.button("Simular Alineamiento Óptimo"):
            ejecutar_barra_progreso("Calculando matriz dinámica y alineación óptima...")
            
            n, m = len(s2), len(s1)
            matriz = [[0] * (m + 1) for _ in range(n + 1)]
            for i in range(n + 1): matriz[i][0] = int(i * gap_val)
            for j in range(m + 1): matriz[0][j] = int(j * gap_val)
            
            for i in range(1, n + 1):
                for j in range(1, m + 1):
                    match = matriz[i-1][j-1] + (match_val if s2[i-1] == s1[j-1] else mismatch_val)
                    delete = matriz[i-1][j] + gap_val
                    insert = matriz[i][j-1] + gap_val
                    matriz[i][j] = int(max(match, delete, insert))
                    
            st.markdown("### Matriz de Puntuación Acumulada")
            st.table(matriz)
            
            st.markdown("### Resultado del Alineamiento Computado")
            
            st.markdown(f"""
            <div style="background-color: #F8F9FA; border-radius: 10px; padding: 20px; border: 1px solid #E0E0E0;">
                <p style="margin-bottom: 5px; font-weight: bold; color: #555;">Secuencia 1 (Referencia):</p>
                <div class='align-seq-box'>{s1}</div>
                <p style="margin-top: 15px; margin-bottom: 5px; font-weight: bold; color: #555;">Secuencia 2 (Objeto):</p>
                <div class='align-seq-box' style='color: #29B6F6;'>{s2}</div>
            </div>
            """, unsafe_allow_html=True)
            
            coincidencias = sum(1 for a, b in zip(s1, s2) if a == b)
            pct_identidad = (coincidencias / max(len(s1), len(s2))) * 100
            
            st.markdown("<br>", unsafe_allow_html=True)
            
            col_m1, col_m2 = st.columns(2)
            with col_m1:
                st.markdown(f"""
                <div style="background-color: #E8F5E9; border-left: 6px solid #43A047; padding: 15px; border-radius: 6px;">
                    <span style="font-size: 14px; color: #2E7D32; font-weight: bold;">PUNTUACIÓN FINAL DEL ALINEAMIENTO</span><br>
                    <span style="font-size: 24px; font-weight: 800; color: #1B5E20;">{matriz[n][m]} puntos</span>
                </div>
                """, unsafe_allow_html=True)
            with col_m2:
                st.markdown(f"""
                <div style="background-color: #E3F2FD; border-left: 6px solid #2196F3; padding: 15px; border-radius: 6px;">
                    <span style="font-size: 14px; color: #1565C0; font-weight: bold;">PORCENTAJE DE IDENTIDAD APROXIMADO</span><br>
                    <span style="font-size: 24px; font-weight: 800; color: #0D47A1;">{pct_identidad:.1f}% de Homología</span>
                </div>
                """, unsafe_allow_html=True)
                
            completar_modulo("Alineamiento", 20)

# --- ESTACIÓN 3: ENSAMBLE GENÓMICO ---
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

# --- ESTACIÓN 4: FILOGENIA MOLECULAR DINÁMICA ---
elif opcion == "Estación 4: Filogenia Molecular":
    st.markdown("## Estación 4: Análisis Cladístico Basado en Distancias de Fauna Dominicana")
    st.markdown("---")
    
    lista_especies = [
        "Solenodonte de la Hispaniola", 
        "Jutía de la Hispaniola", 
        "Gavilán de la Hispaniola", 
        "Iguana de Ricord", 
        "Cigua Palmera"
    ]
    
    col1, col2, col3 = st.columns(3)
    with col1: 
        sp1 = st.selectbox("Especie Dominicana A:", lista_especies, index=0)
    with col2: 
        sp2 = st.selectbox("Especie Dominicana B:", lista_especies, index=1)
    with col3: 
        # Ajuste: Especies estrictamente endémicas/nativas de nuestra isla
        sp3 = st.selectbox("Especie de Referencia C:", ["Cotorra de la Española", "Cigua Palmera"], index=0)
        
    st.markdown("### Parámetro de Distancia Evolutiva")
    d12 = st.slider(f"Distancia genética estimada entre {sp1} y {sp2}:", min_value=1, max_value=20, value=8)
    
    if st.button("Renderizar Árbol Filogenético Dinámico"):
        ejecutar_barra_progreso("Computando agrupamientos estructurales UPGMA...")
        st.markdown("<div class='step-card'><b>Cladograma Interactivo y Reactivo en Tiempo Real</b></div>", unsafe_allow_html=True)
        
        canvas_html = f"""
        <div style="text-align: center; background-color: #FAFAFA; padding: 15px; border-radius: 10px; border: 1px solid #E0E0E0;">
            <canvas id="treeCanvas" width="750" height="350" style="background-color: #FFFFFF; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,0,0,0.05);"></canvas>
        </div>
        <script>
            const canvas = document.getElementById('treeCanvas');
            const ctx = canvas.getContext('2d');
            const dist = {d12};

            let v_len = 40 + (dist * 8);

            ctx.lineWidth = 3;
            ctx.font = "bold 13px Arial";

            // Raíz del Clado
            ctx.strokeStyle = "#455A64";
            ctx.beginPath();
            ctx.moveTo(40, 175);
            ctx.lineTo(140, 175);
            ctx.stroke();
            
            // Nodo del Ancestro Común
            ctx.fillStyle = "#FF7043";
            ctx.beginPath();
            ctx.arc(140, 175, 6, 0, 2 * Math.PI);
            ctx.fill();
            ctx.fillStyle = "#37474F";
            ctx.fillText("Ancestro Común", 45, 160);

            // Bifurcación Vertical Principal
            ctx.strokeStyle = "#1E88E5";
            ctx.beginPath();
            ctx.moveTo(140, 80);
            ctx.lineTo(140, 270);
            ctx.stroke();

            // Brazo hacia el Sub-Nodo de especies dominicanas
            ctx.beginPath();
            ctx.moveTo(140, 80);
            ctx.lineTo(280, 80);
            ctx.stroke();

            // Sub-Nodo Evolutivo Reactivo
            ctx.fillStyle = "#AB47BC";
            ctx.beginPath();
            ctx.arc(280, 80, 6, 0, 2 * Math.PI);
            ctx.fill();
            ctx.fillStyle = "#7B1FA2";
            ctx.fillText("Nodo Interno (D: " + (dist/2).toFixed(1) + ")", 210, 60);

            // Sub-Bifurcación Vertical para A y B
            ctx.strokeStyle = "#43A047";
            ctx.beginPath();
            ctx.moveTo(280, 40);
            ctx.lineTo(280, 120);
            ctx.stroke();

            // Brazos Dinámicos finales
            ctx.beginPath();
            ctx.moveTo(280, 40);
            ctx.lineTo(280 + v_len, 40);
            ctx.moveTo(280, 120);
            ctx.lineTo(280 + v_len, 120);
            ctx.stroke();

            ctx.fillStyle = "#2E7D32";
            ctx.fillText("{sp1}", 295 + v_len, 45);
            ctx.fillText("{sp2}", 295 + v_len, 125);

            // Brazo de la Especie de Control Externa
            ctx.strokeStyle = "#E53935";
            ctx.beginPath();
            ctx.moveTo(140, 270);
            ctx.lineTo(520, 270);
            ctx.stroke();

            ctx.fillStyle = "#C62828";
            ctx.fillText("{sp3} (Grupo de Control)", 535, 275);
        </script>
        """
        components.html(canvas_html, height=390)
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
        <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
        <script src="https://3dmol.org/build/3Dmol-min.js"></script>
        
        <div id="container-3dmol" style="height: 450px; width: 100%; position: relative; border: 1px solid #ddd; border-radius: 8px;"></div>
        
        <script>
        $(document).ready(function() {{
            let element = $('#container-3dmol');
            let config = {{ backgroundColor: 'white' }};
            let viewer = $3Dmol.createViewer(element, config);
            
            $3Dmol.download("pdb:{info_p['id']}", viewer, {{}}, function() {{
                viewer.setStyle({{}}, {{cartoon: {{color: 'spectrum'}}}});
                viewer.zoomTo();
                viewer.render();
            }});
        }});
        </script>
        """
        components.html(html_code, height=470)
        st.caption("Interacción: Clic izquierdo para rotar la estructura, clic derecho para trasladar y rueda del mouse para zoom continuo.")
        
    with col_i:
        st.markdown("<div class='bio-card' style='border-left-color: #7E57C2;'><h4>Ficha Técnico-Científica</h4></div>", unsafe_allow_html=True)
        st.write(f"Código de Acceso PDB: `{info_p['id']}`")
        st.write(f"Función Celular: {info_p['fun']}")
        st.write(f"Dimensión Estructural: {info_p['aa']}")
        st.write(f"Patología Asociada: {info_p['enf']}")
        
    completar_modulo("Estructures", 20)

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
    
    st.code("Cadena Normal:   ATG GTG CAC CTG ACT CCT GAG GAG\nCadena Paciente: ATG GTG CAC CTG ACT CCT GTG GAG", language="text")
    
    diagnostico = st.radio("Tras observar detenidamente el set de secuencias, ¿existe una mutación puntual en el paciente?", ["Seleccionar...", "Sí, se detecta un cambio puntual de bases.", "No, las cadenas son completamente idénticas."], index=0)
    
    if diagnostico == "Sí, se detecta un cambio puntual de bases.":
        st.success("Diagnóstico Correcto. Has identificado con precisión la mutación. El nucleótido Adenina (A) fue sustituido por una Timina (T). Esto altera por completo el codón GAG (Ácido Glutámico) mutándolo a GTG (Valina), provocando la polimerización anómala de la Hemoglobina que desencadena la Anemia Falciforme.")
        completar_modulo("CasoClinico", 20)

# --- DOCUMENTACIÓN Y EVALUACIÓN ---
elif opcion == "Manual, Errores y Evaluación Técnica":
    st.title("Documentación y Evaluación del Aprendizaje")
    
    tab1, tab2, tab3 = st.tabs(["Manual del Usuario", "Protocolo de Errores", "Evaluación Formativa de Genética"])
    
    with tab1:
        st.markdown("""
            ### Guía Operativa del Laboratorio Virtual
            Esta plataforma automatiza procesos bioinformáticos avanzados a través de simuladores específicos:
            * **Estación 1:** Modelado del Dogma Central (Transcripción/Traducción).
            * **Estación 2:** Alineamientos usando matrices dinámicas de homología de nucleótidos.
            * **Estación 3:** Reconstrucción de genomas fragmentados en k-meros.
            * **Estación 4:** Filogenia matemática basada en matrices de distancias de fauna endémica dominicana.
            * **Estación 5:** Modelado molecular 3D dinámico.
        """)
        
    with tab2:
        st.markdown("""
            ### Sistema Interno de Gestión de Excepciones
            * **Caracteres No Biológicos:** El sistema bloquea de manera inmediata cualquier análisis si la secuencia de ADN de entrada contiene caracteres fuera de las bases estandarizadas (A, T, C, G).
            * **Desajuste de k-meros:** Control lógico para impedir que la variable del deslizador supere la extensión lineal real de la secuencia genómica dada.
        """)
        
    with tab3:
        st.markdown("### Examen de Conocimientos Esenciales: Fundamentos de Genética")
        st.write("Responde las siguientes 10 preguntas básicas para evaluar tus conocimientos académicos:")
        
        # 1. ¿Qué es el ADN?
        p1 = st.radio(
            "1. ¿Qué es el ADN (Ácido Desoxirribonucleico)?",
            [
                "Una proteína globular encargada de la contracción muscular celular.",
                "La macromolécula que almacena y transmite la información genética de los seres vivos.",
                "Un carbohidrato simple utilizado para la obtención de energía inmediata."
            ],
            index=None
        )
        
        # 2. Bases del ADN
        p2 = st.radio(
            "2. ¿Cuáles son las cuatro bases nitrogenadas fundamentales que componen la molécula de ADN?",
            [
                "Adenina, Timina, Citosina y Guanina.",
                "Adenina, Uracilo, Citosina y Guanina.",
                "Alanina, Treonina, Cisteína y Glicina."
            ],
            index=None
        )
        
        # 3. Estructura del ADN
        p3 = st.radio(
            "3. ¿Qué forma o estructura geométrica característica posee la molécula de ADN bicatenario?",
            [
                "Estructura lineal simple monocatenaria.",
                "Forma de doble hélice o escala de caracol helicoidal.",
                "Estructura perfectamente simétrica en forma de anillo cerrado único."
            ],
            index=None
        )
        
        # 4. Localización celular
        p4 = st.radio(
            "4. ¿En qué organelo especializado de las células eucariotas se localiza principalmente el ADN genómico?",
            [
                "En el Aparato de Golgi.",
                "En los Ribosomas libres del citoplasma.",
                "En el Núcleo celular."
            ],
            index=None
        )

        # 5. Sustitución en el ARN
        p5 = st.radio(
            "5. ¿Qué base nitrogenada sustituye a la Timina durante el proceso de transcripción a ARN?",
            [
                "Uracilo.",
                "Guanina.",
                "Adenina."
            ],
            index=None
        )

        # 6. Definición de Gen
        p6 = st.radio(
            "6. ¿Qué es un gen desde el punto de vista molecular?",
            [
                "Un segmento específico de ADN que contiene las instrucciones para sintetizar una proteína o ARN funcional.",
                "Un orgánulo celular responsable de la digestión de macromoléculas defectuosas.",
                "La secuencia completa de aminoácidos unidos en un enlace peptídico circular."
            ],
            index=None
        )

        # 7. Los Cromosomas
        p7 = st.radio(
            "7. ¿Qué son los cromosomas?",
            [
                "Estructuras altamente condensadas formadas por ADN y proteínas que se organizan durante la división celular.",
                "Moléculas lipídicas que delimitan la membrana plasmática.",
                "Vesículas citoplasmáticas que transportan proteínas exógenas."
            ],
            index=None
        )

        # 8. Mutación Genética
        p8 = st.radio(
            "8. ¿A qué se refiere el término 'mutación genética'?",
            [
                "A cualquier cambio o alteración permanente en la secuencia de nucleótidos del ADN.",
                "Al proceso normal de duplicación exacta de las cadenas celulares.",
                "A la destrucción programada de las mitocondrias por falta de oxígeno."
            ],
            index=None
        )

        # 9. Función del ARNm
        p9 = st.radio(
            "9. ¿Cuál es la función principal del ARN mensajero (ARNm) en la célula?",
            [
                "Llevar la información genética copiada del ADN desde el núcleo hacia los ribosomas para la síntesis de proteínas.",
                "Catalizar la degradación de los azúcares en la respiración celular anaeróbica.",
                "Unir físicamente los fosfatos para dar rigidez a la pared celular de los tejidos."
            ],
            index=None
        )

        # 10. Unidad estructural (Nucleótido)
        p10 = st.radio(
            "10. ¿Cuál es la unidad estructural básica (monómero) que compone los ácidos nucleicos como el ADN y el ARN?",
            [
                "El Aminoácido.",
                "El Nucleótido (compuesto por un azúcar, un fosfato y una base nitrogenada).",
                "El Ácido graso saturado."
            ],
            index=None
        )
        
        if st.button("Enviar y Calificar Evaluación"):
            # Comprobación estricta de que las 10 preguntas tengan respuesta
            preguntas = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
            if any(p is None for p in preguntas):
                st.warning("Por favor, responde a todas las preguntas (1 a 10) del examen antes de enviar tu calificación.")
            else:
                nota = 0
                if p1 == "La macromolécula que almacena y transmite la información genética de los seres vivos.": nota += 10
                if p2 == "Adenina, Timina, Citosina y Guanina.": nota += 10
                if p3 == "Forma de doble hélice o escala de caracol helicoidal.": nota += 10
                if p4 == "En el Núcleo celular.": nota += 10
                if p5 == "Uracilo.": nota += 10
                if p6 == "Un segmento específico de ADN que contiene las instrucciones para sintetizar una proteína o ARN funcional.": nota += 10
                if p7 == "Estructuras altamente condensadas formadas por ADN y proteínas que se organizan durante la división celular.": nota += 10
                if p8 == "A cualquier cambio o alteración permanente en la secuencia de nucleótidos del ADN.": nota += 10
                if p9 == "Llevar la información genética copiada del ADN desde el núcleo hacia los ribosomas para la síntesis de proteínas.": nota += 10
                if p10 == "El Nucleótido (compuesto por un azúcar, un fosfato y una base nitrogenada).": nota += 10
                
                st.markdown(f"### Resultado Final de la Evaluación: `{nota} / 100` puntos.")
                if nota == 100:
                    st.success("¡Excelente! Has demostrado un conocimiento perfecto de las bases esenciales de la genética.")
                elif nota >= 70:
                    st.warning("Buen intento. Has aprobado la evaluación, pero se recomienda repasar los conceptos fundamentales.")
                else:
                    st.error("Te sugerimos volver a revisar el material de estudio e intentar la evaluación de nuevo para consolidar tu aprendizaje.")
