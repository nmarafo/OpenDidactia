# 💻 Prompt 8: Generador de Herramienta de Calificación y Seguimiento en HTML

Este prompt permite a un modelo de IA avanzado (ej. Gemini Pro en Canvas o Claude) generar una **aplicación web interactiva y completa en un único archivo HTML autocontenido (con CSS y JavaScript integrados)** para el registro, calificación y seguimiento criterial del alumnado, con datos anonimizados y exportación a CSV.

---

## Variante para Primaria, ESO y Bachillerato

```markdown
Actúa como un Desarrollador Full-Stack Senior y experto en evaluación educativa LOMLOE de Canarias.

TU TAREA:
Crear una aplicación web interactiva completa en un ÚNICO archivo HTML autocontenido (con CSS moderno y JavaScript modular integrados) para calificar y realizar el seguimiento del alumnado de [INDICAR CURSO Y MATERIA], con datos rigurosamente anonimizados.

REGLA DE PRIVACIDAD:
No inventar ni solicitar ningún dato personal. Utilizar nombres de prueba como "Alumno 01", "Alumna 02".

REQUISITOS FUNCIONALES OBLIGATORIOS:
1. Calificación Criterial por Instrumentos:
   - Permite calificar cada Criterio de Evaluación en función del Instrumento de Evaluación (Producto) asociado de la deconstrucción curricular.
   - Determina el grado de adquisición de las Competencias Clave a través de los Descriptores Operativos trabajados, mostrando la equivalencia oficial:
     * "Poco adecuado (PA)" [1 - 4]
     * "Adecuado (AD)" [5 - 6]
     * "Muy adecuado (MA)" [7 - 8]
     * "Excelente (EX)" [9 - 10]
2. Organización por Evaluaciones y SAs:
   - Distribuye las secciones de calificación entre las 9 Situaciones de Aprendizaje del curso agrupadas por trimestres:
     * 1.ª Evaluación: SA 1, SA 2, SA 3.
     * 2.ª Evaluación: SA 4, SA 5, SA 6.
     * 3.ª Evaluación: SA 7, SA 8, SA 9.
3. Gestión Dinámica de Estudiantes:
   - Botones para agregar, editar y eliminar estudiantes.
   - Campo para añadir observaciones cualitativas por alumno.
   - Tipología del alumno: 1. "Sin Apoyo y Refuerzo", 2. "Siguiendo Plan de Apoyo y Refuerzo", 3. "Siguiendo Plan de Recuperación".
4. Planes de Refuerzo y Recuperación Integrados:
   - Funcionalidad para asociar manualmente Planes de Refuerzo y Recuperación con nuevos instrumentos de calificación.
   - En la media del 2.º y 3.er Trimestre, si un alumno ha seguido un Plan de Apoyo y Refuerzo donde se ha vuelto a trabajar un criterio previo, el cálculo actualiza la calificación con la nota del Plan.
5. Exportación de Datos:
   - Botón para exportar todos los registros y calificaciones a formato `.csv`.

PREGUNTA DE CIERRE DE FASE:
Al finalizar la generación del código, pregunta al docente:
"¿Deseas que prepare el archivo HTML independiente descargable con la aplicación de calificación Canvas lista para usar en navegador?"
```

---

## Variante para Educación Infantil

```markdown
Actúa como un Desarrollador Full-Stack Senior y especialista en evaluación cualitativa de Educación Infantil en Canarias (Decreto 196/2022).

TU TAREA:
Crear una aplicación web interactiva en un ÚNICO archivo HTML autocontenido para el registro, seguimiento y valoración cualitativa del alumnado de Educación Infantil (datos anonimizados).

REQUISITOS ESPECÍFICOS PARA INFANTIL:
1. Evaluación Exclusivamente Cualitativa:
   - La aplicación NO debe calcular medias aritméticas ni usar notas numéricas.
   - Registra el nivel de desempeño en cada Criterio de Evaluación mediante la escala oficial:
     * "Poco adecuado (PA)"
     * "Adecuado (AD)"
     * "Muy adecuado (MA)"
     * "Excelente (EX)"
2. Historial de Progresión Visual:
   - En lugar de cálculos matemáticos, muestra una gráfica o matriz visual con la evolución cualitativa de cada niño a lo largo de las SAs y trimestres.
   - Prioriza los logros alcanzados tras la aplicación de Planes de Refuerzo Educativo para fundamentar el juicio global docente.
3. Informe Final de Etapa:
   - Sección para que, al finalizar el ciclo, el docente asigne el grado de adquisición de las Competencias Clave (PA, AD, MA, EX) basado en los criterios observados.
4. Exportación en `.csv`.

PREGUNTA DE CIERRE DE FASE:
Al finalizar la generación del código, pregunta al docente:
"¿Deseas que prepare el archivo HTML independiente descargable con la aplicación cualitativa de Educación Infantil lista para usar en navegador?"
```
