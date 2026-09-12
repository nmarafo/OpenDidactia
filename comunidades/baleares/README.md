# 🏛️ Comunidad Autónoma: Illes Balears (Marco Curricular y Normativo OKF)

Este directorio contiene la estructura del marco normativo y curricular oficial de la **Comunidad Autónoma de Illes Balears**, adaptado al estándar **Open Knowledge Framework (OKF)** para la generación rigurosa de **Programaciones Didácticas (PD)** y **Situaciones de Aprendizaje (SDA)** plenamente conformes a la LOMLOE.

---

## 1. Decretos Curriculares Autonómicos Oficiales

| Etapa Educativa | Disposición Oficial | Boletín de Referencia | Estado OKF |
| :--- | :--- | :---: | :---: |
| **Educación Infantil** | Decreto 29/2022, de 18 de julio (BOIB n.º 94, 21/07/2022) | BOIB (Butlletí Oficial de les Illes Balears) | Estructurado |
| **Educación Primaria** | Decreto 32/2022, de 1 de agosto (BOIB n.º 102, 06/08/2022) | BOIB (Butlletí Oficial de les Illes Balears) | Estructurado |
| **Educación Secundaria Obligatoria** | Decreto 33/2022, de 1 de agosto (BOIB n.º 102, 06/08/2022) | BOIB (Butlletí Oficial de les Illes Balears) | Estructurado |
| **Formación Profesional** | Decret 36/2024, de 12 de juliol (BOIB n.º 93, 16/07/2024), pel qual s'... | BOIB | Estructurado |
| **Bachillerato** | Decreto 34/2022, de 1 de agosto (BOIB n.º 102, 06/08/2022) | BOIB (Butlletí Oficial de les Illes Balears) | Estructurado |

> Los textos y disposiciones normativas se organizan en [`normativa/`](normativa/) siguiendo el estándar de metadatos de [nmarafo/open-lex-edu](https://github.com/nmarafo/open-lex-edu).

---

## 2. Singularidades y Contexto Autonómico para el Diseño de SDAs

Al diseñar Situaciones de Aprendizaje y Programaciones Didácticas para centros educativos de Illes Balears, los docentes y agentes de IA deben integrar:

* **Marco Lingüístico:** Cooficialidad lingüística: Llengua Catalana i Literatura y Lengua Castellana.
* **Patrimonio y Realidad Territorial:** Condición insular balear (Mallorca, Menorca, Eivissa, Formentera), ecosistemas costeros y posidonia marina, cultura talayótica, Diada de les Illes Balears (1 de marzo)..
* **Atención a la Diversidad e Inclusión (DUA):** Aplicación universal de las tres redes neuronales del DUA (Representación, Acción/Expresión e Implicación), adaptando los andamiajes a la realidad sociocultural del centro.
* **Evaluación Criterial:** Calificación vinculada a los criterios de evaluación del currículo de Illes Balears, graduados mediante rúbricas analíticas oficiales.

---

## 3. Estructura de Directorios

```text
baleares/
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
