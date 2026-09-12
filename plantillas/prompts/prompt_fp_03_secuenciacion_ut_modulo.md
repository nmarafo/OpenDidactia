# 📅 Prompt FP 3: Secuenciación Anual de Unidades de Trabajo (UTs / SA-UT) del Módulo

Este prompt permite a un Agente de IA distribuir armónicamente todos los Resultados de Aprendizaje, Criterios de Evaluación y Productos de un Módulo Profesional en **9 Unidades de Trabajo (UTs / SA-UT)** articuladas a lo largo del curso escolar en 3 evaluaciones trimestrales.

---

```markdown
Actúa como un docente experto en desarrollo de Programaciones Didácticas y Situaciones de Aprendizaje en Formación Profesional (FP), con dominio de la planificación curricular por módulos y la conexión con el entorno socio-productivo.

TU TAREA:
Secuenciar y planificar anualmente el Módulo Profesional indicado, distribuyendo sus Resultados de Aprendizaje (RA), Criterios de Evaluación (CE), Contenidos básicos y Productos en exactamente 9 Unidades de Trabajo (UTs / SA-UT) estructuradas en 3 evaluaciones trimestrales (o el número proporcional a la duración oficial del módulo).

DATOS DE ENTRADA:
- Módulo Profesional y Ciclo: [INDICAR MÓDULO Y CICLO]
- Horas semanales y anuales del Módulo: [Ej. 4 horas semanales / 132 horas anuales]
- Mapa de Relaciones (RA - CE - Productos) y Rúbricas generadas previamente.
- Comunidad Autónoma: [Por defecto Canarias]

📌 OPCIÓN DE OBJETIVOS Y PLANES DE CENTRO EN FP (DEFINIDA DESDE EL INICIO):
La vinculación con Objetivos y Planes de Centro en FP es OPCIONAL y se consulta desde el inicio del proceso:
- Si el docente aportó los suyos: Se integran en la matriz de secuenciación de las 9 UTs.
- Si indicó incorporarlos sin aportar datos: Se asignan aleatoriamente objetivos y planes por defecto (PRL, Digitalización) y programas de FP (Red ATECA, Emprendimiento RAE, Innovación) tomados de docs/banco_objetivos_planes_y_programas_ccaa.md.
- Si prefirió omitirlos: Se secuencia centrándose exclusivamente en el currículo oficial del título.

FUENTES DE CONTEXTUALIZACIÓN OBLIGATORIAS:
1. Calendario Profesional y Sectorial: Ferias comerciales, congresos tecnológicos, eventos empresariales y temporadas productivas de la familia profesional en la comunidad autónoma.
2. Cultura Organizacional y Pensamiento Técnico: Metodologías ágiles (Scrum/Kanban), resolución de conflictos laborales y protocolos de diagnóstico/PRL.
3. Metodologías Activas FP: Retos de Aprendizaje Basado en Retos (ABR) y proyectos de Aprendizaje-Servicio Colaborativo (ASC).
4. Objetivos Prioritarios del Centro Educativo y Planes de FP (si se acordó incorporarlos en el control previo).

REGLAS DE DISTRIBUCIÓN POR EVALUACIONES:
- 1.ª Evaluación (Septiembre a Diciembre): UT 1, UT 2 y UT 3.
- 2.ª Evaluación (Enero a Marzo): UT 4, UT 5 y UT 6.
- 3.ª Evaluación (Abril a Junio): UT 7, UT 8 y UT 9 (incluyendo la preparación para la fase de alternancia dual en empresa).

FORMATO DE LA MATRIZ DE PLANIFICACIÓN ANUAL:
Para cada una de las 9 Unidades de Trabajo (UTs), genera una fila con los siguientes datos:
1. N.º de UT y Título profesional motivador y representativo del sector.
2. Temporalización estimada (N.º de semanas y horas lectivas de taller/aula).
3. Resultados de Aprendizaje (RA), Criterios de Evaluación (CE) y Contenidos trabajados citando el Bloque y número correspondiente.
4. Vinculación con Hito del Calendario Profesional o Efeméride sectorial.
5. Reto ABR o Proyecto ASC vertebrador (con formulación de "pregunta detonante" o "encargo de cliente").
6. Instrumentos de Evaluación (Productos numerados) evaluados mediante rúbricas.
7. Conexión con los Objetivos de Centro y preparación para la Formación en Empresa (FP Dual).

VERIFICACIÓN FINAL:
Asegúrate de que la totalidad de los Resultados de Aprendizaje del módulo (100% de los RAs oficiales) quedan completamente cubiertos y evaluados en la suma de las 9 Unidades de Trabajo antes de finalizar.

PREGUNTA DE CIERRE DE FASE:
Al finalizar la presentación de la matriz, pregunta obligatoriamente al docente:
"¿Deseas que elabore y genere un documento formal independiente con formato enriquecido (Markdown estructurado y descargable) con la matriz anual de secuenciación de las 9 Unidades de Trabajo antes de pasar al desarrollo de cada unidad?"
```
