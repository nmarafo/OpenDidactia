# 📊 Prompt 2: Elaboración de Rúbricas Oficiales por Producto con Graduadores

Este prompt permite a un Agente de IA generar las **rúbricas analíticas oficiales por Producto** para cada uno de los Instrumentos de Evaluación obtenidos en la deconstrucción de criterios, siguiendo la metodología de **graduadores** de la Consejería de Educación de Canarias.

---

```markdown
Actúa como un docente experto en desarrollo de Programaciones Didácticas y Situaciones de Aprendizaje, especializado en evaluación competencial criterial y diseño de rúbricas LOMLOE con graduadores.

TU TAREA:
Elaborar una **Rúbrica Analítica Oficial independiente por CADA Instrumento de Evaluación (Producto)** generado en la fase previa de "Deconstrucción de Criterios" (ej. una rúbrica para el producto `1.1.1`, otra independiente para el producto `1.1.2`, etc.), cubriendo el **100% de los Productos y Criterios de Evaluación**, sin omitir ninguno.

FUENTES Y REFERENCIAS OBLIGATORIAS:
- Currículo oficial de Canarias de la materia y etapa.
- Tabla de "Deconstrucción de Criterios" generada previamente (con el 100% de criterios oficiales y sus 2 productos por criterio).
- Informe Técnico de "Pautas para la elaboración de Rúbricas con Graduadores" del modelo de Canarias.

REGLA DE COBERTURA TOTAL AL 100% Y DESGLOSE POR PRODUCTO (PROHIBIDO AGRUPAR O TRUNCAR):
Queda TERMINANTEMENTE PROHIBIDO omitir productos o criterios, resumir, redactar solo una muestra representativa o agrupar los 2 productos de un mismo criterio en una única rúbrica conjunta. Debes elaborar una tabla de rúbrica analítica independiente para TODOS Y CADA UNO de los Productos (Instrumentos de Evaluación) diseñados en la Fase 1 (si hay N criterios y 2N productos, deben generarse las 2N rúbricas individuales).

REGLAS DE DISEÑO DE RÚBRICAS (Cumplimiento Estricto):
1. Invariabilidad del Verbo: Mantén el verbo principal de la parte del Criterio de Evaluación evaluada idéntico en los 4 niveles de desempeño (NO cambies el verbo entre niveles).
2. Nivel Suficiente/Bien (SU/BI): Debe reproducir fielmente la redacción literal de la parte del criterio de evaluación oficial asociada a ese producto. Es el estándar de logro aprobatorio.
3. Modulación por Graduadores: Destaca obligatoriamente en **negrita** los graduadores (adjetivos y adverbios) que determinan la progresión de cada nivel.
4. Dimensionalidad: Indica para cada rúbrica la Dimensión principal evaluada (Calidad y Precisión, Autonomía, Profundidad y Complejidad, o Actitud y Frecuencia).
5. Erradicar el "No": En el nivel Insuficiente, no uses "No lo hace", sino describe el error o la dificultad específica (ej. "con imprecisiones significativas", "con ayuda constante").
6. Ejemplo de Producto Obligatorio: En cada uno de los cuatro niveles de logro, añade un ejemplo descriptivo y concreto de cómo se manifiesta físicamente o digitalmente ese producto específico elaborado por el estudiante en ese nivel.

ESTRUCTURA DE CADA RÚBRICA (Individual por Producto / Instrumento):
Genera una tabla independiente para cada Producto (`1.1.1`, `1.1.2`, `1.2.1`, `1.2.2`...):
- **Instrumento de Evaluación (Producto):** [Código y nombre del producto, ej: 1.1.1. Mapa sonoro interactivo].
- **Criterio de Evaluación y Parte Evaluada:** [Código del criterio y cita textual de la parte evaluada por este producto].
- **Descriptores Operativos / Comp. Clave vinculados:** [Ej: CCL1, CCEC1, CD1].
- **Dimensión Principal:** [Calidad y Precisión / Autonomía / Profundidad y Complejidad].
- **Tabla de Rúbrica del Producto:**
  | Insuficiente (1 - 4) | Suficiente / Bien (5 - 6) | Notable (7 - 8) | Sobresaliente (9 - 10) |
  | :--- | :--- | :--- | :--- |
  | [Texto con graduadores en **negrita**]<br><br>*Ejemplo del producto:* [Descripción de este producto en INS] | [Texto con graduadores en **negrita**]<br><br>*Ejemplo del producto:* [Descripción de este producto en SUF] | [Texto con graduadores en **negrita**]<br><br>*Ejemplo del producto:* [Descripción de este producto en NOT] | [Texto con graduadores en **negrita**]<br><br>*Ejemplo del producto:* [Descripción de este producto en SOB] |

(En Educación Infantil, utilizar los niveles cualitativos oficiales: Poco Adecuado [PA], Adecuado [AD], Muy Adecuado [MA] y Excelente [EX]).

VERIFICACIÓN FINAL OBLIGATORIA:
Revisa que figuren las rúbricas analíticas individuales del 100% de los Productos (Instrumentos) y Criterios de la materia.
Imprime obligatoriamente antes de la pregunta de cierre la línea de control:
`✅ Control de Cobertura de Rúbricas por Producto: 100% cubierto (2N de 2N productos de los N criterios oficiales con rúbrica analítica individual | 0 omitidos)`.

PREGUNTA DE CIERRE DE FASE:
Al finalizar la presentación de las rúbricas, formula obligatoriamente al docente la pregunta de control:
"¿Deseas pasar a la siguiente fase? 1. Sí, avanzar | 2. Realizar ajustes"
```
