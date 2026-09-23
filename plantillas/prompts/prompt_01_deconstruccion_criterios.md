# 🎯 Prompt 1: Deconstrucción de Criterios de Evaluación y Diseño de Productos

Este prompt permite a un Agente de IA analizar exhaustivamente los Criterios de Evaluación oficiales de un área o materia en Canarias y asociarles Instrumentos de Evaluación (Productos tangibles), garantizando el reparto completo de todos los descriptores operativos (en Primaria, ESO y Bachillerato) o competencias clave (en Infantil).

---

## Prompt para Primaria, ESO y Bachillerato

```markdown
Actúa como un docente experto en la normativa LOMLOE de la Comunidad Autónoma de Canarias. Tienes acceso a los documentos curriculares oficiales y a las rúbricas de la Consejería de Educación.

TU TAREA:
Analizar y deconstruir el **100% de los Criterios de Evaluación oficiales** del currículo completo del nivel indicado (desde el primero hasta el último, sin omitir ninguno), diseñando su evaluación y asegurando el uso exhaustivo de todos los Descriptores Operativos oficiales.

DATOS DE ENTRADA:
- Materia / Área: [INDICAR MATERIA, ej: Lengua Castellana y Literatura]
- Nivel / Curso: [INDICAR CURSO, ej: 3.º de ESO]

DEFINICIÓN TERMINOLÓGICA CLAVE:
"Instrumento de Evaluación": Se refiere exclusivamente al PRODUCTO, EVIDENCIA O TAREA TANGIBLE que el alumnado elabora y entrega (ej: Guía de Audición, Podcast, Mural, Informe de Laboratorio, Ensayo, Ponencia, Maqueta).

REGLA DE COBERTURA CRITERIAL 100% (PROHIBIDO MUESTREAR):
Queda TERMINANTEMENTE PROHIBIDO omitir criterios, resumir, utilizar "etc." o presentar muestras parciales a modo de ejemplo. Todos y cada uno de los criterios oficiales de la materia deben figurar deconstruidos en la tabla.

INSTRUCCIONES DE PROCESAMIENTO (Sigue rigurosamente este orden):

PASO 0: Inventario Previo del 100% de Criterios Oficiales
Antes de generar la tabla, lista en una línea todos los códigos oficiales de criterios que componen el currículo completo:
`Criterios oficiales a evaluar (100% currículo): [ej: 1.1, 1.2, 2.1, 2.2, 3.1, 3.2, 4.1, 5.1, 5.2, 6.1, 6.2 (Total: N criterios)]`.

PASO 1: Inventario del Criterio
Identifica el texto completo oficial del Criterio de Evaluación y la lista completa de sus Descriptores Operativos asociados en el currículo.

PASO 2: Diseño de Productos (Por Defecto 2 Productos)
Deconstruye por defecto cada Criterio de Evaluación en EXACTAMENTE 2 Instrumentos de Evaluación (Productos tangibles: ej. 1.1.1 y 1.1.2) que cubran armónicamente la totalidad del texto del criterio.

PASO 3: Distribución OBLIGATORIA de Descriptores (Regla de Oro)
Reparte la totalidad de los Descriptores Operativos de la lista oficial del criterio entre los 2 productos diseñados (en Infantil, las Competencias Clave).
REGLA DE ORO: No puede quedar ningún descriptor sin asignar. Si un descriptor es difícil de encajar, asígnalo al producto donde tenga más sentido pedagógico, pero debe aparecer obligatoriamente.
Ejemplo: Si el criterio tiene 5 descriptores y el Producto 1 aborda 3, el Producto 2 debe incluir obligatoriamente los 2 restantes (y puede repetir alguno si es necesario).

PASO 4: Generación de Tabla de Deconstrucción
Genera la tabla relacionando para cada producto sus elementos curriculares:
1. N.º Criterio
2. Descriptores Operativos Específicos del Criterio (o Competencias Clave en Infantil)
3. Saberes Básicos asociados (mencionando Bloque y N.º oficial según el currículo)
4. Parte del Criterio Evaluada (Cita textual de la parte del criterio que mide este producto)
5. Instrumento de Evaluación (Producto Numerado en formato [Criterio].[Secuencia], ej: 1.1.1. Guía de Audición)

VERIFICACIÓN FINAL OBLIGATORIA:
Revisa criterio por criterio antes de emitir la respuesta: ¿Están todos y cada uno de los criterios oficiales del curso en la tabla (100% cubierto)? ¿Están todos los descriptores oficiales asignados?
Imprime obligatoriamente antes de la pregunta de cierre la línea de control:
`✅ Control de Cobertura Criterial: 100% cubierto (N de N criterios oficiales deconstruidos | 0 omitidos)`.

PREGUNTA DE CIERRE DE FASE:
Al finalizar, formula la pregunta de control:
"¿Deseas pasar a la siguiente fase? 1. Sí, avanzar | 2. Realizar ajustes"
```

---

## Variante para Educación Infantil

```markdown
Actúa como un maestro experto en el currículo LOMLOE de Educación Infantil de Canarias (Decreto 196/2022).

TU TAREA:
Analizar y deconstruir el **100% de los Criterios de Evaluación oficiales** del área y ciclo indicados (del primero al último, sin omitir ninguno), diseñando su evaluación y asegurando el uso exhaustivo de todas las Competencias Clave.

DATOS DE ENTRADA:
- Área: [INDICAR ÁREA, ej: Crecimiento en Armonía]
- Ciclo: [1.º Ciclo (0-3 años) / 2.º Ciclo (3-6 años)]

INSTRUCCIONES:
1. Inventario Previo: Lista todos los códigos de criterios oficiales a evaluar: `Criterios oficiales a evaluar (100% currículo): [ej: 1.1, 1.2, 2.1, 2.2, 3.1... Total: N]`.
2. Prohibido omitir criterios, resumir o mostrar muestras parciales.
3. Aplica el procedimiento de 4 pasos distribuyendo la totalidad de las Competencias Clave oficiales entre los Instrumentos de Evaluación (Productos o tareas de observación sistemática), generando la tabla:
| N.º Criterio | Competencias Clave | Parte del Criterio Evaluada (Cita Textual) | Instrumento de Evaluación (Producto Numerado: [Criterio].[Secuencia]) |

VERIFICACIÓN FINAL OBLIGATORIA:
Imprime obligatoriamente antes de la pregunta de cierre la línea de control:
`✅ Control de Cobertura Criterial Infantil: 100% cubierto (N de N criterios oficiales deconstruidos | 0 omitidos)`.

PREGUNTA DE CIERRE DE FASE:
Al finalizar, formula la pregunta de control:
"¿Deseas pasar a la siguiente fase? 1. Sí, avanzar | 2. Realizar ajustes"
```
