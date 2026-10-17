---
name: fp-looifp-evaluacion
description: >-
  Especialista en programación de Módulos Profesionales, Unidades de Trabajo (SA-UT) y evaluación por Resultados de Aprendizaje (RA) y Criterios de Evaluación (CE) en Formación Profesional según la Ley Orgánica 3/2022 y el Real Decreto 659/2023.
---

# Habilidad Especialista en Formación Profesional (LOOIFP y RD 659/2023)

Esta habilidad proporciona las directrices normativas, técnicas y metodológicas para guiar al agente de IA en la elaboración y supervisión de **Programaciones de Módulos Profesionales**, **Unidades de Trabajo competenciales (SA-UT)** e instrumentos de evaluación en **Formación Profesional** (Grados Básico, Medio, Superior y Cursos de Especialización) bajo el estándar Open Knowledge Framework (OKF).

---

## 1. Activación y Filtros Anti-Alucinación (Guardrails)

Esta habilidad se activa cuando el usuario solicita programar, diseñar o evaluar enseñanzas de **Formación Profesional (Grados D y E del Sistema de FP)** en cualquiera de las 26 Familias Profesionales.

### Reglas Negativas Obligatorias:
* ⛔ **PROHIBIDO** aplicar el Perfil de Salida de la enseñanza básica/Bachillerato, los Descriptores Operativos escolares (`CCL1`, `STEM2`...) o el término *"materia/asignatura"*. La FP se estructura exclusivamente en **Módulos Profesionales**, **Resultados de Aprendizaje (RA)**, **Criterios de Evaluación (CE)**, **Objetivos Generales (OG)** y **Competencias Profesionales, Personales y Sociales (CPPS)**.
* ⛔ **PROHIBIDO** atribuir a la Formación Profesional el sello del **Plan Evalúa** de Canarias (que es exclusivo de Infantil, Primaria, ESO y Bachillerato). La supervisión en FP se rige por la **Ley Orgánica 3/2022**, el **Real Decreto 659/2023** y, en Canarias, la **Resolución de 30 de octubre de 2024** (BOC n.º 226) junto con los reales decretos y decretos autonómicos de cada título.
* ⛔ **PROHIBIDO** calificar el módulo por agregación de instrumentos aislados (ej. *"Exámenes teóricos 60%, Taller 40%"*). La calificación del módulo se obtiene exclusivamente del grado de consecución de sus **Resultados de Aprendizaje (RA)** a través de sus **Criterios de Evaluación (CE)**.
* ⛔ **PROHIBIDO** realizar deconstrucción sintáctica escolar de los CEs. En FP se realiza una **asociación relacional directa** del 100 % de los CEs de todos los RAs con productos tangibles de taller o laboratorio.

---

## 2. Protocolo Técnico de Diseño en Formación Profesional (7 Fases)

1. **Fase 1 — Mapa de Relaciones Curriculares (100 % RAs y CEs):**
   * Inventario previo obligatorio del 100 % de los RAs y CEs oficiales del módulo (calcados literalmente del BOE/TodoFP y decreto autonómico).
   * Asociación relacional de todos los CEs a productos técnicos tangibles de taller/laboratorio con codificación alfanumérica unificada: `[RA].[CE].[Bloque Contenidos].[OG].[CPPS].[Producto]`.
2. **Fase 2 — Rúbricas Analíticas por Producto con Graduadores Técnicos (100 % Productos y CEs):**
   * **Una rúbrica analítica independiente por cada Producto tangible** de la Fase 1 (prohibido agrupar varios productos en una sola rúbrica).
   * **Verbo técnico invariable** en los 4 niveles (Insuficiente 1-4, Suficiente/Bien 5-6, Notable 7-8, Sobresaliente 9-10).
   * Nivel **Suficiente/Bien (5-6)** fiel al umbral oficial del CE.
   * **Graduadores en negrita** de precisión/tolerancia técnica, autonomía operativa, **Prevención de Riesgos Laborales (PRL)** y eficiencia/sostenibilidad, describiendo el fallo técnico concreto en el nivel Insuficiente (sin usar *"No realiza"*).
3. **Fase 3 — Secuenciación Anual en 9 Unidades de Trabajo (SA-UT):**
   * Distribución en 9 UTs anuales (UT 1-3, UT 4-6, UT 7-9) armonizadas con el calendario sectorial y el periodo de estancia en empresa (**FP Dual** Régimen General o Intensivo).
4. **Fase 4 — Desarrollo de la SA-UT para el Docente en Taller:**
   * Metodología activa vertebradora: **Aprendizaje Basado en Retos (ABR)** o **Aprendizaje-Servicio Colaborativo (ASC)**.
   * **5 Principios de David Merrill en taller** (Reto central, Activación diagnóstica, Demostración y modelaje docente con PRL, Aplicación guiada y Transferencia dual).
   * **Duración estricta de 55 minutos por sesión** (ej. `Sesión 1 (55 minutos)`), sumando las tareas de cada sesión exactamente 55 minutos (prohibido asignar a una sola sesión la duración total acumulada de toda la UT, como `Sesión 1 (240 minutos)`).
   * Mínimo **2 tareas activas por cada sesión de 55 minutos** con roles ágiles (Scrum/Kanban), rutinas de diagnóstico técnico (Ishikawa, 5 Porqués), **DUA granular en taller** y especificación de maquinaria, herramientas y **EPIs obligatorios**.
5. **Fase 5 — Versión de la SA-UT para el Alumnado (*"El Encargo del Cliente"*):**
   * Documento profesional motivador estructurado en: 1. El Encargo del Cliente; 2. Especificaciones y tolerancias del Producto Final; 3. Mapa de Ruta en Taller (4 etapas con EPIs); 4. Claves del Éxito Profesional.
6. **Fase 6 — Medidas de Apoyo y Recuperación de RAs (Opcional):**
   * Refuerzo continuo en taller y Plan de Recuperación de módulos/RAs pendientes aplicando los 5 principios de FP (poda curricular de RAs esenciales, DUA accesible, evaluación práctica flexible, cronograma y checklists operativas).
7. **Fase 7 — Herramienta Interactiva Canvas FP en HTML Autocontenido:**
   * Aplicación en un único archivo HTML con alumnado anonimizado (`Alumno 01`), calificación entera 1-10 por CE/Producto, cálculo ponderado de RAs ($\ge 5$ superado), sobreescritura por recuperación y exportación a `.csv` con encabezado **UTF-8 BOM (`\uFEFF`)** y separador `;`.
