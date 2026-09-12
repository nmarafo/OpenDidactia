# 🏛️ Comunidad Autónoma: Comunitat Valenciana (Marco Curricular y Normativo OKF)

Este directorio contiene la estructura del marco normativo y curricular oficial de la **Comunidad Autónoma de Comunitat Valenciana**, adaptado al estándar **Open Knowledge Framework (OKF)** para la generación rigurosa de **Programaciones Didácticas (PD)** y **Situaciones de Aprendizaje (SDA)** plenamente conformes a la LOMLOE.

---

## 1. Decretos Curriculares Autonómicos Oficiales

| Etapa Educativa | Disposición Oficial | Boletín de Referencia | Estado OKF |
| :--- | :--- | :---: | :---: |
| **Educación Infantil** | Decret 100/2022, de 29 de juliol (DOGV n.º 9399, 05/08/2022) | DOGV (Diari Oficial de la Generalitat Valenciana) | Estructurado |
| **Educación Primaria** | Decret 106/2022, de 5 d'agost (DOGV n.º 9403, 11/08/2022) | DOGV (Diari Oficial de la Generalitat Valenciana) | Estructurado |
| **Educación Secundaria Obligatoria** | Decret 107/2022, de 5 d'agost (DOGV n.º 9404, 12/08/2022) | DOGV (Diari Oficial de la Generalitat Valenciana) | Estructurado |
| **Bachillerato** | Decret 108/2022, de 5 d'agost (DOGV n.º 9405, 12/08/2022) | DOGV (Diari Oficial de la Generalitat Valenciana) | Estructurado |

> Los textos y disposiciones normativas se organizan en [`normativa/`](normativa/) siguiendo el estándar de metadatos de [nmarafo/open-lex-edu](https://github.com/nmarafo/open-lex-edu).

---

## 2. Singularidades y Contexto Autonómico para el Diseño de SDAs

Al diseñar Situaciones de Aprendizaje y Programaciones Didácticas para centros educativos de Comunitat Valenciana, los docentes y agentes de IA deben integrar:

* **Marco Lingüístico:** Cooficialidad lingüística: Valencià: Llengua i Literatura y Lengua Castellana.
* **Patrimonio y Realidad Territorial:** Ecosistemas mediterráneos (L'Albufera, marjal), patrimonio inmaterial (Falles, Fogueres, Misteri d'Elx, Tribunal de les Aigües), 9 d'Octubre (Dia de la Comunitat Valenciana)..
* **Atención a la Diversidad e Inclusión (DUA):** Aplicación universal de las tres redes neuronales del DUA (Representación, Acción/Expresión e Implicación), adaptando los andamiajes a la realidad sociocultural del centro.
* **Evaluación Criterial:** Calificación vinculada a los criterios de evaluación del currículo de Comunitat Valenciana, graduados mediante rúbricas analíticas oficiales.

---

## 3. Estructura de Directorios

```text
comunitat_valenciana/
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
