# 🏛️ Comunidad Autónoma: Galicia (Marco Curricular y Normativo OKF)

Este directorio contiene la estructura del marco normativo y curricular oficial de la **Comunidad Autónoma de Galicia**, adaptado al estándar **Open Knowledge Framework (OKF)** para la generación rigurosa de **Programaciones Didácticas (PD)** y **Situaciones de Aprendizaje (SDA)** plenamente conformes a la LOMLOE.

---

## 1. Decretos Curriculares Autonómicos Oficiales

| Etapa Educativa | Disposición Oficial | Boletín de Referencia | Estado OKF |
| :--- | :--- | :---: | :---: |
| **Educación Infantil** | Decreto 150/2022, do 8 de setembro (DOG n.º 179, 20/09/2022) | DOG (Diario Oficial de Galicia) | Estructurado |
| **Educación Primaria** | Decreto 155/2022, do 15 de setembro (DOG n.º 183, 26/09/2022) | DOG (Diario Oficial de Galicia) | Estructurado |
| **Educación Secundaria Obligatoria** | Decreto 156/2022, do 15 de setembro (DOG n.º 183, 26/09/2022) | DOG (Diario Oficial de Galicia) | Estructurado |
| **Bachillerato** | Decreto 157/2022, do 15 de setembro (DOG n.º 183, 26/09/2022) | DOG (Diario Oficial de Galicia) | Estructurado |

> Los textos y disposiciones normativas se organizan en [`normativa/`](normativa/) siguiendo el estándar de metadatos de [nmarafo/open-lex-edu](https://github.com/nmarafo/open-lex-edu).

---

## 2. Singularidades y Contexto Autonómico para el Diseño de SDAs

Al diseñar Situaciones de Aprendizaje y Programaciones Didácticas para centros educativos de Galicia, los docentes y agentes de IA deben integrar:

* **Marco Lingüístico:** Cooficialidade lingüística: Lingua Galega e Literatura e Lingua Castelá.
* **Patrimonio y Realidad Territorial:** Camiño de Santiago e cultura xacobea, patrimonio natural atlántico (Rías Baixas/Altas, Illas Atlánticas), Día das Letras Galegas (17 de maio), Día Nacional de Galicia (25 de xullo)..
* **Atención a la Diversidad e Inclusión (DUA):** Aplicación universal de las tres redes neuronales del DUA (Representación, Acción/Expresión e Implicación), adaptando los andamiajes a la realidad sociocultural del centro.
* **Evaluación Criterial:** Calificación vinculada a los criterios de evaluación del currículo de Galicia, graduados mediante rúbricas analíticas oficiales.

---

## 3. Estructura de Directorios

```text
galicia/
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
