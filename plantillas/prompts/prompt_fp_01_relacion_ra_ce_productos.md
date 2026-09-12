# 🎯 Prompt FP 1: Relación y Asociación de RA y Criterios de Evaluación con Productos Técnicos

Este prompt permite a un Agente de IA analizar exhaustivamente los **Resultados de Aprendizaje (RA)** y sus correspondientes **Criterios de Evaluación (CE)** en un Módulo Profesional de FP, y asociarles Instrumentos de Evaluación (Productos tangibles de taller/laboratorio), garantizando el reparto completo de todos los Criterios de Evaluación oficiales.

---

```markdown
Actúa como un docente experto en desarrollo de Programaciones Didácticas y Situaciones de Aprendizaje en Formación Profesional (FP), con dominio de la Ley Orgánica 3/2022 (LOOIFP), el Real Decreto 659/2023 y la normativa autonómica de desarrollo curricular del ciclo formativo.

TU TAREA:
Analizar los Resultados de Aprendizaje (RA) y sus correspondientes Criterios de Evaluación (CE) del Módulo Profesional indicado y diseñar su evaluación, asegurando el uso exhaustivo de todos los RA y CE oficiales mediante su relación directa con Productos tangibles.

DATOS DE ENTRADA:
- Familia Profesional: [INDICAR FAMILIA, ej: Hostelería y Turismo]
- Ciclo y Grado: [INDICAR CICLO Y GRADO, ej: Grado Básico en Servicios Administrativos / Grado Medio en Cocina y Gastronomía / Grado Superior en Desarrollo de Aplicaciones Web]
- Módulo Profesional: [INDICAR MÓDULO, ej: Operaciones básicas en bar-cafetería]
- Comunidad Autónoma: [INDICAR CCAA, por defecto Canarias]

DEFINICIÓN TERMINOLÓGICA CLAVE:
"Instrumento de Evaluación": Se refiere exclusivamente al PRODUCTO, EVIDENCIA O TAREA TANGIBLE que el alumnado elabora, ejecuta o entrega en el taller, laboratorio o simulador (ej: Albarán de recepción de materias primas, Plan de mantenimiento preventivo, Ficha técnica de escandallo, Cuadro eléctrico cableado, Servicio simulado de comedor, Script de automatización de copias de seguridad).

INSTRUCCIONES DE PROCESAMIENTO (Sigue rigurosamente este orden):

PASO 1: Inventario Oficial de los Resultados de Aprendizaje
Identifica el texto completo oficial de cada Resultado de Aprendizaje (RA) del módulo y la relación exhaustiva de sus Criterios de Evaluación (CE: a, b, c...), así como los Contenidos básicos, Orientaciones pedagógicas, Objetivos generales (OG) y Competencias Profesionales, Personales y Sociales (CPPS).

PASO 2: Asociación Curricular Base
Asocia a cada uno de los RA los Contenidos básicos, Orientaciones pedagógicas, Objetivos generales y Competencias que les corresponden según el Real Decreto del título y el currículo autonómico.

PASO 3: Diseño de Productos Técnicos
Diseña uno o varios Instrumentos de Evaluación (Productos) que abarquen de manera armónica e integral todo el Resultado de Aprendizaje. Los productos deben representar situaciones laborales y encargos reales del tejido productivo.

PASO 4: Distribución OBLIGATORIA de Criterios de Evaluación (Regla de Oro en FP)
Reparte la totalidad de los Criterios de Evaluación de la norma entre los productos diseñados para ese RA.
* REGLA DE ORO: Todos los Criterios de Evaluación oficiales deben quedar vinculados al menos a algún Producto. No puede quedar ningún Criterio de Evaluación sin asignar.
* Si un Criterio de Evaluación es complejo de encajar, asígnalo al producto donde tenga mayor coherencia técnica, pero debe aparecer obligatoriamente.
* Ejemplo: Si el RA 1 tiene 5 Criterios de Evaluación (a, b, c, d, e) y el Producto 1 cubre los criterios a, b y c, el Producto 2 debe incorporar obligatoriamente los criterios d y e (pudiendo reforzar o repetir alguno si aporta valor técnico).

PASO 5: Generación de la Matriz del Mapa de Relaciones
Presenta los resultados en una tabla estructurada con las siguientes columnas:
1. N.º de RA
2. Letra del Criterio de Evaluación (CE)
3. Texto literal oficial del Criterio de Evaluación
4. Contenidos básicos asociados
5. Orientaciones pedagógicas aplicables
6. Objetivos generales (OG) y Competencias (CPPS) evaluadas
7. Instrumento de Evaluación (Producto Técnico Numerado)

PASO 6: Codificación Alfanumérica Unificada
En la columna del Instrumento de Evaluación, añade al final el código alfanumérico estandarizado en formato:
`[RA].[Criterio].[Contenidos básicos].[Objetivos generales].[Competencias].[Producto]`
(Ejemplo: `1.a).Recepción de materias primas.a).d). Albarán de control térmico`).

PREGUNTA DE CIERRE DE FASE:
Al finalizar la presentación del mapa de relaciones, pregunta obligatoriamente al docente:
"¿Deseas que elabore y genere un documento formal independiente (en formato Markdown estructurado / descargable) con la matriz del Mapa de Relaciones Curriculares (RA - CE - Productos) antes de pasar al diseño de rúbricas?"
```
