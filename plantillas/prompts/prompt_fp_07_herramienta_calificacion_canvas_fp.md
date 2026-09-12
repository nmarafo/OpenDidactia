# 💻 Prompt FP 7: Herramienta Interactiva Canvas de Calificación y Seguimiento en FP

Este prompt permite a un Agente de IA o modelo de lenguaje generar una **aplicación web interactiva completa en un único archivo HTML autocontenido** (con Tailwind CSS y JavaScript vanilla) para el registro criterial, cálculo ponderado de Resultados de Aprendizaje (RA) y seguimiento de planes de recuperación en Formación Profesional.

---

```markdown
Actúa como un Desarrollador Web Full-Stack Senior y especialista en evaluación formativa criterial en Formación Profesional (FP).

TU TAREA:
Crear una aplicación web interactiva completa, moderna, accesible y en un ÚNICO ARCHIVO HTML autocontenido (con estilos embebidos mediante Tailwind CSS vía CDN y JavaScript vanilla) para calificar al alumnado (utilizando exclusivamente datos anonimizados) de un Módulo Profesional de FP.

DATOS DE ENTRADA QUE DEBES INTEGRAR:
- Módulo Profesional: [Indicar Nombre del Módulo]
- Ciclo Formativo y Familia Profesional: [Indicar Ciclo]
- Mapa completo de Resultados de Aprendizaje (RA) y Criterios de Evaluación (CE) del Módulo.
- Unidades de Trabajo (UT) y su distribución por evaluaciones trimestrales.

ESPECIFICACIONES TÉCNICAS Y FUNCIONALES OBLIGATORIAS:
1. Privacidad y Anonimización: La aplicación debe trabajar exclusivamente con datos anonimizados (ej: Alumno 01, Alumno 02).
2. Escala Criterial Numérica: Permitir asignar una calificación numérica del 1 al 10 (números enteros, sin decimales) a cada Criterio de Evaluación (CE) asociado a su Instrumento de Evaluación (Producto).
3. Consecución de Resultados de Aprendizaje (RA): Calcular en tiempo real la media aritmética o ponderada de los CEs pertenecientes a cada RA, determinando visualmente si el RA está superado (calificación >= 5) o no superado (< 5).
4. Organización por Evaluaciones y UTs:
   - Panel de pestañas o acordeones para navegar entre la 1.ª Evaluación (UT 1, 2, 3), 2.ª Evaluación (UT 4, 5, 6) y 3.ª Evaluación (UT 7, 8, 9).
5. Gestión de Alumnado:
   - Botones interactivos para agregar alumnos manualmente, editar su alias anonimizado y eliminarlos.
   - Campo para añadir observaciones cualitativas individuales por alumno y por UT.
6. Tipología y Situación del Estudiante:
   - Selector por alumno con 3 estados visuales diferenciados mediante badges de color:
     1. "Evaluación Continua Ordinaria" (verde)
     2. "Con Necesidades Específicas de Apoyo Formativo / Adaptación DUA" (azul)
     3. "Siguiendo Plan de Recuperación de RA no superados" (naranja)
7. Módulo de Planes de Recuperación con Sobreescritura:
   - Funcionalidad para crear y asociar individualmente Planes de Recuperación a los que se añaden los RAs y CEs no superados.
   - Si el alumno supera el Plan de Recuperación en una evaluación posterior, el sistema debe SOBREESCRIBIR automáticamente la calificación anterior del RA por la nueva nota obtenida.
8. Gestión Dinámica de Taller: Opción de añadir manualmente nuevos Instrumentos de Evaluación (Productos de taller) o nuevas UTs.
9. Exportación a CSV: Botón para descargar de forma inmediata la matriz completa de calificaciones de todos los alumnos, CEs y RAs en formato `.csv` compatible con Excel y Google Sheets.
10. Interfaz Moderna y Responsive: Diseño limpio, profesional, modo oscuro/claro, con tipografía legible, apto para ser incrustado en Google Sites o ejecutado localmente en cualquier navegador sin dependencias de servidor.
```
