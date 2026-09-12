# 🏛️ Comunidad Autónoma: Castilla-La Mancha (Marco Curricular y Normativo OKF)

Este directorio contiene la estructura del marco normativo y curricular oficial de la **Comunidad Autónoma de Castilla-La Mancha**, adaptado al estándar **Open Knowledge Framework (OKF)** para la generación rigurosa de **Programaciones Didácticas (PD)** y **Situaciones de Aprendizaje (SDA)** plenamente conformes a la LOMLOE.

---

## 1. Decretos Curriculares Autonómicos Oficiales

| Etapa Educativa | Disposición Oficial | Boletín de Referencia | Estado OKF |
| :--- | :--- | :---: | :---: |
| **Educación Infantil** | Decreto 80/2022, de 12 de julio (DOCM n.º 138, 20/07/2022) | DOCM (Diario Oficial de Castilla-La Mancha) | Estructurado |
| **Educación Primaria** | Decreto 81/2022, de 12 de julio (DOCM n.º 139, 21/07/2022) | DOCM (Diario Oficial de Castilla-La Mancha) | Estructurado |
| **Educación Secundaria Obligatoria** | Decreto 82/2022, de 12 de julio (DOCM n.º 140, 22/07/2022) | DOCM (Diario Oficial de Castilla-La Mancha) | Estructurado |
| **Formación Profesional** | Decreto 39/2024, de 9 de julio (DOCM n.º 136, 15/07/2024), por el que ... | DOCM | Estructurado |
| **Bachillerato** | Decreto 83/2022, de 12 de julio (DOCM n.º 141, 25/07/2022) | DOCM (Diario Oficial de Castilla-La Mancha) | Estructurado |

> Los textos y disposiciones normativas se organizan en [`normativa/`](normativa/) siguiendo el estándar de metadatos de [nmarafo/open-lex-edu](https://github.com/nmarafo/open-lex-edu).

---

## 2. Singularidades y Contexto Autonómico para el Diseño de SDAs

Al diseñar Situaciones de Aprendizaje y Programaciones Didácticas para centros educativos de Castilla-La Mancha, los docentes y agentes de IA deben integrar:

* **Marco Lingüístico:** Castellano.
* **Patrimonio y Realidad Territorial:** Patrimonio universal cervantino (El Quijote), humedales de La Mancha (Tablas de Daimiel, Ruidera), ciudades históricas (Toledo, Cuenca), Día de la Región (31 de mayo)..
* **Atención a la Diversidad e Inclusión (DUA):** Aplicación universal de las tres redes neuronales del DUA (Representación, Acción/Expresión e Implicación), adaptando los andamiajes a la realidad sociocultural del centro.
* **Evaluación Criterial:** Calificación vinculada a los criterios de evaluación del currículo de Castilla-La Mancha, graduados mediante rúbricas analíticas oficiales.

---

## 3. Estructura de Directorios

```text
castilla_la_mancha/
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
