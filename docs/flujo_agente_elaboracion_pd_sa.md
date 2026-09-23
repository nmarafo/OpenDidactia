# 🧭 Protocolo Oficial de 9 Pasos para Agentes de IA: Elaboración de Programaciones Didácticas y Situaciones de Aprendizaje (Canarias)

Este documento constituye la **guía maestra de instrucciones y procedimientos** para que cualquier Agente de Inteligencia Artificial (o docente) elabore paso a paso, con rigor metodológico y jurídico pleno, una **Programación Didáctica (PD)** completa y sus correspondientes **Situaciones de Aprendizaje (SDA)** según el modelo oficial de la **Consejería de Educación del Gobierno de Canarias** (*LOMLOE*).

---

## 🗺️ Mapa del Flujo de Trabajo en Fases Pedagógicas

```text
[ 📌 PASO 0: Datos de Partida (Etapa, Materia/Módulo, Nivel, CCAA) ]
                                │
                                ▼
[ PASO 1: Concreción Criterial / Deconstrucción e Instrumentos (Productos) ]
                                │
                                ▼  ◄─── [Pausa de Control Inter-Fase: Avanzar o Ajustar]
[ PASO 2: Elaboración de Rúbricas Oficiales con Graduadores y Ejemplos ]
                                │
                                ▼  ◄─── [Pausa de Control Inter-Fase: Avanzar o Ajustar]
[ PASO 3: Activación del Ecosistema Metodológico (Merrill, DUA, Calendario, Red InnovAS) ]
                                │
                                ▼  ◄─── [Integración Automática: Fuentes o Centro Ficticio]
[ PASO 4: Secuenciación Anual de la Programación Didáctica (9 SAs por Trimestres) ]
                                │
                                ▼  ◄─── [Pausa de Control Inter-Fase: Avanzar o Ajustar]
[ PASO 5: Elaboración de la SA para el Docente (Sesiones Merrill + DUA Granular) ]
                                │
                                ├──────► 🔀 [Menú: 1. Versión Alumnado | 2. Siguiente SA | 3. Detallar Sesión]
                                ▼
[ PASO 6: Elaboración de la SA para el Alumnado (Guion Cercano "El Reto") ]
                                │
                                ▼  ◄─── 🔀 [Menú: 1. Siguiente SA Docente | 2. Medidas de Apoyo]
[ PASO 7 Y 8 (OPCIONAL): Medidas de Apoyo, Refuerzo Continuo y Recuperación ]
                                │       (El docente decide si ejecutarlas u omitirlas)
                                ▼  ◄─── [Transición directa a Paso 9 (Canvas)]
[ PASO 9: Herramienta de Calificación y Seguimiento en HTML Autocontenido ]
                                │
                                ▼  ◄─── [Menú Final: 1. Descargar HTML interactivo | 2. Concluir]
```

### 📋 Regla Obligatoria de Interacción Inter-Fases (Preguntas Claras con Menú Numerado)
Al concluir cada fase o unidad didáctica, el agente **se detiene obligatoriamente** y formula una **pregunta clara con opciones numeradas** para que el usuario responda indicando solo el número (ej. `1`, `2` o `3`):

* **Al concluir Paso 1, Paso 2 o Paso 4 (Secuenciación Anual):**
  > *"¿Deseas pasar a la siguiente fase?*  
  > *1. Sí, avanzar a la siguiente fase.*  
  > *2. Realizar ajustes en esta fase."*

* **Al concluir cada SA para el Docente (Paso 5):**
  > *"¿Cómo deseas proceder con esta unidad ([N.º y Título de la SA])?*  
  > *1. Diseñar versión ALUMNADO (Paso 6) de esta misma unidad (versión comunicativa 'El Reto').*  
  > *2. Desarrollar siguiente SA DOCENTE (Paso 5) (pasar a diseñar la siguiente unidad).*  
  > *3. Desarrollar con más detalle la Sesión [indicar n.º de Sesión] (desglose minucioso paso a paso de tareas, modelado docente, preguntas guía, andamiajes DUA y recursos específicos)."*  
  > *(Si se elige la opción 3 o se solicita más detalle de una sesión concreta, el agente la desarrolla exhaustivamente antes de continuar).*

