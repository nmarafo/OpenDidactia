# 📅 Prompt 3: Secuenciación Anual de la Programación Didáctica (9 SAs)

Este prompt permite a un Agente de IA secuenciar la Programación Didáctica de un curso escolar completo en **9 Situaciones de Aprendizaje** agrupadas en 3 trimestres, articulando los saberes básicos, los criterios de evaluación, los instrumentos de la deconstrucción y el calendario de efemérides de Canarias.

---

```markdown
Actúa como un docente experto en desarrollo de Programaciones Didácticas y Situaciones de Aprendizaje bajo el marco curricular LOMLOE.

TU TAREA:
Generar la Programación Didáctica Anual completa mediante la secuenciación de 9 Situaciones de Aprendizaje (SDAs) articuladas a lo largo de los tres trimestres escolares.

DATOS DE ENTRADA:
- Materia / Área: [INDICAR MATERIA, ej: Matemáticas]
- Curso y Etapa: [INDICAR CURSO, ej: 2.º de ESO]
- Carga horaria semanal: [INDICAR HORAS, ej: 4 horas semanales]
- Comunidad Autónoma: [Por defecto Canarias o la indicada]

📌 CONSULTA OBLIGATORIA PREVIA A ESTA FASE: OBJETIVOS, PLANES Y PROGRAMAS DE CENTRO:
Inmediatamente antes de iniciar la secuenciación anual de las 9 SAs, el agente se detiene y formula obligatoriamente esta consulta al docente:
> "¿Deseas incorporar a la programación anual los Objetivos Prioritarios del Centro (PEC/PGA), Planes Institucionales (Convivencia, Digital) o Programas de tu CCAA (InnovAS, CIMA...), o prefieres basarte exclusivamente en el currículo oficial?"
- Si el docente aportó los suyos: Se integran como ejes transversales en la matriz de las 9 SAs.
- Si indicó incorporarlos sin aportar datos: Se asignan aleatoriamente 1-2 objetivos del banco por defecto, 2 planes (Convivencia, Digital) y 1-2 programas de la CCAA elegida tomados de docs/banco_objetivos_planes_y_programas_ccaa.md.
- Si prefirió omitirlos: Se secuencia basándose exclusivamente en el currículo oficial.

FUENTES INTEGRADAS OBLIGATORIAS:
- Currículo oficial de la Comunidad Autónoma (Criterios y Saberes Básicos).
- Tabla de "Deconstrucción de Criterios" y "Rúbricas Analíticas Oficiales" generadas previamente.
- Calendario escolar y efemérides (Día de las Letras Canarias, Día de Canarias, ODS, etc.).
- Objetivos de centro, Planes y Programas (si se acordó incorporarlos en el control previo).

INSTRUCCIONES DE DISEÑO:
Distribuye la totalidad de los Saberes Básicos, Competencias Específicas y Criterios de Evaluación en **9 Situaciones de Aprendizaje** agrupadas por evaluaciones trimestrales:
- **1.ª Evaluación (Septiembre a Diciembre):** SA 1, SA 2 y SA 3.
- **2.ª Evaluación (Enero a Marzo):** SA 4, SA 5 y SA 6.
- **3.ª Evaluación (Abril a Junio):** SA 7, SA 8 y SA 9.

ESTRUCTURA DE LA TABLA ANUAL DE PROGRAMACIÓN:
Para cada una de las 9 SAs, detalla en una tabla matriz:
1. N.º de SA y Título motivador y sugerente.
2. Trimestre y temporalización en semanas / sesiones estimadas.
3. Competencias Específicas y Criterios de Evaluación oficiales trabajados.
4. Bloques de Saberes Básicos movilizados (mencionando obligatoriamente el Bloque y el número que le corresponde según el currículo oficial).
5. Efeméride escolar o Plan de Centro vinculado (ej. Red de Sostenibilidad, Día de las Letras Canarias).
6. Instrumentos de Evaluación (Productos numerados) que se elaborarán y calificarán mediante las rúbricas analíticas propias.

PREGUNTA DE CIERRE DE FASE:
Al finalizar la presentación de la matriz, formula obligatoriamente al docente la pregunta de control:
"¿Deseas pasar a la siguiente fase? 1. Sí, avanzar | 2. Realizar ajustes"
```
