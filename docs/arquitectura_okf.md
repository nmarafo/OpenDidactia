# 🏛️ Arquitectura del Open Knowledge Framework (OKF) en OpenDidactia

El **Open Knowledge Framework (OKF)** en **OpenDidactia** es una especificación estructurada, estandarizada y modular diseñada para organizar el corpus curricular, metodológico y normativo de la educación en España, optimizado tanto para la consulta por profesionales de la educación como para su procesamiento por **Sistemas RAG (Retrieval-Augmented Generation)** y **Agentes de Inteligencia Artificial**.

---

## 1. Propósito y Filosofía

Tradicionalmente, las normativas y currículos educativos se publican en extensos boletines oficiales (BOC, BOE, BOCM, BOJA) en formatos PDF no estructurados, lo que dificulta la automatización, la extracción de competencias y la elaboración ágil de documentos docentes.

El framework **OKF** resuelve esta barrera al:
1. **Estructurar la información en Markdown limpio y modular**, eliminando el ruido burocrático y manteniendo la fidelidad legal.
2. **Incorporar metadatos enriquecidos en YAML Frontmatter** que permiten el filtrado semántico, la indexación determinista y la vinculación con el marco normativo de [open-lex-edu](https://github.com/nmarafo/open-lex-edu).
3. **Ofrecer esquemas formales (JSON Schema)** para validar que las Programaciones Didácticas (PD) y Situaciones de Aprendizaje (SDA) generadas cumplan rigurosamente la normativa vigente y los estándares metodológicos.
4. **Implementar el Protocolo Oficial Canario en 9 Pasos**: Guiar a los agentes de IA en la deconstrucción de criterios, diseño de productos numerados, elaboración de rúbricas con graduadores, aplicación de las fases de David Merrill, operacionalización granular del DUA y diseño de planes de refuerzo y recuperación.

---

## 2. Taxonomía Integral de Directorios

```text
OpenDidactia/
├── README.md                            # Guía principal del repositorio y protocolo de 9 pasos
├── LICENSE.md                           # Licencia CC BY-SA 4.0 y cláusula de atribución
├── .gitignore
├── schema/                              # Esquemas formales JSON Schema
│   ├── norm_schema.json                 # Esquema OKF de disposiciones normativas (open-lex-edu)
│   ├── esquema_programacion_didactica.json # Validación de PDs anuales (9 SAs)
│   └── esquema_situacion_aprendizaje.json  # Validación de SDAs (Merrill + DUA granular)
├── docs/                                # Base teórica, metodológica y guías técnicas
│   ├── flujo_agente_elaboracion_pd_sa.md   # Protocolo maestro de 9 pasos para Agentes de IA
│   ├── catalogo_rutinas_pensamiento_y_dinamicas_grupo.md # Base de conocimiento: Pensamiento visible y cooperativo
│   ├── catalogo_metodologias_aprendizaje.md # Base de conocimiento: Metodologías activas (ABP, ApS, Design Thinking...)
│   ├── guia_elaboracion_rubricas_graduadores.md # Rúbricas con graduadores y ejemplos
│   ├── guia_operacionalizacion_dua.md      # DUA granular en sesiones y contexto canario
│   ├── ecosistema_herramientas_activas.md  # Merrill, cooperativo, rutinas y efemérides
│   ├── guia_planes_apoyo_y_recuperacion.md # Planes de refuerzo continuo y recuperación
│   ├── arquitectura_okf.md                 # Este documento
│   ├── taxonomia_curricular_lomloe.md      # Grafo curricular y relaciones competenciales
│   ├── guia_situaciones_aprendizaje.md     # Metodología DUA, fases y rúbricas en SDAs
│   └── guia_programaciones_didacticas.md   # Planificación anual y concreción en PDs
├── plantillas/                          # Plantillas operativas y biblioteca de prompts
│   ├── plantilla_situacion_aprendizaje.md  # Plantilla enriquecida para SDAs
│   ├── plantilla_programacion_didactica.md # Plantilla enriquecida para PDs
│   └── prompts/                         # Prompts del sistema modulares para IA
│       ├── prompt_01_deconstruccion_criterios.md
│       ├── prompt_02_elaboracion_rubricas_graduadores.md
│       ├── prompt_03_secuenciacion_programacion_anual.md
│       ├── prompt_04_desarrollo_sa_docente_merrill_dua.md
│       ├── prompt_05_sa_para_alumnado.md
│       ├── prompt_06_plan_apoyo_refuerzo_individualizado.md
│       ├── prompt_07_plan_recuperacion_pendientes.md
│       └── prompt_08_herramienta_calificacion_canvas.md
└── comunidades/                         # Implementación por Comunidades Autónomas
    └── canarias/                        # Comunidad Autónoma de Canarias
        ├── README.md                    # Singularidades del sistema canario (DUA, contexto)
        ├── guias_oficiales/             # Documentos técnicos oficiales de la Consejería (PDF)
        ├── normativa/                   # Decretos oficiales íntegros con metadatos OKF
        │   ├── D196_2022_ordenacion_curriculo_educacion_infantil_canarias.md
        │   ├── D211_2022_ordenacion_curriculo_educacion_primaria_canarias.md
        │   └── D30_2023_ordenacion_curriculo_eso_bachillerato_canarias.md
        └── curricular/                  # Matrices de competencias, criterios y saberes
            ├── infantil/
            ├── primaria/
            ├── eso/
            └── bachillerato/
```

---

## 3. Consumo por Agentes de IA y Sistemas RAG

Cuando un Agente de IA deba elaborar una Programación Didáctica o una Situación de Aprendizaje para Canarias:
1. **Paso Inicial:** Carga [flujo_agente_elaboracion_pd_sa.md](flujo_agente_elaboracion_pd_sa.md) para comprender la secuencia completa.
2. **Fase de Deconstrucción:** Ejecuta el prompt [prompt_01_deconstruccion_criterios.md](../plantillas/prompts/prompt_01_deconstruccion_criterios.md), cruzando los criterios de `comunidades/canarias/curricular/` para producir la tabla de instrumentos (productos).
3. **Fase de Rúbricas:** Consulta [guia_elaboracion_rubricas_graduadores.md](guia_elaboracion_rubricas_graduadores.md) y ejecuta [prompt_02_elaboracion_rubricas_graduadores.md](../plantillas/prompts/prompt_02_elaboracion_rubricas_graduadores.md).
4. **Fase de Secuenciación:** Aplica [catalogo_metodologias_aprendizaje.md](catalogo_metodologias_aprendizaje.md) y [prompt_03_secuenciacion_programacion_anual.md](../plantillas/prompts/prompt_03_secuenciacion_programacion_anual.md) para asignar a cada SA su metodología activa rectora y estructurar la matriz anual de 9 SAs.
5. **Fase de Diseño de Sesión:** Aplica [catalogo_rutinas_pensamiento_y_dinamicas_grupo.md](catalogo_rutinas_pensamiento_y_dinamicas_grupo.md), [guia_operacionalizacion_dua.md](guia_operacionalizacion_dua.md), [ecosistema_herramientas_activas.md](ecosistema_herramientas_activas.md) y [prompt_04_desarrollo_sa_docente_merrill_dua.md](../plantillas/prompts/prompt_04_desarrollo_sa_docente_merrill_dua.md) para generar las sesiones Merrill integrando dinámicas y rutinas procedimentadas con DUA granular en tareas.
6. **Fase de Comunicación al Alumnado:** Aplica [prompt_05_sa_para_alumnado.md](../plantillas/prompts/prompt_05_sa_para_alumnado.md).
7. **Fase de Inclusión y Refuerzo:** Consulta [guia_planes_apoyo_y_recuperacion.md](guia_planes_apoyo_y_recuperacion.md) y aplica los prompts de apoyo y recuperación con datos rigurosamente anonimizados.
