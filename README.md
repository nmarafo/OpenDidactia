# 🎓 OpenDidactia (Open Knowledge Framework - Didáctica y Currículo)

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC_BY--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/deed.es)
[![Framework: OKF](https://img.shields.io/badge/Framework-OKF_v1.2-blue.svg)](#arquitectura-okf)
[![Coverage: Canarias](https://img.shields.io/badge/Canarias-Infantil_|_Primaria_|_ESO_|_Bachillerato-green.svg)](#-comunidades-autónomas)
[![Metodología: DUA + Merrill](https://img.shields.io/badge/Metodología-DUA_|_David_Merrill_|_Rúbricas_Graduadores-orange.svg)](#-ecosistema-metodológico)

Base de conocimiento estructurada y abierta basada en el estándar **Open Knowledge Framework (OKF)** para la gestión, diseño y generación asistida por Inteligencia Artificial de **Programaciones Didácticas (PD)** y **Situaciones de Aprendizaje (SDA)** plenamente adaptadas a la LOMLOE y a la normativa autonómica.

Organizado por **Comunidades Autónomas**, comenzando con la cobertura completa de la **Comunidad Autónoma de Canarias** para **Educación Infantil, Primaria, Educación Secundaria Obligatoria (ESO) y Bachillerato** (incorporando la Formación Profesional en las siguientes fases).

---

## 🎯 Propósito del Proyecto

El objetivo de **OpenDidactia** es dotar a la comunidad educativa (docentes, centros, opositores e inspectores) y a los agentes de Inteligencia Artificial de un marco operativo integral que permite:
1. **Garantizar la Trazabilidad Curricular:** Conectar de forma transparente los descriptores operativos del Perfil de Salida, las competencias clave y específicas, los criterios de evaluación y los saberes básicos.
2. **Deconstrucción Oficial de Criterios:** Desglosar cada criterio en Instrumentos de Evaluación (Productos tangibles numerados `[Criterio].[Secuencia]`), distribuyendo exhaustivamente todos los descriptores operativos.
3. **Rúbricas Criteriales con Graduadores:** Diseñar rúbricas analíticas oficiales donde el verbo principal se mantiene invariable, modulando el desempeño mediante **graduadores en negrita** e incluyendo ejemplos de producto por nivel.
4. **Operacionalización Granular del DUA:** Aplicar los 3 principios y 9 pautas del Diseño Universal para el Aprendizaje en cada tarea de aula (redes afectivas, de reconocimiento y estratégicas), integrando los principios instruccionales de **David Merrill**.
5. **Planes de Refuerzo y Recuperación:** Gestionar planes de apoyo individualizado en evaluación continua con seguimiento invisible en las SAs siguientes y estricta privacidad (`[DATOS ANONIMIZADOS]`).

---

## 🔗 Sinergia con `nmarafo/open-lex-edu`

Este repositorio complementa y se apoya en el marco normativo de **[open-lex-edu](https://github.com/nmarafo/open-lex-edu)**:
* **open-lex-edu:** Proporciona el corpus legal completo, consolidado y auditado de la normativa educativa estatal y autonómica en formato OKF.
* **OpenDidactia:** Utiliza esa base jurídica para desarrollar la ingeniería didáctica, los catálogos curriculares, las matrices competenciales, los esquemas de validación y las herramientas operativas de aula.

---

## 📁 Estructura del Repositorio

```text
OpenDidactia/
├── README.md                            # Presentación y arquitectura general
├── LICENSE.md                           # Licencia CC BY-SA 4.0 y requisitos de atribución
├── .gitignore
├── schema/                              # Esquemas de validación formales (JSON Schema)
│   ├── norm_schema.json                 # Esquema OKF de disposiciones normativas (open-lex-edu)
│   ├── esquema_programacion_didactica.json # Validación de PDs anuales (9 SAs)
│   └── esquema_situacion_aprendizaje.json  # Validación de SDAs (Merrill + DUA granular)
├── docs/                                # Documentación técnica y metodológica
│   ├── flujo_agente_elaboracion_pd_sa.md   # Protocolo maestro de 9 pasos para Agentes de IA
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

## 🤖 Protocolo de 9 Pasos para Agentes de IA

Para elaborar una Programación Didáctica y sus Situaciones de Aprendizaje, el Agente debe ejecutar de forma secuencial:

| Paso | Acción del Agente | Documentación / Prompt de Apoyo |
| :---: | :--- | :--- |
| **1** | **Deconstrucción de Criterios** en Instrumentos/Productos numerados | `docs/flujo_agente_elaboracion_pd_sa.md`<br>`plantillas/prompts/prompt_01_deconstruccion_criterios.md` |
| **2** | **Diseño de Rúbricas con Graduadores** (verbo invariable y ejemplos) | `docs/guia_elaboracion_rubricas_graduadores.md`<br>`plantillas/prompts/prompt_02_elaboracion_rubricas_graduadores.md` |
| **3** | **Activación del Ecosistema** (Merrill, Cooperativo, Rutinas y Efemérides) | `docs/ecosistema_herramientas_activas.md` |
| **4** | **Secuenciación Anual de la PD** en 9 SAs por trimestres | `plantillas/prompts/prompt_03_secuenciacion_programacion_anual.md` |
| **5** | **Desarrollo Pormenorizado de la SA** (Sesiones Merrill + DUA Granular) | `docs/guia_operacionalizacion_dua.md`<br>`plantillas/prompts/prompt_04_desarrollo_sa_docente_merrill_dua.md` |
| **6** | **Concreción de la SA para el Alumnado** (Guion sin tecnicismos) | `plantillas/prompts/prompt_05_sa_para_alumnado.md` |
| **7** | **Elaboración del Plan de Apoyo y Refuerzo** (Seguimiento invisible) | `docs/guia_planes_apoyo_y_recuperacion.md`<br>`plantillas/prompts/prompt_06_plan_apoyo_refuerzo_individualizado.md` |
| **8** | **Elaboración del Plan de Recuperación de Materias Pendientes** | `plantillas/prompts/prompt_07_plan_recuperacion_pendientes.md` |
| **9** | **Generación de la Herramienta de Calificación** (HTML interactivo Canvas) | `plantillas/prompts/prompt_08_herramienta_calificacion_canvas.md` |

---

## 📄 Licencia y Atribución

Este repositorio y todos sus contenidos se distribuyen bajo los términos de la licencia **[Creative Commons Atribución-CompartirIgual 4.0 Internacional (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/deed.es)**.

### Cláusula de Atribución Obligatoria
En cualquier obra derivada, adaptación o integración en sistemas informáticos o de inteligencia artificial, **debe incluirse la siguiente mención explícita**:

> *Basado en los repositorios [OpenDidactia](https://github.com/nmarafo/OpenDidactia) y [open-lex-edu](https://github.com/nmarafo/open-lex-edu) creados por **Norberto Martín Afonso**, distribuidos bajo licencia Creative Commons Atribución-CompartirIgual 4.0 Internacional (CC BY-SA 4.0).*
