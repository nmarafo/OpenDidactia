# 🧬 Taxonomía Curricular LOMLOE y Trazabilidad Competencial

La Ley Orgánica 3/2020 (LOMLOE) introdujo un cambio estructural en el modelo curricular español, transitando de un modelo enciclopédico basado en contenidos a un modelo **competencial, inclusivo y aplicado**, vertebrado en torno al **Perfil de Salida** y a las **Situaciones de Aprendizaje**.

Este documento define la taxonomía unificada empleada en **OpenDidactia** para asegurar la trazabilidad estricta entre todos los elementos del currículo.

---

## 1. El Grafo Curricular LOMLOE

El currículo LOMLOE no es una lista plana de temas, sino un **grafo dirigido** donde cada elemento se conecta jerárquica y funcionalmente:

```text
[ Competencias Clave de la UE (8) ]
               │
               ▼
[ Descriptores Operativos del Perfil de Salida ]
               │
               ▼
[ Competencias Específicas de Área/Materia ] ◄────────┐
               │                                      │
       ┌───────┴────────┐                             │  (Contextualizan)
       ▼                ▼                             │
[ Criterios de   [ Saberes Básicos ]                  │
  Evaluación ]     (Conocimientos,                    │
       │            Destrezas, Actitudes)             │
       │                │                             │
       └───────┬────────┘                             │
               ▼                                      │
   [ Situación de Aprendizaje ]                       │
       (Reto, Secuencia DUA, Tareas) ─────────────────┘
               │
               ▼
   [ Evaluación Formativa y Rúbricas ]
```

---

## 2. Definición de Elementos Curriculares

### 2.1. Competencias Clave (8)
Constituyen las capacidades integradas que todo el alumnado debe alcanzar para su desarrollo personal, ciudadano y profesional:
1. **CCL**: Competencia en comunicación lingüística.
2. **CP**: Competencia plurilingüe.
3. **STEM**: Competencia matemática y competencia en ciencia, tecnología e ingeniería.
4. **CD**: Competencia digital.
5. **CPSAA**: Competencia personal, social y de aprender a aprender.
6. **CC**: Competencia ciudadana.
7. **CE**: Competencia emprendedora.
8. **CCEC**: Competencia en conciencia y expresión culturales.

### 2.2. Perfil de Salida y Descriptores Operativos
El **Perfil de Salida** concreta la forma en que las competencias clave deben haberse desarrollado al finalizar la etapa educativa (enseñanza básica al terminar 4º ESO, con hitos intermedios al finalizar la Educación Primaria).
* Los **Descriptores Operativos** son enunciados precisos (ej. `CCL1`, `STEM2`, `CD3`, `CCEC4`) que describen lo que el alumno es capaz de hacer en un nivel de desempeño determinado.

### 2.3. Competencias Específicas
Son los desempeños que el alumnado debe poder desplegar en actividades o situaciones cuyo abordaje requiere de los saberes básicos de cada área o materia.
* Actúan como **puente conector** entre el Perfil de Salida general y los saberes propios de la disciplina.
* Cada competencia específica se vincula con uno o varios descriptores operativos del Perfil de Salida.

### 2.4. Criterios de Evaluación
Son el **referente fundamental para valorar el grado de adquisición de las competencias específicas**.
* Se formulan con un verbo en infinitivo que denota un proceso cognitivo observable (según taxonomías como Bloom o Marzano), un objeto de conocimiento o saber básico, un contexto o situación de aplicación, y una finalidad o sentido del aprendizaje.
* Son medibles, graduables y universales para todo el alumnado.

### 2.5. Saberes Básicos
Constituyen los conocimientos, destrezas y actitudes que componen los contenidos propios de un área o materia y cuyo aprendizaje es necesario para la adquisición de las competencias específicas.
* Se estructuran en **bloques temáticos**, abandonando la concepción de "temarios memorísticos" y enfatizando su aplicación en situaciones reales.

---

## 3. La Situación de Aprendizaje (SDA) como Unidad de Integración

La **Situación de Aprendizaje** es el dispositivo didáctico fundamental de la LOMLOE. Consiste en la articulación contextualizada de un conjunto de tareas complejas orientadas a resolver un **reto, problema o centro de interés**, movilizando de forma integrada saberes básicos para el desarrollo de competencias específicas.

Toda SDA debe satisfacer los siguientes principios canónicos:
1. **Contextualización significativa:** Conectada con la vida real del alumnado, su comunidad local o regional (en Canarias: su entorno geográfico, histórico, cultural y natural insular) o retos globales (ODS).
2. **Accesibilidad e Inclusión (DUA):** Diseñada desde el inicio bajo los principios del Diseño Universal para el Aprendizaje, ofreciendo múltiples formas de implicación, representación y expresión.
3. **Evaluación Formativa y Rúbricas:** Los criterios de evaluación deben traducirse en descriptores cualitativos graduados en niveles de desempeño (Insuficiente, Suficiente/Bien, Notable y Sobresaliente) conocidos por el alumnado.
