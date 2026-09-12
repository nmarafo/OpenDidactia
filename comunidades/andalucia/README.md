# 🏛️ Comunidad Autónoma: Andalucía (Marco Curricular y Normativo OKF)

Este directorio contiene la estructura del marco normativo y curricular oficial de la **Comunidad Autónoma de Andalucía**, adaptado al estándar **Open Knowledge Framework (OKF)** para la generación rigurosa de **Programaciones Didácticas (PD)** y **Situaciones de Aprendizaje (SDA)** plenamente conformes a la LOMLOE.

---

## 1. Decretos Curriculares Autonómicos Oficiales

| Etapa Educativa | Disposición Oficial | Boletín de Referencia | Estado OKF |
| :--- | :--- | :---: | :---: |
| **Educación Infantil** | Decreto 100/2023, de 9 de mayo (BOJA n.º 90, 15/05/2023) | BOJA (Boletín Oficial de la Junta de Andalucía) | Estructurado |
| **Educación Primaria** | Decreto 101/2023, de 9 de mayo (BOJA n.º 90, 15/05/2023) | BOJA (Boletín Oficial de la Junta de Andalucía) | Estructurado |
| **Educación Secundaria Obligatoria** | Decreto 102/2023, de 9 de mayo (BOJA n.º 90, 15/05/2023) | BOJA (Boletín Oficial de la Junta de Andalucía) | Estructurado |
| **Bachillerato** | Decreto 103/2023, de 9 de mayo (BOJA n.º 90, 15/05/2023) | BOJA (Boletín Oficial de la Junta de Andalucía) | Estructurado |

> Los textos y disposiciones normativas se organizan en [`normativa/`](normativa/) siguiendo el estándar de metadatos de [nmarafo/open-lex-edu](https://github.com/nmarafo/open-lex-edu).

---

## 2. Singularidades y Contexto Autonómico para el Diseño de SDAs

Al diseñar Situaciones de Aprendizaje y Programaciones Didácticas para centros educativos de Andalucía, los docentes y agentes de IA deben integrar:

* **Marco Lingüístico:** Modalidad lingüística andaluza (hablas andaluzas).
* **Patrimonio y Realidad Territorial:** Patrimonio histórico-artístico (andalusí, renacentista, barroco), flamenco como patrimonio inmaterial, Programa CIMA (Innovación y Mejora del Aprendizaje), Día de Andalucía (28 de febrero)..
* **Atención a la Diversidad e Inclusión (DUA):** Aplicación universal de las tres redes neuronales del DUA (Representación, Acción/Expresión e Implicación), adaptando los andamiajes a la realidad sociocultural del centro.
* **Evaluación Criterial:** Calificación vinculada a los criterios de evaluación del currículo de Andalucía, graduados mediante rúbricas analíticas oficiales.

---

## 3. Estructura de Directorios

```text
andalucia/
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
