import os
from generate_pdf_engine import CSS_STYLES, OUTPUT_DIR, generate_pdf_from_html

# ==========================================
# 1. EDUCACIÓN INFANTIL (MARCO PLAN EVALÚA)
# ==========================================
html_infantil = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Checklist Supervisión Programaciones Didácticas - Educación Infantil</title>
<style>
{CSS_STYLES}
</style>
</head>
<body>

<!-- PÁGINA 1 -->
<div class="page">
    <div>
        <!-- Cabecera -->
        <div class="top-header">
            <div class="header-left">
                <div class="org-title">PROPUESTA TÉCNICA PEDAGÓGICA · COORDINACIÓN DOCENTE</div>
                <div class="org-sub">Herramienta Guía de Supervisión y Homologación Curricular de Programaciones Didácticas</div>
                <div class="org-sub">Comisión de Coordinación Pedagógica (CCP) · Equipos de Ciclo de Educación Infantil · Marco Plan Evalúa</div>
            </div>
            <div class="header-right">
                <div class="badge-box">
                    <div class="badge-title">MARCO PLAN EVALÚA</div>
                    <div class="badge-sub">EDUCACIÓN INFANTIL</div>
                </div>
            </div>
        </div>

        <!-- Banner Título -->
        <div class="banner">
            <div>
                <div class="banner-title">CHECKLIST DE SUPERVISIÓN DE PROGRAMACIONES DIDÁCTICAS</div>
                <div class="banner-sub">Herramienta Técnica para Jefaturas de Estudios y Comisión de Coordinación Pedagógica (CCP)</div>
            </div>
            <div class="banner-badge">CURSO 2026-2027</div>
        </div>

        <!-- Cajetín Metadatos -->
        <div class="metadata-box">
            <div class="metadata-row divider">
                <div class="meta-item"><span class="meta-label">CENTRO EDUCATIVO:</span> __________________________________________________</div>
                <div class="meta-item"><span class="meta-label">CÓDIGO DE CENTRO:</span> ____________</div>
                <div class="meta-item"><span class="meta-label">FECHA DE REVISIÓN:</span> ____________</div>
            </div>
            <div class="metadata-row">
                <div class="meta-item"><span class="meta-label">EQUIPO DE CICLO:</span> __________________________</div>
                <div class="meta-item"><span class="meta-label">ÁREAS / PROYECTOS:</span> __________________________</div>
                <div class="meta-item"><span class="meta-label">CICLO:</span> 1.er Ciclo (0-3) ☐ / 2.º Ciclo (3-6) ☐</div>
                <div class="meta-item"><span class="meta-label">JEFATURA REVISORA:</span> ____________________</div>
            </div>
        </div>

        <!-- DIMENSIÓN 1 -->
        <div class="dimension-block">
            <div class="dim-header">
                <span class="dim-title">DIMENSIÓN 1: MARCO CURRICULAR Y CONCRECIÓN PRECEPTIVA</span>
                <span class="dim-sub">Referentes normativos de Canarias (D. 196/2022 y O. 24 de mayo de 2023)</span>
            </div>
            <table class="dim-table">
                <thead>
                    <tr>
                        <th style="width: 4%; text-align: center;">ID</th>
                        <th style="width: 63%;">INDICADOR TÉCNICO DE SUPERVISIÓN</th>
                        <th style="width: 17%; text-align: center;">VALORACIÓN</th>
                        <th style="width: 16%;">OBSERVACIONES / AJUSTES</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td class="col-id">1.1</td>
                        <td class="col-indicator">
                            <span class="ind-title">Criterios oficiales de Canarias íntegros por ciclo:</span><br>
                            Se adoptan los criterios preceptivos de ciclo para las tres áreas (<em>Crecimiento en Armonía</em>, <em>Descubrimiento y Exploración del Entorno</em>, y <em>Comunicación y Representación de la Realidad</em>) según el D. 196/2022, respetando su formulación competencial y sin supresiones.
                        </td>
                        <td class="col-val"><div class="checkbox-group"><span>☐ Sí</span><span>☐ No</span><span>☐ Ajustar</span></div></td>
                        <td class="col-obs"></td>
                    </tr>
                    <tr>
                        <td class="col-id">1.2</td>
                        <td class="col-indicator">
                            <span class="ind-title">Alineación con las Competencias Específicas de Etapa:</span><br>
                            Cada criterio de evaluación está explícitamente vinculado a sus correspondientes Competencias Específicas de área y contribuye a los objetivos formativos de la etapa de Educación Infantil.
                        </td>
                        <td class="col-val"><div class="checkbox-group"><span>☐ Sí</span><span>☐ No</span><span>☐ Ajustar</span></div></td>
                        <td class="col-obs"></td>
                    </tr>
                    <tr>
                        <td class="col-id">1.3</td>
                        <td class="col-indicator">
                            <span class="ind-title">Saberes básicos globalizados y contextualizados:</span><br>
                            Los saberes básicos se articulan de manera integrada y globalizada al servicio de las experiencias de aprendizaje, incorporando los elementos del entorno cultural, social y natural de Canarias prescritos normativamente.
                        </td>
                        <td class="col-val"><div class="checkbox-group"><span>☐ Sí</span><span>☐ No</span><span>☐ Ajustar</span></div></td>
                        <td class="col-obs"></td>
                    </tr>
                </tbody>
            </table>
        </div>

        <!-- DIMENSIÓN 2 -->
        <div class="dimension-block">
            <div class="dim-header">
                <span class="dim-title">DIMENSIÓN 2: SECUENCIACIÓN DE SITUACIONES DE APRENDIZAJE GLOBALIZADAS</span>
                <span class="dim-sub">Distribución temporal, enfoque lúdico y rutinas de desarrollo</span>
            </div>
            <table class="dim-table">
                <thead>
                    <tr>
                        <th style="width: 4%; text-align: center;">ID</th>
                        <th style="width: 63%;">INDICADOR TÉCNICO DE SUPERVISIÓN</th>
                        <th style="width: 17%; text-align: center;">VALORACIÓN</th>
                        <th style="width: 16%;">OBSERVACIONES / AJUSTES</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td class="col-id">2.1</td>
                        <td class="col-indicator">
                            <span class="ind-title">Número, temporización y globalización de SdA:</span><br>
                            El curso está organizado en una secuenciación equilibrada de Situaciones de Aprendizaje, proyectos lúdicos o centros de interés interdisciplinares (habitualmente 6 a 9 anuales; 2-3 por trimestre), respetando los ritmos biológicos, de juego y de descanso del alumnado.
                        </td>
                        <td class="col-val"><div class="checkbox-group"><span>☐ Sí</span><span>☐ No</span><span>☐ Ajustar</span></div></td>
                        <td class="col-obs"></td>
                    </tr>
                    <tr>
                        <td class="col-id">2.2</td>
                        <td class="col-indicator">
                            <span class="ind-title">Coherencia metodológica, principio lúdico y DUA en Infantil:</span><br>
                            Las SdA parten de la curiosidad, el juego libre y guiado, la experimentación sensorial, la psicomotricidad y la afectividad, estructurándose en experiencias motivadoras y accesibles desde el Diseño Universal para el Aprendizaje.
                        </td>
                        <td class="col-val"><div class="checkbox-group"><span>☐ Sí</span><span>☐ No</span><span>☐ Ajustar</span></div></td>
                        <td class="col-obs"></td>
                    </tr>
                </tbody>
            </table>
        </div>

        <!-- DIMENSIÓN 3 -->
        <div class="dimension-block">
            <div class="dim-header">
                <span class="dim-title critical">DIMENSIÓN 3: CARÁCTER DE LA EVALUACIÓN Y CRITERIOS DE VALORACIÓN *(NÚCLEO CRÍTICO)*</span>
                <span class="dim-sub">Garantía de evaluación formativa, cualitativa y no discriminatoria</span>
            </div>
            <table class="dim-table">
                <thead>
                    <tr>
                        <th style="width: 4%; text-align: center;">ID</th>
                        <th style="width: 63%;">INDICADOR TÉCNICO DE SUPERVISIÓN</th>
                        <th style="width: 17%; text-align: center;">VALORACIÓN</th>
                        <th style="width: 16%;">OBSERVACIONES / AJUSTES</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td class="col-id">3.1</td>
                        <td class="col-indicator">
                            <span class="ind-title">Evaluación 100% cualitativa, global, continua y formativa:</span><br>
                            La evaluación tiene carácter estrictamente procesual, global y cualitativo. Queda <strong>terminantemente prohibida</strong> la utilización de calificaciones numéricas, pruebas estandarizadas clasificatorias o medias aritméticas.<br>
                            <span class="critical-callout">Infracción crítica: cuantificar numéricamente o calificar por fichas/frecuencias</span>
                        </td>
                        <td class="col-val"><div class="checkbox-group"><span>☐ Sí</span><span>☐ No</span><span>☐ Ajustar</span></div></td>
                        <td class="col-obs"></td>
                    </tr>
                    <tr>
                        <td class="col-id">3.2</td>
                        <td class="col-indicator">
                            <span class="ind-title">Observación directa y sistemática como técnica nuclear:</span><br>
                            Se definen con precisión los procedimientos de valoración cualitativa continua en las situaciones habituales de aula, juego y patio, registrando los progresos sin emitir juicios de valor deterministas sobre la madurez del infante.
                        </td>
                        <td class="col-val"><div class="checkbox-group"><span>☐ Sí</span><span>☐ No</span><span>☐ Ajustar</span></div></td>
                        <td class="col-obs"></td>
                    </tr>
                    <tr>
                        <td class="col-id">3.3</td>
                        <td class="col-indicator">
                            <span class="ind-title">Enfoque preventivo y no penalizador:</span><br>
                            La evaluación no se emplea como elemento sancionador ni de retención. Se orienta exclusivamente a identificar fortalezas, ritmos madurativos y barreras para ajustar la intervención pedagógica del equipo educativo.
                        </td>
                        <td class="col-val"><div class="checkbox-group"><span>☐ Sí</span><span>☐ No</span><span>☐ Ajustar</span></div></td>
                        <td class="col-obs"></td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

    <!-- Pie Página 1 -->
    <div>
        <div class="page-footer">
            <span>Marco Normativo de Referencia: Decreto 196/2022 • Orden de 24 de mayo de 2023 • Ley Orgánica 2/2006 (LOE-LOMLOE)</span>
            <span>Propuesta Técnica Pedagógica · Uso Interno de Coordinación</span>
        </div>
        <div class="page-footer-center">Página 1 de 2</div>
    </div>