* **Al concluir cada SA para el Alumnado (Paso 6):**
  > *"¿Cómo deseas proceder?*  
  > *1. Continuar con la siguiente SA Docente (Paso 5).*  
  > *2. Pasar a Medidas de Apoyo y Refuerzo (Pasos 7 y 8 opcionales) si ya se completaron las 9 unidades."*

* **Al llegar al Punto de Decisión de Medidas de Apoyo (Pasos 7 y 8 - Opcional):**
  > *"¿Deseas diseñar las medidas de apoyo ordinario, refuerzo continuo y recuperación (Pasos 7 y 8)?*  
  > *1. Sí, elaborar el plan de refuerzo y recuperación.*  
  > *2. No, omitir estas medidas y pasar directamente a la Herramienta Canvas (Paso 9).*  
  > *3. No, dar por concluida la programación didáctica aquí."*

* **Al finalizar la Herramienta Canvas (Paso 9):**
  > *"¿Cómo deseas proceder?*  
  > *1. Generar el archivo interactivo autocontenido HTML/Canvas descargable.*  
  > *2. Dar por concluida la programación didáctica."*

*Cada salida generada en el chat es definitiva, completa y autosuficiente, por lo que no se solicita generar documentación formal intermedia.*

---

## PASO 1: Deconstrucción de Criterios de Evaluación

### Definición Terminológica Esencial
* **"Instrumento de Evaluación"**: En el modelo canario se refiere **exclusivamente al PRODUCTO, EVIDENCIA O TAREA TANGIBLE** que el alumnado elabora y entrega (ej. *Guía de Audición, Podcast, Mural, Informe de Laboratorio, Maqueta, Ponencia Oral*). No se refiere a la herramienta de calificación (la rúbrica o escala).

### Reglas de Procesamiento para el Agente:
1. **Inventario del Criterio:** Identificar el texto íntegro oficial del Criterio de Evaluación, la relación completa de sus Descriptores Operativos asociados (en Primaria, ESO y Bachillerato) o Competencias Clave (en Infantil) y los Saberes Básicos vinculados indicando su Bloque y número oficial.
2. **Diseño de Productos (Regla por Defecto: 2 Productos):** Deconstruir por defecto cada Criterio de Evaluación en **EXACTAMENTE 2 Instrumentos de Evaluación** (Productos tangibles: ej. 1.1.1 y 1.1.2) que cubran armónicamente la totalidad de su redacción.
3. **Relación Curricular Obligatoria (Regla de Oro):**
   * A cada uno de los 2 Productos diseñados se le relacionan obligatoriamente sus **Descriptores Operativos específicos** (excepto en Educación Infantil, donde se asocian Competencias Clave al no haber descriptores operativos de salida) y los **Saberes Básicos (citando Bloque y número oficial según el currículo)**.
   * Repartir la **totalidad** de los descriptores oficiales del criterio entre los 2 productos diseñados (**no puede quedar ningún descriptor sin asignar**).
4. **Formato Numérico Estándar:** Cada instrumento se numera como `[Criterio].[Secuencia]` (ej: `1.1.1. Guía de Audición`, `1.1.2. Infografía de Hábitos Saludables`).
5. **Tabla de Deconstrucción Obligatoria:**
   * `N.º Criterio` | `Descriptores Operativos / Comp. Clave` | `Saberes Básicos (Bloque y N.º Oficial)` | `Parte del Criterio Evaluada (Cita Textual)` | `Instrumento de Evaluación (Producto Numerado)`

> **Pausa de Control Inter-Fase:** Al finalizar el Paso 1, pregunta al docente si desea pasar a la siguiente fase o realizar ajustes.

---

## PASO 2: Elaboración de Rúbricas con Graduadores

Basado en el *Informe Técnico: Uso de Graduadores en la Evaluación Competencial (Modelo LOMLOE Canarias)*:

### Reglas de Oro en el Diseño de Rúbricas:
1. **Invariabilidad del Verbo Cognitivo:**
   * **PROHIBIDO cambiar el verbo del criterio entre niveles** (a diferencia de Bloom tradicional). Si el criterio prescribe *"Analizar"*, el nivel Insuficiente analiza (con graves errores o de forma incompleta) y el Sobresaliente analiza (críticamente y con máxima precisión).
