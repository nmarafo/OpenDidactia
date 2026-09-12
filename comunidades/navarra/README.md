# 🏛️ Comunidad Autónoma: Comunidad Foral de Navarra (Marco Curricular y Normativo OKF)

Este directorio contiene la estructura del marco normativo y curricular oficial de la **Comunidad Autónoma de Comunidad Foral de Navarra**, adaptado al estándar **Open Knowledge Framework (OKF)** para la generación rigurosa de **Programaciones Didácticas (PD)** y **Situaciones de Aprendizaje (SDA)** plenamente conformes a la LOMLOE.

---

## 1. Decretos Curriculares Autonómicos Oficiales

| Etapa Educativa | Disposición Oficial | Boletín de Referencia | Estado OKF |
| :--- | :--- | :---: | :---: |
| **Educación Infantil** | Decreto Foral 60/2022, de 8 de junio (BON n.º 125, 23/06/2022) | BON (Boletín Oficial de Navarra) | Estructurado |
| **Educación Primaria** | Decreto Foral 67/2022, de 22 de junio (BON n.º 129, 29/06/2022) | BON (Boletín Oficial de Navarra) | Estructurado |
| **Educación Secundaria Obligatoria** | Decreto Foral 68/2022, de 22 de junio (BON n.º 129, 29/06/2022) | BON (Boletín Oficial de Navarra) | Estructurado |
| **Formación Profesional** | Decreto Foral 41/2024, de 19 de junio (BON n.º 129, 26/06/2024), por e... | BON | Estructurado |
| **Bachillerato** | Decreto Foral 69/2022, de 22 de junio (BON n.º 129, 29/06/2022) | BON (Boletín Oficial de Navarra) | Estructurado |

> Los textos y disposiciones normativas se organizan en [`normativa/`](normativa/) siguiendo el estándar de metadatos de [nmarafo/open-lex-edu](https://github.com/nmarafo/open-lex-edu).

---

## 2. Singularidades y Contexto Autonómico para el Diseño de SDAs

Al diseñar Situaciones de Aprendizaje y Programaciones Didácticas para centros educativos de Comunidad Foral de Navarra, los docentes y agentes de IA deben integrar:

* **Marco Lingüístico:** Cooficialidad del euskera en zona vascófona; modelos lingüísticos A, B, D y G.
* **Patrimonio y Realidad Territorial:** Régimen foral histórico e instituciones de autogobierno, diversidad geográfica desde el Pirineo a la Ribera, Día de Navarra (3 de diciembre)..
* **Atención a la Diversidad e Inclusión (DUA):** Aplicación universal de las tres redes neuronales del DUA (Representación, Acción/Expresión e Implicación), adaptando los andamiajes a la realidad sociocultural del centro.
* **Evaluación Criterial:** Calificación vinculada a los criterios de evaluación del currículo de Comunidad Foral de Navarra, graduados mediante rúbricas analíticas oficiales.

---

## 3. Estructura de Directorios

```text
navarra/
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