</div>

<!-- PÁGINA 2 -->
<div class="page">
    <div>
        <!-- Cabecera Compacta Página 2 -->
        <div class="top-header">
            <div class="header-left">
                <div class="org-title">PROPUESTA TÉCNICA PEDAGÓGICA · SUPERVISIÓN DE PROGRAMACIONES</div>
                <div class="org-sub">Educación Infantil (1.er y 2.º Ciclo) · Herramienta de Coordinación y Homologación Curricular</div>
            </div>
            <div class="header-right">
                <div class="badge-box">
                    <div class="badge-title">CURSO 2026-2027</div>
                    <div class="badge-sub">EVALUACIÓN CUALITATIVA</div>
                </div>
            </div>
        </div>

        <!-- DIMENSIÓN 4 -->
        <div class="dimension-block">
            <div class="dim-header">
                <span class="dim-title">DIMENSIÓN 4: TÉCNICAS, INSTRUMENTOS Y EVIDENCIAS DE DESARROLLO</span>
                <span class="dim-sub">Variedad de registros cualitativos, triangulación y graduación madurativa</span>
            </div>
            <table class="dim-table">
                <thead>
                    <tr>
                        <th style="width: 4%; text-align: center;">ID</th>
                        <th style="width: 63%;">INDICADOR TÉCNICO DE SUPERVISIÓN</th>
                        <th style="width: 17%; text-align: center;">VALORACIÓN</th>
                        <th style="width: 16%;">OBSERVACIONES / AJUSTES</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td class="col-id">4.1</td>
                        <td class="col-indicator">
                            <span class="ind-title">Diversidad de instrumentos cualitativos:</span><br>
                            Se definen múltiples técnicas e instrumentos adaptados a la etapa: escalas de estimación descriptivas, diarios de aula, anecdotarios, registros de observación sistemática, listas de cotejo de hitos evolutivos y portfolios de producciones infantiles.
                        </td>
                        <td class="col-val"><div class="checkbox-group"><span>☐ Sí</span><span>☐ No</span><span>☐ Ajustar</span></div></td>
                        <td class="col-obs"></td>
                    </tr>
                    <tr>
                        <td class="col-id">4.2</td>
                        <td class="col-indicator">
                            <span class="ind-title">Graduación descriptiva de niveles de autonomía:</span><br>
                            Los instrumentos cuentan con descriptores cualitativos centrados en el grado de autonomía y andamiaje requerido (<em>Iniciándose con ayuda continua, En proceso con acompañamiento, Logrado con autonomía</em>), descartando términos negativos o estigmatizantes.
                        </td>
                        <td class="col-val"><div class="checkbox-group"><span>☐ Sí</span><span>☐ No</span><span>☐ Ajustar</span></div></td>
                        <td class="col-obs"></td>
                    </tr>
                    <tr>
                        <td class="col-id">4.3</td>
                        <td class="col-indicator">
                            <span class="ind-title">Evaluación formativa y participación familiar:</span><br>
                            Se recogen evidencias empíricas mediante observación compartida entre el profesorado y personal de apoyo, integrando momentos guiados de autopercepción de logros por parte del alumnado y entrevistas de contraste con las familias.
                        </td>
                        <td class="col-val"><div class="checkbox-group"><span>☐ Sí</span><span>☐ No</span><span>☐ Ajustar</span></div></td>
                        <td class="col-obs"></td>
                    </tr>
                </tbody>
            </table>
        </div>

        <!-- DIMENSIÓN 5 -->
        <div class="dimension-block">
            <div class="dim-header">
                <span class="dim-title">DIMENSIÓN 5: PLAN DE DETECCIÓN, REFUERZO Y ESTIMULACIÓN TEMPRANA</span>
                <span class="dim-sub">Intervención temprana ordinaria y coordinación especializada</span>
            </div>
            <table class="dim-table">
                <thead>
                    <tr>
                        <th style="width: 4%; text-align: center;">ID</th>
                        <th style="width: 63%;">INDICADOR TÉCNICO DE SUPERVISIÓN</th>
                        <th style="width: 17%; text-align: center;">VALORACIÓN</th>
                        <th style="width: 16%;">OBSERVACIONES / AJUSTES</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td class="col-id">5.1</td>
                        <td class="col-indicator">
                            <span class="ind-title">Medidas de refuerzo y estimulación integradas en el aula:</span><br>
                            Se detallan las medidas pedagógicas inmediatas y ordinarias de estimulación comunicativa, motriz y socioafectiva para dar respuesta a desajustes en el desarrollo sin segregar al alumnado de su grupo de referencia.
                        </td>
                        <td class="col-val"><div class="checkbox-group"><span>☐ Sí</span><span>☐ No</span><span>☐ Ajustar</span></div></td>
                        <td class="col-obs"></td>
                    </tr>
                    <tr>
                        <td class="col-id">5.2</td>
                        <td class="col-indicator">
                            <span class="ind-title">Protocolo de derivación y coordinación con el EOEP:</span><br>
                            Se especifican los procedimientos de coordinación con el Equipo de Orientación Educativa y Psicopedagógico (EOEP) de zona o específico para la detección e intervención temprana ante indicios de NEAE.
                        </td>
                        <td class="col-val"><div class="checkbox-group"><span>☐ Sí</span><span>☐ No</span><span>☐ Ajustar</span></div></td>
                        <td class="col-obs"></td>
                    </tr>
                </tbody>
            </table>
        </div>

        <!-- DIMENSIÓN 6 -->
        <div class="dimension-block">
            <div class="dim-header">
                <span class="dim-title">DIMENSIÓN 6: ATENCIÓN A LAS DIFERENCIAS INDIVIDUALES (DUA) Y FAMILIAS</span>
                <span class="dim-sub">Inclusión educativa, accesibilidad física/cognitiva y comunicación sistemática</span>
            </div>
            <table class="dim-table">
                <thead>
                    <tr>
                        <th style="width: 4%; text-align: center;">ID</th>
                        <th style="width: 63%;">INDICADOR TÉCNICO DE SUPERVISIÓN</th>
                        <th style="width: 17%; text-align: center;">VALORACIÓN</th>
                        <th style="width: 16%;">OBSERVACIONES / AJUSTES</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td class="col-id">6.1</td>
                        <td class="col-indicator">
                            <span class="ind-title">Pautas DUA en espacios, materiales y actividades:</span><br>
                            La propuesta pedagógica contempla variedad de canales sensoriales, rincones multinivel, materiales manipulativos accesibles y múltiples formas de interacción y expresión de emociones e intereses.
                        </td>
                        <td class="col-val"><div class="checkbox-group"><span>☐ Sí</span><span>☐ No</span><span>☐ Ajustar</span></div></td>
                        <td class="col-obs"></td>
                    </tr>
                    <tr>
                        <td class="col-id">6.2</td>
                        <td class="col-indicator">
                            <span class="ind-title">Adaptaciones y personalización del aprendizaje:</span><br>
                            Se prevén medidas para la flexibilización de los ritmos y adaptaciones curriculares o de acceso para el alumnado con NEAE en coordinación con el profesorado de apoyo a las NEAE.
                        </td>
                        <td class="col-val"><div class="checkbox-group"><span>☐ Sí</span><span>☐ No</span><span>☐ Ajustar</span></div></td>
                        <td class="col-obs"></td>
                    </tr>
                    <tr>
                        <td class="col-id">6.3</td>
                        <td class="col-indicator">
                            <span class="ind-title">Coordinación y transparencia con las familias:</span><br>
                            Se planifican las entrevistas iniciales de anamnesis, las reuniones de seguimiento trimestral y el informe de evaluación cualitativo final, garantizando la corresponsabilidad educativa con las familias o tutores legales.
                        </td>
                        <td class="col-val"><div class="checkbox-group"><span>☐ Sí</span><span>☐ No</span><span>☐ Ajustar</span></div></td>
                        <td class="col-obs"></td>
                    </tr>
                </tbody>
            </table>
        </div>

        <!-- DICTAMEN OFICIAL -->
        <div class="dictamen-box">
            <div class="dictamen-header">DICTAMEN TÉCNICO DE LA JEFATURA DE ESTUDIOS / COMISIÓN DE SUPERVISIÓN</div>
            <div class="dictamen-options">
                <div class="dictamen-card">
                    <div class="dictamen-card-title">☐ FAVORABLE</div>
                    Cumple los requisitos curriculares y pedagógicos preceptivos. Aprobada para su integración en la PGA.
                </div>
                <div class="dictamen-card">
                    <div class="dictamen-card-title">☐ FAVORABLE CONDICIONADA</div>
                    Aprobación condicionada a subsanar los ajustes señalados en un plazo de _____ días hábiles.
                </div>
                <div class="dictamen-card danger">
                    <div class="dictamen-card-title">☐ REQUERIMIENTO DE SUBSANACIÓN</div>
                    No cumple aspectos nucleares (Dimensión 3 o 5). Debe reformularse antes del _____ / _____ / 2026.
                </div>
            </div>
        </div>

        <!-- FIRMAS -->
        <div class="signatures-box">
            <div class="sig-col">
                <div class="sig-title">POR LA JEFATURA DE ESTUDIOS / COMISIÓN DE SUPERVISIÓN</div>
                <div class="sig-line">Fdo.: __________________________________________________</div>
            </div>
            <div class="sig-col">
                <div class="sig-title">ENTERADO / POR EL EQUIPO DE CICLO DE EDUCACIÓN INFANTIL</div>
                <div class="sig-line">Fdo.: __________________________________________________</div>
            </div>
        </div>
    </div>

    <!-- Pie Página 2 -->
    <div>
        <div class="page-footer">
            <span>Marco Normativo de Referencia: Decreto 196/2022 • Orden de 24 de mayo de 2023 • Ley Orgánica 2/2006</span>
            <span>Propuesta Técnica Pedagógica · Uso Interno de Coordinación</span>
        </div>
        <div class="page-footer-center">Página 2 de 2</div>
    </div>
