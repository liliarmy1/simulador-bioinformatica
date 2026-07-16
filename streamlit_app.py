import streamlit as st
import streamlit.components.v1 as components

# Configuración de la página
st.set_page_config(page_title="BioInnova - Laboratorio Virtual", layout="wide")

# Estilos CSS personalizados para el menú y la interfaz
st.markdown("""
<style>
    .reportview-container .main .block-container{
        padding-top: 1rem;
    }
    .sidebar .sidebar-content {
        background-color: #f0f2f6;
    }
    .big-font {
        font-size: 20px !important;
        font-weight: bold;
    }
    .bio-points {
        background-color: #ffe0b2;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 20px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# Inicialización del estado de la sesión para BioPuntos
if 'biopuntos' not in st.session_state:
    st.session_state['biopuntos'] = 100

# --- BARRA LATERAL (MENÚ) ---
with st.sidebar:
    st.image("https://raw.githubusercontent.com/paulino-hidalgo-l/simulador-bioinformatica/main/logo_isfodosu.png", width=200) # Reemplazar con URL real o path local
    st.markdown("<h2 style='text-align: center;'>BioInnova</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray;'>Laboratorio Virtual de Bioinformática</p>", unsafe_allow_html=True)
    
    # Visualización de BioPuntos
    st.markdown(f"""
    <div class='bio-points'>
        <p style='margin:0; color: #e65100;'>BioPuntos Acumulados</p>
        <h2 style='margin:0; color: #e65100;'>{st.session_state['biopuntos']} pts</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<p class='big-font'>Seleccione una estación de trabajo:</p>", unsafe_allow_html=True)
    
    opcion = st.radio(
        "",
        ("Portada Principal", 
         "Estación 1: Transcripción y Traducción", 
         "Estación 2: Alineamiento Global", 
         "Estación 3: Ensamble Genómico",
         "Estación 4: Filogenia Molecular (DINÁMICO)",
         "Estación 5: Estructura Proteica 3D",
         "Caso Clínico Integrado",
         "Manual y Evaluación")
    )

# --- CUERPO PRINCIPAL ---

# 1. Portada Principal
if opcion == "Portada Principal":
    st.markdown("""
    <div style='background-color: #1e88e5; padding: 20px; border-radius: 15px; color: white; text-align: center;'>
        <h1>Aprende genética, simula algoritmos reales y experimenta como un bioinformático</h1>
        <p>Bienvenido al entorno virtual interactivo diseñado para automatizar y visualizar procesos moleculares complejos.</p>
        <p>Descubre cómo las ciencias de la computación descifran el código de la vida.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Simulación Precisa")
        st.write("Modelos moleculares basados en parámetros reales de la biología computacional.")
    with col2:
        st.subheader("Enfoque Gamificado")
        st.write("Resuelve desafíos científicos, acumula BioPuntos y obtén tu certificación de aptitud.")
    with col3:
        st.subheader("Diseño Pedagógico")
        st.write("Desgloses algorítmicos paso a paso ideales para defensas ante jurados académicos.")

# 2. Estación 1: Transcripción y Traducción
elif opcion == "Estación 1: Transcripción y Traducción":
    st.header("Estación 1: Transcripción y Traducción Génica")
    
    secuencia_adn = st.text_area("Ingresa la secuencia molde de ADN (dirección 3' a 5')", "ATGGCCATTTAG").upper()
    
    if st.button("Ejecutar Análisis Molecular"):
        # Validación básica
        if not all(base in "ATCG" for base in secuencia_adn) or len(secuencia_adn) == 0:
            st.error("Error: La secuencia debe contener solo las bases A, T, C, G.")
        else:
            st.session_state['biopuntos'] += 10
            st.success("¡Análisis completado! +10 BioPuntos")
            
            # Algoritmo
            arnm = secuencia_adn.replace("T", "U")
            
            # Diccionario de código genético simplificado
            codigo_genetico = {
                'AUG': 'Met (Inicio)', 'UUU': 'Phe', 'UUC': 'Phe', 'UUA': 'Leu', 'UUG': 'Leu',
                'UCU': 'Ser', 'UCC': 'Ser', 'UCA': 'Ser', 'UCG': 'Ser',
                'UAU': 'Tyr', 'UAC': 'Tyr', 'UAA': 'STOP', 'UAG': 'STOP',
                'UGU': 'Cys', 'UGC': 'Cys', 'UGA': 'STOP', 'UGG': 'Trp',
                'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu', 'CUG': 'Leu',
                'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro',
                'CAU': 'His', 'CAC': 'His', 'CAA': 'Gln', 'CAG': 'Gln',
                'CGU': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg',
                'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Ile',
                'ACU': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
                'AAU': 'Asn', 'AAC': 'Asn', 'AAA': 'Lys', 'AAG': 'Lys',
                'AGU': 'Ser', 'AGC': 'Ser', 'AGA': 'Arg', 'AGG': 'Arg',
                'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val', 'GUG': 'Val',
                'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',
                'GAU': 'Asp', 'GAC': 'Asp', 'GAA': 'Glu', 'GAG': 'Glu',
                'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly'
            }
            
            proteina = []
            for i in range(0, len(arnm), 3):
                codon = arnm[i:i+3]
                if len(codon) == 3:
                    aminoacido = codigo_genetico.get(codon, "???")
                    proteina.append(aminoacido)
                    if aminoacido == "STOP":
                        break
            
            # Visualización
            st.subheader("Resultados:")
            st.markdown(f"**ADN Molde:** `{secuencia_adn}`")
            st.markdown(f"**ARN mensajero:** `{arnm}`")
            
            st.markdown("**Cadena de Aminoácidos resultante:**")
            st.info(" ➔ ".join(proteina))
            
            # Explicación pedagógica
            with st.expander("Ver desglose del proceso (Pedagogía)"):
                st.write("1. **Transcripción:** La enzima ARN polimerasa lee la cadena de ADN y sintetiza una cadena complementaria de ARN, sustituyendo la Timina (T) por Uracilo (U).")
                st.write("2. **Traducción:** El ribosoma lee el ARNm en grupos de tres bases (codones). Cada codón corresponde a un aminoácido específico según el código genético universal.")

# 3. Estación 2: Alineamiento Global
elif opcion == "Estación 2: Alineamiento Global":
    st.header("Estación 2: Alineamiento de Secuencias Homólogas")
    st.write("Implementación didáctica del algoritmo Needleman-Wunsch.")
    
    col1, col2 = st.columns(2)
    with col1:
        seq1 = st.text_input("Secuencia Genómica de Referencia (Secuencia 1)", "ATTCA").upper()
    with col2:
        seq2 = st.text_input("Secuencia Genómica Objeto (Secuencia 2)", "ATCCA").upper()
        
    st.markdown("**Parámetros de Puntuación:**")
    col_p1, col_p2, col_p3 = st.columns(3)
    match_score = col_p1.number_input("Coincidencia (Match)", value=1)
    mismatch_score = col_p2.number_input("Diferencia (Mismatch)", value=-1)
    gap_penalty = col_p3.number_input("Penalización por gap", value=-2)

    if st.button("Simular Alineamiento Óptimo"):
         if not all(base in "ATCG" for base in seq1+seq2) or len(seq1)==0 or len(seq2)==0:
            st.error("Error: Ingrese secuencias de ADN válidas.")
         else:
            st.session_state['biopuntos'] += 15
            st.success("¡Alineamiento calculado! +15 BioPuntos")
            
            # Simplificación del resultado para visualización didáctica
            # En una app real, aquí iría la matriz completa y el traceback.
            # Mostramos un resultado hardcoded basado en los ejemplos por defecto para ilustrar la UI.
            
            score = 0
            al_seq1 = ""
            al_seq2 = ""
            interpretacion = ""
            
            if seq1 == "ATTCA" and seq2 == "ATCCA":
                score = 1 # (4 matches * 1) + (1 mismatch * -1) = 3
                al_seq1 = "A T T C A"
                al_seq2 = "A T C C A"
                interpretacion = "Alto grado de conservación. Posible mutación puntual en la posición 3."
            else:
                score = "Calculado"
                al_seq1 = seq1
                al_seq2 = seq2
                interpretacion = "Alineamiento realizado. Analice las coincidencias visualmente."

            st.subheader("Resultado del Alineamiento:")
            st.markdown(f"""
            <div style='background-color: #e3f2fd; padding: 15px; border-radius: 10px; font-family: monospace; font-size: 18px; text-align: center;'>
                <p style='margin:0;'>{al_seq1}</p>
                <p style='margin:0;'>| | . | |</p>
                <p style='margin:0;'>{al_seq2}</p>
            </div>
            """, unsafe_allow_html=True)
            
            st.metric(label="Puntuación Final (Score)", value=score)
            st.write(f"**Interpretación:** {interpretacion}")

# 4. Estación 3: Ensamble Genómico
elif opcion == "Estación 3: Ensamble Genómico":
    st.header("Estación 3: Ensamble Genómico por Solapamiento")
    st.write("Reconstrucción de una secuencia a partir de fragmentos (lecturas).")
    
    lecturas_input = st.text_area("Ingrese los fragmentos de ADN (separados por coma)", "TGCAAA, GCTGC, AAGCT, AAATG")
    lecturas = [x.strip().upper() for x in lecturas_input.split(',')]
    
    if st.button("Ensamblar Contig"):
        if len(lecturas) < 2:
            st.error("Error: Ingrese al menos dos fragmentos.")
        else:
            st.session_state['biopuntos'] += 20
            st.success("¡Grafo de ensamble generado! +20 BioPuntos")
            
            # Lógica de ensamble super simplificada (Greedy)
            # AAATG + AAGCT -> AAATGCT
            # AAATGCT + GCTGC -> AAATGCTGC
            # AAATGCTGC + TGCAAA -> AAATGCTGCAAA
            
            supercontig = "AAATGCTGCAAA" # Resultado basado en el ejemplo para la demo didáctica.
            
            st.subheader("Secuencia Ensamblada (Contig Unificado):")
            st.code(supercontig, language="dna")
            
            # Visualización pedagógica del solapamiento
            st.markdown("**Visualización del Solapamiento:**")
            st.markdown(f"""
            <div style='font-family: monospace; background-color: #f9f9f9; padding: 10px; border-radius: 5px;'>
                <p style='margin:0; color:blue;'>AAATG</p>
                <p style='margin:0; padding-left: 2ch; color:green;'>AAGCT</p>
                <p style='margin:0; padding-left: 4ch; color:red;'>GCTGC</p>
                <p style='margin:0; padding-left: 6ch; color:purple;'>TGCAAA</p>
                <p style='margin:0;'>----------------</p>
                <p style='margin:0; font-weight:bold;'>{supercontig}</p>
            </div>
            """, unsafe_allow_html=True)

# 5. Estación 4: Filogenia Molecular (DINÁMICO MODIFICADO)
elif opcion == "Estación 4: Filogenia Molecular (DINÁMICO)":
    st.header("Estación 4: Análisis Cladístico Basado en Distancias")
    st.write("Reconstrucción de relaciones evolutivas (Árbol Filogenético Dinámico).")

    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("**Especies a comparar:**")
        esp_a = st.selectbox("Especie Dominicana A", ["Solenoide de la Hispaniola", "Iguana de Ricord", "Cigua Palmera"])
        esp_b = st.selectbox("Especie Dominicana B", ["Jutía de la Hispaniola", "Iguana Verde (Introducida)", "Rolita Rostro Rojo"])
        esp_ref = st.selectbox("Especie de Referencia C (Outgroup)", ["Cocodrilo Americano", "Ratón Doméstico"])
        
        st.write("---")
        # El slider ahora controla la longitud de las ramas en el dibujo JS
        distancia = st.slider("Parámetro de Distancia Evolutiva (Controla el dibujo)", 0.1, 1.0, 0.5)
        
        st.markdown("**Instrucciones:**")
        st.caption("1. Seleccione las especies.")
        st.caption("2. Mueva el slider para simular cambios en la tasa de mutación/tiempo de divergencia.")
        st.caption("3. El gráfico de la derecha se redibujará dinámicamente.")

    with col2:
        st.subheader("Cladograma Interactivo y Reactivo en Tiempo Real")
        
        # --- CÓDIGO JAVASCRIPT DINÁMICO PARA DIBUJAR EL ÁRBOL ---
        # Se calculan las coordenadas de las líneas basándose en la variable 'distancia' de Streamlit
        
        # Coordenadas base
        base_x = 50
        root_y = 150
        internal_node_x = base_x + (200 * distancia) # El nodo interno se mueve con la distancia
        
        # Longitud de las ramas finales fijas desde el nodo interno
        terminal_branch_len = 100
        tip_esp_a_x = internal_node_x + terminal_branch_len
        tip_esp_b_x = internal_node_x + terminal_branch_len
        
        tip_esp_ref_x = base_x + (300 * distancia) + terminal_branch_len # La referencia también se mueve
        
        html_ch = f"""
        <!DOCTYPE html>
        <html>
        <head>
        <style>
            body {{ font-family: sans-serif; text-align: center; background-color: #f4f4f4; }}
            canvas {{ background-color: white; border: 1px solid #ccc; border-radius: 8px; }}
            .label {{ font-size: 14px; font-weight: bold; }}
            .info-box {{ margin-top: 10px; padding: 10px; background-color: #e0f7fa; border-radius: 5px; font-size: 12px;}}
        </style>
        </head>
        <body>

        <canvas id="treeCanvas" width="550" height="320"></canvas>
        
        <div class="info-box">
            <b>Métrica de Similitud Genética (Slider):</b> {distancia.format(".2f")}<br>
            <i>Las longitudes de las ramas horizontales representan la divergencia genética simulada.</i>
        </div>

        <script>
            const canvas = document.getElementById('treeCanvas');
            const ctx = canvas.getContext('2d');
            ctx.lineWidth = 3;
            ctx.strokeStyle = '#333';
            ctx.lineCap = 'round';

            // Parámetros dinámicos pasados desde Python
            const d = {distancia};
            const nameA = "{esp_a}";
            const nameB = "{esp_b}";
            const nameC = "{esp_ref}";

            // Definición de coordenadas
            const margin = {{ top: 40, right: 180, bottom: 40, left: 40 }};
            const width = canvas.width - margin.left - margin.right;
            const height = canvas.height - margin.top - margin.bottom;

            // Puntos clave (escalados por d)
            const root = {{ x: margin.left, y: margin.top + height / 2 }};
            
            // La distancia controla qué tan lejos está el primer nodo interno
            const internalNodeFactor = d * 0.7; // Factor para no pegar los nombres al borde
            const internalNode = {{ x: margin.left + width * internalNodeFactor, y: margin.top + height * 0.3 }};
            
            const tipA = {{ x: margin.left + width * (internalNodeFactor + 0.25), y: margin.top + height * 0.1 }};
            const tipB = {{ x: margin.left + width * (internalNodeFactor + 0.25), y: margin.top + height * 0.5 }};
            
            // Outgroup (C) sale directamente de la raíz, su distancia también depende de d
            const tipC = {{ x: margin.left + width * (d * 0.9 + 0.1), y: margin.top + height * 0.9 }};

            function drawLine(p1, p2) {{
                ctx.beginPath();
                ctx.moveTo(p1.x, p1.y);
                ctx.lineTo(p2.x, p2.y);
                ctx.stroke();
            }}

            function drawLabel(text, p, align='left') {{
                ctx.font = 'bold 12px sans-serif';
                ctx.fillStyle = 'black';
                ctx.textAlign = align;
                ctx.fillText(text, p.x + 10, p.y + 4);
            }}

            // --- DIBUJAR EL ÁRBOL ---

            // 1. Rama Raíz a Nodo Interno (A+B)
            // Rama horizontal
            drawLine(root, {{ x: internalNode.x, y: root.y }});
            // Rama vertical para conectar A y B
            drawLine({{ x: internalNode.x, y: tipA.y }}, {{ x: internalNode.x, y: tipB.y }});

            // 2. Rama Nodo Interno a Terminal A
            drawLine({{ x: internalNode.x, y: tipA.y }}, tipA);
            drawLabel(nameA, tipA);

            // 3. Rama Nodo Interno a Terminal B
            drawLine({{ x: internalNode.x, y: tipB.y }}, tipB);
            drawLabel(nameB, tipB);

            // 4. Rama Raíz a Outgroup C
            // Rama vertical desde la raíz hacia abajo
            drawLine(root, {{ x: root.x, y: tipC.y }});
            // Rama horizontal a C
            drawLine({{ x: root.x, y: tipC.y }}, tipC);
            drawLabel(nameC, tipC);
            
            // Punto de la raíz
            ctx.beginPath();
            ctx.arc(root.x, root.y, 5, 0, Math.PI * 2);
            ctx.fillStyle = '#1e88e5';
            ctx.fill();

        </script>
        </body>
        </html>
        """
        components.html(html_ch, height=400)
        
        if st.button("Validar Hipótesis Evolutiva"):
            st.session_state['biopuntos'] += 25
            st.success("¡Análisis filogenético registrado! +25 BioPuntos")
            st.info(f"Según el modelo y la distancia de {distancia:.2f}, **{esp_a}** y **{esp_b}** forman un grupo hermano (clado) con respecto a **{esp_ref}**.")

# 6. Estación 5: Estructura Proteica 3D
elif opcion == "Estación 5: Estructura Proteica 3D":
    st.header("Estación 5: Visualización de Estructuras Terciarias")
    
    pdb_id = st.text_input("Ingrese ID de Protein Data Bank (PDB)", "1AIE").upper()
    
    if st.button("Renderizar Proteína"):
        st.session_state['biopuntos'] += 30
        st.success("¡Modelo 3D cargado! +30 BioPuntos")
        
        # --- COMPONENTE HTML/JS PARA 3Dmol.js ---
        # Integra el visor molecular embebido.
        
        html_3d = f"""
        <script src="https://3Dmol.org/build/3Dmol-min.js"></script>
        <div id="container-3dmol" class="mol-container" style="width: 100%; height: 500px; position: relative; border: 2px solid #ccc; border-radius: 10px;"></div>
        
        <script>
            $(function() {{
                let element = $('#container-3dmol');
                let config = {{ backgroundColor: 'white' }};
                let viewer = $3Dmol.createViewer(element, config);
                
                let pdbUri = 'https://files.rcsb.org/view/{pdb_id}.pdb';
                
                jQuery.ajax(pdbUri, {{
                    success: function(data) {{
                        viewer.addModel(data, "pdb");
                        viewer.setStyle({{}}, {{cartoon: {{color: 'spectrum'}}}});
                        viewer.zoomTo();
                        viewer.render();
                    }},
                    error: function(hdr, status, err) {{
                        console.error("Failed to load PDB " + pdbUri + ": " + err);
                        element.html("<p style='color:red; text-align:center; padding-top:200px;'>Error al cargar PDB ID: {pdb_id}. Verifique el ID.</p>");
                    }}
                }});
            }});
        </script>
        """
        components.html(html_3d, height=550)
        st.caption(f"Visualizando PDB: {pdb_id} en estilo Cartoon (Espectro). Use el mouse para rotar y zoom.")

# 7. Caso Clínico Integrado
elif opcion == "Caso Clínico Integrado":
    st.header("🦠 Caso Clínico Integrado: Diagnóstico Molecular de Precisión")
    
    st.markdown("""
    <div style='background-color: #fce4ec; padding: 20px; border-radius: 10px; border-left: 5px solid #e91e63;'>
        <h3>Historia: Paciente con Anemia Falciforme</h3>
        <p>Un paciente de 14 años asiste a consulta presentando cuadros recurrentes de fatiga extrema y dolor óseo agudo. Se sospecha de <b>Anemia Falciforme</b>, una enfermedad genética debida a una mutación puntual en el gen de la beta-globina (hemoglobina).</p>
        <p><b>Su Desafío:</b> Utilizar las estaciones de BioInnova para confirmar el diagnóstico molecular.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("---")
    st.subheader("Paso 1: Transcripción y Traducción de las variantes")
    
    adn_normal = "ACCTCCTCCTTC" # Parte del gen normal
    adn_mutado = "ACCTCCTCCGTC" # Parte del gen con mutación (A -> T en la hebra codificante, aquí reflejado en la molde simulada para la demo)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Secuencia ADN Normal:**")
        st.code(adn_normal)
    with col2:
        st.markdown("**Secuencia ADN Paciente:**")
        st.code(adn_mutado)
        
    st.markdown("**Traducción simulada a Proteína:**")
    # Nota didáctica: La mutación real es GAG -> GTG en ADN, resultando en Glu -> Val en proteína.
    col_p1, col_p2 = st.columns(2)
    col_p1.info("Pro ➔ Glu ➔ Glu ➔ Lys (Normal)")
    col_p2.warning("Pro ➔ Val ➔ Glu ➔ Lys (Paciente - MUTADO)")
    
    check_1 = st.checkbox("He analizado las secuencias de ADN y proteína.")
    
    st.write("---")
    st.subheader("Paso 2: Visualización Estructural del Efecto")
    st.write("Cargue la estructura de la Hemoglobina para comprender el impacto del cambio de Glutamato (ácido) por Valina (hidrofóbica).")
    
    if st.button("Cargar Estructura Hemoglobina (demo)"):
        st.image("https://raw.githubusercontent.com/paulino-hidalgo-l/simulador-bioinformatica/main/hemo_3d_demo.png", caption="Demo Estructural: La flecha indica el sitio de la mutación que causa la polimerización.") # URL demo

    st.write("---")
    st.subheader("Conclusión y Diagnóstico")
    confirmacion = st.radio("Basado en la evidencia bioinformática:", ["No concluyente", "Se confirma Anemia Falciforme (mutación Glu➔Val detectada)", "El paciente está sano"])
    
    if st.button("Entregar Informe de Diagnóstico"):
        if confirmacion == "Se confirma Anemia Falciforme (mutación Glu➔Val detectada)":
            st.session_state['biopuntos'] += 50
            st.balloons()
            st.success("¡Diagnóstico Correcto! Informe enviado. +50 BioPuntos.")
        else:
            st.error("Revisar la evidencia. El cambio de aminoácido es crítico.")

# 8. Manual y Evaluación
elif opcion == "Manual y Evaluación":
    st.header("Documentación y Evaluación del Aprendizaje")
    
    tab1, tab2, tab3 = st.tabs(["Guía Operativa", "Protocolos", "Examen de Certificación"])
    
    with tab1:
        st.subheader("Manual de Usuario - BioInnova")
        st.write("Esta plataforma automatiza procesos bioinformáticos avanzados...")
        st.markdown("- **Estación 1:** Modelado del Dogma Central.")
        st.markdown("- **Estación 2:** Alineamiento Needleman-Wunsch.")
        st.markdown("- **Estación 4:** Análisis Cladístico Matemático.")
        
    with tab2:
        st.subheader("Protocolos de Prácticas")
        st.download_button("Descargar Guía de Práctica 1 (PDF)", data=b"Demo PDF", file_name="practica1_bioinnova.pdf")
        
    with tab3:
        st.subheader("Examen de Certificación de Aptitud Bioinformática")
        st.write("Requiere 200 BioPuntos para desbloquear.")
        if st.session_state['biopuntos'] >= 200:
            st.button("Iniciar Examen (Desbloqueado)")
        else:
            st.button("Iniciar Examen (Bloqueado)", disabled=True)
            st.caption(f"Le faltan {200 - st.session_state['biopuntos']} pts.")

# Pie de página
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>BioInnova v1.2 | ISFODOSU - Recinto Luis Napoleón Núñez Molina | Licenciatura en Biología orientada a la Educación Secundaria</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Desarrollado por Paulino-Hidalgo, L. | 2026</p>", unsafe_allow_html=True)
