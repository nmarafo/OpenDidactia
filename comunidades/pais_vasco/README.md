# 🏛️ Comunidad Autónoma: País Vasco / Euskadi (Marco Curricular y Normativo OKF)

Este directorio contiene la estructura del marco normativo y curricular oficial de la **Comunidad Autónoma de País Vasco / Euskadi**, adaptado al estándar **Open Knowledge Framework (OKF)** para la generación rigurosa de **Programaciones Didácticas (PD)** y **Situaciones de Aprendizaje (SDA)** plenamente conformes a la LOMLOE.

---

## 1. Decretos Curriculares Autonómicos Oficiales

| Etapa Educativa | Disposición Oficial | Boletín de Referencia | Estado OKF |
| :--- | :--- | :---: | :---: |
| **Educación Infantil** | Decreto 75/2023, de 30 de mayo (BOPV n.º 109, 09/06/2023) | BOPV (Boletín Oficial del País Vasco) | Estructurado |
| **Educación Primaria** | Decreto 77/2023, de 30 de mayo (Educación Básica - BOPV n.º 109, 09/06/2023) | BOPV (Boletín Oficial del País Vasco) | Estructurado |
| **Educación Secundaria Obligatoria** | Decreto 77/2023, de 30 de mayo (Educación Básica - BOPV n.º 109, 09/06/2023) | BOPV (Boletín Oficial del País Vasco) | Estructurado |
| **Bachillerato** | Decreto 76/2023, de 30 de mayo (BOPV n.º 109, 09/06/2023) | BOPV (Boletín Oficial del País Vasco) | Estructurado |

> Los textos y disposiciones normativas se organizan en [`normativa/`](normativa/) siguiendo el estándar de metadatos de [nmarafo/open-lex-edu](https://github.com/nmarafo/open-lex-edu).

---

## 2. Singularidades y Contexto Autonómico para el Diseño de SDAs

Al diseñar Situaciones de Aprendizaje y Programaciones Didácticas para centros educativos de País Vasco / Euskadi, los docentes y agentes de IA deben integrar:

* **Marco Lingüístico:** Cooficialidad lingüística: Euskara eta Literatura y Lengua Castellana (Modelos A, B y D).
* **Patrimonio y Realidad Territorial:** Marco pedagógico vasco y perfil de salida euskaldun, patrimonio industrial, marinero y cultural tradicional vasco, autogobierno y Concierto Económico..
* **Atención a la Diversidad e Inclusión (DUA):** Aplicación universal de las tres redes neuronales del DUA (Representación, Acción/Expresión e Implicación), adaptando los andamiajes a la realidad sociocultural del centro.
* **Evaluación Criterial:** Calificación vinculada a los criterios de evaluación del currículo de País Vasco / Euskadi, graduados mediante rúbricas analíticas oficiales.

---

## 3. Estructura de Directorios

```text
pais_vasco/
├── README.md                            # Este documento informativo
├── normativa/                           # Textos normativos y decretos curriculares autonómicos
└── curricular/                          # Catálogo curricular operativo por etapas
    ├── infantil/                        # Perfil de etapa, áreas y saberes básicos
    ├── primaria/                        # Descriptores de salida, áreas y criterios
    ├── eso/                             # Perfil de salida básico y materias
    └── bachillerato/                    # Modalidades, materias comunes y de modalidad
```

---

## 🔗 Referencia Metodológica
Para la elaboración de documentos en esta comunidad, aplique el protocolo oficial del proyecto disponible en [`docs/flujo_agente_elaboracion_pd_sa.md`](../../docs/flujo_agente_elaboracion_pd_sa.md) y las plantillas operativas de [`plantillas/`](../../plantillas/).
