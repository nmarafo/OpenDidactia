# 🏛️ Comunidad Autónoma: Región de Murcia (Marco Curricular y Normativo OKF)

Este directorio contiene la estructura del marco normativo y curricular oficial de la **Comunidad Autónoma de Región de Murcia**, adaptado al estándar **Open Knowledge Framework (OKF)** para la generación rigurosa de **Programaciones Didácticas (PD)** y **Situaciones de Aprendizaje (SDA)** plenamente conformes a la LOMLOE.

---

## 1. Decretos Curriculares Autonómicos Oficiales

| Etapa Educativa | Disposición Oficial | Boletín de Referencia | Estado OKF |
| :--- | :--- | :---: | :---: |
| **Educación Infantil** | Decreto n.º 196/2022, de 3 de noviembre (BORM n.º 256, 05/11/2022) | BORM (Boletín Oficial de la Región de Murcia) | Estructurado |
| **Educación Primaria** | Decreto n.º 209/2022, de 17 de noviembre (BORM n.º 268, 19/11/2022) | BORM (Boletín Oficial de la Región de Murcia) | Estructurado |
| **Educación Secundaria Obligatoria** | Decreto n.º 235/2022, de 7 de diciembre (BORM n.º 283, 09/12/2022) | BORM (Boletín Oficial de la Región de Murcia) | Estructurado |
| **Formación Profesional** | Decreto 92/2024, de 4 de julio (BORM n.º 157, 09/07/2024), de ordenación de FP | BORM | Estructurado |
| **Bachillerato** | Decreto n.º 251/2022, de 22 de diciembre (BORM n.º 295, 24/12/2022) | BORM (Boletín Oficial de la Región de Murcia) | Estructurado |

> Los textos y disposiciones normativas se organizan en [`normativa/`](normativa/) siguiendo el estándar de metadatos de [nmarafo/open-lex-edu](https://github.com/nmarafo/open-lex-edu).

---

## 2. Singularidades y Contexto Autonómico para el Diseño de SDAs

Al diseñar Situaciones de Aprendizaje y Programaciones Didácticas para centros educativos de Región de Murcia, los docentes y agentes de IA deben integrar:

* **Marco Lingüístico:** Castellano con variedad dialectal murciana / panocho.
* **Patrimonio y Realidad Territorial:** Cultura y regadío tradicional de la Vega del Segura, laguna del Mar Menor y costa mediterránea, patrimonio cartagenero y barroco, Día de la Región de Murcia (9 de junio)..
* **Atención a la Diversidad e Inclusión (DUA):** Aplicación universal de las tres redes neuronales del DUA (Representación, Acción/Expresión e Implicación), adaptando los andamiajes a la realidad sociocultural del centro.
* **Evaluación Criterial:** Calificación vinculada a los criterios de evaluación del currículo de Región de Murcia, graduados mediante rúbricas analíticas oficiales.

---

## 3. Estructura de Directorios

```text
murcia/
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