</div>

</body>
</html>
"""

# ==========================================
# 2. FORMACIÓN PROFESIONAL (FP)
# ==========================================
html_fp = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Checklist Supervisión Programaciones Didácticas - Formación Profesional</title>
<style>
{CSS_STYLES}
</style>
</head>
<body>

<!-- PÁGINA 1 -->
<div class="page">
    <div>
        <!-- Cabecera -->
        <div class="top-header">
            <div class="header-left">
                <div class="org-title">PROPUESTA TÉCNICA PEDAGÓGICA · COORDINACIÓN DOCENTE</div>
                <div class="org-sub">Herramienta Guía de Supervisión y Homologación de Módulos Profesionales</div>
                <div class="org-sub">Comisión de Coordinación Pedagógica (CCP) · Departamentos de Familia Profesional</div>
            </div>
            <div class="header-right">
                <div class="badge-box">
                    <div class="badge-title">PROPUESTA TÉCNICA</div>
                    <div class="badge-sub">FORMACIÓN PROFESIONAL</div>
                </div>
            </div>
        </div>

        <!-- Banner Título -->
        <div class="banner">
            <div>
                <div class="banner-title">CHECKLIST DE SUPERVISIÓN DE PROGRAMACIONES DE MÓDULOS (FP)</div>
                <div class="banner-sub">Herramienta Técnica para Jefaturas de Estudios y Comisión de Coordinación Pedagógica (CCP)</div>
            </div>
            <div class="banner-badge">CURSO 2026-2027</div>
        </div>

        <!-- Cajetín Metadatos -->
        <div class="metadata-box">
            <div class="metadata-row divider">
                <div class="meta-item"><span class="meta-label">CENTRO EDUCATIVO:</span> __________________________________________________</div>
                <div class="meta-item"><span class="meta-label">CÓDIGO DE CENTRO:</span> ____________</div>
                <div class="meta-item"><span class="meta-label">FECHA DE REVISIÓN:</span> ____________</div>
            </div>
            <div class="metadata-row">
                <div class="meta-item"><span class="meta-label">FAMILIA PROFESIONAL:</span> __________________________</div>
                <div class="meta-item"><span class="meta-label">CICLO FORMATIVO / CURSO:</span> __________________________</div>
                <div class="meta-item"><span class="meta-label">MÓDULO (CÓDIGO):</span> ____________________</div>
                <div class="meta-item"><span class="meta-label">RÉGIMEN:</span> General ☐ / Intensivo ☐ (Dual)</div>
                <div class="meta-item"><span class="meta-label">JEFATURA:</span> ________________</div>
            </div>
        </div>

        <!-- DIMENSIÓN 1 -->
        <div class="dimension-block">
            <div class="dim-header">
                <span class="dim-title">DIMENSIÓN 1: MARCO CURRICULAR Y CONCRECIÓN PRECEPTIVA DEL MÓDULO</span>
                <span class="dim-sub">Referentes de la Ley Orgánica 3/2022, Real Decreto 659/2023 y Decretos de Título</span>
            </div>
            <table class="dim-table">
                <thead>
                    <tr>
                        <th style="width: 4%; text-align: center;">ID</th>
                        <th style="width: 63%;">INDICADOR TÉCNICO DE SUPERVISIÓN</th>
                        <th style="width: 17%; text-align: center;">VALORACIÓN</th>
                        <th style="width: 16%;">OBSERVACIONES / AJUSTES</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td class="col-id">1.1</td>
                        <td class="col-indicator">
                            <span class="ind-title">Cobertura íntegra del 100% de RA y CE oficiales:</span><br>
                            Se programan íntegramente todos los Resultados de Aprendizaje (RA) y Criterios de Evaluación (CE) preceptivos del currículo oficial del módulo, respetando su redacción oficial, estructura técnica y sin supresión alguna.
                        </td>
                        <td class="col-val"><div class="checkbox-group"><span>☐ Sí</span><span>☐ No</span><span>☐ Ajustar</span></div></td>
                        <td class="col-obs"></td>
                    </tr>
                    <tr>
                        <td class="col-id">1.2</td>
                        <td class="col-indicator">
                            <span class="ind-title">Alineación con el Perfil Profesional y Competencias (CPPS):</span><br>
                            Cada Resultado de Aprendizaje está vinculado de forma explícita a las Competencias Profesionales, Personales y Sociales del título, a los Objetivos Generales del ciclo y al Catálogo Nacional de Estándares de Competencias Profesionales.
                        </td>
                        <td class="col-val"><div class="checkbox-group"><span>☐ Sí</span><span>☐ No</span><span>☐ Ajustar</span></div></td>
                        <td class="col-obs"></td>
                    </tr>
                    <tr>
                        <td class="col-id">1.3</td>
                        <td class="col-indicator">
                            <span class="ind-title">Contenidos y saberes técnicos aplicados con PRL y Sostenibilidad:</span><br>
                            Los saberes básicos se articulan al servicio de tareas profesionales reales, integrando la Prevención de Riesgos Laborales (PRL) específica, la gestión medioambiental, la digitalización del sector y las particularidades del tejido productivo canario.
                        </td>
                        <td class="col-val"><div class="checkbox-group"><span>☐ Sí</span><span>☐ No</span><span>☐ Ajustar</span></div></td>
                        <td class="col-obs"></td>
                    </tr>
                </tbody>
            </table>
        </div>

        <!-- DIMENSIÓN 2 -->
        <div class="dimension-block">
            <div class="dim-header">
                <span class="dim-title">DIMENSIÓN 2: SECUENCIACIÓN DE UNIDADES DE TRABAJO (SA-UT) Y DUALIDAD</span>
                <span class="dim-sub">Distribución temporal, retos productivos y alternancia en empresa</span>
            </div>
            <table class="dim-table">
                <thead>
                    <tr>
                        <th style="width: 4%; text-align: center;">ID</th>
                        <th style="width: 63%;">INDICADOR TÉCNICO DE SUPERVISIÓN</th>
                        <th style="width: 17%; text-align: center;">VALORACIÓN</th>
                        <th style="width: 16%;">OBSERVACIONES / AJUSTES</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td class="col-id">2.1</td>
                        <td class="col-indicator">
                            <span class="ind-title">Secuenciación y carga horaria modular equilibrada:</span><br>
                            El módulo está estructurado en una secuenciación coherente de Unidades de Trabajo / Situaciones de Aprendizaje (SA-UT), con asignación de horas acorde a la complejidad técnica y armonizadas con el calendario de alternancia en empresa (FP Dual).
                        </td>
                        <td class="col-val"><div class="checkbox-group"><span>☐ Sí</span><span>☐ No</span><span>☐ Ajustar</span></div></td>
                        <td class="col-obs"></td>
                    </tr>
                    <tr>
                        <td class="col-id">2.2</td>
                        <td class="col-indicator">
                            <span class="ind-title">Metodología activa de taller (ABR, Simulación y Merrill):</span><br>
                            Las SA-UT se formulan como retos profesionales verosímiles («El Encargo del Cliente»), organizando las sesiones en fases de demostración técnica por el docente, modelado, simulación guiada, ejecución autónoma en taller/laboratorio y protocolos de PRL.
                        </td>
                        <td class="col-val"><div class="checkbox-group"><span>☐ Sí</span><span>☐ No</span><span>☐ Ajustar</span></div></td>
                        <td class="col-obs"></td>
                    </tr>
                </tbody>
            </table>
        </div>

        <!-- DIMENSIÓN 3 -->
        <div class="dimension-block">
            <div class="dim-header">
                <span class="dim-title critical">DIMENSIÓN 3: CRITERIOS DE CALIFICACIÓN *(NÚCLEO CRÍTICO)*</span>
                <span class="dim-sub">Superación de RAs, garantía de legalidad evaluativa y erradicación del promedio por instrumentos</span>
            </div>
            <table class="dim-table">
                <thead>
                    <tr>
                        <th style="width: 4%; text-align: center;">ID</th>
                        <th style="width: 63%;">INDICADOR TÉCNICO DE SUPERVISIÓN</th>
                        <th style="width: 17%; text-align: center;">VALORACIÓN</th>
                        <th style="width: 16%;">OBSERVACIONES / AJUSTES</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td class="col-id">3.1</td>
                        <td class="col-indicator">
                            <span class="ind-title">Calificación 100% vinculada a Resultados de Aprendizaje y CE:</span><br>
                            La calificación del módulo se extrae exclusivamente del grado de logro de los Resultados de Aprendizaje mediante sus Criterios de Evaluación. Queda <strong>prohibido calificar por agregación de instrumentos aislados</strong> (ej. «Exámenes teóricos 60%, Prácticas taller 40%»).<br>
                            <span class="critical-callout">Infracción crítica: ponderar por instrumentos</span>
                        </td>
                        <td class="col-val"><div class="checkbox-group"><span>☐ Sí</span><span>☐ No</span><span>☐ Ajustar</span></div></td>
                        <td class="col-obs"></td>
                    </tr>
                    <tr>
                        <td class="col-id">3.2</td>
                        <td class="col-indicator">
                            <span class="ind-title">Ponderación objetiva y superación independiente de RAs:</span><br>
                            Se detalla el peso porcentual de cada RA en el módulo (justificado por su carga horaria o relevancia técnica) y se explicita la condición necesaria de superar cada RA (calificación mínima de 5,0) para la superación del módulo profesional.
                        </td>
                        <td class="col-val"><div class="checkbox-group"><span>☐ Sí</span><span>☐ No</span><span>☐ Ajustar</span></div></td>
                        <td class="col-obs"></td>
                    </tr>
                    <tr>
                        <td class="col-id">3.3</td>
                        <td class="col-indicator">
                            <span class="ind-title">Tratamiento de hábitos de taller, seguridad y actitud profesional:</span><br>
                            Los aspectos de orden, puntualidad, trabajo en equipo, rigor procedimental y cumplimiento de la normativa de PRL solo se califican cuando forman parte expresa de la formulación de los Criterios de Evaluación del currículo del módulo.
                        </td>
                        <td class="col-val"><div class="checkbox-group"><span>☐ Sí</span><span>☐ No</span><span>☐ Ajustar</span></div></td>
                        <td class="col-obs"></td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

    <!-- Pie Página 1 -->
    <div>
        <div class="page-footer">
            <span>Marco Normativo de Referencia: Ley Orgánica 3/2022 • Real Decreto 659/2023 • Decretos de Título de la Comunidad Autónoma de Canarias</span>
            <span>Propuesta Técnica Pedagógica · Uso Interno de Coordinación</span>
        </div>
        <div class="page-footer-center">Página 1 de 2</div>
    </div>
</div>

<!-- PÁGINA 2 -->
<div class="page">
    <div>
        <!-- Cabecera Compacta Página 2 -->
        <div class="top-header">
            <div class="header-left">
                <div class="org-title">PROPUESTA TÉCNICA PEDAGÓGICA · SUPERVISIÓN DE MÓDULOS DE FP</div>
                <div class="org-sub">Formación Profesional · Herramienta de Coordinación y Homologación Curricular</div>
            </div>
            <div class="header-right">
                <div class="badge-box">
                    <div class="badge-title">CURSO 2026-2027</div>
                    <div class="badge-sub">EVALUACIÓN POR RA Y CE</div>
                </div>
            </div>
        </div>

        <!-- DIMENSIÓN 4 -->
        <div class="dimension-block">
            <div class="dim-header">
                <span class="dim-title">DIMENSIÓN 4: INSTRUMENTOS DE EVALUACIÓN Y EVIDENCIAS TÉCNICAS</span>
                <span class="dim-sub">Productos tangibles, rúbricas analíticas profesionales y seguimiento Dual</span>
            </div>
            <table class="dim-table">
                <thead>
                    <tr>
                        <th style="width: 4%; text-align: center;">ID</th>
                        <th style="width: 63%;">INDICADOR TÉCNICO DE SUPERVISIÓN</th>
                        <th style="width: 17%; text-align: center;">VALORACIÓN</th>
                        <th style="width: 16%;">OBSERVACIONES / AJUSTES</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td class="col-id">4.1</td>
                        <td class="col-indicator">
                            <span class="ind-title">Evidencias técnicas auténticas y productos profesionales:</span><br>
                            Se definen instrumentos vinculados al desempeño real: órdenes de trabajo, memorias de cálculo, planos, piezas ejecutadas, cuadros cableados, software desarrollado, diagnósticos de averías o presentaciones técnicas ante clientes.
                        </td>
                        <td class="col-val"><div class="checkbox-group"><span>☐ Sí</span><span>☐ No</span><span>☐ Ajustar</span></div></td>
                        <td class="col-obs"></td>
                    </tr>
                    <tr>
                        <td class="col-id">4.2</td>
                        <td class="col-indicator">
                            <span class="ind-title">Rúbricas analíticas con tolerancias y graduadores técnicos:</span><br>
                            Los instrumentos incorporan escalas y rúbricas graduadas con criterios observables (1 a 10) que describen con precisión márgenes de tolerancia, corrección técnica, destreza operativa, autonomía y protocolos de calidad.
                        </td>
                        <td class="col-val"><div class="checkbox-group"><span>☐ Sí</span><span>☐ No</span><span>☐ Ajustar</span></div></td>
                        <td class="col-obs"></td>
                    </tr>
                    <tr>
                        <td class="col-id">4.3</td>
                        <td class="col-indicator">
                            <span class="ind-title">Evaluación de la formación en empresa (FP Dual):</span><br>
                            Se especifican los mecanismos de coordinación, hojas de seguimiento y cuadernos de campo acordados con el tutor de empresa para la valoración compartida de los resultados de aprendizaje desarrollados en el centro de trabajo.
                        </td>
                        <td class="col-val"><div class="checkbox-group"><span>☐ Sí</span><span>☐ No</span><span>☐ Ajustar</span></div></td>
                        <td class="col-obs"></td>
                    </tr>
                </tbody>
            </table>
        </div>

        <!-- DIMENSIÓN 5 -->
        <div class="dimension-block">
            <div class="dim-header">
                <span class="dim-title">DIMENSIÓN 5: PLAN DE REFUERZO, APOYO Y RECUPERACIÓN CONTINUA DE RAs</span>
                <span class="dim-sub">Recuperación integrada en el proceso ordinario y seguimiento de módulos pendientes</span>
            </div>
            <table class="dim-table">
                <thead>
                    <tr>
                        <th style="width: 4%; text-align: center;">ID</th>
                        <th style="width: 63%;">INDICADOR TÉCNICO DE SUPERVISIÓN</th>
                        <th style="width: 17%; text-align: center;">VALORACIÓN</th>
                        <th style="width: 16%;">OBSERVACIONES / AJUSTES</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td class="col-id">5.1</td>
                        <td class="col-indicator">
                            <span class="ind-title">Recuperación continua de RAs no superados en periodo ordinario:</span><br>
                            Se prevé un procedimiento transparente para que el alumnado recupere RAs/CEs no alcanzados durante el curso ordinario (repetición guiada de prácticas, nuevos retos en taller, entregas técnicas corregidas), erradicando el examen único final de memoria como vía exclusiva.
                        </td>
                        <td class="col-val"><div class="checkbox-group"><span>☐ Sí</span><span>☐ No</span><span>☐ Ajustar</span></div></td>
                        <td class="col-obs"></td>
                    </tr>
                    <tr>
                        <td class="col-id">5.2</td>
                        <td class="col-indicator">
                            <span class="ind-title">Plan de seguimiento para alumnado con el módulo pendiente:</span><br>
                            Se detalla el programa de recuperación para alumnado con el módulo no superado de cursos anteriores: profesorado responsable del seguimiento, cronograma de actividades prácticas y calendario de las convocatorias de evaluación ordinaria y extraordinaria.
                        </td>
                        <td class="col-val"><div class="checkbox-group"><span>☐ Sí</span><span>☐ No</span><span>☐ Ajustar</span></div></td>
                        <td class="col-obs"></td>
                    </tr>
                </tbody>
            </table>
        </div>

        <!-- DIMENSIÓN 6 -->
        <div class="dimension-block">
            <div class="dim-header">
                <span class="dim-title">DIMENSIÓN 6: ATENCIÓN A LA DIVERSIDAD (DUA), TRANSVERSALIDAD Y PUBLICIDAD</span>
                <span class="dim-sub">Accesibilidad en entornos profesionales y transparencia informativa</span>
            </div>
            <table class="dim-table">
                <thead>
                    <tr>
                        <th style="width: 4%; text-align: center;">ID</th>
                        <th style="width: 63%;">INDICADOR TÉCNICO DE SUPERVISIÓN</th>
                        <th style="width: 17%; text-align: center;">VALORACIÓN</th>
                        <th style="width: 16%;">OBSERVACIONES / AJUSTES</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td class="col-id">6.1</td>
                        <td class="col-indicator">
                            <span class="ind-title">Estrategias DUA adaptadas al entorno productivo:</span><br>
                            Se incorporan adaptaciones metodológicas y de formato (simuladores virtuales, documentación gráfica, checklists ilustradas, subtítulos en vídeos técnicos) sin comprometer las cualificaciones del perfil profesional.
                        </td>
                        <td class="col-val"><div class="checkbox-group"><span>☐ Sí</span><span>☐ No</span><span>☐ Ajustar</span></div></td>
                        <td class="col-obs"></td>
                    </tr>
                    <tr>
                        <td class="col-id">6.2</td>
                        <td class="col-indicator">
                            <span class="ind-title">Coordinación con módulos transversales y Proyecto Intermodular:</span><br>
                            Se prevén conexiones pedagógicas con los módulos de <em>Itinerario Personal para la Empleabilidad (IPE)</em>, <em>Digitalización</em>, <em>Sostenibilidad</em> o el <em>Proyecto Intermodular</em>, optimizando tareas compartidas.
                        </td>
                        <td class="col-val"><div class="checkbox-group"><span>☐ Sí</span><span>☐ No</span><span>☐ Ajustar</span></div></td>
                        <td class="col-obs"></td>
                    </tr>
                    <tr>
                        <td class="col-id">6.3</td>
                        <td class="col-indicator">
                            <span class="ind-title">Extracto informativo accesible para el alumnado:</span><br>
                            Se acompaña una ficha resumen o guía de aprendizaje clara y pública desde el primer día de clase, con el catálogo de RAs, sus ponderaciones, requisitos de evaluación continua, condiciones de la estancia dual y procedimientos de recuperación.
                        </td>
                        <td class="col-val"><div class="checkbox-group"><span>☐ Sí</span><span>☐ No</span><span>☐ Ajustar</span></div></td>
                        <td class="col-obs"></td>
                    </tr>
                </tbody>
            </table>
        </div>

        <!-- DICTAMEN OFICIAL -->
        <div class="dictamen-box">
            <div class="dictamen-header">DICTAMEN TÉCNICO DE LA JEFATURA DE ESTUDIOS / COMISIÓN DE SUPERVISIÓN</div>
            <div class="dictamen-options">
                <div class="dictamen-card">
                    <div class="dictamen-card-title">☐ FAVORABLE</div>
                    Cumple los requisitos curriculares y profesionales preceptivos. Aprobada para su integración en la PGA.
                </div>
                <div class="dictamen-card">
                    <div class="dictamen-card-title">☐ FAVORABLE CONDICIONADA</div>
                    Aprobación condicionada a subsanar los ajustes señalados en un plazo de _____ días hábiles.
                </div>
                <div class="dictamen-card danger">
                    <div class="dictamen-card-title">☐ REQUERIMIENTO DE SUBSANACIÓN</div>
                    No cumple aspectos nucleares (Dimensión 3 o 5). Debe reformularse antes del _____ / _____ / 2026.
                </div>
            </div>
        </div>

        <!-- FIRMAS -->
        <div class="signatures-box">
            <div class="sig-col">
                <div class="sig-title">POR LA JEFATURA DE ESTUDIOS / COMISIÓN DE SUPERVISIÓN</div>
                <div class="sig-line">Fdo.: __________________________________________________</div>
            </div>
            <div class="sig-col">
                <div class="sig-title">ENTERADO / POR EL DEPARTAMENTO DE FAMILIA PROFESIONAL</div>
                <div class="sig-line">Fdo.: __________________________________________________</div>
            </div>
        </div>
    </div>

    <!-- Pie Página 2 -->
    <div>
        <div class="page-footer">
            <span>Marco Normativo de Referencia: Ley Orgánica 3/2022 • Real Decreto 659/2023 • Decretos de Currículo de Canarias</span>
            <span>Propuesta Técnica Pedagógica · Uso Interno de Coordinación</span>
        </div>
        <div class="page-footer-center">Página 2 de 2</div>
    </div>
</div>

</body>
</html>
"""

