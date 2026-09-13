# 🏛️ Comunidad Autónoma: Cantabria (Marco Curricular y Normativo OKF)

Este directorio contiene la estructura del marco normativo y curricular oficial de la **Comunidad Autónoma de Cantabria**, adaptado al estándar **Open Knowledge Framework (OKF)** para la generación rigurosa de **Programaciones Didácticas (PD)** y **Situaciones de Aprendizaje (SDA)** plenamente conformes a la LOMLOE.

---

## 1. Decretos Curriculares Autonómicos Oficiales

| Etapa Educativa | Disposición Oficial | Boletín de Referencia | Estado OKF |
| :--- | :--- | :---: | :---: |
| **Educación Infantil** | Decreto 66/2022, de 7 de julio (BOC n.º 135, 13/07/2022) | BOC (Boletín Oficial de Cantabria) | Estructurado |
| **Educación Primaria** | Decreto 66/2022, de 7 de julio (BOC n.º 135, 13/07/2022) | BOC (Boletín Oficial de Cantabria) | Estructurado |
| **Educación Secundaria Obligatoria** | Decreto 73/2022, de 21 de julio (BOC n.º 144, 26/07/2022) | BOC (Boletín Oficial de Cantabria) | Estructurado |
| **Formación Profesional** | Decreto 45/2024, de 27 de junio (BOC n.º 128, 03/07/2024), de ordenación de FP | BOC | Estructurado |
| **Bachillerato** | Decreto 73/2022, de 21 de julio (BOC n.º 144, 26/07/2022) | BOC (Boletín Oficial de Cantabria) | Estructurado |

> Los textos y disposiciones normativas se organizan en [`normativa/`](normativa/) siguiendo el estándar de metadatos de [nmarafo/open-lex-edu](https://github.com/nmarafo/open-lex-edu).

---

## 2. Singularidades y Contexto Autonómico para el Diseño de SDAs

Al diseñar Situaciones de Aprendizaje y Programaciones Didácticas para centros educativos de Cantabria, los docentes y agentes de IA deben integrar:

* **Marco Lingüístico:** Castellano con variantes y léxico tradicional cántabro.
* **Patrimonio y Realidad Territorial:** Arte rupestre paleolítico (Cueva de Altamira), tradición marinera y ganadera montañesa, Día de las Instituciones de Cantabria (28 de julio)..
* **Atención a la Diversidad e Inclusión (DUA):** Aplicación universal de las tres redes neuronales del DUA (Representación, Acción/Expresión e Implicación), adaptando los andamiajes a la realidad sociocultural del centro.
* **Evaluación Criterial:** Calificación vinculada a los criterios de evaluación del currículo de Cantabria, graduados mediante rúbricas analíticas oficiales.

---

## 3. Estructura de Directorios

```text
cantabria/
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
