# 🏛️ Comunidad Autónoma: Catalunya (Marco Curricular y Normativo OKF)

Este directorio contiene la estructura del marco normativo y curricular oficial de la **Comunidad Autónoma de Catalunya**, adaptado al estándar **Open Knowledge Framework (OKF)** para la generación rigurosa de **Programaciones Didácticas (PD)** y **Situaciones de Aprendizaje (SDA)** plenamente conformes a la LOMLOE.

---

## 1. Decretos Curriculares Autonómicos Oficiales

| Etapa Educativa | Disposición Oficial | Boletín de Referencia | Estado OKF |
| :--- | :--- | :---: | :---: |
| **Educación Infantil** | Decret 21/2023, de 7 de febrer (DOGC n.º 8851, 09/02/2023) | DOGC (Diari Oficial de la Generalitat de Catalunya) | Estructurado |
| **Educación Primaria** | Decret 175/2022, de 27 de setembre (Educació Bàsica - DOGC n.º 8762, 29/09/2022) | DOGC (Diari Oficial de la Generalitat de Catalunya) | Estructurado |
| **Educación Secundaria Obligatoria** | Decret 175/2022, de 27 de setembre (Educació Bàsica - DOGC n.º 8762, 29/09/2022) | DOGC (Diari Oficial de la Generalitat de Catalunya) | Estructurado |
| **Formación Profesional** | Decret 124/2024, de 25 de juny (DOGC n.º 9193, 27/06/2024), d'ordenaci... | DOGC | Estructurado |
| **Bachillerato** | Decret 171/2022, de 20 de setembre (Batxillerat - DOGC n.º 8758, 22/09/2022) | DOGC (Diari Oficial de la Generalitat de Catalunya) | Estructurado |

> Los textos y disposiciones normativas se organizan en [`normativa/`](normativa/) siguiendo el estándar de metadatos de [nmarafo/open-lex-edu](https://github.com/nmarafo/open-lex-edu).

---

## 2. Singularidades y Contexto Autonómico para el Diseño de SDAs

Al diseñar Situaciones de Aprendizaje y Programaciones Didácticas para centros educativos de Catalunya, los docentes y agentes de IA deben integrar:

* **Marco Lingüístico:** Cooficialitat lingüística: Llengua Catalana, Aranès (Occità a l'Aran) i Llengua Castellana.
* **Patrimonio y Realidad Territorial:** Model d'immersió i cohesió lingüística, modernisme i avantguardes, tradicions populars (castells, Sant Jordi), Diada Nacional de Catalunya (11 de setembre)..
* **Atención a la Diversidad e Inclusión (DUA):** Aplicación universal de las tres redes neuronales del DUA (Representación, Acción/Expresión e Implicación), adaptando los andamiajes a la realidad sociocultural del centro.
* **Evaluación Criterial:** Calificación vinculada a los criterios de evaluación del currículo de Catalunya, graduados mediante rúbricas analíticas oficiales.

---

## 3. Estructura de Directorios

```text
catalunya/
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
