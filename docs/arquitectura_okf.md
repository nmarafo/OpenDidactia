# 🏛️ Arquitectura del Open Knowledge Framework (OKF) en OpenDidactia

El **Open Knowledge Framework (OKF)** en **OpenDidactia** es una especificación estructurada y estandarizada diseñada para organizar el corpus curricular y normativo de la educación en España, optimizado tanto para la consulta por profesionales de la educación como para su procesamiento por **Sistemas RAG (Retrieval-Augmented Generation)** y **Agentes de Inteligencia Artificial**.

---

## 1. Propósito y Filosofía

Tradicionalmente, las normativas y currículos educativos se publican en extensos boletines oficiales (BOC, BOE, BOCM, BOJA) en formatos PDF no estructurados, lo que dificulta la automatización, la extracción de competencias y la elaboración ágil de documentos docentes.

El framework **OKF** resuelve esta barrera al:
1. **Estructurar la información en Markdown limpio y modular**, eliminando el ruido burocrático.
2. **Incorporar metadatos enriquecidos en YAML Frontmatter** que permiten el filtrado semántico y la indexación determinista.
3. **Ofrecer esquemas JSON Schema formales** para validar que las Programaciones Didácticas (PD) y Situaciones de Aprendizaje (SDA) generadas cumplan rigurosamente la legalidad vigente.
4. **Facilitar la trazabilidad curricular:** desde las competencias clave y los descriptores operativos del perfil de salida hasta los criterios de evaluación y los saberes básicos de cada materia y comunidad autónoma.

---

## 2. Taxonomía de Directorios

El repositorio sigue un patrón simétrico, jerárquico y escalable:

```text
OpenDidactia/
├── README.md                            # Guía principal del repositorio y acceso rápido
├── LICENSE.md                           # Licencia CC BY-SA 4.0
├── schema/                              # Esquemas formales JSON Schema
│   ├── norm_schema.json                 # Esquema OKF de disposiciones normativas (open-lex-edu)
│   ├── esquema_programacion_didactica.json # Validación de Programaciones Didácticas
│   └── esquema_situacion_aprendizaje.json  # Validación de Situaciones de Aprendizaje
├── docs/                                # Base teórica, metodológica y taxonómica
│   ├── arquitectura_okf.md              # Este documento
│   ├── guia_situaciones_aprendizaje.md  # Metodología DUA, fases y rúbricas
│   ├── guia_programaciones_didacticas.md# Planificación anual y concreción
│   └── taxonomia_curricular_lomloe.md   # Mapeo de elementos curriculares
├── plantillas/                          # Plantillas operativas y prompts de IA
│   ├── plantilla_programacion_didactica.md
│   ├── plantilla_situacion_aprendizaje.md
│   └── prompts/
│       ├── prompt_generar_situacion_aprendizaje.md
│       └── prompt_generar_programacion_didactica.md
└── comunidades/                         # Implementación por Comunidades Autónomas
    └── canarias/                        # Comunidad Autónoma de Canarias
        ├── README.md                    # Peculiaridades del sistema canario (DUA, contexto)
        ├── normativa/                   # Textos íntegros de los decretos curriculares
        └── curricular/                  # Matrices de competencias, criterios y saberes
            ├── infantil/
            ├── primaria/
            ├── eso/
            └── bachillerato/
```

---

## 3. Especificación del Frontmatter de Documentos Normativos

Siguiendo el estándar fijado en [nmarafo/open-lex-edu](https://github.com/nmarafo/open-lex-edu), cada disposición normativa cuenta con un encabezado YAML con los siguientes campos:

```yaml
---
id: norm-can-d-30-2023
codigo_sintetizado: D30_2023 Ordenacion y Curriculo de ESO y Bachillerato en Canarias
titulo: Decreto 30/2023, de 16 de marzo, por el que se establece la ordenación y el currículo de la Educación Secundaria Obligatoria y del Bachillerato en la Comunidad Autónoma de Canarias.
jurisdiccion: Canarias
ambito: Autonómico
organo_emisor: Gobierno de Canarias / Consejería de Educación, Universidades, Cultura y Deportes
tipo_disposicion: Decreto
numero_disposicion: 30/2023
fecha_disposicion: '2023-03-16'
fecha_publicacion: '2023-03-23'
boletin: BOC
numero_boletin: '58'
estado: Vigente
redaccion: texto_integro_boc
fuente_oficial: https://www.gobiernodecanarias.org/boc/2023/058/001.html
fuente_pdf_oficial: https://sede.gobiernodecanarias.org/boc/boc-a-2023-058-848.pdf
fuente_juriscan: https://www.gobiernodecanarias.org/juriscan/ficha.jsp?id=82361
clasificacion:
  categoria_canonica: 03_ordenacion_curricular_y_ensenanzas
  subcategoria: Educación Secundaria Obligatoria y Bachillerato
tags:
  - educacion-secundaria-obligatoria
  - bachillerato
  - curriculo-eso
  - curriculo-bachillerato
  - situaciones-aprendizaje
  - lomloe
relaciones:
  fundamentado_en:
    - norma_id: norm-es-c-1978
    - norma_id: norm-can-lo-1-2018
    - norma_id: norm-es-lo-2-2006
    - norma_id: norm-can-l-6-2014
  desarrolla:
    - norma_id: norm-es-rd-217-2022
    - norma_id: norm-es-rd-243-2022
---
```

---

## 4. Consumo por Agentes de IA y Sistemas RAG

Para utilizar este repositorio en arquitecturas de generación aumentada por recuperación:
1. **Localización de la Norma:** El agente consulta `comunidades/<comunidad>/normativa/` para extraer el marco legal y las directrices pedagógicas de la etapa.
2. **Inyección de Elementos Curriculares:** El agente extrae de `comunidades/<comunidad>/curricular/<etapa>/` las competencias específicas, los criterios de evaluación exactos y los bloques de saberes básicos.
3. **Estructuración Asistida:** El agente utiliza los esquemas JSON (`schema/`) y las plantillas Markdown (`plantillas/`) para estructurar la respuesta, garantizando que incluya todas las fases DUA, las rúbricas graduadas y la contextualización autonómica requerida.