# ==========================================
# 3. ENSEÑANZAS DE RÉGIMEN ESPECIAL (ERE)
# ==========================================
html_ere = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Checklist Supervisión Programaciones Didácticas - Enseñanzas de Régimen Especial</title>
<style>
{CSS_STYLES}
</style>
</head>
<body>

<!-- PÁGINA 1 -->
<div class="page">
    <div>
        <!-- Cabecera -->
        <div class="top-header">
            <div class="header-left">
                <div class="org-title">PROPUESTA TÉCNICA PEDAGÓGICA · COORDINACIÓN DOCENTE</div>
                <div class="org-sub">Herramienta Guía de Supervisión de Programaciones Didácticas y Guías Docentes</div>
                <div class="org-sub">Comisión de Coordinación Pedagógica (CCP) · Departamentos Didácticos ERE</div>
            </div>
            <div class="header-right">
                <div class="badge-box">
                    <div class="badge-title">PROPUESTA TÉCNICA</div>
                    <div class="badge-sub">RÉGIMEN ESPECIAL (ERE)</div>
                </div>
            </div>
        </div>

        <!-- Banner Título -->
        <div class="banner">
            <div>
                <div class="banner-title">CHECKLIST DE SUPERVISIÓN: PROGRAMACIONES Y GUÍAS DOCENTES (ERE)</div>
                <div class="banner-sub">Herramienta Técnica para Idiomas (EOI), Conservatorios, Escuelas de Arte, Deportivas y EEAASS</div>
            </div>
            <div class="banner-badge">CURSO 2026-2027</div>
        </div>

        <!-- Cajetín Metadatos -->
        <div class="metadata-box">
            <div class="metadata-row divider">
                <div class="meta-item"><span class="meta-label">CENTRO EDUCATIVO:</span> __________________________________________________</div>
                <div class="meta-item"><span class="meta-label">CÓDIGO DE CENTRO:</span> ____________</div>
                <div class="meta-item"><span class="meta-label">FECHA DE REVISIÓN:</span> ____________</div>
            </div>
            <div class="metadata-row">
                <div class="meta-item"><span class="meta-label">ENSEÑANZA:</span> EOI ☐ / Deportiva ☐ / Conservatorio ☐ / Arte y Diseño ☐ / EEAASS ☐</div>
                <div class="meta-item"><span class="meta-label">ASIGNATURA / MÓDULO / GUÍA:</span> __________________________</div>
                <div class="meta-item"><span class="meta-label">NIVEL / ECTS:</span> __________</div>
                <div class="meta-item"><span class="meta-label">JEFATURA:</span> ____________________</div>
            </div>
        </div>

        <!-- DIMENSIÓN 1 -->
        <div class="dimension-block">
            <div class="dim-header">
                <span class="dim-title">DIMENSIÓN 1: MARCO NORMATIVO SECTORIAL Y CONCRECIÓN PRECEPTIVA</span>
                <span class="dim-sub">Referentes normativos de cada rama ERE en Canarias (Sin aplicar Perfil de Salida de ESO)</span>
            </div>
            <table class="dim-table">
                <thead>
                    <tr>
                        <th style="width: 4%; text-align: center;">ID</th>
                        <th style="width: 63%;">INDICADOR TÉCNICO DE SUPERVISIÓN</th>
                        <th style="width: 17%; text-align: center;">VALORACIÓN</th>
                        <th style="width: 16%;">OBSERVACIONES / AJUSTES</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td class="col-id">1.1</td>
                        <td class="col-indicator">
                            <span class="ind-title">Adopción del marco normativo sectorial específico íntegro:</span><br>
                            La programación se fundamenta estrictamente en la normativa reguladora de su enseñanza en Canarias (EOI: Orden 15/09/2022; EDRE: D. 93/2019; APyD: Orden 22/03/2013; Conservatorios: D. 364/2007 y O. 28/05/2008; EEAASS: Ley 1/2024 y D. 30/2014), sin extrapolar elementos ajenos del régimen general.
                        </td>
                        <td class="col-val"><div class="checkbox-group"><span>☐ Sí</span><span>☐ No</span><span>☐ Ajustar</span></div></td>
                        <td class="col-obs"></td>
                    </tr>
                    <tr>
                        <td class="col-id">1.2</td>
                        <td class="col-indicator">
                            <span class="ind-title">Alineación con los estándares terminales de la rama:</span><br>
                            Los objetivos y criterios responden al nivel oficial correspondiente: descriptores del MCERL (A2 a C2 en EOI), estándares técnicos de la modalidad deportiva (EDRE), competencias de taller artesanal/diseño (APyD), exigencias de técnica y repertorio (Música/Danza) o competencias de Grado EEES (EEAASS).
                        </td>
                        <td class="col-val"><div class="checkbox-group"><span>☐ Sí</span><span>☐ No</span><span>☐ Ajustar</span></div></td>
                        <td class="col-obs"></td>
                    </tr>
                    <tr>
                        <td class="col-id">1.3</td>
                        <td class="col-indicator">
                            <span class="ind-title">Contenidos y repertorios especializados actualizados:</span><br>
                            Se planifican con precisión los contenidos técnicos, programas de obras por curso, directrices de entrenamiento/reglamento, corpus léxico-discursivo o proyectos artísticos, incorporando la creación y contexto cultural de Canarias cuando proceda.
                        </td>
                        <td class="col-val"><div class="checkbox-group"><span>☐ Sí</span><span>☐ No</span><span>☐ Ajustar</span></div></td>
                        <td class="col-obs"></td>
                    </tr>
                </tbody>
            </table>
        </div>

        <!-- DIMENSIÓN 2 -->
        <div class="dimension-block">
            <div class="dim-header">
                <span class="dim-title">DIMENSIÓN 2: ORGANIZACIÓN PEDAGÓGICA Y MODELOS DIDÁCTICOS SINGULARES</span>
                <span class="dim-sub">Coherencia con las metodologías de alto rendimiento técnico, interpretativo y práctico</span>
            </div>
            <table class="dim-table">
                <thead>
                    <tr>
                        <th style="width: 4%; text-align: center;">ID</th>
                        <th style="width: 63%;">INDICADOR TÉCNICO DE SUPERVISIÓN</th>
                        <th style="width: 17%; text-align: center;">VALORACIÓN</th>
                        <th style="width: 16%;">OBSERVACIONES / AJUSTES</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td class="col-id">2.1</td>
                        <td class="col-indicator">
                            <span class="ind-title">Estructura adaptada al modelo de la enseñanza:</span><br>
                            La temporización se adecúa al formato propio de la especialidad: 5 actividades de lengua en EOI; bloques común/específico en EDRE; módulos teóricos y talleres en APyD; asignaturas individuales/colectivas en Conservatorios; guías docentes semestrales por créditos ECTS en EEAASS.
                        </td>
                        <td class="col-val"><div class="checkbox-group"><span>☐ Sí</span><span>☐ No</span><span>☐ Ajustar</span></div></td>
                        <td class="col-obs"></td>
                    </tr>
                    <tr>
                        <td class="col-id">2.2</td>
                        <td class="col-indicator">
                            <span class="ind-title">Metodologías activas especializadas:</span><br>
                            El diseño pedagógico se articula a través de enfoques comunicativos auténticos (EOI), modelado y táctica de campo (EDRE), producción tangible en talleres y oficios (APyD), audiciones y técnica instrumental (Conservatorios) o investigación y praxis proyectual (EEAASS).
                        </td>
                        <td class="col-val"><div class="checkbox-group"><span>☐ Sí</span><span>☐ No</span><span>☐ Ajustar</span></div></td>
                        <td class="col-obs"></td>
                    </tr>
                </tbody>
            </table>
        </div>

        <!-- DIMENSIÓN 3 -->
        <div class="dimension-block">
            <div class="dim-header">
                <span class="dim-title critical">DIMENSIÓN 3: SISTEMAS DE CALIFICACIÓN SECTORIALES *(NÚCLEO CRÍTICO)*</span>
                <span class="dim-sub">Rigor en las escalas de calificación legales de cada rama y prohibición de compensaciones indebidas</span>
            </div>
            <table class="dim-table">
                <thead>
                    <tr>
                        <th style="width: 4%; text-align: center;">ID</th>
                        <th style="width: 63%;">INDICADOR TÉCNICO DE SUPERVISIÓN</th>
                        <th style="width: 17%; text-align: center;">VALORACIÓN</th>
                        <th style="width: 16%;">OBSERVACIONES / AJUSTES</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td class="col-id">3.1</td>
                        <td class="col-indicator">
                            <span class="ind-title">Cumplimiento riguroso de la escala y fórmula de calificación sectorial:</span><br>
                            La calificación respeta de forma inexcusable el marco legal propio: EOI (5 actividades de lengua estancas independientes sin compensación); Conservatorios (escala 1 a 10 sin decimales y primacía de instrumento); EDRE y APyD (1 a 10 y Apto/No Apto en prácticas/proyectos); EEAASS (0 a 10 con un decimal según RD 1614/2009).<br>
                            <span class="critical-callout">Infracción crítica: aplicar escalas o promedios impropios de la rama</span>
                        </td>
                        <td class="col-val"><div class="checkbox-group"><span>☐ Sí</span><span>☐ No</span><span>☐ Ajustar</span></div></td>
                        <td class="col-obs"></td>
                    </tr>
                    <tr>
                        <td class="col-id">3.2</td>
                        <td class="col-indicator">
                            <span class="ind-title">Transparencia en tribunales, comisiones y defensas públicas:</span><br>
                            Se detallan las rúbricas y criterios colegiados objetivos para la valoración de audiciones, pruebas de certificación de idiomas, defensas de Proyectos Integrados, Obras Finales o Trabajos Fin de Estudios (TFE).
                        </td>
                        <td class="col-val"><div class="checkbox-group"><span>☐ Sí</span><span>☐ No</span><span>☐ Ajustar</span></div></td>
                        <td class="col-obs"></td>
                    </tr>
                    <tr>
                        <td class="col-id">3.3</td>
                        <td class="col-indicator">
                            <span class="ind-title">Tratamiento estricto de la actitud y asistencia:</span><br>
                            No se asignan porcentajes arbitrarios a la «actitud» o a la simple asistencia física, salvo que la regulación sectorial fije porcentajes de presencialidad preceptivos para conservar el derecho a la evaluación continua.
                        </td>
                        <td class="col-val"><div class="checkbox-group"><span>☐ Sí</span><span>☐ No</span><span>☐ Ajustar</span></div></td>
                        <td class="col-obs"></td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

    <!-- Pie Página 1 -->
    <div>
        <div class="page-footer">
            <span>Marco Normativo Sectorial de Referencia: Ley Orgánica 2/2006 (art. 3.2 y 58-65) • Decretos y Órdenes reguladoras de ERE en Canarias</span>
            <span>Propuesta Técnica Pedagógica · Uso Interno de Coordinación</span>
        </div>
        <div class="page-footer-center">Página 1 de 2</div>
    </div>
