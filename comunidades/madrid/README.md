# 🏛️ Comunidad Autónoma: Comunidad de Madrid (Marco Curricular y Normativo OKF)

Este directorio contiene la estructura del marco normativo y curricular oficial de la **Comunidad Autónoma de Comunidad de Madrid**, adaptado al estándar **Open Knowledge Framework (OKF)** para la generación rigurosa de **Programaciones Didácticas (PD)** y **Situaciones de Aprendizaje (SDA)** plenamente conformes a la LOMLOE.

---

## 1. Decretos Curriculares Autonómicos Oficiales

| Etapa Educativa | Disposición Oficial | Boletín de Referencia | Estado OKF |
| :--- | :--- | :---: | :---: |
| **Educación Infantil** | Decreto 36/2022, de 8 de junio (BOCM n.º 136, 09/06/2022) | BOCM (Boletín Oficial de la Comunidad de Madrid) | Estructurado |
| **Educación Primaria** | Decreto 61/2022, de 13 de julio (BOCM n.º 166, 14/07/2022) | BOCM (Boletín Oficial de la Comunidad de Madrid) | Estructurado |
| **Educación Secundaria Obligatoria** | Decreto 65/2022, de 20 de julio (BOCM n.º 176, 26/07/2022) | BOCM (Boletín Oficial de la Comunidad de Madrid) | Estructurado |
| **Formación Profesional** | Decreto 49/2024, de 12 de junio (BOCM n.º 141, 14/06/2024), del Consej... | BOCM | Estructurado |
| **Bachillerato** | Decreto 64/2022, de 20 de julio (BOCM n.º 176, 26/07/2022) | BOCM (Boletín Oficial de la Comunidad de Madrid) | Estructurado |

> Los textos y disposiciones normativas se organizan en [`normativa/`](normativa/) siguiendo el estándar de metadatos de [nmarafo/open-lex-edu](https://github.com/nmarafo/open-lex-edu).

---

## 2. Singularidades y Contexto Autonómico para el Diseño de SDAs

Al diseñar Situaciones de Aprendizaje y Programaciones Didácticas para centros educativos de Comunidad de Madrid, los docentes y agentes de IA deben integrar:

* **Marco Lingüístico:** Castellano.
* **Patrimonio y Realidad Territorial:** Gran entorno metropolitano, eje cultural del Paisaje de la Luz (Prado-Retiro), Sierra de Guadarrama, centros de innovación tecnológica e investigación, Fiesta de la Comunidad de Madrid (2 de mayo)..
* **Atención a la Diversidad e Inclusión (DUA):** Aplicación universal de las tres redes neuronales del DUA (Representación, Acción/Expresión e Implicación), adaptando los andamiajes a la realidad sociocultural del centro.
* **Evaluación Criterial:** Calificación vinculada a los criterios de evaluación del currículo de Comunidad de Madrid, graduados mediante rúbricas analíticas oficiales.

---

## 3. Estructura de Directorios

```text
madrid/
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
