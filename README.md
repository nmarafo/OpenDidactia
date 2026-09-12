# 🎓 OpenDidactia (Open Knowledge Framework - Didáctica y Currículo)

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC_BY--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/deed.es)
[![Framework: OKF](https://img.shields.io/badge/Framework-OKF_v1.0-blue.svg)](#arquitectura-okf)
[![Coverage: Canarias](https://img.shields.io/badge/Canarias-Infantil_|_Primaria_|_ESO_|_Bachillerato-green.svg)](#-comunidades-autónomas)

Base de conocimiento estructurada y abierta basada en el estándar **Open Knowledge Framework (OKF)** para la gestión, diseño y generación asistida por Inteligencia Artificial de **Programaciones Didácticas (PD)** y **Situaciones de Aprendizaje (SDA)** plenamente adaptadas a la LOMLOE y a la normativa autonómica.

Organizado por **Comunidades Autónomas**, comenzando con la cobertura completa de la **Comunidad Autónoma de Canarias** para **Educación Infantil, Primaria, Educación Secundaria Obligatoria (ESO) y Bachillerato** (incorporando la Formación Profesional en las siguientes fases).

---

## 🎯 Propósito del Proyecto

El objetivo de **OpenDidactia** es dotar a la comunidad educativa (docentes, centros, opositores e inspectores) y a los desarrolladores de herramientas educativas con IA de un marco unificado que permite:
1. **Garantizar la Trazabilidad Curricular:** Conectar de forma transparente los descriptores operativos del Perfil de Salida, las competencias clave y específicas, los criterios de evaluación y los saberes básicos.
2. **Aplicar el Diseño Universal para el Aprendizaje (DUA):** Proporcionar secuencias didácticas estructuradas en 4 fases competenciales libres de barreras de aprendizaje.
3. **Calificación Criterial Objetiva:** Facilitar el diseño de rúbricas graduadas en 4 niveles de desempeño asociadas a los criterios de evaluación de cada decreto autonómico.
4. **Alimentar Agentes de IA y Sistemas RAG:** Ofrecer esquemas JSON formales (`schema/`), metadatos en YAML frontmatter y prompts optimizados para generar documentos de programación rigurosos en segundos.

---

## 🔗 Sinergia con `nmarafo/open-lex-edu`

Este repositorio complementa y se apoya en el marco normativo de **[open-lex-edu](https://github.com/nmarafo/open-lex-edu)**:
* **open-lex-edu:** Proporciona el corpus legal completo, consolidado y auditado de la normativa educativa estatal y autonómica en formato OKF.
* **OpenDidactia:** Utiliza esa base jurídica para desarrollar la ingeniería didáctica, los catálogos curriculares, las matrices competenciales, los esquemas de validación y las herramientas operativas de aula.

---

## 📁 Estructura del Repositorio

```text
OpenDidactia/
├── README.md                            # Documento de bienvenida y arquitectura
├── LICENSE.md                           # Licencia CC BY-SA 4.0 y requisitos de atribución
├── .gitignore
├── schema/                              # Esquemas de validación formales (JSON Schema)
│   ├── norm_schema.json                 # Esquema OKF de disposiciones normativas (open-lex-edu)
│   ├── esquema_programacion_didactica.json # Validación de Programaciones Didácticas
│   └── esquema_situacion_aprendizaje.json  # Validación de Situaciones de Aprendizaje
├── docs/                                # Fundamentación teórica y metodológica
│   ├── arquitectura_okf.md              # Especificación del estándar OKF para didáctica
│   ├── taxonomia_curricular_lomloe.md   # Grafo curricular y relaciones competenciales
│   ├── guia_situaciones_aprendizaje.md  # Metodología DUA, fases y rúbricas en SDAs
│   └── guia_programaciones_didacticas.md# Planificación anual y concreción en PDs
├── plantillas/                          # Plantillas operativas y meta-prompts
│   ├── plantilla_situacion_aprendizaje.md  # Plantilla en blanco para SDAs
│   ├── plantilla_programacion_didactica.md # Plantilla en blanco para PDs
│   └── prompts/                         # Prompts del sistema para asistentes de IA
│       ├── prompt_generar_situacion_aprendizaje.md
│       └── prompt_generar_programacion_didactica.md
└── comunidades/                         # Implementación por Comunidades Autónomas
    └── canarias/                        # Comunidad Autónoma de Canarias
        ├── README.md                    # Singularidades del marco canario (contexto, DUA)
        ├── normativa/                   # Decretos oficiales con metadatos OKF
        │   ├── D196_2022_ordenacion_curriculo_educacion_infantil_canarias.md
        │   ├── D211_2022_ordenacion_curriculo_educacion_primaria_canarias.md
        │   └── D30_2023_ordenacion_curriculo_eso_bachillerato_canarias.md
        └── curricular/                  # Matrices de competencias, criterios y saberes
            ├── infantil/                # Perfil y las 3 áreas del 1.º y 2.º ciclo
            ├── primaria/                # Descriptores de salida y áreas de Primaria
            ├── eso/                     # Descriptores de salida y materias de 1.º a 4.º ESO
            └── bachillerato/            # Objetivos de etapa, modalidades y materias comunes
```

---

## 🏝️ Estado del Módulo: Canarias

La Comunidad Autónoma de Canarias cuenta con su marco curricular completamente integrado:

| Etapa Educativa | Decreto de Referencia | Publicación Oficial | Estado OKF |
| :--- | :--- | :---: | :---: |
| **Educación Infantil** | **Decreto 196/2022**, de 13 de octubre | BOC n.º 212 (26/10/2022) | **Completo (100%)** |
| **Educación Primaria** | **Decreto 211/2022**, de 10 de noviembre | BOC n.º 231 (23/11/2022) | **Completo (100%)** |
| **Educación Secundaria Obligatoria** | **Decreto 30/2023**, de 16 de marzo | BOC n.º 58 (23/03/2023) | **Completo (100%)** |
| **Bachillerato** | **Decreto 30/2023**, de 16 de marzo | BOC n.º 58 (23/03/2023) | **Completo (100%)** |
| **Formación Profesional (FP)** | Ley Orgánica 3/2022 y RD 659/2023 | En desarrollo | *Fase 2 (Próximamente)* |

---

## 🚀 Guía Rápida de Uso

### Para Docentes y Formadores
1. Para elaborar una **Situación de Aprendizaje**, consulta la [Guía Metodológica](docs/guia_situaciones_aprendizaje.md) y descarga la [Plantilla de SDA](plantillas/plantilla_situacion_aprendizaje.md).
2. Para elaborar tu **Programación Anual**, revisa la [Guía de Programaciones](docs/guia_programaciones_didacticas.md) y utiliza la [Plantilla de PD](plantillas/plantilla_programacion_didactica.md).
3. Localiza las competencias, criterios y saberes específicos de tu etapa en [comunidades/canarias/curricular/](comunidades/canarias/curricular/).

### Para Asistentes de IA y Agentes Autónomos
1. Copia el contenido del meta-prompt correspondiente en [plantillas/prompts/](plantillas/prompts/).
2. Alimenta el contexto del modelo con las competencias y criterios del área ubicados en `comunidades/canarias/curricular/`.
3. Valida la salida estructuralmente frente a los esquemas formales en `schema/`.

---

## 📄 Licencia y Atribución

Este repositorio y todos sus contenidos se distribuyen bajo los términos de la licencia **[Creative Commons Atribución-CompartirIgual 4.0 Internacional (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/deed.es)**.

### Cláusula de Atribución Obligatoria
En cualquier obra derivada, adaptación o integración en sistemas informáticos o de inteligencia artificial, **debe incluirse la siguiente mención explícita**:

> *Basado en los repositorios [OpenDidactia](https://github.com/nmarafo/OpenDidactia) y [open-lex-edu](https://github.com/nmarafo/open-lex-edu) creados por **Norberto Martín Afonso**, distribuidos bajo licencia Creative Commons Atribución-CompartirIgual 4.0 Internacional (CC BY-SA 4.0).*
