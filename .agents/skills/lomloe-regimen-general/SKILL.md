---
name: lomloe-regimen-general
description: >-
  Especialista en evaluación criterial, Plan Evalúa (Canarias), Programaciones Didácticas y Situaciones de Aprendizaje LOMLOE para Régimen General: Educación Infantil, Educación Primaria, ESO y Bachillerato en las 17 CCAA y Ceuta/Melilla.
---

# Habilidad Especialista en Régimen General (LOMLOE) y Plan Evalúa

Esta habilidad proporciona las directrices normativas, metodológicas y de supervisión para guiar al agente de IA en el diseño y auditoría de **Programaciones Didácticas (PD)**, **Situaciones de Aprendizaje (SA)** e instrumentos de evaluación en **Educación Infantil, Educación Primaria, Educación Secundaria Obligatoria (ESO) y Bachillerato** bajo el estándar Open Knowledge Framework (OKF).

---

## 1. Activación y Filtros de Aislamiento Ontológico (Guardrails)

Esta habilidad se activa cuando el usuario solicita diseñar, evaluar o supervisar enseñanzas de:
1. **Educación Infantil** (1.er Ciclo 0-3 años y 2.º Ciclo 3-6 años).
2. **Educación Primaria** (1.º a 6.º curso).
3. **Educación Secundaria Obligatoria (ESO)** (1.º a 4.º curso y Diversificación Curricular).
4. **Bachillerato** (1.º y 2.º curso en todas sus modalidades).

### Reglas Negativas Obligatorias:
* ⛔ **PROHIBIDO** mezclar terminología de Formación Profesional (Resultados de Aprendizaje, Criterios de Evaluación por letras `a), b), c)`, CPPS o módulos profesionales) ni de Enseñanzas de Régimen Especial (ERE).
* ⛔ **PROHIBIDO** inventar códigos o enunciados de Competencias Específicas, Criterios de Evaluación, Saberes Básicos o Descriptores Operativos. Deben calcarse literalmente de la fuente normativa externa ([open-lex-edu](https://github.com/nmarafo/open-lex-edu) o boletines oficiales).
* ⛔ **PROHIBIDO** calificar por agregación porcentual de instrumentos aislados (ej. *"Exámenes 60%, Cuaderno 20%, Actitud 20%"*). La calificación en Primaria, ESO y Bachillerato emana exclusivamente de los **Criterios de Evaluación**.
* ⛔ **PROHIBIDO** utilizar calificaciones numéricas, exámenes clasificatorios o medias aritméticas en **Educación Infantil**, cuya evaluación es **100 % cualitativa, global, continua y formativa**.

---

## 2. Encaje del Plan Evalúa (Exclusivo Régimen General en Canarias)

En la Comunidad Autónoma de Canarias, el **Plan Evalúa** del Servicio de Inspección Educativa es de aplicación **exclusiva** para las etapas de Régimen General:
* **Educación Infantil:** Decreto 196/2022 y Orden de 24 de mayo de 2023 (BOC n.º 109, 06/06/2023).
* **Educación Primaria:** Decreto 211/2022 y Orden de 21 de abril de 2023.
* **ESO y Bachillerato:** Decreto 30/2023 y Orden de 31 de mayo de 2023.

*(Nota: Ni la Formación Profesional ni las Enseñanzas de Régimen Especial forman parte del Plan Evalúa).*

---

## 3. Protocolo Técnico de Diseño Curricular (7 Fases)

1. **Fase 1 — Concreción Criterial y Deconstrucción (100 % Criterios):**
   * Inventario previo obligatorio del 100 % de los criterios oficiales del curso/materia.
   * Deconstrucción de cada criterio en **2 productos tangibles** (`[Criterio].[Secuencia]`, ej. `1.1.1` y `1.1.2`), repartiendo el 100 % de los Descriptores Operativos del Perfil de Salida (o Competencias Clave en Infantil) y vinculando los Saberes Básicos (Bloque y n.º).
2. **Fase 2 — Rúbricas Analíticas Oficiales con Graduadores (100 % Criterios):**
   * **Verbo invariable** en los 4 niveles de desempeño.
   * Nivel **Suficiente/Bien (5-6 / AD en Infantil)** idéntico al criterio oficial.
   * **Graduadores cualitativos en negrita** y ejemplo tangible de producto en cada nivel.
   * Nivel **Insuficiente (1-4 / PA en Infantil)** redactado en positivo describiendo el grado de apoyo requerido o el error concreto (prohibido usar *"No realiza"*).
3. **Fase 3 — Secuenciación Anual en 9 Situaciones de Aprendizaje:**
   * 3 SAs por evaluación trimestral (1.ª Eval: SA 1-3; 2.ª Eval: SA 4-6; 3.ª Eval: SA 7-9), articuladas con efemérides del calendario escolar autonómico, metodologías activas (ABP, ApS, Design Thinking...) y planes/programas de centro.
4. **Fase 4 — Desarrollo de la SA para el Docente:**
   * Secuencia instruccional de **David Merrill** (Problema central, Activación, Demostración/Modelado, Aplicación y Transferencia).
   * Mínimo **2 tareas activas por sesión** con roles docente/discente, rutinas de pensamiento visible o estructuras cooperativas procedimentadas y **DUA granular en sus 3 redes** (Representación, Acción y Expresión, Implicación).
5. **Fase 5 — Versión de la SA para el Alumnado:**
   * Guion motivador en 2.ª persona (*"El Reto"* o *"La Misión"*), mapa de ruta en 3-4 etapas y claves del éxito sin jerga burocrática.
6. **Fase 6 — Medidas de Apoyo, Refuerzo y Recuperación (Opcional):**
   * Refuerzo inclusivo ordinario en las siguientes 3 SAs y Plan de Recuperación de materias pendientes con ajustes DUA y datos estrictamente anonimizados.
7. **Fase 7 — Herramienta Interactiva Canvas en HTML Autocontenido:**
   * Aplicación en un único archivo HTML con alumnado anonimizado (`Alumno 01`), evaluación cualitativa (Infantil) o criterial ponderada (Primaria/ESO/Bachillerato), recálculo por recuperación y exportación a `.csv` con encabezado **UTF-8 BOM (`\uFEFF`)** y separador `;`.
