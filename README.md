# 🎓 OpenDidactia (Open Knowledge Framework - Didáctica y Currículo)

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC_BY--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/deed.es)
[![Framework: OKF](https://img.shields.io/badge/Framework-OKF_v1.3-blue.svg)](#arquitectura-okf)
[![Coverage: 17 CCAA + 2 Ciudades Autónomas](https://img.shields.io/badge/Cobertura-17_CCAA_+_Ceuta_y_Melilla-green.svg)](#-cobertura-curricular-nacional-por-comunidades-autónomas-17-ccaa--2-ciudades-autónomas)
[![Metodología: Activas + DUA + Merrill](https://img.shields.io/badge/Metodología-ABP_|_ApS_|_Design_Thinking_|_DUA_|_Merrill-orange.svg)](#-secuencia-oficial-de-diseño-curricular-para-agentes-de-ia)
[![Pensamiento Visible: Harvard Project Zero](https://img.shields.io/badge/Pensamiento_Visible-Project_Zero_|_Cooperativo-purple.svg)](docs/catalogo_rutinas_pensamiento_y_dinamicas_grupo.md)
[![NotebookLM: Cuaderno Oficial](https://img.shields.io/badge/NotebookLM-Cuaderno_Oficial-4285F4.svg)](https://notebook.google.com/notebook/2758ede6-33b4-4ca7-a77b-ee8ef99a9602)

Base de conocimiento estructurada y abierta basada en el estándar **Open Knowledge Framework (OKF)** para la gestión, diseño y generación asistida por Inteligencia Artificial de **Programaciones Didácticas (PD)** y **Situaciones de Aprendizaje (SDA)** plenamente adaptadas a la LOMLOE y a la totalidad del marco normativo autonómico español.

Integra de forma nativa el **Diseño Universal para el Aprendizaje (DUA)**, los **Principios Instruccionales de David Merrill**, **Rúbricas analíticas con graduadores**, **Metodologías Activas Vertebradoras** (ABP, ApS, Design Thinking, ABR...) y dinamización de aula mediante **Rutinas de Pensamiento Visible** (*Harvard Project Zero*) y **Estructuras Cooperativas** (*Spencer Kagan y Pere Pujolàs*).

Organizado territorialmente con **cobertura nacional 100% íntegra** para las **17 Comunidades Autónomas** y las **2 Ciudades Autónomas (Ceuta y Melilla)** en **Educación Infantil, Primaria, Educación Secundaria Obligatoria (ESO), Bachillerato y Formación Profesional**, en perfecta sincronía con el corpus de disposiciones normativas de [**nmarafo/open-lex-edu**](https://github.com/nmarafo/open-lex-edu).

---

### 🧭 Secuencia Oficial de Diseño Curricular para Agentes de IA

Cualquier modelo de lenguaje o agente autónomo que genere programaciones o situaciones de aprendizaje en OpenDidactia debe seguir de forma estricta este flujo secuencial de fases pedagógicas:

```text
┌─────────────────────────────────────────────────────────────────────────────────────────────┐
│ 0. ENTRADA DE DATOS CURRICULARES DE PARTIDA                                                 │
│    • CCAA, Etapa/Curso, Materia o Módulo y Horas (o fórmula sintética '2º ESO Música...').  │
│    • Particularidades de centro (entorno, talleres, proyectos de aula).                     │
└──────────────────────────────────────────────┬──────────────────────────────────────────────┘
                                               │
┌──────────────────────────────────────────────▼──────────────────────────────────────────────┐
│ 1. CONCRECIÓN CRITERIAL Y ASOCIACIÓN CON PRODUCTOS (100% DE CRITERIOS)                      │
│    • Inventario Previo: Lista obligatoria de todos los criterios oficiales (prohibido omitir).│
│    • Primaria, ESO y Bach.: Deconstrucción por defecto en 2 productos (con Descriptores).   │
│    • FP: Asociación del 100% de CEs de todos los RAs a productos (Mapa Alfanumérico).       │
│    • Línea de auditoría obligatoria de cobertura antes del control de fase.                 │
│    ► CONTROL DE FASE: ¿Deseas pasar a la siguiente fase o realizar ajustes?                 │
└──────────────────────────────────────────────┬──────────────────────────────────────────────┘
                                               │
┌──────────────────────────────────────────────▼──────────────────────────────────────────────┐
│ 2. ELABORACIÓN DE RÚBRICAS OFICIALES CON GRADUADORES (100% DE CRITERIOS)                    │
│    • Rúbricas analíticas para el 100% de criterios oficiales (prohibido emitir muestras).   │
│    • Rúbrica integral por criterio para optimización de longitud sin saturar el contexto.   │
│    • Invariabilidad del verbo cognitivo y nivel SU/BI idéntico al criterio oficial.         │
│    • Graduadores en **negrita**, ejemplos de productos y línea de auditoría de cierre.      │
│    ► CONTROL DE FASE: ¿Deseas pasar a la siguiente fase o realizar ajustes?                 │
└──────────────────────────────────────────────┬──────────────────────────────────────────────┘
                                               │
┌──────────────────────────────────────────────▼──────────────────────────────────────────────┐
│ INTEGRACIÓN DE OBJETIVOS, PLANES Y PROGRAMAS (SIN CONSULTA AL USUARIO)                     │
│    • Si constan en las fuentes aportadas, se integran directamente como ejes vertebradores. │
│    • Si no, se asignan aleatoriamente del banco simulando un centro ficticio de la etapa.  │
└──────────────────────────────────────────────┬──────────────────────────────────────────────┘
                                               │
┌──────────────────────────────────────────────▼──────────────────────────────────────────────┐
│ 3. SECUENCIACIÓN ANUAL DE LA PROGRAMACIÓN DIDÁCTICA (9 SAs / 9 UTs)                         │
│    • Distribución de contenidos en 9 unidades anuales (1ª eval: 1-3; 2ª: 4-6; 3ª: 7-9).      │
│    • Articulación con Efemérides (Calendario Escolar) o Calendario Profesional/Sectorial.    │
│    • Integración de Metodología Activa Vertebradora (ABP, ApS, Design Thinking, ABR...).     │
│    • Conexión con Objetivos/Planes/Programas (tomados de fuentes o del centro ficticio).    │
│    • Vinculación con los Productos e Instrumentos numerados del Paso 1.                     │
│    ► CONTROL DE FASE: ¿Deseas pasar a la siguiente fase o realizar ajustes?                 │
└──────────────────────────────────────────────┬──────────────────────────────────────────────┘
                                               │
┌──────────────────────────────────────────────▼──────────────────────────────────────────────┐
│ 4. ELABORACIÓN DE LA SITUACIÓN DE APRENDIZAJE / UT PARA EL DOCENTE                          │
│    • Fases instruccionales de David Merrill (Problema, Activación, Modelado, Práctica...).  │
│    • Mínimo de 2 tareas activas por sesión (con roles de docente y alumnado).               │
│    • Aplicación granular de las 3 Redes DUA (Representación, Acción y Expresión, Implica).  │
│    • Metodología activa: Rutinas de Pensamiento (Veo-Pienso-Me pregunto) y Cooperativo       │
│      (Lápices al centro, Folio Giratorio, 1-2-4...) procedimentados por tarea.               │
│    🔀 DECISIÓN: 1. Versión Alumnado | 2. Siguiente SA Docente | 3. Desarrollar Sesión [n.º]  │
└──────────────────────────────────────────────┬──────────────────────────────────────────────┘
                                               │
┌──────────────────────────────────────────────▼──────────────────────────────────────────────┐
│ 5. ELABORACIÓN DE LA SITUACIÓN DE APRENDIZAJE / UT PARA EL ALUMNADO                         │
│    • Guion motivador en 2ª persona sin jerga burocrática ("El Reto" o "El Encargo Cliente").│
│    • Desglose: Misión/Reto, Producto Final, Mapa de ruta en 3-4 etapas y Claves del éxito.  │
│    🔀 DECISIÓN: 1. Siguiente SA Docente | 2. Medidas de Apoyo (Fase 6 opcional)              │
└──────────────────────────────────────────────┬──────────────────────────────────────────────┘
                                               │
┌──────────────────────────────────────────────▼──────────────────────────────────────────────┐
│ 6. MEDIDAS DE APOYO, REFUERZO INDIVIDUALIZADO Y RECUPERACIÓN (OPCIONAL)                     │
│    • Carácter opcional a criterio del docente (se puede omitir y pasar directo a Canvas).   │
│    • Refuerzo continuo invisible y planes de pendientes con adaptación DUA / 5 principios FP│
│    ► CONTINUACIÓN: Transición directa a Fase 7 (Canvas HTML)                                 │
└──────────────────────────────────────────────┬──────────────────────────────────────────────┘
                                               │
┌──────────────────────────────────────────────▼──────────────────────────────────────────────┐
│ 7. HERRAMIENTA DE CALIFICACIÓN Y SEGUIMIENTO EN HTML AUTOCONTENIDO                          │
│    • Aplicación web interactiva completa en un solo archivo HTML (Tailwind + JS vanilla).  │
│    • Evaluación cualitativa (Infantil), criterial ponderada (Primaria/ESO/BAC) o RAs (FP).  │
│    • Anonimización estricta, tipología de alumnado, sobreescritura/recuperación y CSV.      │
│    ► SALIDA FINAL: 1. Generar HTML interactivo descargable | 2. Concluir                     │
└─────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 🤖 Prompt Maestro de Arranque para Agentes de IA

Para instruir a cualquier agente de IA (Gemini, Claude, GPT, DeepSeek, Ollama...) y que comience a trabajar con este repositorio, **copia y pega el siguiente bloque** indicando tu nivel, materia y comunidad (Ej.: *2º ESO Música Canarias*, *1º DAM Programación Canarias*, *3º Primaria Matemáticas Madrid*, *1º Bachillerato Filosofía Andalucía*...):

```markdown
Eres un docente experto en Programaciones Didácticas (PD) y Situaciones de Aprendizaje (SA/UT) LOMLOE/FP basado en el estándar OKF de OpenDidactia (https://github.com/nmarafo/OpenDidactia), con dominio de normativa estatal y autonómica (17 CCAA y Ceuta/Melilla), DUA, evaluación criterial, metodologías activas (ABP, ApS, Design Thinking, ABR...) y dinamización mediante pensamiento visible y aprendizaje cooperativo. Guíe y genere la PROGRAMACIÓN DIDÁCTICA (PD) y sus SITUACIONES DE APRENDIZAJE (SAs/UTs).

ESTÁNDAR OKF:
1. Currículo Externo Literal: Criterios, Saberes y Descriptores (en FP: RAs, CEs y contenidos) provienen de normativa EXTERNA y deben CALCARSE (prohibido inventar códigos o redacciones). El OKF (`docs/`, `comunidades/<ccaa>/`) aporta solo la metodología (DUA, Merrill, rúbricas, efemérides, plantillas) sin sustituir al currículo.
2. Trazabilidad Ontológica: Cadena estricta Currículo Externo -> Criterio/CE -> Descriptor/RA -> Producto tangible -> Rúbrica con graduadores -> Tareas de aula.
3. Validación con Esquemas: Coherencia formal con esquemas JSON (`schema/`).

Datos de partida (solicítelos o dedúzcalos de fórmula sintética, ej: "2º ESO Música Canarias", "1º DAM Programación Canarias"):
1. CCAA. 2. Etapa/Curso. 3. Materia/Área/Módulo (Ciclo/Familia en FP). 4. Horas semanales/anuales. 5. Contexto del centro.

REGLA INTER-FASES (MENÚS NUMERADOS):
Al concluir cada fase/unidad, DETÉNGASE y plantee el menú (responder solo con el número):
- Fases 1, 2 y 3: "¿Desean pasar a la siguiente fase? 1. Sí, avanzar | 2. Realizar ajustes".
- Fase 4: "¿Cómo desean proceder con [N.º y Título]? 1. Versión ALUMNADO (Fase 5) | 2. Siguiente SA DOCENTE | 3. Desarrollar Sesión [n.º]".
- Fase 5: "¿Cómo desean proceder? 1. Siguiente SA Docente | 2. Medidas de Apoyo (Fase 6 opcional)".
- Fase 6: "¿Diseñar medidas de apoyo? 1. Sí, plan apoyo | 2. No, pasar a Fase 7 (Canvas) | 3. Concluir".
- Fase 7: "¿Cómo desean proceder? 1. Generar HTML interactivo descargable | 2. Concluir".
*Ajustes: aplicarlos antes de avanzar. Opción 3 en Fase 4: desarrollar la sesión completa (tareas paso a paso, modelado, dinámicas, DUA y recursos). Cada entrega es definitiva y autosuficiente (sin pedir documentación previa).*

PROTOCOLO SECUENCIAL POR FASES:

---
### FASE 1: CONCRECIÓN CRITERIAL Y ASOCIACIÓN CON PRODUCTOS (EVIDENCIAS TANGIBLES)
El "Instrumento de Evaluación" es EXCLUSIVAMENTE el PRODUCTO TANGIBLE entregado por el alumnado (Podcast, Guía, Albarán, Informe, Maqueta, Cableado...).

COBERTURA CRITERIAL 100% OBLIGATORIA (PROHIBIDO MUESTREAR):
- Inventario previo: Antes de la tabla, liste todos los códigos oficiales a evaluar: `Criterios oficiales a evaluar (100% currículo): [1.1, 1.2, ..., Total: N]`.
- Cobertura total: Incluya y deconstruya TODOS Y CADA UNO de los criterios oficiales (del primero al último). PROHIBIDO omitir criterios, resumir, usar "etc." o presentar muestras parciales.
- Cierre con auditoría: Línea obligatoria antes del menú: `✅ Control de Cobertura Criterial: 100% cubierto (N de N criterios oficiales deconstruidos | 0 omitidos)`.

A. INFANTIL, PRIMARIA, ESO Y BACHILLERATO:
- Deconstruya cada Criterio en 2 Productos tangibles (ej: 1.1.1 y 1.1.2).
- Vincule Descriptores Operativos (o CC en EI), Saberes Básicos (Bloque y n.º) y cita textual evaluada. Reparta el 100% de descriptores. Código: [Criterio].[Secuencia] (ej: 1.1.1. Guía).
- Tabla: | N.º Criterio | Descriptores Operativos (o CC en EI) | Saberes Básicos (Bloque y N.º) | Cita Textual Evaluada | Instrumento (Producto Numerado) |

B. FORMACIÓN PROFESIONAL:
- RAs y CEs de TodoFP/BOE y orden autonómica (`docs/catalogo_familias_profesionales_todofp.md`).
- Asocie el 100% de Criterios (CEs) de TODOS los RAs a productos de taller/laboratorio que cubran el RA.
- Vincule RAs, CEs (letras oficiales), Contenidos (Bloque y n.º), OG y CPPS. Código: [RA].[CE].[Bloque].[OG].[CPPS].[Producto].
- Matriz: | N.º RA | Criterios de Evaluación (Letras CE) | Contenidos Básicos (Bloque y N.º) | OG y CPPS | Instrumento (Producto Alfanumérico) |
[AL COMPLETAR: Imprima línea de auditoría y menú de Fase 1].

---
### FASE 2: RÚBRICAS ANALÍTICAS CON GRADUADORES (COBERTURA 100%)
Para el 100% de Criterios e Instrumentos de Fase 1 (SIN OMITIR NINGUNO), elabore su Rúbrica Analítica:
- Cobertura universal: Prohibido omitir criterios, truncar o incluir rúbricas "de ejemplo". Deben redactarse para todos los criterios.
- Rúbrica integral por criterio: Para abarcar el 100% sin truncamiento, genere una rúbrica analítica integral por criterio que gradúe conjuntamente sus 2 productos.
- Regla 2.1 (Verbo invariable): Verbo principal IDÉNTICO en los 4 niveles.
- Regla 2.2 (Fidelidad SU/BI): Nivel Suficiente/Bien (5-6) reproduce literalmente el criterio/CE oficial.
- Regla 2.3 (Graduadores en negrita): Resalte en **negrita** graduadores de Calidad, Autonomía o PRL.
- Regla 2.4 (Sin "No"): En Insuficiente describa el error técnico; nunca "No lo hace".
- Regla 2.5 (Ejemplo tangible): Cada nivel incluye un ejemplo concreto del producto.
- Niveles: | Insuficiente (1-4 / PA en EI) | Suficiente/Bien (5-6 / AD en EI) | Notable (7-8 / MA en EI) | Sobresaliente (9-10 / EX en EI) |
- Cierre con auditoría: Línea obligatoria antes del menú: `✅ Control de Cobertura de Rúbricas: 100% cubierto (N de N criterios con rúbrica analítica completa | 0 omitidos)`.
[AL COMPLETAR: Imprima línea de auditoría y menú de Fase 2].

---
### INTEGRACIÓN AUTOMÁTICA DE OBJETIVOS, PLANES Y PROGRAMAS (SIN CONSULTA)
El agente NO formula preguntas sobre este aspecto:
- Si constan en fuentes/datos: se integran como ejes transversales en las 9 SAs/UTs.
- Si NO constan: se integran directamente desde `docs/banco_objetivos_planes_y_programas_ccaa.md` simulando un centro ficticio (1-2 objetivos, 2 planes institucionales y 1-2 programas de CCAA o FP) sin detenerse ni pedir confirmación.

---
### FASE 3: SECUENCIACIÓN ANUAL DE LA PROGRAMACIÓN (9 SAs / 9 UTs)
Distribuya contenidos en 9 Unidades (3 por trimestre: 1ª Eval: U1-U3; 2ª: U4-U6; 3ª: U7-U9).
Tabla matriz anual: 1. N.º y Título motivador / reto. 2. Temporalización (semanas y horas). 3. Criterios/CEs y Saberes Básicos (Bloque y n.º; en FP: RAs, CEs y Contenidos). 4. Efemérides o Calendario Profesional. 5. Metodología Activa justificada (ABP, ApS, Design Thinking...) y conexión con Objetivos/Planes/Programas (fuentes o centro ficticio). 6. Instrumentos (productos de Fase 1 con rúbricas de Fase 2).
[AL COMPLETAR: Aplique menú de Fase 3].

---
### FASE 4: ELABORACIÓN DE LA SA / UT PARA EL DOCENTE
Para la unidad a abordar (iniciando en U1), genere la versión técnica docente (documento independiente):
- Metodología Activa Vertebradora (ABP, ApS, Design Thinking, ABR...) justificada.
- Temporalización y elementos curriculares: Criterios/CEs y Saberes Básicos (Bloque y n.º).
- Estructura instruccional de David Merrill (en FP: taller práctico con modelaje y PRL obligatoria).
- Cada sesión incluye MÍNIMO 2 TAREAS activas detallando:
  1. Título y duración (minutos).
  2. Rol docente y rol discente.
  3. Dinámica/Rutina obligatoria: catálogo de pensamiento/cooperativo (ej: 1-2-4, Folio Giratorio, 3-2-1 Puente, Scrum) detallando en 2 líneas dinamización (roles, reglas, materiales).
  4. Agrupamiento (individual, parejas, equipos cooperativos, gran grupo).
  5. DUA Granular (3 Redes): Representación (apoyos visuales, QR), Acción/Expresión (checklists, menús), Implicación (roles, retos, feedback).
  6. Instrumento/Producto evaluable de la tarea (si aplica).
  7. Saberes Básicos / Contenidos movilizados (Bloque y n.º).
  8. Recursos y EPIs obligatorios.
[AL COMPLETAR: DETÉNGASE y plantee menú de Fase 4].

---
### FASE 5: ELABORACIÓN DE LA SA / UT PARA EL ALUMNADO
Documento complementario e independiente para el estudiante:
- Tono motivador ("El Reto" o "El Encargo del Cliente") sin tecnicismos burocráticos.
- Desglose: 1. Desafío/Misión; 2. Producto Final; 3. Mapa de Ruta (3-4 etapas); 4. Claves del Éxito (rúbrica visual y autoevaluación), conectado a Saberes Básicos (Bloque y n.º).
[AL COMPLETAR: Aplique menú de Fase 5].

---
### FASE 6 (OPCIONAL): MEDIDAS DE APOYO, REFUERZO Y RECUPERACIÓN
Carácter opcional. Privacidad estricta ([DATOS ANONIMIZADOS]).
- Evaluación Continua: Refuerzo no segregador en las siguientes 3 unidades citando Criterios y Saberes (Bloque y n.º).
- Pendientes: Plan trimestral con DUA; en FP aplica los 5 principios (focalización RAs/CEs clave, DUA, evaluación flexible, cronograma y checklists).
[AL COMPLETAR: Pase a Fase 7 (Canvas)].

---
### FASE 7: HERRAMIENTA DE CALIFICACIÓN Y SEGUIMIENTO EN HTML AUTOCONTENIDO
Genera una app web interactiva local en un ÚNICO ARCHIVO HTML autocontenido (Tailwind CSS CDN + JS vanilla modular):
- Privacidad: Alumnado anonimizado ("Alumno 01", "Alumna 02"). Prohibido requerir datos reales.
- Infantil: Evaluación exclusivamente cualitativa (PA, AD, MA, EX; sin notas numéricas), historial interactivo, Informe Final (Competencias Clave) y exportación `.csv`.
- Primaria, ESO y Bachillerato: Calificación numérica (1-10) por Criterio y Producto; equivalencias (PA 1-4, AD 5-6, MA 7-8, EX 9-10); matriz de 9 SAs; gestión de alumnado (alias, recuperación con recálculo) y exportación `.csv`.
- FP: Registro numérico (1-10) por CE y producto; cálculo de RA (>= 5); 9 UTs; recuperación con sobreescritura de RA; exportación `.csv`.
[AL COMPLETAR: Aplique menú de Fase 7].
```

---

## 📓 Uso directo con Google NotebookLM

También puedes utilizar **Google NotebookLM** como entorno de trabajo guiado para diseñar tus programaciones y situaciones de aprendizaje siguiendo las siguientes instrucciones:

1. **Enlace al siguiente cuaderno de NotebookLM:** [https://notebook.google.com/notebook/2758ede6-33b4-4ca7-a77b-ee8ef99a9602](https://notebook.google.com/notebook/2758ede6-33b4-4ca7-a77b-ee8ef99a9602)
2. **Copiar el cuaderno.**
3. **Añadir el currículo del área/Materia correspondiente** (suministrado externamente a través de [open-lex-edu](https://github.com/nmarafo/open-lex-edu), boletines oficiales o documentos curriculares oficiales; es de donde se extraen y calcan literalmente los criterios, competencias y saberes).
4. **En el chat poner la palabra “Comenzar”**.

---

## 🏛️ Cobertura Curricular Nacional por Comunidades Autónomas (17 CCAA + 2 Ciudades Autónomas)

Con la actualización del repositorio jurídico hermano [**nmarafo/open-lex-edu**](https://github.com/nmarafo/open-lex-edu), que ha incorporado los **52 decretos y órdenes curriculares autonómicos** de las 14 comunidades restantes (alcanzando 696 disposiciones normativas OKF auditadas con 0 incidencias), **OpenDidactia cuenta con cobertura curricular y pedagógica completa para todo el territorio del Estado español**.

Cualquier docente o agente de IA puede generar de forma rigurosa su programación didáctica o situación de aprendizaje para **cualquiera de las 17 Comunidades Autónomas o las 2 Ciudades Autónomas**, vinculando los descriptores operativos, criterios de evaluación, saberes básicos autonómicos y ponderaciones vigentes:

| Comunidad Autónoma / Ámbito | Boletín Oficial | Educación Infantil | Educación Primaria | Educación Secundaria Obligatoria | Bachillerato | Formación Profesional | Directorio Territorial |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Andalucía** | BOJA | D 100/2023 | D 101/2023 | D 102/2023 | D 103/2023 | D 102/2024 / O 18/9/2025 | [`comunidades/andalucia/`](comunidades/andalucia/) |
| **Aragón** | BOA | O ECD/853/2022 | O ECD/1112/2022 | O ECD/1172/2022 | O ECD/1173/2022 | D 105/2024 | [`comunidades/aragon/`](comunidades/aragon/) |
| **Asturias (Principado de)** | BOPA | D 56/2022 | D 57/2022 | D 59/2022 | D 60/2022 | D 48/2024 | [`comunidades/asturias/`](comunidades/asturias/) |
| **Illes Balears** | BOIB | D 30/2022 | D 31/2022 | D 32/2022 | D 33/2022 | D 36/2024 | [`comunidades/baleares/`](comunidades/baleares/) |
| **Canarias** | BOC | D 196/2022 / D 30/2023 | D 211/2022 / D 30/2023 | D 30/2023 / D 34/2023 | D 30/2023 / D 36-37/2023 | RD 659/2023 / Res. 30/10/2024 | [`comunidades/canarias/`](comunidades/canarias/) |
| **Cantabria** | BOC | D 66/2022 | D 66/2022 | D 73/2022 | D 73/2022 | D 45/2024 | [`comunidades/cantabria/`](comunidades/cantabria/) |
| **Castilla-La Mancha** | DOCM | D 80/2022 | D 81/2022 | D 82/2022 | D 83/2022 | D 39/2024 | [`comunidades/castilla_la_mancha/`](comunidades/castilla_la_mancha/) |
| **Castilla y León** | BOCyL | D 37/2022 | D 38/2022 | D 39/2022 | D 40/2022 | D 24/2024 | [`comunidades/castilla_y_leon/`](comunidades/castilla_y_leon/) |
| **Cataluña (Catalunya)** | DOGC | D 21/2023 | D 175/2022 | D 175/2022 | D 171/2022 | D 124/2024 | [`comunidades/catalunya/`](comunidades/catalunya/) |
| **Comunitat Valenciana** | DOGV | D 100/2022 | D 106/2022 | D 107/2022 | D 108/2022 | D 74/2024 | [`comunidades/comunitat_valenciana/`](comunidades/comunitat_valenciana/) |
| **Extremadura** | DOE | D 98/2022 | D 107/2022 | D 110/2022 | D 109/2022 | D 58/2024 | [`comunidades/extremadura/`](comunidades/extremadura/) |
| **Galicia** | DOG | D 150/2022 | D 155/2022 | D 156/2022 | D 157/2022 | D 56/2024 | [`comunidades/galicia/`](comunidades/galicia/) |
| **La Rioja** | BOR | D 36/2022 | D 41/2022 | D 42/2022 | D 43/2022 | D 29/2024 | [`comunidades/la_rioja/`](comunidades/la_rioja/) |
| **Madrid (Comunidad de)** | BOCM | D 36/2022 | D 61/2022 | D 65/2022 | D 64/2022 | D 27/2025 / D 49/2024 | [`comunidades/madrid/`](comunidades/madrid/) |
| **Murcia (Región de)** | BORM | D 196/2022 | D 209/2022 | D 235/2022 | D 251/2022 | D 92/2024 | [`comunidades/murcia/`](comunidades/murcia/) |
| **Navarra (C. Foral de)** | BON | DF 61/2022 | DF 67/2022 | DF 71/2022 | DF 72/2022 | DF 41/2024 | [`comunidades/navarra/`](comunidades/navarra/) |
| **País Vasco (Euskadi)** | BOPV | D 75/2023 | D 77/2023 | D 77/2023 | D 76/2023 | D 82/2024 | [`comunidades/pais_vasco/`](comunidades/pais_vasco/) |
| **Ceuta y Melilla** | BOE | RD 95/2022 / O EFP/608 | RD 157/2022 / O EFP/678 | RD 217/2022 / O EFP/754 | RD 243/2022 / O EFP/755 | RD 659/2023 | [`comunidades/ceuta_y_melilla/`](comunidades/ceuta_y_melilla/) |
| **Enseñanzas Mínimas Estatales** | BOE | **RD 95/2022** | **RD 157/2022** | **RD 217/2022** | **RD 243/2022** | **LO 3/2022 / RD 659/2023** | [open-lex-edu estatal](https://github.com/nmarafo/open-lex-edu) |

> ℹ️ **Suministro Curricular Externo y Sincronización Jurídica:** El corpus legislativo íntegro y consolidado con las disposiciones autonómicas, articulados y anexos de competencias específicas, criterios de evaluación y saberes básicos auditados reside en el repositorio jurídico externo [**open-lex-edu**](https://github.com/nmarafo/open-lex-edu) y en los boletines oficiales correspondientes. OpenDidactia opera exclusivamente como el framework metodológico y operativo del que se nutre el agente para estructurar y aplicar dicho currículo en el aula, debiendo **calcarse fielmente** los elementos curriculares de la fuente externa sin ser inventados.

---

## 📁 Estructura del Repositorio

```text
OpenDidactia/
├── README.md                            # Presentación, protocolo de 9 pasos, cobertura nacional y prompt maestro
├── LICENSE.md                           # Licencia CC BY-SA 4.0 y requisitos de atribución
├── .gitignore
├── schema/                              # Esquemas de validación formales (JSON Schema)
│   ├── esquema_programacion_didactica.json # Validación de PDs anuales de Régimen General (9 SAs)
│   ├── esquema_situacion_aprendizaje.json  # Validación de SDAs (Merrill + DUA granular)
│   ├── esquema_programacion_modulo_fp.json # Validación de Programaciones de Módulos de FP (LOOIFP / RD 659)
│   └── esquema_unidad_trabajo_fp.json   # Validación de SA-UT competenciales en FP (ABR/ASC + Taller)
├── docs/                                # Documentación técnica y metodológica
│   ├── flujo_agente_elaboracion_pd_sa.md   # Protocolo maestro pormenorizado para Agentes de IA
│   ├── catalogo_rutinas_pensamiento_y_dinamicas_grupo.md # Base de conocimiento: Pensamiento visible y cooperativo
│   ├── catalogo_metodologias_aprendizaje.md # Base de conocimiento: Metodologías activas (ABP, ApS, Design Thinking...)
│   ├── guia_elaboracion_programaciones_y_ut_fp.md # GUÍA OFICIAL PARA FORMACIÓN PROFESIONAL (9 Fases)
│   ├── catalogo_familias_profesionales_todofp.md # Catálogo oficial: 26 Familias Profesionales y títulos TodoFP (MEFPD)
│   ├── banco_objetivos_planes_y_programas_ccaa.md # Banco de Objetivos, Planes y Programas oficiales por CCAA y FP
│   ├── catalogo_efemerides_calendario_escolar_ccaa.md # Calendario escolar, efemérides de las 17 CCAA y calendario sectorial FP
│   ├── guia_elaboracion_rubricas_graduadores.md # Informe técnico: Rúbricas con graduadores
│   ├── guia_operacionalizacion_dua.md      # DUA granular en sesiones y contexto autonómico
│   ├── ecosistema_herramientas_activas.md  # Merrill, cooperativo, rutinas y efemérides
│   ├── guia_planes_apoyo_y_recuperacion.md # Planes de refuerzo continuo y recuperación
│   ├── arquitectura_okf.md                 # Especificación del estándar OKF para didáctica
│   ├── taxonomia_curricular_lomloe.md      # Grafo curricular y relaciones competenciales
│   ├── guia_situaciones_aprendizaje.md     # Fundamentos pedagógicos de las SDAs
│   └── guia_programaciones_didacticas.md   # Fundamentos de la planificación anual
├── plantillas/                          # Plantillas operativas oficiales
│   ├── plantilla_situacion_aprendizaje.md  # Plantilla enriquecida para SDAs (Infantil/Primaria/ESO/Bachillerato)
│   ├── plantilla_programacion_didactica.md # Plantilla enriquecida para PDs anuales de Régimen General
│   ├── plantilla_unidad_trabajo_sa_fp.md   # Plantilla oficial de SA-UT para Formación Profesional (Docente + Alumnado)
│   ├── plantilla_programacion_modulo_fp.md # Plantilla oficial de Programación de Módulo Profesional de FP
│   └── prompts/                         # Biblioteca modular de Prompts del Sistema
│       ├── prompt_maestro_arranque_agente.md # PROMPT MAESTRO DE ARRANQUE GENERAL (Todas las etapas + FP)
│       ├── prompt_01_deconstruccion_criterios.md
│       ├── prompt_02_elaboracion_rubricas_graduadores.md
│       ├── prompt_03_secuenciacion_programacion_anual.md
│       ├── prompt_04_desarrollo_sa_docente_merrill_dua.md
│       ├── prompt_05_sa_para_alumnado.md
│       ├── prompt_06_plan_apoyo_refuerzo_individualizado.md
│       ├── prompt_07_plan_recuperacion_pendientes.md
│       ├── prompt_08_herramienta_calificacion_canvas.md
│       ├── prompt_fp_01_relacion_ra_ce_productos.md          # [FP] Mapa de relaciones RA-CE-Productos
│       ├── prompt_fp_02_rubricas_tecnicas_graduadores.md     # [FP] Rúbricas técnicas con graduadores
│       ├── prompt_fp_03_secuenciacion_ut_modulo.md           # [FP] Secuenciación anual de UTs
│       ├── prompt_fp_04_desarrollo_ut_docente_taller_merrill.md # [FP] SA-UT docente (Merrill taller + DUA)
│       ├── prompt_fp_05_ut_para_alumnado_encargo_cliente.md  # [FP] SA-UT alumnado ("Encargo de Cliente")
│       ├── prompt_fp_06_plan_recuperacion_ra_pendientes_fp.md# [FP] Poda curricular y evaluación flexible
│       └── prompt_fp_07_herramienta_calificacion_canvas_fp.md# [FP] Canvas interactivo de calificación FP
└── comunidades/                         # Base territorial completa por Comunidades Autónomas (17 CCAA + Ceuta y Melilla)
    ├── andalucia/, aragon/, asturias/, baleares/, canarias/, cantabria/, castilla_la_mancha/,
    ├── castilla_y_leon/, catalunya/, ceuta_y_melilla/, comunitat_valenciana/, extremadura/,
    ├── galicia/, la_rioja/, madrid/, murcia/, navarra/, pais_vasco/
    │   ├── README.md                    # Identificación del marco autonómico, contexto cultural y lingüístico
    │   ├── orientaciones_elaboracion_pd_sa.md # Guía metodológica adaptada a la CCAA y FP (evaluación, DUA)
    │   ├── plantilla_programacion_didactica.md # Plantilla oficial de PD anual adaptada (9 SDAs)
    │   └── plantilla_situacion_aprendizaje.md # Plantilla oficial de SDA adaptada (Merrill + DUA)
    └── canarias/
        ├── guias_oficiales/             # Documentos técnicos oficiales en PDF de referencia metodológica
        └── ejemplos/                    # Modelos de referencia didáctica
```

---

## 🔗 Sinergia con `nmarafo/open-lex-edu`

Este repositorio complementa y se apoya bidireccionalmente en el marco normativo de **[open-lex-edu](https://github.com/nmarafo/open-lex-edu)**:
* **open-lex-edu (696 normas OKF - Pilar Jurídico y Curricular Externo):** Proporciona el corpus legal completo, consolidado y auditado de la normativa educativa estatal y de las **17 Comunidades Autónomas más Ceuta y Melilla** en formato OKF (con el 100% de los decretos y órdenes de ordenación y currículos LOMLOE). Es la fuente obligatoria de la que se **extraen y calcan literalmente** los elementos curriculares (competencias específicas, criterios, saberes básicos, RAs y CEs).
* **OpenDidactia (Pilar Pedagógico y Operativo OKF):** Framework de ingeniería didáctica que proporciona las guías operativas, instrucciones metodológicas (David Merrill, DUA granular), rúbricas analíticas con graduadores, matrices de secuenciación anual, catálogos pedagógicos (efemérides, dinámicas cooperativas, rutinas de pensamiento), esquemas JSON de validación de programaciones y herramientas de aula.

---

## 📄 Licencia y Atribución

Este repositorio y todos sus contenidos se distribuyen bajo los términos de la licencia **[Creative Commons Atribución-CompartirIgual 4.0 Internacional (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/deed.es)**.

### Cláusula de Atribución Obligatoria
En cualquier obra derivada, adaptación o integración en sistemas informáticos o de inteligencia artificial, **debe incluirse la siguiente mención explícita**:

> *Basado en los repositorios [OpenDidactia](https://github.com/nmarafo/OpenDidactia) y [open-lex-edu](https://github.com/nmarafo/open-lex-edu) creados por **Norberto Martín Afonso**, distribuidos bajo licencia Creative Commons Atribución-CompartirIgual 4.0 Internacional (CC BY-SA 4.0).*