2. **Fidelidad al Criterio en Suficiente/Bien (SU/BI):**
   * El nivel `SU/BI` corresponde a la **redacción literal del criterio** (es el estándar mínimo aprobatorio).
3. **Modulación mediante Graduadores en Negrita:**
   * Los niveles se gradúan mediante adjetivos y adverbios (*graduadores*) que deben escribirse en **negrita** (ej. **con imprecisiones significativas**, **adecuadamente**, **con gran rigor**, **con máxima precisión e iniciativa**).
4. **Las 4 Dimensiones de Graduación:**
   * **Calidad y Precisión:** Mide el rigor técnico y la exactitud.
   * **Autonomía:** Mide la dependencia respecto al docente (**con ayuda constante**, **de manera guiada**, **con autonomía**, **con plena autonomía y liderazgo**).
   * **Profundidad y Complejidad:** Mide el nivel de procesamiento (**fragmentada**, **comprensiva**, **analítica**, **crítica y reflexiva**).
   * **Actitud y Frecuencia:** Regularidad y disposición.
5. **Erradicar el "No":** En el nivel Insuficiente, no utilizar la fórmula negativa *"No lo hace"*, sino describir la naturaleza de la limitación (*"Lo realiza con errores graves..."*).
6. **Ejemplo Tangible del Producto:** En cada nivel de logro, incluir un ejemplo descriptivo concreto de cómo luce el producto elaborado por el estudiante.

> **Pausa de Control Inter-Fase:** Al finalizar el Paso 2, pregunta al docente si desea pasar a la siguiente fase o realizar ajustes.

---

## PASO 3: Base de Conocimiento y Ecosistema de Herramientas Activas

Para planificar la secuencia anual y las sesiones diarias, el agente debe activar e integrar obligatoriamente las bases de conocimiento de OpenDidactia:
1. **Bases de Conocimiento Pedagógicas Oficiales:**
   * 📖 [Catálogo de Rutinas de Pensamiento y Dinámicas de Grupo](catalogo_rutinas_pensamiento_y_dinamicas_grupo.md): *Veo-Pienso-Me Pregunto, 3-2-1 Puente, Palabra-Idea-Frase, Círculo de Puntos de Vista, Comparar-Contrastar, Antes pensaba - Ahora pienso, Lápices al centro, Folio Giratorio, 1-2-4, Rompecabezas (Jigsaw), Parada de 3 minutos, etc.*
   * 📖 [Catálogo de Metodologías Activas de Aprendizaje](catalogo_metodologias_aprendizaje.md): *Aprendizaje Basado en Proyectos (ABP), Aprendizaje y Servicio (ApS), Design Thinking, Aprendizaje Basado en Retos (ABR), Aprendizaje Basado en Problemas, Flipped Classroom, Gamificación/ABJ, Cooperativo formal, Estaciones/Paisajes e Indagación STEAM.*
2. **Calendario Escolar y Efemérides:** Integrar fechas significativas autonómicas e hitos internacionales en cada trimestre consultando el 📖 [Catálogo de Efemérides del Calendario Escolar, Hitos Autonómicos y Calendario Sectorial FP](catalogo_efemerides_calendario_escolar_ccaa.md).
3. **Fases de David Merrill para el Diseño Instruccional:**
   * *Fase 1: Tarea / Problema central.*
   * *Fase 2: Activación de experiencias previas.*
   * *Fase 3: Demostración (modelado).*
   * *Fase 4: Aplicación práctica guiada.*
   * *Fase 5: Integración y transferencia a la vida real.*
4. **Planes y Programas del Centro:** Integración con el PIDAS (Red Canaria InnovAS o equivalente autonómico), plan de lectura, sostenibilidad y convivencia (tomados de las fuentes aportadas o asignados automáticamente para un centro ficticio de la etapa).

---

## Integración Automática de Objetivos, Planes y Programas de Centro (Sin Consulta Previa)

El agente **NO realiza ninguna indicación ni consulta previa al usuario al respecto**. La articulación de la Programación Anual (Paso 4) con los Objetivos Prioritarios del Centro y sus Planes y Programas Institucionales se realiza de manera totalmente autónoma y fluida:

