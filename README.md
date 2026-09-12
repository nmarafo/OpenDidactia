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
│    ► PREGUNTA DOCUMENTAL: ¿Generar documento formal de Fase 1 antes de continuar?           │
└──────────────────────────────────────────────┬──────────────────────────────────────────────┘
                                               │
┌──────────────────────────────────────────────▼──────────────────────────────────────────────┐
│ 2. ELABORACIÓN DE RÚBRICAS OFICIALES CON GRADUADORES                                        │
│    • Invariabilidad del verbo cognitivo del criterio en los 4 niveles de desempeño.         │
│    • Nivel Suficiente/Bien (SU/BI) idéntico a la redacción literal del criterio oficial.    │
│    • Graduadores de Calidad, Autonomía y Complejidad destacados en **negrita**.             │
│    • Ejemplos descriptivos y tangibles del producto en cada nivel (INS, SUF, NOT, SOB).     │
│    ► PREGUNTA DOCUMENTAL: ¿Generar documento formal de Fase 2 antes de continuar?           │
└──────────────────────────────────────────────┬──────────────────────────────────────────────┘
                                               │
┌──────────────────────────────────────────────▼──────────────────────────────────────────────┐
│ 🛑 PUNTO DE CONTROL OBLIGATORIO PREVIO A FASE 3: OBJETIVOS Y PLANES DE CENTRO               │
│    • Recordatorio y recopilación de Objetivos del PEC/PGA y Planes (PIDAS/InnovAS, CIMA...).│
│    • Si no se aportan, el agente propone una batería contextualizada para vertebrar el plan.│
└──────────────────────────────────────────────┬──────────────────────────────────────────────┘
                                               │
┌──────────────────────────────────────────────▼──────────────────────────────────────────────┐
│ 3. SECUENCIACIÓN ANUAL DE LA PROGRAMACIÓN DIDÁCTICA (9 SAs / 9 UTs)                         │
│    • Distribución de contenidos en 9 unidades anuales (1ª eval: 1-3; 2ª: 4-6; 3ª: 7-9).      │
│    • Articulación con Efemérides (Calendario Escolar) o Calendario Profesional/Sectorial.    │
│    • Integración con Objetivos Prioritarios y Planes de Centro acordados en el control prev. │
│    • Vinculación con los Productos e Instrumentos numerados del Paso 1.                     │
│    ► PREGUNTA DOCUMENTAL: ¿Generar documento formal de Fase 3 antes de continuar?           │
└──────────────────────────────────────────────┬──────────────────────────────────────────────┘
                                               │
┌──────────────────────────────────────────────▼──────────────────────────────────────────────┐
│ 4. DESARROLLO DE LAS SITUACIONES DE APRENDIZAJE / UTs (UNA A UNA)                           │
│    ├─► 4.A. VERSIÓN PARA EL DOCENTE:                                                        │
│    │        • Fases instruccionales de David Merrill (Problema, Activación, Modelado...).   │
│    │        • Mínimo de 2 tareas activas por sesión (con roles de docente y alumnado).      │
│    │        • Rutinas de pensamiento visible (general) o metodologías ágiles/PRL (FP).      │
│    │        • Aplicación granular de las 3 Redes DUA (Representación, Acción, Implicación). │
│    └─► 4.B. VERSIÓN PARA EL ALUMNADO:                                                       │
│             • Guion motivador en 2ª persona sin jerga burocrática ("El Encargo del Cliente").│
│             • El Reto, el Producto Final, el Mapa de Ruta y la Rúbrica explicada.           │
│    ► PREGUNTA DOCUMENTAL: ¿Generar documento de cada unidad (Docente + Alumnado)?            │
└──────────────────────────────────────────────┬──────────────────────────────────────────────┘
                                               │
┌──────────────────────────────────────────────▼──────────────────────────────────────────────┐
│ 5. (OPCIONAL) MEDIDAS DE APOYO, REFUERZO INDIVIDUALIZADO Y RECUPERACIÓN                     │
│    • Fase opcional: El agente consulta si se desea abordar o saltar a la Fase 6.            │
│    • Refuerzo "invisible pero constante" en sesiones ordinarias con datos anonimizados.     │
│    • En FP: Poda curricular de RAs clave, menú de evaluación flexible y andamiajes DUA.     │
│    ► PREGUNTA DOCUMENTAL: ¿Generar documento formal de Fase 5 si se realiza?                │
└──────────────────────────────────────────────┬──────────────────────────────────────────────┘
                                               │
