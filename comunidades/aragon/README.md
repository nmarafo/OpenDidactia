# 🏛️ Comunidad Autónoma: Aragón (Marco Curricular y Normativo OKF)

Este directorio contiene la estructura del marco normativo y curricular oficial de la **Comunidad Autónoma de Aragón**, adaptado al estándar **Open Knowledge Framework (OKF)** para la generación rigurosa de **Programaciones Didácticas (PD)** y **Situaciones de Aprendizaje (SDA)** plenamente conformes a la LOMLOE.

---

## 1. Decretos Curriculares Autonómicos Oficiales

| Etapa Educativa | Disposición Oficial | Boletín de Referencia | Estado OKF |
| :--- | :--- | :---: | :---: |
| **Educación Infantil** | Decreto 45/2022, de 6 de abril (BOA n.º 77, 22/04/2022) | BOA (Boletín Oficial de Aragón) | Estructurado |
| **Educación Primaria** | Decreto 59/2022, de 27 de abril (BOA n.º 84, 04/05/2022) | BOA (Boletín Oficial de Aragón) | Estructurado |
| **Educación Secundaria Obligatoria** | Decreto 65/2022, de 11 de mayo (BOA n.º 97, 23/05/2022) | BOA (Boletín Oficial de Aragón) | Estructurado |
| **Formación Profesional** | Decreto 105/2024, de 3 de julio (BOA n.º 134, 11/07/2024), de ordenaci... | BOA | Estructurado |
| **Bachillerato** | Decreto 73/2022, de 18 de mayo (BOA n.º 104, 01/06/2022) | BOA (Boletín Oficial de Aragón) | Estructurado |

> Los textos y disposiciones normativas se organizan en [`normativa/`](normativa/) siguiendo el estándar de metadatos de [nmarafo/open-lex-edu](https://github.com/nmarafo/open-lex-edu).

---

## 2. Singularidades y Contexto Autonómico para el Diseño de SDAs

Al diseñar Situaciones de Aprendizaje y Programaciones Didácticas para centros educativos de Aragón, los docentes y agentes de IA deben integrar:

* **Marco Lingüístico:** Castellano con modalidades y lenguas propias históricas (aragonés y catalán de Aragón).
* **Patrimonio y Realidad Territorial:** Patrimonio mudéjar Patrimonio de la Humanidad, geografía pirenaica y esteparia, reto demográfico en el medio rural, Día de Aragón / San Jorge (23 de abril)..
* **Atención a la Diversidad e Inclusión (DUA):** Aplicación universal de las tres redes neuronales del DUA (Representación, Acción/Expresión e Implicación), adaptando los andamiajes a la realidad sociocultural del centro.
* **Evaluación Criterial:** Calificación vinculada a los criterios de evaluación del currículo de Aragón, graduados mediante rúbricas analíticas oficiales.

---

## 3. Estructura de Directorios

```text
aragon/
├── README.md                            # Este documento informativo
├── normativa/                           # Textos normativos y decretos curriculares autonómicos
└── curricular/                          # Catálogo curricular operativo por etapas
    ├── infantil/                        # Perfil de etapa, áreas y saberes básicos
    ├── primaria/                        # Descriptores de salida, áreas y criterios
    ├── eso/                             # Perfil de salida básico y materias
    ├── bachillerato/                    # Modalidades, materias comunes y de modalidad
    └── fp/                              # Módulos profesionales, Resultados de Aprendizaje y SA-UT Modalidades, materias comunes y de modalidad
```

---

## 🔗 Referencia Metodológica
Para la elaboración de documentos en esta comunidad, aplique el protocolo oficial del proyecto disponible en [`docs/flujo_agente_elaboracion_pd_sa.md`](../../docs/flujo_agente_elaboracion_pd_sa.md) y las plantillas operativas de [`plantillas/`](../../plantillas/).