- **Si se encuentran entre las fuentes aportadas:** Se tendrán en cuenta y se integran como ejes transversales y vertebradores en la matriz de la programación anual (Paso 4).
- **Si NO se encuentran entre las fuentes:** Se añadirán de manera aleatoria a partir del [Banco de Objetivos, Planes y Programas por CCAA](banco_objetivos_planes_y_programas_ccaa.md) como si fuese un centro ficticio donde se imparta la etapa (asignando automáticamente 1-2 objetivos de centro prioritarios coherentes con la etapa, 2 planes institucionales —Plan de Convivencia y Plan Digital de Centro— y 1-2 programas o redes oficiales de la Comunidad Autónoma correspondiente, ej. Red InnovAS en Canarias, CIMA en Andalucía, etc.), garantizando una contextualización realista sin interrumpir el flujo ni formular preguntas.

---

## PASO 4: Secuenciación Anual de la Programación (9 SAs)

La Programación Didáctica Anual se articula en **9 Situaciones de Aprendizaje** distribuidas en 3 trimestres:
* **1.º Trimestre (Septiembre - Diciembre):** SA 1, SA 2 y SA 3.
* **2.º Trimestre (Enero - Marzo):** SA 4, SA 5 y SA 6.
* **3.º Trimestre (Abril - Junio):** SA 7, SA 8 y SA 9.

Cada SA de la tabla anual debe especificar:
* Número y Título motivador.
* Trimestre y número de sesiones estimadas.
* Criterios de evaluación y Saberes Básicos implicados mencionando obligatoriamente el Bloque y el número oficial que le corresponde según el currículo.
* **Metodología Activa Vertebradora:** Asignación explícita de la metodología rectora de cada SA (ABP, ApS, Design Thinking, ABR, etc., según el [Catálogo de Metodologías](catalogo_metodologias_aprendizaje.md)), justificando brevemente su adecuación al reto.
* Conexión con efemérides del calendario escolar y Objetivos Prioritarios / Planes de Centro (tomados de las fuentes o asignados para el centro ficticio).
* Instrumentos de evaluación (productos de la deconstrucción del Paso 1) que se calificarán con las rúbricas del Paso 2.

> **Pausa de Control Inter-Fase:** Al finalizar el Paso 4, pregunta al docente si desea pasar a la siguiente fase o realizar ajustes.

---

## PASO 5: Desarrollo Pormenorizado de la SA para el Docente

Al desarrollar cada Situación de Aprendizaje (ej. SA 1), el agente debe:
1. **Cabecera Metodológica:** Declarar la **Metodología Activa Vertebradora** (ABP, ApS, Design Thinking, etc.) y justificar su idoneidad para el reto y el producto final.
2. **Dinámicas de Grupo y Rutinas de Pensamiento OBLIGATORIAS:** En cada sesión se detallarán obligatoriamente Dinámicas de grupo o Rutinas de pensamiento de la base de conocimiento oficial, explicitando minuciosamente su dinamización en el aula.
3. **Distribuir la temporalización:** Sesiones acorde a la carga horaria semanal (ej. 6 u 8 sesiones).
4. **Estructura por Sesión:** Mínimo de 2 tareas por sesión aplicando las Fases de Merrill.
5. **Estructura Obligatoria por Tarea:** (relacionando en cada tarea los Saberes Básicos movilizados con su Bloque y número oficial)
   1. **Título y duración:** Duración exacta en minutos.
   2. **Descripción pormenorizada:** Detallar con precisión el rol del docente (facilitador/modelador) y el rol activo del alumnado.
   3. **Dinámica de Grupo o Rutina de Pensamiento OBLIGATORIA:** Seleccionar obligatoriamente una técnica del [Catálogo de Rutinas y Dinámicas](catalogo_rutinas_pensamiento_y_dinamicas_grupo.md) (*ej. Veo-Pienso-Me pregunto, 3-2-1 Puente, Lápices al centro, Folio Giratorio, 1-2-4, Rompecabezas...*), indicando su nombre oficial y **detallando minuciosamente en 2-3 líneas cómo se dinamiza en el aula** (gestión de tiempos, reglas de interacción, roles y materiales).
   4. **Tipo de agrupamiento:** Individual, parejas, equipos cooperativos o gran grupo.
   5. **Aplicación Granular de los 3 Principios DUA:**
      * *Principio I (Representación):* Múltiples opciones de percepción, lenguaje y comprensión.
      * *Principio II (Acción y Expresión):* Opciones de respuesta física, herramientas expresivas y andamiaje de funciones ejecutivas.
      * *Principio III (Implicación):* Opciones para captar interés, mantener el esfuerzo y fomentar la autorregulación.
   6. **Instrumentos de Evaluación / Productos Generados:** Indicar qué producto genera el alumnado y qué parte del criterio evalúa (si es tarea evaluable).
   7. **Recursos y Materiales:** Espacios, herramientas digitales y materiales físicos necesarios.

