# 🏛️ Comunidad Autónoma: Principado de Asturias (Marco Curricular y Normativo OKF)

Este directorio contiene la estructura del marco normativo y curricular oficial de la **Comunidad Autónoma de Principado de Asturias**, adaptado al estándar **Open Knowledge Framework (OKF)** para la generación rigurosa de **Programaciones Didácticas (PD)** y **Situaciones de Aprendizaje (SDA)** plenamente conformes a la LOMLOE.

---

## 1. Decretos Curriculares Autonómicos Oficiales

| Etapa Educativa | Disposición Oficial | Boletín de Referencia | Estado OKF |
| :--- | :--- | :---: | :---: |
| **Educación Infantil** | Decreto 56/2022, de 5 de agosto (BOPA n.º 159, 17/08/2022) | BOPA (Boletín Oficial del Principado de Asturias) | Estructurado |
| **Educación Primaria** | Decreto 57/2022, de 5 de agosto (BOPA n.º 164, 24/08/2022) | BOPA (Boletín Oficial del Principado de Asturias) | Estructurado |
| **Educación Secundaria Obligatoria** | Decreto 59/2022, de 30 de agosto (BOPA n.º 169, 31/08/2022) | BOPA (Boletín Oficial del Principado de Asturias) | Estructurado |
| **Formación Profesional** | Decreto 48/2024, de 21 de junio (BOPA n.º 126, 28/06/2024), por el que... | BOPA | Estructurado |
| **Bachillerato** | Decreto 60/2022, de 30 de agosto (BOPA n.º 169, 31/08/2022) | BOPA (Boletín Oficial del Principado de Asturias) | Estructurado |

> Los textos y disposiciones normativas se organizan en [`normativa/`](normativa/) siguiendo el estándar de metadatos de [nmarafo/open-lex-edu](https://github.com/nmarafo/open-lex-edu).

---

## 2. Singularidades y Contexto Autonómico para el Diseño de SDAs

Al diseñar Situaciones de Aprendizaje y Programaciones Didácticas para centros educativos de Principado de Asturias, los docentes y agentes de IA deben integrar:

* **Marco Lingüístico:** Llingua Asturiana y Gallego-Asturiano (Eonaviego).
* **Patrimonio y Realidad Territorial:** Arte prerrománico asturiano, patrimonio industrial y minero, orografía cantábrica y Picos de Europa, Día de Asturias (8 de septiembre)..
* **Atención a la Diversidad e Inclusión (DUA):** Aplicación universal de las tres redes neuronales del DUA (Representación, Acción/Expresión e Implicación), adaptando los andamiajes a la realidad sociocultural del centro.
* **Evaluación Criterial:** Calificación vinculada a los criterios de evaluación del currículo de Principado de Asturias, graduados mediante rúbricas analíticas oficiales.

---

## 3. Estructura de Directorios

```text
asturias/
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
