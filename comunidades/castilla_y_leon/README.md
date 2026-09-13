# 🏛️ Comunidad Autónoma: Castilla y León (Marco Curricular y Normativo OKF)

Este directorio contiene la estructura del marco normativo y curricular oficial de la **Comunidad Autónoma de Castilla y León**, adaptado al estándar **Open Knowledge Framework (OKF)** para la generación rigurosa de **Programaciones Didácticas (PD)** y **Situaciones de Aprendizaje (SDA)** plenamente conformes a la LOMLOE.

---

## 1. Decretos Curriculares Autonómicos Oficiales

| Etapa Educativa | Disposición Oficial | Boletín de Referencia | Estado OKF |
| :--- | :--- | :---: | :---: |
| **Educación Infantil** | Decreto 37/2022, de 29 de septiembre (BOCyL n.º 190, 30/09/2022) | BOCyL (Boletín Oficial de Castilla y León) | Estructurado |
| **Educación Primaria** | Decreto 38/2022, de 29 de septiembre (BOCyL n.º 190, 30/09/2022) | BOCyL (Boletín Oficial de Castilla y León) | Estructurado |
| **Educación Secundaria Obligatoria** | Decreto 39/2022, de 29 de septiembre (BOCyL n.º 190, 30/09/2022) | BOCyL (Boletín Oficial de Castilla y León) | Estructurado |
| **Formación Profesional** | Decreto 24/2024, de 20 de junio (BOCyL n.º 120, 21/06/2024), de ordenación de FP | BOCyL | Estructurado |
| **Bachillerato** | Decreto 40/2022, de 29 de septiembre (BOCyL n.º 190, 30/09/2022) | BOCyL (Boletín Oficial de Castilla y León) | Estructurado |

> Los textos y disposiciones normativas se organizan en [`normativa/`](normativa/) siguiendo el estándar de metadatos de [nmarafo/open-lex-edu](https://github.com/nmarafo/open-lex-edu).

---

## 2. Singularidades y Contexto Autonómico para el Diseño de SDAs

Al diseñar Situaciones de Aprendizaje y Programaciones Didácticas para centros educativos de Castilla y León, los docentes y agentes de IA deben integrar:

* **Marco Lingüístico:** Castellano con presencia del leonés y gallego en comarcas limítrofes.
* **Patrimonio y Realidad Territorial:** Mayor concentración mundial de patrimonio románico, gótico y ciudades Patrimonio, cuna histórica del castellano (Cartularios de Valpuesta), Día de la Comunidad (Villalar, 23 de abril)..
* **Atención a la Diversidad e Inclusión (DUA):** Aplicación universal de las tres redes neuronales del DUA (Representación, Acción/Expresión e Implicación), adaptando los andamiajes a la realidad sociocultural del centro.
* **Evaluación Criterial:** Calificación vinculada a los criterios de evaluación del currículo de Castilla y León, graduados mediante rúbricas analíticas oficiales.

---

## 3. Estructura de Directorios

```text
castilla_y_leon/
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
