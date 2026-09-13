# 🏛️ Comunidad Autónoma: La Rioja (Marco Curricular y Normativo OKF)

Este directorio contiene la estructura del marco normativo y curricular oficial de la **Comunidad Autónoma de La Rioja**, adaptado al estándar **Open Knowledge Framework (OKF)** para la generación rigurosa de **Programaciones Didácticas (PD)** y **Situaciones de Aprendizaje (SDA)** plenamente conformes a la LOMLOE.

---

## 1. Decretos Curriculares Autonómicos Oficiales

| Etapa Educativa | Disposición Oficial | Boletín de Referencia | Estado OKF |
| :--- | :--- | :---: | :---: |
| **Educación Infantil** | Decreto 36/2022, de 29 de junio (BOR n.º 126, 01/07/2022) | BOR (Boletín Oficial de La Rioja) | Estructurado |
| **Educación Primaria** | Decreto 41/2022, de 13 de julio (BOR n.º 135, 14/07/2022) | BOR (Boletín Oficial de La Rioja) | Estructurado |
| **Educación Secundaria Obligatoria** | Decreto 42/2022, de 13 de julio (BOR n.º 135, 14/07/2022) | BOR (Boletín Oficial de La Rioja) | Estructurado |
| **Formación Profesional** | Decreto 29/2024, de 25 de junio (BOR n.º 125, 27/06/2024), de ordenación de FP | BOR | Estructurado |
| **Bachillerato** | Decreto 43/2022, de 21 de julio (BOR n.º 141, 22/07/2022) | BOR (Boletín Oficial de La Rioja) | Estructurado |

> Los textos y disposiciones normativas se organizan en [`normativa/`](normativa/) siguiendo el estándar de metadatos de [nmarafo/open-lex-edu](https://github.com/nmarafo/open-lex-edu).

---

## 2. Singularidades y Contexto Autonómico para el Diseño de SDAs

Al diseñar Situaciones de Aprendizaje y Programaciones Didácticas para centros educativos de La Rioja, los docentes y agentes de IA deben integrar:

* **Marco Lingüístico:** Castellano.
* **Patrimonio y Realidad Territorial:** Cuna del castellano y primer vestigio escrito en euskera (Glosas Emilianenses en San Millán de la Cogolla), paisaje vitivinícola y del río Ebro, Día de La Rioja (9 de junio)..
* **Atención a la Diversidad e Inclusión (DUA):** Aplicación universal de las tres redes neuronales del DUA (Representación, Acción/Expresión e Implicación), adaptando los andamiajes a la realidad sociocultural del centro.
* **Evaluación Criterial:** Calificación vinculada a los criterios de evaluación del currículo de La Rioja, graduados mediante rúbricas analíticas oficiales.

---

## 3. Estructura de Directorios

```text
la_rioja/
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
