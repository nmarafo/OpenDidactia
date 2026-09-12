# 🏛️ Comunidad Autónoma: Extremadura (Marco Curricular y Normativo OKF)

Este directorio contiene la estructura del marco normativo y curricular oficial de la **Comunidad Autónoma de Extremadura**, adaptado al estándar **Open Knowledge Framework (OKF)** para la generación rigurosa de **Programaciones Didácticas (PD)** y **Situaciones de Aprendizaje (SDA)** plenamente conformes a la LOMLOE.

---

## 1. Decretos Curriculares Autonómicos Oficiales

| Etapa Educativa | Disposición Oficial | Boletín de Referencia | Estado OKF |
| :--- | :--- | :---: | :---: |
| **Educación Infantil** | Decreto 98/2022, de 20 de julio (DOE n.º 142, 25/07/2022) | DOE (Diario Oficial de Extremadura) | Estructurado |
| **Educación Primaria** | Decreto 105/2022, de 3 de agosto (DOE n.º 151, 05/08/2022) | DOE (Diario Oficial de Extremadura) | Estructurado |
| **Educación Secundaria Obligatoria** | Decreto 110/2022, de 22 de agosto (DOE n.º 164, 25/08/2022) | DOE (Diario Oficial de Extremadura) | Estructurado |
| **Formación Profesional** | Decreto 58/2024, de 25 de junio (DOE n.º 126, 01/07/2024), por el que ... | DOE | Estructurado |
| **Bachillerato** | Decreto 109/2022, de 22 de agosto (DOE n.º 164, 25/08/2022) | DOE (Diario Oficial de Extremadura) | Estructurado |

> Los textos y disposiciones normativas se organizan en [`normativa/`](normativa/) siguiendo el estándar de metadatos de [nmarafo/open-lex-edu](https://github.com/nmarafo/open-lex-edu).

---

## 2. Singularidades y Contexto Autonómico para el Diseño de SDAs

Al diseñar Situaciones de Aprendizaje y Programaciones Didácticas para centros educativos de Extremadura, los docentes y agentes de IA deben integrar:

* **Marco Lingüístico:** Castellano con variedades dialectales extremeñas y fala de Xálima.
* **Patrimonio y Realidad Territorial:** Patrimonio romano (Augusta Emerita / Mérida) y medieval (Cáceres, Guadalupe), ecosistema dehesa y Parque Nacional de Monfragüe, Día de Extremadura (8 de septiembre)..
* **Atención a la Diversidad e Inclusión (DUA):** Aplicación universal de las tres redes neuronales del DUA (Representación, Acción/Expresión e Implicación), adaptando los andamiajes a la realidad sociocultural del centro.
* **Evaluación Criterial:** Calificación vinculada a los criterios de evaluación del currículo de Extremadura, graduados mediante rúbricas analíticas oficiales.

---

## 3. Estructura de Directorios

```text
extremadura/
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
