---
name: ere-evaluacion
description: >-
  Especialista en evaluación, programación y diseño curricular para Enseñanzas de Régimen Especial (ERE)
  en Canarias y a nivel estatal: Idiomas (EOI), Deportivas (EDRE), Artes Plásticas y Diseño, Conservatorios de Música y Danza, y Artísticas Superiores (EEAASS).
---

# Habilidad Especialista en Enseñanzas de Régimen Especial (ERE)

Esta habilidad proporciona las directrices instruccionales, normativas y metodológicas para guiar al agente de IA en la generación de instrumentos de evaluación, programaciones y unidades formativas de las **Enseñanzas de Régimen Especial (ERE)** en el estándar Open Knowledge Framework (OKF).

---

## 1. Activación y Filtros Anti-Alucinación (Guardrails)

La habilidad se activa cuando el usuario solicita programar, diseñar o evaluar enseñanzas pertenecientes a:
1. **Escuelas Oficiales de Idiomas (EOI)** (Niveles A2, B1, B2, C1, C2).
2. **Enseñanzas Deportivas de Régimen Especial (EDRE)** (Técnico Deportivo y Técnico Deportivo Superior).
3. **Artes Plásticas y Diseño** (Ciclos Formativos de Grado Medio y Superior en Escuelas de Arte).
4. **Música y Danza** (Enseñanzas Elementales y Profesionales en Conservatorios).
5. **Enseñanzas Artísticas Superiores (EEAASS)** (Grados en Música, Diseño, Arte Dramático - EEES / ECTS).

### Reglas Negativas Obligatorias:
* ⛔ **PROHIBIDO** aplicar el Perfil de Salida de ESO/Bachillerato o las 8 Competencias Clave LOMLOE de la enseñanza obligatoria.
* ⛔ **PROHIBIDO** forzar el esquema de 9 Situaciones de Aprendizaje escolares con las 3 redes DUA por sesión cuando la enseñanza responde a módulos técnicos, audiciones o guías docentes ECTS.
* ⛔ **PROHIBIDO** inventar códigos o enunciados curriculares. Todo criterio, RA o saber debe ser calcado literalmente de la normativa externa de referencia ([open-lex-edu](https://github.com/nmarafo/open-lex-edu) o boletines oficiales).

---

## 2. Marco Normativo Sectorial por Rama (con Foco en Canarias)

### Rama A: Idiomas de Régimen Especial (EOI)
* **Marco:** Marco Común Europeo de Referencia para las Lenguas (MCERL), Real Decreto 1/2019, Decreto 142/2018 y **Orden de 15 de septiembre de 2022** (BOC n.º 190, 26/09/2022).
* **Organización:** No se evalúa por temas generales, sino por **5 Actividades de Lengua estancas**:
  1. Comprensión de Textos Escritos (CTE).
  2. Comprensión de Textos Orales (CTO).
  3. Producción y Coproducción de Textos Escritos (PCTE).
  4. Producción y Coproducción de Textos Orales (PCTO).
  5. Mediación Lingüística (MED - intralingüística e interlingüística).
* **Calificación y Certificación:** Baremos porcentuales independientes por destreza con umbrales mínimos aprobatorios.

### Rama B: Enseñanzas Deportivas (EDRE)
* **Marco:** Real Decreto 1363/2007, **Decreto 93/2019** (Capítulo V, BOC n.º 105, 04/06/2019) y **Resolución de 4 de febrero de 2017** (BOC n.º 34, 17/02/2017).
* **Organización:** Estructura modular dividida en **Bloque Común**, **Bloque Específico** y **Bloque Complementario**.
* **Calificación:** Escala numérica 1 a 10 para módulos teóricos y prácticos. Calificación de **Apto / No Apto** obligatoria para el Módulo de Formación Práctica (en entidades federadas/clubes) y el Módulo de Proyecto Final.

### Rama C: Artes Plásticas y Diseño (Escuelas de Arte)
* **Marco:** Real Decreto 596/2007, **Orden de 22 de marzo de 2013** (BOC n.º 65, 05/04/2013) y **Resolución de 6 de noviembre de 2017** (BOC n.º 220, 15/11/2017).
* **Organización:** Módulos profesionales de taller y teóricos.
* **Calificación y Proyecto:** Calificación numérica 1 a 10 en módulos. Fase de Formación Práctica en Empresas (FCT) y defensa pública del **Proyecto Integrado / Obra Final** evaluado por comisión evaluadora colegiada con rúbricas específicas.

### Rama D: Música y Danza (Conservatorios)
* **Marco:** Enseñanzas Elementales: **Orden de 16 de marzo de 2018** (BOC n.º 62, 28/03/2018). Enseñanzas Profesionales: **Decreto 364/2007** (BOC n.º 208, 17/10/2007) y **Orden de 28 de mayo de 2008** (BOC n.º 114, 10/06/2008).
* **Organización:** Asignaturas individuales (Instrumento Principal) y colectivas (Lenguaje Musical, Armonía, Música de Cámara, Coro, Orquesta).
* **Calificación y Promoción:** Escala numérica entera de **1 a 10 sin decimales**. Requisito imperativo: la no superación de la asignatura troncal de instrumento principal impide la promoción de curso con independencia de las demás asignaturas.

### Rama E: Enseñanzas Artísticas Superiores (EEAASS)
* **Marco:** **Ley 1/2024, de 7 de junio** (BOE 08/06/2024), Real Decreto 1614/2009, **Decreto 30/2014** (BOC 27/05/2014) y **Resolución de 8 de febrero de 2017** (BOC n.º 34, 17/02/2017).
* **Organización:** Nivel Grado EEES. Estructurado en **Guías Docentes y créditos ECTS** (25-30 horas por crédito).
* **Calificación:** Escala numérica de **0 a 10 con un decimal** (0-4.9: Suspenso, 5.0-6.9: Aprobado, 7.0-8.9: Notable, 9.0-10: Sobresaliente, Matrícula de Honor). Trabajo Fin de Estudios (TFE) defendido ante tribunal colegiado.

---

## 3. Protocolo de Construcción de Rúbricas Analíticas Oficiales ERE

Toda rúbrica generada bajo esta habilidad debe satisfacer los estándares de calidad técnica de OpenDidactia:
1. **Verbo Invariable:** El verbo cognitivo o performativo principal debe ser idéntico en los 4 niveles de desempeño.
2. **Referencia Aprobatoria Oficial:** El nivel Suficiente o Aprobado debe describir con total fidelidad el nivel umbral fijado en la normativa.
3. **Graduadores Cualitativos en Negrita:** Utilizar graduadores que expresen calidad, precisión, autonomía, fluidez o rigor técnico resaltados en **negrita**.
4. **Prohibición de Negaciones Simples:** El nivel inferior (Insuficiente / No Apto) debe tipificar y describir el error técnico o interpretativo concreto, evitando expresiones como *"No realiza..."* o *"No sabe..."*.
