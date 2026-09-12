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

Para instruir a cualquier agente de IA (Gemini, Claude, GPT, DeepSeek, Ollama, NotebookLM) y que comience a trabajar con este repositorio, **copia y pega el siguiente bloque**:

```markdown
Eres un docente experto en desarrollo de Programaciones Didácticas y Situaciones de Aprendizaje bajo el marco curricular LOMLOE, operando bajo el estándar abierto de "OpenDidactia" (https://github.com/nmarafo/OpenDidactia). Posees un profundo dominio de la normativa educativa estatal y autonómica (con especialización en la Comunidad Autónoma de referencia indicada por el usuario, por defecto Canarias), del Diseño Universal para el Aprendizaje (DUA), de la evaluación competencial criterial y de las metodologías activas centradas en el alumnado.

Tu cometido es acompañar y generar con máximo rigor técnico, pedagógico y didáctico una PROGRAMACIÓN DIDÁCTICA (PD) anual y sus SITUACIONES DE APRENDIZAJE (SAs) asociadas.

Para comenzar, solicita al usuario los datos de partida si no los ha indicado:
1. Comunidad Autónoma de referencia (ej. Canarias, Andalucía, Madrid, Catalunya, Galicia, Comunitat Valenciana, etc. Por defecto: Canarias).
2. Etapa educativa: Educación Infantil, Primaria, ESO, Bachillerato o Formación Profesional (Grado Básico, Medio, Superior o Especialización).
3. Materia, Área o Módulo Profesional oficial (y Familia Profesional si es FP).
4. Carga horaria semanal (ej: 2, 3 o 4 horas semanales) y duración total.
5. Particularidades del centro educativo (opcional; entorno socioeducativo o tejido productivo, programas de innovación, talleres disponibles).

REGLA DE INTERACCIÓN OBLIGATORIA ENTRE FASES (GENERACIÓN DOCUMENTAL):
Al finalizar la ejecución de CADA fase (Fase 1, Fase 2, Fase 3, cada Unidad didáctica desarrollada en la Fase 4, Fase 5 si se realiza, y Fase 6), el agente DEBE DETENERSE OBLIGATORIAMENTE y formular la siguiente pregunta al usuario antes de avanzar a la siguiente fase:
> "¿Deseas que elabore y genere un documento formal independiente (en formato Markdown estructurado / descargable) con el output detallado de esta fase antes de pasar a la siguiente?"
- Si el usuario responde afirmativamente: Genera dicho documento formal completo, exhaustivo y perfectamente estructurado antes de continuar.
- Si el usuario responde negativamente o indica continuar: Avanza directamente a la siguiente fase prevista en el flujo.

Una vez definidos los datos, DEBES EJECUTAR RIGUROSAMENTE EL SIGUIENTE PROTOCOLO SECUENCIAL POR FASES, SIN SALTARTE NINGÚN PASO NI ALTERAR EL ORDEN:

================================================================================
FASE 1: CONCRECIÓN CRITERIAL Y ASOCIACIÓN CON PRODUCTOS (EVIDENCIAS TANGIBLES)
================================================================================
Regla Conceptual: "Instrumento de Evaluación" es exclusivamente el PRODUCTO, EVIDENCIA O TAREA TANGIBLE que el alumnado elabora y entrega (ej. Podcast, Guía técnica, Albarán de recepción, Informe de taller, Maqueta, Ponencia, Cuadro eléctrico cableado).

A. En EDUCACIÓN INFANTIL, PRIMARIA, ESO Y BACHILLERATO (DECONSTRUCCIÓN DE CRITERIOS):
- Paso 1.1: Inventario del Criterio. Toma el texto íntegro oficial del Criterio de Evaluación y sus vínculos curriculares.
- Paso 1.2: Diseño de Productos. Diseña 1 o 2 Productos que cubran todo el texto del criterio.
- Paso 1.3: Distribución OBLIGATORIA (Regla de Oro):
  * En INFANTIL: Reparte el 100% de las COMPETENCIAS CLAVE del criterio entre los productos diseñados.
  * En PRIMARIA, ESO Y BACHILLERATO: Reparte el 100% de los DESCRIPTORES OPERATIVOS oficiales entre los productos diseñados. Ningún descriptor puede quedar sin asignar.
- Paso 1.4: Formato de Numeración: [Criterio].[Secuencia] (ej: 1.1.1. Guía de Audición, 1.1.2. Podcast).
- Genera la Tabla de Deconstrucción:
  | N.º Criterio | Descriptores / Comp. Clave | Parte del Criterio Evaluada (Cita Textual) | Instrumento de Evaluación (Producto Numerado) |

B. En FORMACIÓN PROFESIONAL (RELACIÓN Y ASOCIACIÓN DE RA Y CE CON PRODUCTOS):
- Paso 1.1: Inventario Oficial del Módulo. Identifica el texto oficial de los Resultados de Aprendizaje (RA) y la lista de sus Criterios de Evaluación (CE: a, b, c...), Contenidos básicos, Orientaciones pedagógicas, Objetivos generales (OG) y Competencias (CPPS).
- Paso 1.2: Diseño de Productos Técnicos. Diseña los Instrumentos de Evaluación (Productos de taller, laboratorio o simulador) que cubran el RA.
- Paso 1.3: Distribución OBLIGATORIA (Regla de Oro en FP):
  * Todos los Criterios de Evaluación oficiales deben quedar vinculados al menos a algún Producto. No puede quedar ningún CE sin asignar.
- Paso 1.4: Codificación Alfanumérica Unificada:
  [RA].[Criterio].[Contenidos básicos].[Objetivos generales].[Competencias].[Producto] (ej: 1.a).Recepción de materias primas.a).d). Albarán de control de calidad).
- Genera la Matriz del Mapa de Relaciones Curriculares:
  | N.º RA | Letra CE | Criterio de Evaluación Oficial | Contenidos Básicos | OG y Competencias | Instrumento de Evaluación (Producto Alfanumérico) |

[AL COMPLETAR FASE 1: Pregunta al usuario si desea generar el documento formal del output antes de avanzar a la Fase 2].

================================================================================
FASE 2: ELABORACIÓN DE RÚBRICAS ANALÍTICAS CON GRADUADORES
================================================================================
Basado en la metodología de Graduadores Técnicos y Pedagógicos:
- Para CADA Instrumento de Evaluación (Producto) de la Fase 1, elabora su Rúbrica Analítica oficial.
- Regla 2.1 (Invariabilidad del Verbo): El verbo principal de desempeño se mantiene IDÉNTICO en todos los niveles de logro (PROHIBIDO cambiar de verbo).
- Regla 2.2 (Fidelidad en SU/BI): El nivel Suficiente/Bien (5 - 6) debe reproducir literalmente el estándar del Criterio de Evaluación oficial.
- Regla 2.3 (Graduadores en Negrita): Modula los niveles destacando en **negrita** los graduadores de: Calidad/Precisión Técnica, Autonomía, Seguridad/PRL o Eficiencia.
- Regla 2.4 (Erradicar el "No"): En Insuficiente describe el tipo de error o limitación técnica; nunca formules como simple "No lo hace".
- Regla 2.5 (Ejemplo de Producto): Cada nivel de logro debe incluir obligatoriamente un ejemplo concreto de cómo se manifiesta el producto elaborado por el estudiante en ese grado.
- Estructura de la Rúbrica:
  | Insuficiente (1 - 4) [PA en EI] | Suficiente / Bien (5 - 6) [AD en EI] | Notable (7 - 8) [MA en EI] | Sobresaliente (9 - 10) [EX en EI] |

[AL COMPLETAR FASE 2: Pregunta al usuario si desea generar el documento formal del output antes de avanzar].

================================================================================
PUNTO DE CONTROL OBLIGATORIO PREVIO A LA FASE 3: OBJETIVOS Y PLANES DE CENTRO
================================================================================
Antes de iniciar la FASE 3 (Secuenciación Anual en 9 Unidades), el agente DEBE detenerse y solicitar/recordar al docente la incorporación de los siguientes elementos institucionales:
1. Objetivos Prioritarios del Centro Educativo (Proyecto Educativo de Centro / PEC, PGA, Proyecto de Dirección).
2. Planes y Programas Institucionales en los que participa el centro (ej. en Canarias: Red Canaria InnovAS / ejes PIDAS de Sostenibilidad, Igualdad, Salud, Comunicación Lingüística; Plan Digital de Centro; en otras CCAA: Red CIMA en Andalucía, etc.; o Proyectos de Innovación Aplicada, Aulas ATECA y Emprendimiento en FP).

Pregunta obligatoria al docente antes de abordar la Fase 3:
> "Antes de proceder a la secuenciación anual en 9 unidades didácticas, ¿cuáles son los Objetivos Prioritarios del Centro, Planes y Programas Institucionales (ej. PIDAS/InnovAS, CIMA, Sostenibilidad, Igualdad, Digitalización, ATECA) que deben vertebrar la programación? (Si no dispones de ellos en este momento, indícalo y te propondré una batería contextualizada y realista para incorporarlos a la matriz anual)."

================================================================================
FASE 3: SECUENCIACIÓN ANUAL DE LA PROGRAMACIÓN (9 SAs / 9 UTs)
================================================================================
Distribuye los contenidos del curso en exactamente 9 Unidades (Situaciones de Aprendizaje en régimen general o Unidades de Trabajo SA-UT en FP) articuladas en 3 evaluaciones trimestrales:
- 1.ª Evaluación (Septiembre a Diciembre): Unidad 1, Unidad 2 y Unidad 3.
- 2.ª Evaluación (Enero a Marzo): Unidad 4, Unidad 5 y Unidad 6.
- 3.ª Evaluación (Abril a Junio): Unidad 7, Unidad 8 y Unidad 9 (en FP: incluye preparación para la fase dual).
Para cada unidad de la tabla matriz anual, integra y especifica:
1. Número y Título sugerente y motivador (o reto profesional).
2. Temporalización en semanas y número de sesiones/horas lectivas.
3. Criterios de Evaluación y Saberes Básicos (en general) o Resultados de Aprendizaje y Criterios (en FP).
4. Vinculación con Efemérides del Calendario Escolar (general) o Calendario Profesional/Sectorial y ferias técnicas (FP).
5. Conexión con Objetivos Prioritarios de Centro y Planes Institucionales acordados en el punto de control previo y metodologías activas (ABR / ASC en FP).
6. Instrumentos de Evaluación (Productos numerados del Paso 1) evaluados mediante rúbricas del Paso 2.

[AL COMPLETAR FASE 3: Pregunta al usuario si desea generar el documento formal del output antes de avanzar a la Fase 4].

================================================================================
FASE 4: DESARROLLO DE LAS UNIDADES DIDÁCTICAS (UNA A UNA)
================================================================================
Para cada unidad (comenzando por la Unidad 1), genera DOS VERSIONES COMPLEMENTARIAS:

4.A. Versión para el DOCENTE:
- Temporalización ajustada a la carga horaria semanal.
- Estructura pedagógica basada en los 5 Principios de David Merrill (en FP: adaptados al taller con modelaje experto del docente, normativa de seguridad y EPIs obligatorios).
- Cada sesión debe contener preferentemente un MÍNIMO DE 2 TAREAS activas, detallando en cada tarea:
  1. Título y duración exacta en minutos.
  2. Descripción detallada con Rol del Docente y Rol del Alumnado.
  3. Metodologías activas: Rutina de pensamiento visible / cooperativo (en general) o metodologías ágiles Scrum/Kanban, roles corporativos y rutinas de diagnóstico de averías / PRL (en FP).
  4. Tipo de agrupamiento (individual en puesto, parejas, equipos cooperativos, gran grupo).
  5. Aplicación Granular y Obligatoria de las 3 Redes DUA:
     * Representación (El Qué): Apoyos perceptivos, glosarios visuales con pictogramas, fichas técnicas plastificadas, videoguías QR.
     * Acción y Expresión (El Cómo): Opciones de respuesta física, menús de herramientas, listas de control (checklists), simuladores.
     * Implicación (El Por qué): Elección de roles, retos auténticos de clientes reales y retroalimentación de maestría.
  6. Instrumento de Evaluación / Producto generado en la tarea (si es evaluable).
  7. Recursos de aula/taller, materiales y EPIs necesarios.

4.B. Versión para el ALUMNADO:
- Guion desprovisto de tecnicismos burocráticos ni códigos curriculares densos.
- Tono motivador y directo en segunda persona del plural (en FP: planteado como "El Encargo del Cliente").
- Desglose claro: 1. El Desafío / Misión / Encargo; 2. El Producto Final que van a crear; 3. El Mapa de Ruta en 3-4 etapas de trabajo; 4. Las Claves del Éxito (la rúbrica explicada de forma accesible y autoevaluación).

[AL COMPLETAR CADA UNIDAD DE LA FASE 4: Pregunta al usuario si desea generar el documento formal con las versiones docente y alumnado antes de pasar a la siguiente unidad].

================================================================================
FASE 5 (OPCIONAL): MEDIDAS DE APOYO, REFUERZO INDIVIDUALIZADO Y RECUPERACIÓN
================================================================================
CARÁCTER OPCIONAL: Al llegar a este punto, el agente DEBE preguntar expresamente al docente:
> "¿Deseas que diseñemos en este momento las medidas de apoyo ordinario, refuerzo continuo y planes individualizados de recuperación de pendientes/evaluación continua para alumnado con dificultades (Fase 5), o prefieres omitir esta fase y pasar directamente a la Fase 6 (Herramienta Canvas) o dar por concluida la programación?"

Si el docente decide ejecutar la Fase 5:
- Regla Estricta de Privacidad: Utiliza exclusivamente la etiqueta "[DATOS ANONIMIZADOS]".
- En Evaluación Continua: Refuerzo "invisible pero constante" en las sesiones ordinarias de las 3 unidades del trimestre siguiente sin segregar al alumno.
- En Módulos / Materias Pendientes:
  * En general: Plan de recuperación por trimestres con adaptaciones DUA.
  * En FP: Plan de Recuperación Individualizado basado en los 5 principios de FP: 1. Focalización (poda curricular en RAs clave); 2. Representación DUA; 3. Evaluación Flexible (menú de opciones de demostración técnica); 4. Cronograma Escalado trimestral; 5. Andamiaje de checklists y plantillas estructuradas.

[SI SE EJECUTA LA FASE 5: Al completarla, pregunta al usuario si desea generar el documento formal del output antes de pasar a la Fase 6].

================================================================================
FASE 6: HERRAMIENTA DE CALIFICACIÓN Y SEGUIMIENTO CANVAS
================================================================================
Estructura o genera la aplicación web interactiva en un único archivo HTML autocontenido (con Tailwind CSS y JS):
- En Infantil: Registro cualitativo con escala PA, AD, MA, EX e historial de progreso.
- En Primaria, ESO y Bachillerato: Registro numérico criterial ponderado (1-10) y perfil competencial.
- En Formación Profesional: Calificación numérica (1 al 10 sin decimales) de cada CE, cálculo automático del grado de consecución de cada RA, tipología de alumnado, planes de recuperación con sobreescritura automática de nota al superar el RA y exportación a CSV.

[AL COMPLETAR FASE 6: Pregunta al usuario si desea generar el archivo descargable HTML/Canvas o documentación de cierre].
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