</div>

<!-- PÁGINA 2 -->
<div class="page">
    <div>
        <!-- Cabecera Compacta Página 2 -->
        <div class="top-header">
            <div class="header-left">
                <div class="org-title">PROPUESTA TÉCNICA PEDAGÓGICA · SUPERVISIÓN DE ENSEÑANZAS DE RÉGIMEN ESPECIAL</div>
                <div class="org-sub">EOI · Conservatorios · Escuelas de Arte · Enseñanzas Deportivas · EEAASS</div>
            </div>
            <div class="header-right">
                <div class="badge-box">
                    <div class="badge-title">CURSO 2026-2027</div>
                    <div class="badge-sub">CALIFICACIÓN SECTORIAL</div>
                </div>
            </div>
        </div>

        <!-- DIMENSIÓN 4 -->
        <div class="dimension-block">
            <div class="dim-header">
                <span class="dim-title">DIMENSIÓN 4: INSTRUMENTOS DE EVALUACIÓN Y EVIDENCIAS OBJETIVAS</span>
                <span class="dim-sub">Audiciones, memorias técnicas, pruebas de ejecución y rúbricas analíticas oficiales</span>
            </div>
            <table class="dim-table">
                <thead>
                    <tr>
                        <th style="width: 4%; text-align: center;">ID</th>
                        <th style="width: 63%;">INDICADOR TÉCNICO DE SUPERVISIÓN</th>
                        <th style="width: 17%; text-align: center;">VALORACIÓN</th>
                        <th style="width: 16%;">OBSERVACIONES / AJUSTES</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td class="col-id">4.1</td>
                        <td class="col-indicator">
                            <span class="ind-title">Diversidad de evidencias técnicas, artísticas y comunicativas:</span><br>
                            Se contemplan registros directos de ejecución (grabaciones de audio/vídeo, audiciones de cámara, memorias constructivas, piezas terminadas, simulaciones tácticas deportivas, producciones escritas y monólogos/diálogos).
                        </td>
                        <td class="col-val"><div class="checkbox-group"><span>☐ Sí</span><span>☐ No</span><span>☐ Ajustar</span></div></td>
                        <td class="col-obs"></td>
                    </tr>
                    <tr>
                        <td class="col-id">4.2</td>
                        <td class="col-indicator">
                            <span class="ind-title">Rúbricas analíticas oficiales con graduadores técnicos en negrita:</span><br>
                            Los criterios cuentan con rúbricas que mantienen el verbo invariable, describen el umbral aprobatorio oficial y utilizan graduadores observables en <strong>negrita</strong> para diferenciar fluidez, afinación, precisión métrica o rigor técnico, tipificando los errores en el nivel insuficiente.
                        </td>
                        <td class="col-val"><div class="checkbox-group"><span>☐ Sí</span><span>☐ No</span><span>☐ Ajustar</span></div></td>
                        <td class="col-obs"></td>
                    </tr>
                    <tr>
                        <td class="col-id">4.3</td>
                        <td class="col-indicator">
                            <span class="ind-title">Evaluación continua, coevaluación y feedback formativo:</span><br>
                            Se establecen rutinas sistemáticas de retroalimentación cualitativa tras audiciones, prácticas de taller o simulaciones orales, promoviendo la autocrítica profesional del alumnado.
                        </td>
                        <td class="col-val"><div class="checkbox-group"><span>☐ Sí</span><span>☐ No</span><span>☐ Ajustar</span></div></td>
                        <td class="col-obs"></td>
                    </tr>
                </tbody>
            </table>
        </div>

        <!-- DIMENSIÓN 5 -->
        <div class="dimension-block">
            <div class="dim-header">
                <span class="dim-title">DIMENSIÓN 5: PLAN DE APOYO, SEGUIMIENTO Y RECUPERACIÓN CONTINUA</span>
                <span class="dim-sub">Estrategias de recuperación en el proceso ordinario y superación de asignaturas/módulos pendientes</span>
            </div>
            <table class="dim-table">
                <thead>
                    <tr>
                        <th style="width: 4%; text-align: center;">ID</th>
                        <th style="width: 63%;">INDICADOR TÉCNICO DE SUPERVISIÓN</th>
                        <th style="width: 17%; text-align: center;">VALORACIÓN</th>
                        <th style="width: 16%;">OBSERVACIONES / AJUSTES</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td class="col-id">5.1</td>
                        <td class="col-indicator">
                            <span class="ind-title">Mecanismos ordinarios de recuperación durante el curso:</span><br>
                            Se prevén segundas audiciones, reelaboración de piezas de taller, nuevas oportunidades orales o reentregas técnicas dentro del desarrollo ordinario de las clases, evitando el examen final único no formativo.
                        </td>
                        <td class="col-val"><div class="checkbox-group"><span>☐ Sí</span><span>☐ No</span><span>☐ Ajustar</span></div></td>
                        <td class="col-obs"></td>
                    </tr>
                    <tr>
                        <td class="col-id">5.2</td>
                        <td class="col-indicator">
                            <span class="ind-title">Plan oficial para asignaturas o módulos pendientes:</span><br>
                            Se describe con precisión el programa de recuperación para alumnado con asignaturas o módulos no superados de cursos previos: docente asignado, tareas de seguimiento periódico, audiciones parciales y calendario formal de convocatorias reglamentarias.
                        </td>
                        <td class="col-val"><div class="checkbox-group"><span>☐ Sí</span><span>☐ No</span><span>☐ Ajustar</span></div></td>
                        <td class="col-obs"></td>
                    </tr>
                </tbody>
            </table>
        </div>

        <!-- DIMENSIÓN 6 -->
        <div class="dimension-block">
            <div class="dim-header">
                <span class="dim-title">DIMENSIÓN 6: INCLUSIÓN, PREVENCIÓN DE RIESGOS ESPECÍFICOS Y PUBLICIDAD</span>
                <span class="dim-sub">Accesibilidad, adaptaciones de tiempo/formato en pruebas y transparencia</span>
            </div>
            <table class="dim-table">
                <thead>
                    <tr>
                        <th style="width: 4%; text-align: center;">ID</th>
                        <th style="width: 63%;">INDICADOR TÉCNICO DE SUPERVISIÓN</th>
                        <th style="width: 17%; text-align: center;">VALORACIÓN</th>
                        <th style="width: 16%;">OBSERVACIONES / AJUSTES</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td class="col-id">6.1</td>
                        <td class="col-indicator">
                            <span class="ind-title">Adaptaciones en pruebas y accesibilidad técnica:</span><br>
                            Se articulan las adaptaciones de tiempo, formato y medios para alumnado con discapacidad o NEAE en pruebas de certificación de idiomas, audiciones o exámenes de taller, respetando el nivel de exigencia de la titulación.
                        </td>
                        <td class="col-val"><div class="checkbox-group"><span>☐ Sí</span><span>☐ No</span><span>☐ Ajustar</span></div></td>
                        <td class="col-obs"></td>
                    </tr>
                    <tr>
                        <td class="col-id">6.2</td>
                        <td class="col-indicator">
                            <span class="ind-title">Seguridad en talleres, pistas y salud músculo-esquelética / vocal:</span><br>
                            En enseñanzas que lo requieran (Artes Plásticas, Danza, Música, Deportivas) se detallan los protocolos preceptivos de prevención de lesiones (ergonomía, higiene postural y vocal) y normas de seguridad en el uso de maquinaria e instalaciones.
                        </td>
                        <td class="col-val"><div class="checkbox-group"><span>☐ Sí</span><span>☐ No</span><span>☐ Ajustar</span></div></td>
                        <td class="col-obs"></td>
                    </tr>
                    <tr>
                        <td class="col-id">6.3</td>
                        <td class="col-indicator">
                            <span class="ind-title">Transparencia y difusión de la Programación / Guía Docente:</span><br>
                            Se garantiza la publicación fehaciente al inicio del periodo lectivo de la Programación Didáctica o Guía Docente (con los criterios de evaluación, repertorios, baremos y condiciones de examen de convocatorias ordinarias y extraordinarias).
                        </td>
                        <td class="col-val"><div class="checkbox-group"><span>☐ Sí</span><span>☐ No</span><span>☐ Ajustar</span></div></td>
                        <td class="col-obs"></td>
                    </tr>
                </tbody>
            </table>
        </div>

        <!-- DICTAMEN OFICIAL -->
        <div class="dictamen-box">
            <div class="dictamen-header">DICTAMEN TÉCNICO DE LA JEFATURA DE ESTUDIOS / COMISIÓN DE SUPERVISIÓN</div>
            <div class="dictamen-options">
                <div class="dictamen-card">
                    <div class="dictamen-card-title">☐ FAVORABLE</div>
                    Cumple los requisitos curriculares y disciplinares preceptivos. Aprobada para su integración en la PGA.
                </div>
                <div class="dictamen-card">
                    <div class="dictamen-card-title">☐ FAVORABLE CONDICIONADA</div>
                    Aprobación condicionada a subsanar los ajustes señalados en un plazo de _____ días hábiles.
                </div>
                <div class="dictamen-card danger">
                    <div class="dictamen-card-title">☐ REQUERIMIENTO DE SUBSANACIÓN</div>
                    No cumple aspectos nucleares (Dimensión 3 o 5). Debe reformularse antes del _____ / _____ / 2026.
                </div>
            </div>
        </div>

        <!-- FIRMAS -->
        <div class="signatures-box">
            <div class="sig-col">
                <div class="sig-title">POR LA JEFATURA DE ESTUDIOS / COMISIÓN DE SUPERVISIÓN</div>
                <div class="sig-line">Fdo.: __________________________________________________</div>
            </div>
            <div class="sig-col">
                <div class="sig-title">ENTERADO / POR EL DEPARTAMENTO O COORDINACIÓN DE ENSEÑANZA</div>
                <div class="sig-line">Fdo.: __________________________________________________</div>
            </div>
        </div>
    </div>

    <!-- Pie Página 2 -->
    <div>
        <div class="page-footer">
            <span>Marco Normativo Sectorial de Referencia: Ley Orgánica 2/2006 • Decretos y Órdenes específicas de ERE en Canarias</span>
            <span>Propuesta Técnica Pedagógica · Uso Interno de Coordinación</span>
        </div>
        <div class="page-footer-center">Página 2 de 2</div>
    </div>
</div>

</body>
</html>
"""

# Generación
pdf_infantil_path = os.path.join(OUTPUT_DIR, "Checklist_Supervision_Infantil_Propuesta.pdf")
pdf_fp_path = os.path.join(OUTPUT_DIR, "Checklist_Supervision_FP_Propuesta.pdf")
pdf_ere_path = os.path.join(OUTPUT_DIR, "Checklist_Supervision_ERE_Propuesta.pdf")

print("Generando Checklist de Educación Infantil...")
p1 = generate_pdf_from_html(html_infantil, pdf_infantil_path)

print("Generando Checklist de Formación Profesional...")
p2 = generate_pdf_from_html(html_fp, pdf_fp_path)

print("Generando Checklist de Enseñanzas de Régimen Especial...")
p3 = generate_pdf_from_html(html_ere, pdf_ere_path)

print(f"\n--- Resumen de Generación ---")
print(f"Infantil: {p1} páginas -> {pdf_infantil_path}")
print(f"FP:       {p2} páginas -> {pdf_fp_path}")
print(f"ERE:      {p3} páginas -> {pdf_ere_path}")