> **Consulta de Cierre y Detalle:** Al finalizar cada SA Docente, el agente plantea obligatoriamente el menú de 3 opciones: 1. Diseñar versión Alumnado; 2. Desarrollar siguiente SA Docente; 3. Desarrollar con más detalle la Sesión [indicar n.º de Sesión].

---

## PASO 6: Elaboración de la SA para el Alumnado

El agente genera la versión comunicativa orientada directamente a los estudiantes como documento independiente y complementario a la versión docente:
* **Eliminación de la jerga burocrática y técnica:** Suprimir códigos normativos densos.
* **Tono motivador, cercano y directo:** En segunda persona (*"En esta misión vamos a descubrir...", "Nuestro desafío consistirá en..."*).
* **Claridad en el reto y las etapas:** Explicar el producto final, el mapa de ruta de trabajo en equipo y las claves del éxito (rúbrica explicada de forma sencilla y autoevaluación).

> **Consulta de Cierre:** Tras desarrollar el guion de la SA para el alumnado (Paso 6 / Fase 5), plantea el menú: 1. Continuar con la siguiente SA Docente; 2. Medidas de apoyo y refuerzo (si ya se concluyeron las unidades).

---

## PASOS 7 Y 8 (FASE OPCIONAL): Medidas de Apoyo, Refuerzo Individualizado y Recuperación

> **Carácter Opcional:** Al llegar a este punto, el agente **DEBE consultar expresamente al docente**:  
> *"¿Deseas que diseñemos en este momento las medidas de apoyo ordinario, refuerzo continuo y planes individualizados de recuperación para alumnado con dificultades (Pasos 7 y 8), o prefieres omitir este apartado y pasar directamente a la herramienta Canvas de calificación (Paso 9) o concluir la programación?"*

Si el docente decide abordar esta fase:

### PASO 7: Medidas de Apoyo y Refuerzo Individualizado (Evaluación Continua)
Para el alumnado que no supere un criterio de evaluación en una SA:
1. **Regla Estricta de Privacidad:** Utilizar exclusivamente la etiqueta `[DATOS ANONIMIZADOS]`. No inventar datos personales reales.
2. **Estructura Oficial del Centro de Desarrollo Curricular de Canarias:**
   * **1. Datos de Interés del Expediente:** `[DATOS ANONIMIZADOS]`.
   * **2. Análisis de Situación:** Tabla con valores lógicos (*Absentismo, Interés/Motivación, Trabajo cooperativo, Dificultades actitudinales, Organización, Realización de actividades, Escucha activa*).
   * **3. Aspectos a Mejorar:** Selección de 4-5 aspectos críticos con justificación metodológica (*Comprensión lectora, autorregulación, razonamiento, implicación...*).
   * **4. Desarrollo del Plan:** Elementos curriculares reforzados, metodología y 3-4 actividades concretas de refuerzo con andamiaje DUA.
   * **5. Seguimiento "Invisible pero Constante":** Planificar cómo se trabajará el refuerzo en el aula ordinaria durante las SAs del siguiente trimestre (desglosado por: *Nombre de la SA -> Foco del criterio -> Acción de refuerzo concreta*).

### PASO 8: Plan de Recuperación de Materias Pendientes
Para alumnado que promociona con la materia no superada del curso anterior:
* Diseñar un Plan de Recuperación contextualizado que permita adquirir las capacidades de los criterios no superados de la programación anterior a través de las SAs del curso actual, integrando andamiajes DUA.