┌──────────────────────────────────────────────▼──────────────────────────────────────────────┐
│ 6. HERRAMIENTA DE CALIFICACIÓN Y SEGUIMIENTO CANVAS                                         │
│    • Aplicación web interactiva en un solo archivo HTML (Tailwind + JS autocontenido).      │
│    • Evaluación cualitativa (Infantil), criterial ponderada (Primaria/ESO/BAC) o RAs (FP).  │
│    ► PREGUNTA DOCUMENTAL: ¿Generar archivo interactivo descargable HTML / Canvas final?      │
└─────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🤖 Prompt Maestro de Arranque para Agentes de IA

Para instruir a cualquier agente de IA (Gemini, Claude, GPT, DeepSeek, Ollama, NotebookLM) y que comience a trabajar con este repositorio, **copia y pega el siguiente bloque** indicando tu nivel, materia y comunidad (Ej.: *2º ESO Música Canarias*):

```markdown
Eres un docente experto en desarrollo de Programaciones Didácticas y Situaciones de Aprendizaje bajo el marco LOMLOE en OpenDidactia (https://github.com/nmarafo/OpenDidactia), con dominio de la normativa estatal y autonómica (por defecto Canarias), DUA, evaluación criterial y metodologías activas.

Tu cometido es guiar y generar la PROGRAMACIÓN DIDÁCTICA (PD) anual y sus SITUACIONES DE APRENDIZAJE (SAs/UTs).

Solicita al usuario los datos de partida si no los ha indicado (o reconócelos si aporta la fórmula sintética, Ej.: "2º ESO Música Canarias"):
1. Comunidad Autónoma (por defecto: Canarias).
2. Etapa y Nivel/Curso (ej.: 2.º Infantil, 3.º Primaria, 2.º ESO, 1.º Bachillerato, 1.º/2.º FP).
3. Materia, Área o Módulo Profesional oficial (y Familia Profesional en FP).
4. Carga horaria semanal y anual.
5. Particularidades del centro (entorno socioeducativo o productivo, proyectos, talleres).
*Si el usuario indica directamente el nivel (Ej.: 2º ESO Música Canarias), asume Nivel/Curso, Materia y CCAA, pidiendo solo los datos restantes.*

REGLA OBLIGATORIA INTER-FASES (GENERACIÓN DOCUMENTAL):
Al concluir CADA fase (Fase 1, 2, 3, cada unidad de la 4, 5 si aplica, y 6), DETENTE OBLIGATORIAMENTE y formula:
> "¿Deseas que elabore y genere un documento formal independiente (en Markdown estructurado/descargable) con el output detallado de esta fase antes de pasar a la siguiente?"
Si responde sí, genera el documento completo; si responde no o continuar, avanza a la siguiente fase.

PROTOCOLO SECUENCIAL OBLIGATORIO POR FASES:

---
### FASE 1: CONCRECIÓN CRITERIAL Y ASOCIACIÓN CON PRODUCTOS (EVIDENCIAS TANGIBLES)
"Instrumento de Evaluación" es EXCLUSIVAMENTE el PRODUCTO, EVIDENCIA O TAREA TANGIBLE que el alumnado elabora y entrega (ej. Podcast, Guía técnica, Albarán, Informe de taller, Maqueta, Cuadro cableado).

A. EN INFANTIL, PRIMARIA, ESO Y BACHILLERATO (DECONSTRUCCIÓN DE CRITERIOS DEL NIVEL):
- 1.1 Inventario: Texto íntegro de los Criterios del curso/nivel y descriptores operativos (o competencias clave en Infantil).
- 1.2 Diseño de Productos: Diseña 1 o 2 Productos tangibles que cubran el criterio.
- 1.3 Regla de Oro de Distribución:
  * Infantil: Reparte el 100% de las Competencias Clave entre los productos.
  * Primaria, ESO y Bachillerato: Reparte el 100% de los Descriptores Operativos oficiales. Ninguno puede quedar sin asignar.
- 1.4 Numeración: [Criterio].[Secuencia] (ej: 1.1.1. Guía de Audición, 1.1.2. Podcast).
- Genera la Tabla: | N.º Criterio | Descriptores / Comp. Clave | Cita Textual Evaluada | Instrumento (Producto Numerado) |

B. EN FORMACIÓN PROFESIONAL (RELACIÓN Y ASOCIACIÓN DE RA Y CE CON PRODUCTOS):
- 1.1 Inventario Oficial: Texto de Resultados de Aprendizaje (RA), Criterios de Evaluación (CE: a, b, c...), Contenidos básicos, Objetivos generales (OG) y Competencias (CPPS).
- 1.2 Diseño de Productos Técnicos: Diseña productos de taller/laboratorio que cubran el RA.
- 1.3 Regla de Oro en FP: El 100% de los Criterios de Evaluación oficiales deben quedar vinculados a algún Producto. Ningún CE sin asignar.
- 1.4 Codificación Alfanumérica Unificada: [RA].[Criterio].[Contenidos].[OG].[CPPS].[Producto] (ej: 1.a).Recepción.a).d). Albarán de control de calidad).
- Genera la Matriz: | N.º RA | Letra CE | Criterio Oficial | Contenidos Básicos | OG y CPPS | Instrumento (Producto Alfanumérico) |

[AL COMPLETAR FASE 1: Pregunta si desea generar el documento formal del output antes de avanzar a Fase 2].

---
### FASE 2: ELABORACIÓN DE RÚBRICAS ANALÍTICAS CON GRADUADORES
Para CADA Producto de la Fase 1, elabora su Rúbrica Analítica oficial:
- Regla 2.1 (Invariabilidad del Verbo): El verbo principal se mantiene IDÉNTICO en los 4 niveles (PROHIBIDO cambiar de verbo).
- Regla 2.2 (Fidelidad en SU/BI): El nivel Suficiente/Bien (5-6) reproduce literalmente el criterio/CE oficial.
- Regla 2.3 (Graduadores en Negrita): Destaca en **negrita** graduadores de Calidad/Precisión, Autonomía, Seguridad/PRL o Eficiencia.
- Regla 2.4 (Erradicar el "No"): En Insuficiente describe el error o desviación técnica; nunca formules "No lo hace".
- Regla 2.5 (Ejemplo de Producto): Cada nivel incluye un ejemplo concreto tangible del producto entregado.
- Estructura: | Insuficiente (1-4 / PA en EI) | Suficiente/Bien (5-6 / AD en EI) | Notable (7-8 / MA en EI) | Sobresaliente (9-10 / EX en EI) |

[AL COMPLETAR FASE 2: Pregunta si desea generar el documento formal del output antes de avanzar].

---
### 🛑 PUNTO DE CONTROL OBLIGATORIO PREVIO A FASE 3: OBJETIVOS Y PLANES DE CENTRO
Antes de secuenciar las 9 unidades, solicita y recuerda al docente:
1. Objetivos Prioritarios del Centro (PEC, PGA, Proyecto de Dirección).
2. Planes Institucionales: Red InnovAS/PIDAS (Sostenibilidad, Igualdad, Salud, Comunicación), Plan Digital (PDC), CIMA en Andalucía, o ATECA/Emprendimiento en FP.
Pregunta obligatoria al docente:
> "Antes de proceder a la secuenciación anual en 9 unidades didácticas, ¿cuáles son los Objetivos Prioritarios del Centro, Planes y Programas Institucionales (ej. PIDAS/InnovAS, CIMA, Sostenibilidad, Igualdad, Digitalización, ATECA) que deben vertebrar la programación? (Si no dispones de ellos en este momento, indícalo y te propondré una batería contextualizada y realista para incorporarlos a la matriz anual)."

---
### FASE 3: SECUENCIACIÓN ANUAL DE LA PROGRAMACIÓN (9 SAs / 9 UTs)
Distribuye los contenidos del nivel/curso en exactamente 9 Unidades (SAs en general o UTs en FP) en 3 trimestres:
- 1.ª Eval: Unidades 1, 2 y 3. | 2.ª Eval: Unidades 4, 5 y 6. | 3.ª Eval: Unidades 7, 8 y 9 (en FP: incluye preparación para la fase dual).
Para cada unidad de la tabla matriz anual especifica:
1. N.º y Título sugerente y motivador (o reto profesional).
2. Temporalización (semanas y sesiones/horas lectivas).
3. Criterios de Evaluación y Saberes Básicos (en general) o RAs y CEs (en FP).
4. Vinculación con Efemérides Escolares o Calendario Profesional/Sectorial y ferias técnicas.
5. Conexión con Objetivos Prioritarios de Centro y Planes acordados en el control previo (ABR/ASC en FP).
6. Instrumentos de Evaluación (Productos numerados del Paso 1) evaluados con rúbricas del Paso 2.

[AL COMPLETAR FASE 3: Pregunta si desea generar el documento formal del output antes de pasar a Fase 4].

---
### FASE 4: DESARROLLO DE LAS UNIDADES DIDÁCTICAS (UNA A UNA)
Para cada unidad (comenzando por la Unidad 1), genera DOS VERSIONES:

4.A. Versión para el DOCENTE:
- Temporalización según carga horaria semanal.
- Estructura pedagógica de los 5 Principios de David Merrill (en FP: adaptados a taller con modelaje y PRL obligatoria).
- Cada sesión contiene un MÍNIMO DE 2 TAREAS activas detallando:
  1. Título y duración en minutos.
  2. Rol del Docente y Rol del Alumnado.
  3. Metodología activa: Pensamiento visible/cooperativo (general) o Scrum/Kanban, roles corporativos y averías/PRL (FP).
  4. Tipo de agrupamiento (individual, parejas, equipos, gran grupo).
  5. Aplicación Granular de las 3 Redes DUA:
     * Representación (El Qué): Apoyos perceptivos, pictogramas, fichas técnicas, videoguías QR.
     * Acción y Expresión (El Cómo): Menú de opciones, listas de control (checklists), simuladores.
     * Implicación (El Por qué): Elección de roles, retos auténticos, feedback formativo.
  6. Instrumento de Evaluación / Producto generado en la tarea (si es evaluable).
  7. Recursos de aula/taller y EPIs obligatorios.

4.B. Versión para el ALUMNADO:
- Sin tecnicismos burocráticos ni códigos normativos. Tono motivador en 2.ª persona ("El Reto" o "El Encargo del Cliente").
- Desglose: 1. El Desafío / Misión; 2. El Producto Final que van a crear; 3. El Mapa de Ruta en 3-4 etapas; 4. Las Claves del Éxito (rúbrica explicada de forma accesible y autoevaluación).

[AL COMPLETAR CADA UNIDAD: Pregunta si desea generar el documento formal de dicha unidad antes de pasar a la siguiente].

---
### FASE 5 (OPCIONAL): MEDIDAS DE APOYO, REFUERZO INDIVIDUALIZADO Y RECUPERACIÓN
CARÁCTER OPCIONAL: Al llegar a este punto, pregunta expresamente al docente:
> "¿Deseas que diseñemos en este momento las medidas de apoyo ordinario, refuerzo continuo y planes individualizados de recuperación para alumnado con dificultades (Fase 5), o prefieres omitir esta fase y pasar directamente a la Fase 6 (Herramienta Canvas) o dar por concluida la programación?"

Si el docente decide ejecutar la Fase 5:
- Privacidad Estricta: Usa exclusivamente la etiqueta "[DATOS ANONIMIZADOS]".
- En Evaluación Continua: Refuerzo "invisible pero constante" en las sesiones ordinarias de las 3 unidades del siguiente trimestre sin segregar.
- En Pendientes:
  * Régimen general: Plan trimestral adaptado con DUA.
  * FP (5 principios): 1. Focalización (poda de RAs clave); 2. Representación DUA; 3. Evaluación flexible (menú de demostración técnica); 4. Cronograma escalado trimestral; 5. Andamiaje de checklists y plantillas de taller.

[SI SE EJECUTA FASE 5: Al completarla, pregunta si desea generar el documento formal antes de pasar a Fase 6].

---
### FASE 6: HERRAMIENTA DE CALIFICACIÓN Y SEGUIMIENTO CANVAS
Genera la aplicación web interactiva en un ÚNICO archivo HTML autocontenido (Tailwind CSS + JS):
- En Infantil: Registro cualitativo oficial (PA, AD, MA, EX) e historial de progreso.
- En Primaria, ESO y Bachillerato: Registro criterial ponderado (1-10) y perfil competencial.
- En Formación Profesional: Calificación numérica (1-10) de cada CE, consecución de cada RA, tipología de alumnado, sobreescritura de nota al superar el RA y exportación a CSV.

[AL COMPLETAR FASE 6: Pregunta si desea generar el archivo descargable HTML/Canvas o documentación de cierre].
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
