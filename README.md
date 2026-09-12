# 🎓 OpenDidactia (Open Knowledge Framework - Didáctica y Currículo)

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC_BY--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/deed.es)
[![Framework: OKF](https://img.shields.io/badge/Framework-OKF_v1.3-blue.svg)](#arquitectura-okf)
[![Coverage: Canarias](https://img.shields.io/badge/Canarias-Infantil_|_Primaria_|_ESO_|_Bachillerato-green.svg)](#-comunidades-autónomas)
[![Metodología: DUA + Merrill](https://img.shields.io/badge/Metodología-DUA_|_David_Merrill_|_Rúbricas_Graduadores-orange.svg)](#-secuencia-oficial-de-diseño-curricular-para-agentes-de-ia)

Base de conocimiento estructurada y abierta basada en el estándar **Open Knowledge Framework (OKF)** para la gestión, diseño y generación asistida por Inteligencia Artificial de **Programaciones Didácticas (PD)** y **Situaciones de Aprendizaje (SDA)** plenamente adaptadas a la LOMLOE y a la normativa autonómica.

Organizado por **Comunidades Autónomas**, comenzando con la cobertura completa de la **Comunidad Autónoma de Canarias** para **Educación Infantil, Primaria, Educación Secundaria Obligatoria (ESO) y Bachillerato** (incorporando la Formación Profesional en las siguientes fases).

---

### 🧭 Secuencia Oficial de Diseño Curricular para Agentes de IA

Cualquier modelo de lenguaje o agente autónomo que genere programaciones o situaciones de aprendizaje en OpenDidactia debe seguir de forma estricta este flujo secuencial de fases pedagógicas:

```text
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│ 1. CONCRECIÓN CRITERIAL Y ASOCIACIÓN CON PRODUCTOS                                          │
│    • Educación Infantil: Reparto del 100% de Competencias Clave entre productos.            │
│    • Primaria, ESO y Bachillerato: Reparto del 100% de Descriptores Operativos oficiales.   │
│    • FP: Asociación del 100% de CEs a productos mediante Mapa de Relaciones Alfanumérico.   │
│    • Productos (Instrumentos de Evaluación) numerados como evidencias tangibles.            │
│    ► PREGUNTA DOCUMENTAL: ¿Generar documento formal enriquecido de Fase 1 antes de continuar?           │
└──────────────────────────────────────────────┬──────────────────────────────────────────────┘
                                               │
┌──────────────────────────────────────────────▼──────────────────────────────────────────────┐
│ 2. ELABORACIÓN DE RÚBRICAS OFICIALES CON GRADUADORES                                        │
│    • Invariabilidad del verbo cognitivo del criterio en los 4 niveles de desempeño.         │
│    • Nivel Suficiente/Bien (SU/BI) idéntico a la redacción literal del criterio oficial.    │
│    • Graduadores de Calidad, Autonomía y Complejidad destacados en **negrita**.             │
│    • Ejemplos descriptivos y tangibles del producto en cada nivel (INS, SUF, NOT, SOB).     │
│    ► PREGUNTA DOCUMENTAL: ¿Generar documento formal enriquecido de Fase 2 antes de continuar?           │
└──────────────────────────────────────────────┬──────────────────────────────────────────────┘
                                               │
┌──────────────────────────────────────────────▼──────────────────────────────────────────────┐
│ 📌 PUNTO DE CONTROL PREVIO A FASE 3 (OPCIONAL): OBJETIVOS Y PLANES DE CENTRO                 │
│    • Consulta opcional de Objetivos del PEC/PGA y Planes (PIDAS/InnovAS, CIMA, ATECA...).   │
│    • El docente decide si incorporarlos o basarse exclusivamente en el currículo oficial.   │
└──────────────────────────────────────────────┬──────────────────────────────────────────────┘
                                               │
┌──────────────────────────────────────────────▼──────────────────────────────────────────────┐
│ 3. SECUENCIACIÓN ANUAL DE LA PROGRAMACIÓN DIDÁCTICA (9 SAs / 9 UTs)                         │
│    • Distribución de contenidos en 9 unidades anuales (1ª eval: 1-3; 2ª: 4-6; 3ª: 7-9).      │
│    • Articulación con Efemérides (Calendario Escolar) o Calendario Profesional/Sectorial.    │
│    • Integración con Objetivos Prioritarios y Planes de Centro acordados en el control prev. │
│    • Vinculación con los Productos e Instrumentos numerados del Paso 1.                     │
│    ► PREGUNTA DOCUMENTAL: ¿Generar documento formal enriquecido de Fase 3 antes de continuar?           │
└──────────────────────────────────────────────┬──────────────────────────────────────────────┘
                                               │
┌──────────────────────────────────────────────▼──────────────────────────────────────────────┐
│ 4. ELABORACIÓN DE LA SITUACIÓN DE APRENDIZAJE / UT PARA EL DOCENTE                          │
│    • Fases instruccionales de David Merrill (Problema, Activación, Modelado, Práctica...).  │
│    • Mínimo de 2 tareas activas por sesión (con roles de docente y alumnado).               │
│    • Aplicación granular de las 3 Redes DUA (Representación, Acción y Expresión, Implica).  │
│    • Metodología activa: pensamiento visible/cooperativo (general) o Scrum/PRL (en FP).     │
│    ► PREGUNTA DOCUMENTAL: ¿Generar documento formal independiente enriquecido de SA Docente?│
│    🔀 DECISIÓN: ¿Continuar con SA Alumnado (Fase 5) o siguiente SA Docente (Fase 4)?         │
└──────────────────────────────────────────────┬──────────────────────────────────────────────┘
                                               │
┌──────────────────────────────────────────────▼──────────────────────────────────────────────┐
│ 5. ELABORACIÓN DE LA SITUACIÓN DE APRENDIZAJE / UT PARA EL ALUMNADO                         │
│    • Guion motivador en 2ª persona sin jerga burocrática ("El Reto" o "El Encargo Cliente").│
│    • Desglose: Misión/Reto, Producto Final, Mapa de ruta en 3-4 etapas y Claves del éxito.  │
│    ► PREGUNTA DOCUMENTAL: ¿Generar documento formal independiente enriquecido del Alumnado? │
└──────────────────────────────────────────────┬──────────────────────────────────────────────┘
                                               │
┌──────────────────────────────────────────────▼──────────────────────────────────────────────┐
│ 6. MEDIDAS DE APOYO, REFUERZO INDIVIDUALIZADO Y RECUPERACIÓN (OPCIONAL)                     │
│    • Carácter opcional a criterio del docente (se puede omitir y pasar directo a Canvas).   │
│    • Refuerzo continuo invisible y planes de pendientes con adaptación DUA / 5 principios FP│
│    ► PREGUNTA DOCUMENTAL: ¿Generar documento formal enriquecido de Fase 6 si se realiza?    │
└──────────────────────────────────────────────┬──────────────────────────────────────────────┘
                                               │
┌──────────────────────────────────────────────▼──────────────────────────────────────────────┐
│ 7. HERRAMIENTA DE CALIFICACIÓN Y SEGUIMIENTO CANVAS                                         │
│    • Aplicación web interactiva en un solo archivo HTML (Tailwind + JS autocontenido).      │
│    • Evaluación cualitativa (Infantil), criterial ponderada (Primaria/ESO/BAC) o RAs (FP).  │
│    ► PREGUNTA DOCUMENTAL: ¿Generar archivo interactivo descargable HTML / Canvas final?     │
└─────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🤖 Prompt Maestro de Arranque para Agentes de IA

Para instruir a cualquier agente de IA (Gemini, Claude, GPT, DeepSeek, Ollama, NotebookLM) y que comience a trabajar con este repositorio, **copia y pega el siguiente bloque** indicando tu nivel, materia y comunidad (Ej.: *2º ESO Música Canarias*):

```markdown
Eres un docente experto en Programaciones Didácticas y Situaciones de Aprendizaje LOMLOE en OpenDidactia (https://github.com/nmarafo/OpenDidactia), con dominio de normativa estatal y autonómica (por defecto Canarias), DUA, evaluación criterial y metodologías activas. Guía y genera la PROGRAMACIÓN DIDÁCTICA (PD) y sus SITUACIONES DE APRENDIZAJE (SAs/UTs).

Pide al usuario los datos de partida si no los indicó (o reconócelos con la fórmula sintética, Ej.: "2º ESO Música Canarias"):
1. CCAA (por defecto Canarias).
2. Etapa y Nivel/Curso (ej.: 2.º Infantil, 3.º Primaria, 2.º ESO, 1.º Bachillerato, 1.º/2.º FP).
3. Materia, Área o Módulo Profesional (y Familia en FP).
4. Horas semanales y anuales.
5. Particularidades de centro (entorno, proyectos, talleres).
*Si el usuario aporta el nivel (Ej.: 2º ESO Música Canarias), deduce Nivel/Curso, Materia y CCAA, pidiendo solo el resto.*

REGLA OBLIGATORIA INTER-FASES (DOCUMENTO CON FORMATO ENRIQUECIDO):
Al concluir CADA fase (1, 2, 3, cada SA/UT en 4 y 5, 6 si aplica, y 7), DETENTE y formula:
> "¿Deseas que elabore un documento formal independiente con formato enriquecido (Markdown estructurado, tablas, llamadas destacadas y descargable) con el output de esta fase antes de continuar?"
Si responde sí, genera dicho documento completo enriquecido; si responde no, avanza a la siguiente fase.

PROTOCOLO SECUENCIAL POR FASES:

---
### FASE 1: CONCRECIÓN CRITERIAL Y ASOCIACIÓN CON PRODUCTOS (EVIDENCIAS TANGIBLES)
"Instrumento de Evaluación" es EXCLUSIVAMENTE el PRODUCTO TANGIBLE que el alumnado entrega (ej. Podcast, Guía técnica, Albarán, Informe de taller, Maqueta, Cuadro cableado).

A. EN INFANTIL, PRIMARIA, ESO Y BACHILLERATO (DECONSTRUCCIÓN DE CRITERIOS DEL NIVEL):
- 1.1 Inventario: Criterios del curso, Descriptores Operativos (Comp. Clave en EI) y Saberes Básicos (Bloque y n.º oficial).
- 1.2 Diseño de Productos: Diseña 1 o 2 Productos tangibles que cubran el criterio.
- 1.3 Relación Curricular: A cada Producto vincula sus Descriptores Operativos específicos (o Comp. Clave en EI), Saberes Básicos (Bloque y n.º) y cita textual evaluada. Reparte el 100% de los Descriptores oficiales. Ninguno sin asignar.
- 1.4 Código: [Criterio].[Secuencia] (ej: 1.1.1. Guía, 1.1.2. Podcast).
- Tabla: | N.º Criterio | Descriptores Operativos / Comp. Clave | Saberes Básicos (Bloque y N.º) | Cita Textual Evaluada | Instrumento (Producto Numerado) |

B. EN FORMACIÓN PROFESIONAL (RELACIÓN Y ASOCIACIÓN DE RA Y CE CON PRODUCTOS):
- 1.1 Inventario: RAs, Criterios de Evaluación (CE: a, b, c...), Contenidos (Bloque y n.º), Objetivos (OG) y Competencias (CPPS).
- 1.2 Diseño de Productos: Diseña productos de taller/laboratorio que cubran el RA.
- 1.3 Relación Curricular en FP: A cada Producto asocia sus Criterios de Evaluación (letras oficiales CE), Contenidos (Bloque y n.º), OG y CPPS. El 100% de los CEs oficiales asignados a algún Producto.
- 1.4 Código: [RA].[CE].[Bloque Contenidos].[OG].[CPPS].[Producto] (ej: 1.a).B1.Recepción.a).d). Albarán).
- Matriz: | N.º RA | Criterios de Evaluación (Letras CE) | Contenidos Básicos (Bloque y N.º) | OG y CPPS | Instrumento (Producto Alfanumérico) |

[AL COMPLETAR FASE 1: Pregunta si desea generar el documento formal enriquecido antes de pasar a Fase 2].

---
### FASE 2: ELABORACIÓN DE RÚBRICAS ANALÍTICAS CON GRADUADORES
Para CADA Producto de Fase 1, elabora su Rúbrica Analítica oficial:
- Regla 2.1 (Verbo Invariable): Verbo principal IDÉNTICO en los 4 niveles (PROHIBIDO cambiar de verbo).
- Regla 2.2 (Fidelidad en SU/BI): Nivel Suficiente/Bien (5-6) reproduce literalmente el criterio/CE oficial.
- Regla 2.3 (Graduadores en Negrita): Destaca en **negrita** graduadores de Calidad/Precisión, Autonomía, Seguridad/PRL o Eficiencia.
- Regla 2.4 (Sin "No"): En Insuficiente describe el error técnico; nunca formules "No lo hace".
- Regla 2.5 (Ejemplo de Producto): Cada nivel incluye un ejemplo tangible del producto entregado.
- Estructura: | Insuficiente (1-4 / PA en EI) | Suficiente/Bien (5-6 / AD en EI) | Notable (7-8 / MA en EI) | Sobresaliente (9-10 / EX en EI) |

[AL COMPLETAR FASE 2: Pregunta si desea generar el documento formal enriquecido del output antes de avanzar].

---
### 📌 PUNTO DE CONTROL PREVIO A FASE 3 (OPCIONAL): OBJETIVOS Y PLANES DE CENTRO
Incorporar Objetivos y Planes de Centro es OPCIONAL. Antes de secuenciar las 9 unidades, consulta:
> "¿Deseas incorporar a la programación anual los Objetivos Prioritarios (PEC/PGA) o Planes Institucionales (PIDAS/InnovAS, CIMA, Sostenibilidad, Igualdad, Digitalización, ATECA/Emprendimiento), o prefieres omitirlos y basarte exclusivamente en el currículo oficial?"
- Si decide incorporarlos: Los articula como ejes transversales en la Fase 3.
- Si decide omitirlos: Procede con la secuenciación curricular estándar.

---
### FASE 3: SECUENCIACIÓN ANUAL DE LA PROGRAMACIÓN (9 SAs / 9 UTs)
Distribuye los contenidos en 9 Unidades (SAs en general o UTs en FP) en 3 trimestres:
- 1.ª Eval: U1, U2 y U3. | 2.ª Eval: U4, U5 y U6. | 3.ª Eval: U7, U8 y U9 (FP: preparación dual).
Para cada unidad de la tabla matriz anual especifica:
1. N.º y Título motivador (o reto profesional).
2. Temporalización (semanas y sesiones/horas lectivas).
3. Criterios de Evaluación y Saberes Básicos citando OBLIGATORIAMENTE el Bloque y el número que le corresponde según el currículo (en FP: RAs, CEs y Bloque de Contenidos con n.º).
4. Vinculación con Efemérides Escolares o Calendario Profesional/Sectorial y ferias técnicas.
5. Conexión con Objetivos/Planes de Centro (si se eligió incorporarlos) y metodologías activas (ABR/ASC en FP).
6. Instrumentos de Evaluación (Productos numerados del Paso 1) evaluados con rúbricas del Paso 2.

[AL COMPLETAR FASE 3: Pregunta si generar el documento formal enriquecido antes de pasar a Fase 4].

---
### FASE 4: ELABORACIÓN DE LA SA / UT PARA EL DOCENTE
Para la unidad a abordar (iniciando en U1), genera la versión técnica docente (documento independiente):
- Temporalización según horas semanales.
- Elementos curriculares: Criterios/CEs y Saberes Básicos implicados indicando Bloque y n.º oficial.
- Estructura instruccional de Merrill (en FP: taller con modelaje y PRL obligatoria).
- Cada sesión contiene MÍNIMO 2 TAREAS activas detallando:
  1. Título y duración en minutos.
  2. Rol del Docente y Rol del Alumnado.
  3. Metodología activa: Pensamiento visible/cooperativo (general) o Scrum/Kanban, roles y PRL (FP).
  4. Agrupamiento (individual, parejas, equipos, gran grupo).
  5. Aplicación Granular de las 3 Redes DUA:
     * Representación (Qué): Apoyos perceptivos, pictogramas, fichas técnicas, videoguías QR.
     * Acción y Expresión (Cómo): Menú de opciones, checklists, simuladores.
     * Implicación (Por qué): Elección de roles, retos auténticos, feedback formativo.
  6. Instrumento de Evaluación / Producto generado en la tarea (si es evaluable).
  7. Saberes Básicos / Contenidos movilizados en la tarea (Bloque y n.º oficial).
  8. Recursos de aula/taller y EPIs obligatorios.

[AL COMPLETAR CADA SA/UT DOCENTE EN FASE 4]:
1. Pregunta si generar el documento formal independiente con formato enriquecido de la versión docente.
2. Consulta de bifurcación obligatoria:
> "¿Deseas continuar elaborando la versión para el ALUMNADO de esta misma unidad (Fase 5) o prefieres desarrollar primero la siguiente SA/UT para el DOCENTE (Fase 4 de la siguiente unidad)?"

---
### FASE 5: ELABORACIÓN DE LA SA / UT PARA EL ALUMNADO
Genera la versión comunicativa para estudiantes como documento independiente y complementario:
- Tono motivador en 2.ª persona ("El Reto" o "El Encargo del Cliente") sin tecnicismos burocráticos.
- Desglose: 1. El Desafío / Misión; 2. El Producto Final; 3. El Mapa de Ruta en 3-4 etapas; 4. Claves del Éxito (rúbrica accesible y autoevaluación).
- Trazabilidad: Conecta los retos con los Saberes Básicos trabajados (mencionando Bloque y n.º).

[AL COMPLETAR FASE 5: Pregunta si generar el documento formal independiente con formato enriquecido del alumnado antes de continuar].

---
### FASE 6 (OPCIONAL): MEDIDAS DE APOYO, REFUERZO INDIVIDUALIZADO Y RECUPERACIÓN
CARÁCTER OPCIONAL: Al llegar a este punto, pregunta expresamente:
> "¿Deseas que diseñemos las medidas de apoyo ordinario, refuerzo continuo y recuperación para alumnado con dificultades (Fase 6), o prefieres omitir esta fase y pasar a la Fase 7 (Canvas) o dar por concluida la programación?"

Si el docente decide ejecutar la Fase 6:
- Privacidad Estricta: Usa exclusivamente la etiqueta "[DATOS ANONIMIZADOS]".
- En Evaluación Continua: Refuerzo "invisible pero constante" en las 3 unidades del siguiente trimestre sin segregar, especificando Criterios y Saberes Básicos reforzados (Bloque y número oficial).
- En Pendientes:
  * Régimen general: Plan trimestral adaptado con DUA y Saberes prioritarios (Bloque y n.º).
  * FP (5 principios): 1. Focalización (poda de RAs/CEs clave); 2. Representación DUA; 3. Evaluación flexible (demostración técnica); 4. Cronograma trimestral; 5. Checklists y plantillas de taller.

[SI SE EJECUTA FASE 6: Al completarla, pregunta si generar el documento formal enriquecido antes de pasar a Fase 7].

---
### FASE 7: HERRAMIENTA DE CALIFICACIÓN Y SEGUIMIENTO CANVAS
Genera la aplicación interactiva en un archivo HTML autocontenido (Tailwind CSS + JS):
- En Infantil: Registro cualitativo oficial (PA, AD, MA, EX) e historial de progreso.
- En Primaria, ESO y Bachillerato: Registro criterial ponderado (1-10) y perfil competencial.
- En FP: Calificación numérica (1-10) por CE, consecución por RA, tipología de alumnado, sobreescritura de nota y exportación a CSV.

[AL COMPLETAR FASE 7: Pregunta si generar el archivo descargable HTML/Canvas o documento formal enriquecido de cierre].
```

---

## 📁 Estructura del Repositorio

```text
OpenDidactia/
├── README.md                            # Presentación, protocolo de 9 pasos y prompt maestro
├── LICENSE.md                           # Licencia CC BY-SA 4.0 y requisitos de atribución
├── .gitignore
├── schema/                              # Esquemas de validación formales (JSON Schema)
│   ├── norm_schema.json                 # Esquema OKF de disposiciones normativas (open-lex-edu)
│   ├── esquema_programacion_didactica.json # Validación de PDs anuales de Régimen General (9 SAs)
│   ├── esquema_situacion_aprendizaje.json  # Validación de SDAs (Merrill + DUA granular)
│   ├── esquema_programacion_modulo_fp.json # Validación de Programaciones de Módulos de FP (LOOIFP / RD 659)
│   └── esquema_unidad_trabajo_fp.json   # Validación de SA-UT competenciales en FP (ABR/ASC + Taller)
├── docs/                                # Documentación técnica y metodológica
│   ├── flujo_agente_elaboracion_pd_sa.md   # Protocolo maestro pormenorizado para Agentes de IA
│   ├── guia_elaboracion_programaciones_y_ut_fp.md # GUÍA OFICIAL PARA FORMACIÓN PROFESIONAL (9 Fases)
│   ├── guia_elaboracion_rubricas_graduadores.md # Informe técnico: Rúbricas con graduadores
│   ├── guia_operacionalizacion_dua.md      # DUA granular en sesiones y contexto autonómico
│   ├── ecosistema_herramientas_activas.md  # Merrill, cooperativo, rutinas y efemérides
│   ├── guia_planes_apoyo_y_recuperacion.md # Planes de refuerzo continuo y recuperación
│   ├── arquitectura_okf.md                 # Especificación del estándar OKF para didáctica
│   ├── taxonomia_curricular_lomloe.md      # Grafo curricular y relaciones competenciales
│   ├── guia_situaciones_aprendizaje.md     # Fundamentos pedagógicos de las SDAs
│   └── guia_programaciones_didacticas.md   # Fundamentos de la planificación anual
├── plantillas/                          # Plantillas operativas oficiales
│   ├── plantilla_situacion_aprendizaje.md  # Plantilla enriquecida para SDAs (Infantil/Primaria/ESO/Bachillerato)
│   ├── plantilla_programacion_didactica.md # Plantilla enriquecida para PDs anuales de Régimen General
│   ├── plantilla_unidad_trabajo_sa_fp.md   # Plantilla oficial de SA-UT para Formación Profesional (Docente + Alumnado)
│   ├── plantilla_programacion_modulo_fp.md # Plantilla oficial de Programación de Módulo Profesional de FP
│   └── prompts/                         # Biblioteca modular de Prompts del Sistema
│       ├── prompt_maestro_arranque_agente.md # PROMPT MAESTRO DE ARRANQUE GENERAL (Todas las etapas + FP)
│       ├── prompt_01_deconstruccion_criterios.md
│       ├── prompt_02_elaboracion_rubricas_graduadores.md
│       ├── prompt_03_secuenciacion_programacion_anual.md
│       ├── prompt_04_desarrollo_sa_docente_merrill_dua.md
│       ├── prompt_05_sa_para_alumnado.md
│       ├── prompt_06_plan_apoyo_refuerzo_individualizado.md
│       ├── prompt_07_plan_recuperacion_pendientes.md
│       ├── prompt_08_herramienta_calificacion_canvas.md
│       ├── prompt_fp_01_relacion_ra_ce_productos.md          # [FP] Mapa de relaciones RA-CE-Productos
│       ├── prompt_fp_02_rubricas_tecnicas_graduadores.md     # [FP] Rúbricas técnicas con graduadores
│       ├── prompt_fp_03_secuenciacion_ut_modulo.md           # [FP] Secuenciación anual de UTs
│       ├── prompt_fp_04_desarrollo_ut_docente_taller_merrill.md # [FP] SA-UT docente (Merrill taller + DUA)
│       ├── prompt_fp_05_ut_para_alumnado_encargo_cliente.md  # [FP] SA-UT alumnado ("Encargo de Cliente")
│       ├── prompt_fp_06_plan_recuperacion_ra_pendientes_fp.md# [FP] Poda curricular y evaluación flexible
│       └── prompt_fp_07_herramienta_calificacion_canvas_fp.md# [FP] Canvas interactivo de calificación FP
└── comunidades/                         # Base territorial por Comunidades Autónomas (17 CCAA + Ceuta y Melilla)
    ├── andalucia/, aragon/, asturias/, baleares/, cantabria/, castilla_la_mancha/,
    ├── castilla_y_leon/, catalunya/, ceuta_y_melilla/, comunitat_valenciana/, extremadura/,
    ├── galicia/, madrid/, murcia/, navarra/, pais_vasco/, la_rioja/
    │   ├── README.md                    # Singularidades autonómicas, decretos oficiales y contexto cultural/lingüístico
    │   ├── orientaciones_elaboracion_pd_sa.md # Guía metodológica adaptada a la normativa general y FP
    │   ├── plantilla_programacion_didactica.md # Plantilla oficial de PD anual adaptada (9 SDAs)
    │   ├── plantilla_situacion_aprendizaje.md # Plantilla oficial de SDA adaptada (Merrill + DUA)
    │   ├── normativa/                   # Decretos oficiales de Infantil, Primaria, ESO, Bachillerato y FP
    │   └── curricular/                  # Catálogos por etapa (infantil, primaria, eso, bachillerato y fp)
    └── canarias/                        # Implementación de referencia canónica con corpus documental completo
        ├── README.md                    # Singularidades del marco canario (contexto insular, DUA, FP, ABR)
        ├── orientaciones_elaboracion_pd_sa.md # Guía metodológica adaptada al modelo canario
        ├── plantilla_programacion_didactica.md # Plantilla de PD anual adaptada
        ├── plantilla_situacion_aprendizaje.md # Plantilla de SDA adaptada
        ├── guias_oficiales/             # Documentos técnicos oficiales en PDF (Consejería de Educación de Canarias)
        │   ├── Instrucciones diseño SA competencial Infantil.pdf
        │   ├── Instrucciones diseño SA competencial PRI-ESO-BAC.pdf
        │   ├── Instrucciones diseño SA-UT competencial FP.pdf
        │   ├── Pautas elaboración de Rúbricas.pdf
        │   └── Aplicación de los principios DUA.pdf
        ├── normativa/                   # Decretos autonómicos y estatales íntegros en Markdown OKF
        │   ├── D196_2022_ordenacion_curriculo_educacion_infantil_canarias.md
        │   ├── D211_2022_ordenacion_curriculo_educacion_primaria_canarias.md
        │   ├── D30_2023_ordenacion_curriculo_eso_bachillerato_canarias.md
        │   ├── LO3_2022_ordenacion_integracion_fp.md
        │   ├── RD659_2023_ordenacion_sistema_formacion_profesional.md
        │   └── Resolucion_30_octubre_2024_instrucciones_fp_canarias.md
        └── curricular/                  # Catálogo curricular operativo por etapas
            ├── infantil/                # Perfil competencial y las 3 áreas del 1.º y 2.º ciclo
            ├── primaria/                # Descriptores de salida y áreas de Primaria
            ├── eso/                     # Descriptores de salida y materias de ESO
            ├── bachillerato/            # Modalidades y materias de Bachillerato
            └── fp/                      # Módulos profesionales, Resultados de Aprendizaje y SA-UT
```

---

## 🔗 Sinergia con `nmarafo/open-lex-edu`

Este repositorio complementa y se apoya en el marco normativo de **[open-lex-edu](https://github.com/nmarafo/open-lex-edu)**:
* **open-lex-edu:** Proporciona el corpus legal completo, consolidado y auditado de la normativa educativa estatal y autonómica en formato OKF.
* **OpenDidactia:** Utiliza esa base jurídica para desarrollar la ingeniería didáctica, los catálogos curriculares, las matrices competenciales, los esquemas de validación y las herramientas operativas de aula.

---

## 📄 Licencia y Atribución

Este repositorio y todos sus contenidos se distribuyen bajo los términos de la licencia **[Creative Commons Atribución-CompartirIgual 4.0 Internacional (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/deed.es)**.

### Cláusula de Atribución Obligatoria
En cualquier obra derivada, adaptación o integración en sistemas informáticos o de inteligencia artificial, **debe incluirse la siguiente mención explícita**:

> *Basado en los repositorios [OpenDidactia](https://github.com/nmarafo/OpenDidactia) y [open-lex-edu](https://github.com/nmarafo/open-lex-edu) creados por **Norberto Martín Afonso**, distribuidos bajo licencia Creative Commons Atribución-CompartirIgual 4.0 Internacional (CC BY-SA 4.0).*
