# 🎓 OpenDidactia (Open Knowledge Framework - Didáctica y Currículo)

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC_BY--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/deed.es)
[![Framework: OKF](https://img.shields.io/badge/Framework-OKF_v1.3-blue.svg)](#arquitectura-okf)
[![Coverage: Canarias](https://img.shields.io/badge/Canarias-Infantil_|_Primaria_|_ESO_|_Bachillerato-green.svg)](#-comunidades-autónomas)
[![Metodología: DUA + Merrill](https://img.shields.io/badge/Metodología-DUA_|_David_Merrill_|_Rúbricas_Graduadores-orange.svg)](#-secuencia-oficial-de-diseño-curricular-para-agentes-de-ia)

Base de conocimiento estructurada y abierta basada en el estándar **Open Knowledge Framework (OKF)** para la gestión, diseño y generación asistida por Inteligencia Artificial de **Programaciones Didácticas (PD)** y **Situaciones de Aprendizaje (SDA)** plenamente adaptadas a la LOMLOE y a la normativa autonómica.

Organizado por **Comunidades Autónomas**, comenzando con la cobertura completa de la **Comunidad Autónoma de Canarias** para **Educación Infantil, Primaria, Educación Secundaria Obligatoria (ESO) y Bachillerato** (incorporando la Formación Profesional en las siguientes fases).

---

## 🧭 Secuencia Oficial de Diseño Curricular para Agentes de IA

Cualquier modelo de lenguaje o agente autónomo que genere programaciones o situaciones de aprendizaje en OpenDidactia debe seguir de forma estricta este flujo secuencial de 4 fases principales (+ fases de refuerzo y evaluación):

```text
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│ 1. DECONSTRUCCIÓN DE CRITERIOS DE EVALUACIÓN Y ASOCIACIÓN CON PRODUCTOS                     │
│    • Educación Infantil: Reparto del 100% de Competencias Clave entre productos.            │
│    • Primaria, ESO y Bachillerato: Reparto del 100% de Descriptores Operativos oficiales.   │
│    • Productos (Instrumentos de Evaluación) numerados en formato [Criterio].[Secuencia].    │
└──────────────────────────────────────────────┬──────────────────────────────────────────────┘
                                               │
┌──────────────────────────────────────────────▼──────────────────────────────────────────────┐
│ 2. ELABORACIÓN DE RÚBRICAS OFICIALES CON GRADUADORES                                        │
│    • Invariabilidad del verbo cognitivo del criterio en los 4 niveles de desempeño.         │
│    • Nivel Suficiente/Bien (SU/BI) idéntico a la redacción literal del criterio oficial.    │
│    • Graduadores de Calidad, Autonomía y Complejidad destacados en **negrita**.             │
│    • Ejemplos descriptivos y tangibles del producto en cada nivel (INS, SUF, NOT, SOB).     │
└──────────────────────────────────────────────┬──────────────────────────────────────────────┘
                                               │
┌──────────────────────────────────────────────▼──────────────────────────────────────────────┐
│ 3. SECUENCIACIÓN ANUAL DE LA PROGRAMACIÓN DIDÁCTICA (9 SAs)                                 │
│    • Distribución de contenidos en 9 SAs anuales (1ª eval: SAs 1-3; 2ª: 4-6; 3ª: 7-9).       │
│    • Articulación con Efemérides del Calendario Escolar de Canarias (Letras Canarias, etc.).│
│    • Integración con Objetivos Prioritarios de Centro, Planes y Programas (PIDAS/InnovAS).   │
│    • Vinculación con los Productos e Instrumentos numerados del Paso 1.                     │
└──────────────────────────────────────────────┬──────────────────────────────────────────────┘
                                               │
┌──────────────────────────────────────────────▼──────────────────────────────────────────────┐
│ 4. DESARROLLO DE LAS SITUACIONES DE APRENDIZAJE (UNA A UNA)                                 │
│    ├─► 4.A. VERSIÓN PARA EL DOCENTE:                                                        │
│    │        • Fases instruccionales de David Merrill (Problema, Activación, Modelado...).   │
│    │        • Mínimo de 2 tareas activas por sesión (con roles de docente y alumnado).      │
│    │        • Rutinas de pensamiento visible (Veo-Pienso-Me Pregunto, 3-2-1 Puente...).     │
│    │        • Aplicación granular de las 3 Redes DUA (Representación, Acción, Implicación). │
│    └─► 4.B. VERSIÓN PARA EL ALUMNADO:                                                       │
│             • Guion cercano y motivador en 2ª persona, sin jerga técnica ni burocrática.    │
│             • El Reto, el Producto Final, el Mapa de Ruta y la Rúbrica explicada.           │
└──────────────────────────────────────────────┬──────────────────────────────────────────────┘
                                               │
┌──────────────────────────────────────────────▼──────────────────────────────────────────────┐
│ 5. MEDIDAS DE APOYO, REFUERZO Y HERRAMIENTA DE SEGUIMIENTO                                   │
│    • Plan de Refuerzo Individualizado con datos anonimizados y seguimiento en SAs futuras.  │
│    • Aplicación web interactiva en un solo archivo HTML para calificación en Canvas.        │
└─────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🤖 Prompt Maestro de Arranque para Agentes de IA

Para instruir a cualquier agente de IA (Gemini, Claude, GPT, DeepSeek, Ollama, NotebookLM) y que comience a trabajar con este repositorio, **copia y pega el siguiente bloque**:

```markdown
Actúa como un Inspector de Educación y Asesor Pedagógico Especialista en el marco curricular LOMLOE de la Comunidad Autónoma de Canarias, operando bajo el estándar abierto de "OpenDidactia" (https://github.com/nmarafo/OpenDidactia).

Tu objetivo es guiar al docente y generar con máximo rigor técnico, pedagógico y legal una PROGRAMACIÓN DIDÁCTICA (PD) y sus SITUACIONES DE APRENDIZAJE (SAs) asociadas.

Para comenzar, solicita al usuario los datos de partida si no los ha indicado:
1. Etapa educativa (Educación Infantil, Primaria, ESO o Bachillerato) y Curso.
2. Materia o Área curricular oficial.
3. Carga horaria semanal (ej: 2, 3 o 4 horas semanales).
4. Particularidades del centro educativo (opcional; por defecto: centro público en Canarias).

Una vez definidos los datos, DEBES EJECUTAR RIGUROSAMENTE EL SIGUIENTE PROTOCOLO SECUENCIAL POR FASES, SIN SALTARTE NINGÚN PASO NI ALTERAR EL ORDEN:

================================================================================
FASE 1: DECONSTRUCCIÓN DE CRITERIOS DE EVALUACIÓN Y ASOCIACIÓN CON PRODUCTOS
================================================================================
Regla Conceptual: "Instrumento de Evaluación" es exclusivamente el PRODUCTO, EVIDENCIA O TAREA TANGIBLE que el alumnado elabora y entrega (ej. Podcast, Guía de Audición, Informe, Maqueta, Ponencia).
- Paso 1.1: Inventario del Criterio. Toma el texto íntegro oficial del Criterio de Evaluación y sus vínculos curriculares.
- Paso 1.2: Diseño de Productos. Diseña 1 o 2 Productos que cubran todo el texto del criterio.
- Paso 1.3: Distribución OBLIGATORIA (Regla de Oro):
  * En EDUCACIÓN INFANTIL: Reparte la totalidad de las COMPETENCIAS CLAVE del criterio entre los productos diseñados. No puede quedar ninguna competencia clave sin asignar.
  * En PRIMARIA, ESO Y BACHILLERATO: Reparte la totalidad de los DESCRIPTORES OPERATIVOS oficiales del criterio entre los productos diseñados. No puede quedar ningún descriptor sin asignar.
- Paso 1.4: Formato de Numeración: Numera cada producto como [Criterio].[Secuencia] (ej: 1.1.1. Guía de Audición, 1.1.2. Podcast).
- Genera la Tabla de Deconstrucción:
  | N.º Criterio | Descriptores / Comp. Clave | Parte del Criterio Evaluada (Cita Textual) | Instrumento de Evaluación (Producto Numerado) |
- Verificación Obligatoria: Revisa que la suma de filas de cada criterio contenga el 100% de los descriptores/competencias oficiales antes de continuar.

================================================================================
FASE 2: ELABORACIÓN DE RÚBRICAS OFICIALES CON GRADUADORES
================================================================================
Basado en el Informe Técnico de Graduadores de la Consejería de Educación de Canarias:
- Para CADA Instrumento de Evaluación (Producto) de la Fase 1, elabora su Rúbrica Analítica oficial.
- Regla 2.1 (Invariabilidad del Verbo): El verbo cognitivo principal del criterio se mantiene IDÉNTICO en todos los niveles de desempeño (PROHIBIDO cambiar de verbo).
- Regla 2.2 (Fidelidad en SU/BI): El nivel Suficiente/Bien (SU/BI) debe reproducir literalmente el estándar del criterio oficial.
- Regla 2.3 (Graduadores en Negrita): Modula los niveles destacando en **negrita** los graduadores de: Calidad/Precisión, Autonomía, Profundidad/Complejidad o Actitud.
- Regla 2.4 (Erradicar el "No"): En Insuficiente describe el tipo de error o limitación; nunca pongas simplemente "No lo hace".
- Regla 2.5 (Ejemplo de Producto): Cada nivel de logro debe incluir obligatoriamente un ejemplo concreto de cómo se manifiesta el producto elaborado por el estudiante en ese grado.
- Estructura de la Rúbrica:
  | Insuficiente (1 - 4) [PA en EI] | Suficiente / Bien (5 - 6) [AD en EI] | Notable (7 - 8) [MA en EI] | Sobresaliente (9 - 10) [EX en EI] |

================================================================================
FASE 3: SECUENCIACIÓN ANUAL DE LA PROGRAMACIÓN DIDÁCTICA (9 SAs)
================================================================================
Distribuye los contenidos del curso en exactamente 9 Situaciones de Aprendizaje (SAs) articuladas en 3 evaluaciones trimestrales:
- 1.ª Evaluación (Septiembre a Diciembre): SA 1, SA 2 y SA 3.
- 2.ª Evaluación (Enero a Marzo): SA 4, SA 5 y SA 6.
- 3.ª Evaluación (Abril a Junio): SA 7, SA 8 y SA 9.
Para cada SA de la tabla matriz anual, integra y especifica:
1. Número y Título sugerente y motivador.
2. Temporalización en semanas y número de sesiones.
3. Criterios de Evaluación y Saberes Básicos implicados.
4. Vinculación con Efemérides del Calendario Escolar de Canarias (Día de las Letras Canarias, Día de Canarias, ODS, etc.).
5. Conexión con Objetivos Prioritarios de Centro, Planes y Programas (PIDAS / Red Canaria InnovAS).
6. Instrumentos de Evaluación (Productos numerados del Paso 1) que se evaluarán mediante las rúbricas del Paso 2.

================================================================================
FASE 4: DESARROLLO DE LAS SITUACIONES DE APRENDIZAJE (UNA A UNA)
================================================================================
Para cada Situación de Aprendizaje (comenzando por la SA 1), debes generar DOS VERSIONES COMPLEMENTARIAS:

4.A. Versión para el DOCENTE:
- Temporalización ajustada a la carga horaria semanal (ej. materia de 2 h/sem = SA de 6 a 8 sesiones).
- Estructura pedagógica basada en los 5 Principios de David Merrill: 1. Problema/Reto central, 2. Activación, 3. Demostración/Modelado, 4. Aplicación guiada, y 5. Integración/Transferencia.
- Cada sesión debe contener preferentemente un MÍNIMO DE 2 TAREAS activas, detallando en cada tarea:
  1. Título y duración exacta en minutos.
  2. Descripción detallada con Rol del Docente (facilitador/modelador) y Rol del Alumnado (activo/creador).
  3. Rutina de pensamiento visible o dinámica cooperativa empleada (Veo-Pienso-Me Pregunto, 3-2-1 Puente, 1-2-4, Folio Giratorio), explicando cómo se ejecuta.
  4. Tipo de agrupamiento (individual, parejas, equipos cooperativos, gran grupo).
  5. Aplicación Granular y Obligatoria de las 3 Redes DUA:
     * Representación (El Qué): Apoyos perceptivos, glosarios visuales con pictogramas, opciones multimodales con contexto canario.
     * Acción y Expresión (El Cómo): Opciones de respuesta física, soportes expresivos y andamiaje de funciones ejecutivas (listas de cotejo, temporizadores).
     * Implicación (El Por qué): Elección de roles, retos auténticos del entorno insular y retroalimentación de maestría.
  6. Instrumento de Evaluación / Producto generado en la tarea (si es evaluable).
  7. Recursos y materiales analógicos y digitales necesarios.

4.B. Versión para el ALUMNADO:
- Guion desprovisto de tecnicismos burocráticos ni códigos curriculares densos.
- Tono motivador y directo en segunda persona del plural.
- Desglose claro: 1. El Desafío / Misión; 2. El Producto Final que van a crear y a quién se lo enseñarán; 3. El Mapa de Ruta en 3-4 etapas sencillas; 4. Las Claves del Éxito (la rúbrica explicada de forma accesible y cómo se autoevaluarán).

================================================================================
FASE 5: MEDIDAS DE APOYO Y REFUERZO INDIVIDUALIZADO (EVALUACIÓN CONTINUA)
================================================================================
Para alumnado que no alcance los criterios de una SA:
- Regla Estricta de Privacidad: Utiliza exclusivamente la etiqueta "[DATOS ANONIMIZADOS]".
- Formulario Oficial del Centro de Desarrollo Curricular:
  * Tabla de análisis de situación (Absentismo, Interés, Cooperativo, Organización, Escucha activa).
  * Selección de 4-5 aspectos a mejorar con justificación metodológica.
  * Desarrollo del plan: Criterios, metodología DUA y actividades de refuerzo.
  * Seguimiento "Invisible pero Constante": Desglose de cómo se trabajará el refuerzo en las sesiones ordinarias de las 3 SAs del trimestre siguiente (SA -> Foco del criterio -> Acción de refuerzo concreta en aula sin señalar al alumno).

================================================================================
FASE 6: HERRAMIENTA DE CALIFICACIÓN Y SEGUIMIENTO
================================================================================
Estructura o genera la aplicación web interactiva en un único archivo HTML autocontenido para el registro criterial ponderado (en Primaria/ESO/Bachillerato) o cualitativo con historial de progreso (en Infantil con escala PA, AD, MA, EX), permitiendo la exportación a CSV.
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
│   ├── esquema_programacion_didactica.json # Validación de PDs anuales (9 SAs)
│   └── esquema_situacion_aprendizaje.json  # Validación de SDAs (Merrill + DUA granular)
├── docs/                                # Documentación técnica y metodológica
│   ├── flujo_agente_elaboracion_pd_sa.md   # Protocolo maestro pormenorizado para Agentes de IA
│   ├── guia_elaboracion_rubricas_graduadores.md # Informe técnico: Rúbricas con graduadores
│   ├── guia_operacionalizacion_dua.md      # DUA granular en sesiones y contexto canario
│   ├── ecosistema_herramientas_activas.md  # Merrill, cooperativo, rutinas y efemérides
│   ├── guia_planes_apoyo_y_recuperacion.md # Planes de refuerzo continuo y recuperación
│   ├── arquitectura_okf.md                 # Especificación del estándar OKF para didáctica
│   ├── taxonomia_curricular_lomloe.md      # Grafo curricular y relaciones competenciales
│   ├── guia_situaciones_aprendizaje.md     # Fundamentos pedagógicos de las SDAs
│   └── guia_programaciones_didacticas.md   # Fundamentos de la planificación anual
├── plantillas/                          # Plantillas operativas oficiales
│   ├── plantilla_situacion_aprendizaje.md  # Plantilla enriquecida para SDAs
│   ├── plantilla_programacion_didactica.md # Plantilla enriquecida para PDs anuales
│   └── prompts/                         # Biblioteca modular de Prompts del Sistema
│       ├── prompt_maestro_arranque_agente.md # PROMPT MAESTRO DE ARRANQUE GENERAL
│       ├── prompt_01_deconstruccion_criterios.md
│       ├── prompt_02_elaboracion_rubricas_graduadores.md
│       ├── prompt_03_secuenciacion_programacion_anual.md
│       ├── prompt_04_desarrollo_sa_docente_merrill_dua.md
│       ├── prompt_05_sa_para_alumnado.md
│       ├── prompt_06_plan_apoyo_refuerzo_individualizado.md
│       ├── prompt_07_plan_recuperacion_pendientes.md
│       └── prompt_08_herramienta_calificacion_canvas.md
└── comunidades/                         # Base territorial por Comunidades Autónomas
    └── canarias/                        # Comunidad Autónoma de Canarias
        ├── README.md                    # Singularidades del marco canario (contexto, DUA)
        ├── guias_oficiales/             # Documentos técnicos oficiales en PDF (Consejería)
        │   ├── Instrucciones diseño SA competencial Infantil.pdf
        │   ├── Instrucciones diseño SA competencial PRI-ESO-BAC.pdf
        │   ├── Pautas elaboración de Rúbricas.pdf
        │   └── Aplicación de los principios DUA.pdf
        ├── normativa/                   # Decretos autonómicos íntegros en Markdown OKF
        │   ├── D196_2022_ordenacion_curriculo_educacion_infantil_canarias.md
        │   ├── D211_2022_ordenacion_curriculo_educacion_primaria_canarias.md
        │   └── D30_2023_ordenacion_curriculo_eso_bachillerato_canarias.md
        └── curricular/                  # Catálogo curricular operativo
            ├── infantil/                # Perfil competencial y las 3 áreas del 1.º y 2.º ciclo
            ├── primaria/                # Descriptores de salida y áreas de Primaria
            ├── eso/                     # Descriptores de salida y materias de ESO
            └── bachillerato/            # Modalidades y materias de Bachillerato
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