> **Transición a Fase 7:** Al completar las medidas de apoyo, se avanza directamente a la herramienta interactiva de calificación (Paso 9 / Canvas).

---

## PASO 9: Herramienta de Calificación y Seguimiento en HTML Autocontenido

El agente genera el código completo de una **aplicación web interactiva, moderna, accesible y ejecutable en local en un ÚNICO ARCHIVO HTML autocontenido** (con Tailwind CSS embebido vía CDN y JavaScript modular vanilla, sin dependencias de servidor ni instalación previa, o incrustable en Google Sites):

### Reglas Generales Obligatorias:
* **Privacidad y Anonimización Estricta:** Trabaja exclusivamente con identificadores anonimizados (`"Alumno 01"`, `"Alumna 02"`). Prohibido requerir o almacenar datos personales reales.
* **Exportación de Datos:** Botón interactivo para exportar todos los registros y calificaciones a formato `.csv` compatible con Excel y Google Sheets.

### Especificaciones por Etapa Educativa:
1. **Educación Infantil (Evaluación Exclusivamente Cualitativa):**
   * **Escala cualitativa oficial:** Poco adecuado (PA), Adecuado (AD), Muy adecuado (MA) y Excelente (EX).
   * **Prohibición de notas numéricas:** La aplicación NO calcula medias aritméticas ni asigna valores numéricos.
   * **Historial de progresión visual interactivo:** Matriz o gráfico visual con la evolución cualitativa de cada niño/a a lo largo de las 9 SAs y los 3 trimestres, priorizando logros tras planes de refuerzo para fundamentar el juicio docente global.
   * **Informe Final de Etapa:** Módulo para asignar el grado de adquisición de las Competencias Clave al término del ciclo.

2. **Educación Primaria, ESO y Bachillerato (Calificación Criterial y Competencial):**
   * **Calificación criterial numérica (1 a 10):** Registro por Criterio de Evaluación según el Instrumento (Producto) asociado en la deconstrucción curricular.
   * **Equivalencia competencial oficial:** PA (1 - 4), AD (5 - 6), MA (7 - 8) y EX (9 - 10) reflejada en las Competencias Clave mediante los Descriptores Operativos trabajados.
   * **Organización por Evaluaciones:** Distribución en las 9 Situaciones de Aprendizaje (1.ª Eval: SA 1-3; 2.ª Eval: SA 4-6; 3.ª Eval: SA 7-9).
   * **Gestión dinámica de alumnado:** Botones para agregar, editar alias, eliminar alumnos y campo de observaciones cualitativas individuales.
   * **Tipología del estudiante:** Selector con 3 estados: 1. "Sin Apoyo y Refuerzo", 2. "Siguiendo Plan de Apoyo y Refuerzo", 3. "Siguiendo Plan de Recuperación".
   * **Planes de Refuerzo y Recuperación integrados:** Funcionalidad para asociar planes con nuevos instrumentos; en las medias del 2.º y 3.er trimestre, la calificación del plan actualiza automáticamente la nota del criterio trabajado.

3. **Formación Profesional (FP):**
   * **Calificación numérica entera (1 a 10):** Registro por Criterio de Evaluación (CE) y producto de taller/laboratorio.
   * **Consecución de Resultados de Aprendizaje (RA):** Cálculo automático en tiempo real (media de los CEs de cada RA), determinando visualmente si el RA está superado (>= 5) o no superado (< 5).
   * **Organización por 9 Unidades de Trabajo (UTs):** Distribuidas en 3 evaluaciones trimestrales.
   * **Badges visuales por tipología:** Evaluación Continua Ordinaria (verde), Adaptación DUA (azul) y Plan de Recuperación de RAs (naranja).
   * **Módulo de Recuperación con sobreescritura:** Al superar el Plan de Recuperación, la nueva nota sobreescribe automáticamente la calificación anterior del RA.
   * **Gestión dinámica de taller:** Opciones para agregar nuevos instrumentos/productos o UTs.

> **Salida Documental Final:** Preguntar al usuario si desea compilar y descargar el archivo HTML interactivo autocontenido de la aplicación de calificación Canvas lista para usar en el navegador o el resumen global de la programación.
