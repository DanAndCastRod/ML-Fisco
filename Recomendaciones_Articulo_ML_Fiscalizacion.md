# Recomendaciones — Machine Learning y Fiscalización Tributaria en Colombia

**Documento:** *Entrega 1 — Formulación y Justificación del Problema*
**Autora:** Angie Paola Agudelo Loaiza
**Programa:** Especialización en Legislación Tributaria — UPB Medellín
**Fecha de análisis:** 9 de mayo de 2026

---

## 1. Diagnóstico del Estado Actual

### 1.1 Fortalezas del documento

| Aspecto | Observación |
|---|---|
| **Contexto macro** | Excelente contextualización de la brecha fiscal colombiana con datos del Informe OCDE/DIAN 2021 (6.5% del PIB) |
| **Pensamiento sistémico** | Uso original del arquetipo de *desplazamiento de la carga* para explicar la espiral de reformas tributarias fragmentadas |
| **Visión tecnológica** | Clara articulación de por qué el ML es superior al modelo reactivo actual de la DIAN |
| **Fuentes institucionales** | Buen anclaje en documentos de la OCDE (*Tax Administration 3.0*) y la DIAN |

### 1.2 Debilidades identificadas

| Aspecto | Problema |
|---|---|
| **Amplitud del problema jurídico** | La pregunta de investigación intenta abordar simultáneamente: facultades legales, debido proceso, transparencia, legalidad, protección de datos y cierre de brecha fiscal |
| **Desbalance temático** | ~60% del texto se dedica al problema económico/fiscal, pero el programa es de **Legislación Tributaria** (el análisis jurídico debería dominar) |
| **Bibliografía limitada** | Solo 4 referencias, todas institucionales. No hay artículos académicos indexados (peer-reviewed) |
| **Ausencia de derecho comparado** | No se mencionan experiencias internacionales concretas (UE, Brasil, Chile, México) |
| **Metodología no explícita** | No se define el tipo de investigación ni el enfoque metodológico |

---

## 2. Análisis de los Comentarios del Director

> [!IMPORTANT]
> El director señaló que el tema es **"ambicioso para la extensión y alcance de un artículo de este nivel"** y recomienda **dejarlo planteado de manera más acotada**, presentándolo como una **"aproximación inicial"** que identifique tensiones jurídicas principales.

### Interpretación operativa

El director está pidiendo tres cosas concretas:

1. **Reducir el alcance** — Elegir **una sola tensión jurídica** como eje del artículo
2. **Ajustar la promesa** — No pretender resolver todo, sino *mapear* el problema jurídico
3. **Mantener la solidez** — Lo que se pierda en amplitud, ganarlo en profundidad argumentativa

---

## 3. Opciones de Delimitación del Problema Jurídico

A continuación se presentan tres opciones de enfoque. Se recomienda elegir **solo una** como eje central del artículo.

### Opción A — Debido Proceso y Transparencia Algorítmica ⭐ *Recomendada*

> **Pregunta de investigación propuesta:**
> ¿Cuáles son las principales tensiones jurídicas entre la implementación de modelos de *Machine Learning* para la fiscalización predictiva por parte de la DIAN y la garantía del derecho al debido proceso del contribuyente, particularmente en lo relativo a la transparencia y explicabilidad algorítmica?

**Por qué es la mejor opción:**
- Es el tema con mayor desarrollo académico internacional (EU AI Act, jurisprudencia comparada)
- Toca un nervio constitucional sensible: ¿puede la DIAN fundamentar un acto administrativo (requerimiento especial, liquidación oficial) en la salida de un algoritmo que el contribuyente no puede comprender ni controvertir?
- Permite incorporar derecho comparado con la UE (AI Act, GDPR) y casos latinoamericanos
- Es la tensión más visible y debatida, lo que facilita encontrar bibliografía

**Título sugerido:**
> *"Machine Learning en la Fiscalización Tributaria Colombiana: Tensiones Frente al Debido Proceso y la Transparencia Algorítmica"*

---

### Opción B — Protección de Datos Personales y Habeas Data

> **Pregunta de investigación propuesta:**
> ¿Qué límites impone el derecho fundamental al Habeas Data (Ley 1581 de 2012) y el régimen de protección de datos personales frente al uso de información exógena para el entrenamiento y despliegue de algoritmos de fiscalización predictiva por parte de la DIAN?

**Fortalezas:** Muy concreto jurídicamente; conecta con la Ley 1581/2012 y la Ley 1266/2008. La DIAN ya recoge cantidades masivas de información exógena (Resolución 1255/2022), lo que hace urgente este análisis.

**Título sugerido:**
> *"Fiscalización Predictiva y Habeas Data: Límites al Perfilamiento Algorítmico del Contribuyente en Colombia"*

---

### Opción C — Principio de Legalidad y Automatización de Actos Administrativos

> **Pregunta de investigación propuesta:**
> ¿Cuenta la DIAN con un marco jurídico suficiente para emitir actos administrativos de fiscalización (requerimientos especiales, liquidaciones oficiales) fundamentados total o parcialmente en modelos automatizados de *Machine Learning*, sin vulnerar el principio de legalidad tributaria?

**Fortalezas:** Muy técnico-jurídico; analiza si el Estatuto Tributario y el CPACA permiten la automatización decisional. Permite un análisis dogmático riguroso.

**Título sugerido:**
> *"Legalidad Tributaria y Automatización: ¿Puede la DIAN Fundamentar Actos de Fiscalización en Algoritmos de Machine Learning?"*

---

## 4. Propuesta de Nueva Estructura del Artículo

Basada en la **Opción A** (adaptable a B o C):

```
TÍTULO PROPUESTO:
"Machine Learning en la Fiscalización Tributaria Colombiana:
Tensiones Frente al Debido Proceso y la Transparencia Algorítmica"

ESTRUCTURA:

I.   INTRODUCCIÓN (1-2 páginas)
     - Contexto: brecha fiscal + modelo reactivo (condensar lo actual)
     - Declaración de alcance: "aproximación inicial"
     - Pregunta de investigación delimitada
     - Metodología: investigación jurídica dogmática con enfoque
       analítico-descriptivo y elementos de derecho comparado

II.  MARCO CONCEPTUAL (3-4 páginas)
     a. Machine Learning: conceptos esenciales para juristas
        (supervisado, no supervisado, caja negra vs. interpretable)
     b. Fiscalización predictiva: qué es y cómo opera
     c. Estado actual de la DIAN: información exógena, declaración
        sugerida, cruces de información

III. MARCO JURÍDICO APLICABLE (4-5 páginas)
     a. Debido proceso tributario en Colombia
        (Art. 29 C.P., Estatuto Tributario, CPACA)
     b. Marco normativo de la DIAN para uso de tecnología
        (Ley 2277/2022, Resoluciones 1255/2022 y 162/2023)
     c. Protección de datos (Ley 1581/2012) — tratamiento breve
     d. Transparencia algorítmica: ¿existe regulación en Colombia?

IV.  DERECHO COMPARADO (3-4 páginas)
     a. Unión Europea: AI Act (2024) y su clasificación de "alto
        riesgo" para decisiones automatizadas de la administración pública
     b. América Latina: experiencias de Brasil (RFB), Chile (SII),
        México (SAT)
     c. OCDE: Tax Administration 3.0 y principios de gobernanza AI

V.   TENSIONES JURÍDICAS IDENTIFICADAS (3-4 páginas)
     a. Opacidad algorítmica vs. motivación del acto administrativo
     b. Perfilamiento de riesgo vs. presunción de buena fe del contribuyente
     c. Sesgo algorítmico vs. equidad horizontal tributaria
     d. Derecho de contradicción vs. decisiones automatizadas

VI.  CONCLUSIONES Y RECOMENDACIONES (1-2 páginas)
     - Síntesis de tensiones
     - Condiciones mínimas jurídicas para una implementación legítima
     - Líneas de investigación futura

BIBLIOGRAFÍA
```

> [!TIP]
> **Extensión estimada:** 20-25 páginas (apropiada para un artículo de especialización). La estructura actual de la Entrega 1 quedaría condensada en la Sección I y parte de la II.

---

## 5. Guía de Bases de Datos Académicas

### 5.1 Bases de datos indexadas principales

| Base de datos | Tipo | Acceso | Ideal para |
|---|---|---|---|
| **Scopus** | Multidisciplinar, indexada (Elsevier) | Institucional (UPB) | Artículos peer-reviewed en derecho, tecnología y administración pública. Es la base más grande de literatura revisada por pares |
| **JSTOR** | Multidisciplinar, archivo académico | Institucional / Parcial gratuito | Artículos clásicos y fundacionales en derecho tributario, teoría fiscal y ciencias sociales |
| **Web of Science (WoS)** | Multidisciplinar, alto impacto (Clarivate) | Institucional (UPB) | Mapeo de citaciones, artículos de alto factor de impacto, investigación interdisciplinar |
| **HeinOnline** | Jurídico especializado | Institucional | Revistas jurídicas de todo el mundo, tratados, legislación histórica. *Gold standard* para investigación legal |
| **SSRN** | Pre-prints académicos | **Gratuito** | Working papers recientes sobre IA y derecho. Muchos artículos aparecen aquí *antes* de ser publicados en revistas |

### 5.2 Bases de datos complementarias recomendadas

| Base de datos | Tipo | Acceso | Ideal para |
|---|---|---|---|
| **Google Scholar** | Buscador académico | **Gratuito** | Punto de partida para descubrir artículos; bueno para rastrear citaciones |
| **Redalyc** | Revistas iberoamericanas (acceso abierto) | **Gratuito** | Artículos en español sobre derecho tributario latinoamericano |
| **SciELO** | Revistas latinoamericanas (acceso abierto) | **Gratuito** | Investigación regional de alta calidad en derecho y ciencias sociales |
| **Dialnet** | Revistas hispanoamericanas | **Gratuito** | Tesis doctorales, artículos y reseñas en español |
| **IBFD** (International Bureau of Fiscal Documentation) | Derecho tributario internacional | Institucional | La base de datos más completa del mundo en derecho tributario internacional y comparado |
| **DOAJ** (Directory of Open Access Journals) | Revistas de acceso abierto verificadas | **Gratuito** | Artículos peer-reviewed de acceso libre |

### 5.3 Repositorios institucionales clave

| Repositorio | Contenido relevante |
|---|---|
| **CIAT** (Centro Interamericano de Administraciones Tributarias) — [ciat.org](https://www.ciat.org) | Publicaciones técnicas sobre transformación digital tributaria en América Latina, IA, factura electrónica y gestión de riesgo |
| **CEPAL** — [cepal.org](https://www.cepal.org) | *"La inteligencia artificial en las administraciones tributarias: recomendaciones para implementarla"* (2026, LC/MEX/TS.2026/1) — **referencia imprescindible** |
| **OCDE** — [oecd.org](https://www.oecd.org) | *Tax Administration 3.0* (2020), *Governing with AI* (2025), Forum on Tax Administration reports |
| **BID** (Banco Interamericano de Desarrollo) — [publications.iadb.org](https://publications.iadb.org) | Estudios sobre modernización fiscal y tecnología en América Latina |
| **Repositorio UPB** | Trabajos de grado y tesis de la propia universidad |

### 5.4 Estrategia de búsqueda recomendada

> [!TIP]
> **Términos de búsqueda sugeridos** (combinar en español e inglés):
>
> Para una versión ampliada y directamente utilizable en bases de datos, ver el documento: **`Ecuaciones_Busqueda_Ruta_A.md`**.

**En inglés (Scopus, WoS, SSRN, HeinOnline):**
```
"machine learning" AND "tax administration"
"predictive analytics" AND "tax compliance"
"algorithmic transparency" AND "due process" AND tax
"AI Act" AND "tax" AND "public administration"
"automated decision-making" AND "tax law"
"explainability" AND "tax enforcement"
```

**En español (Redalyc, SciELO, Dialnet, Google Scholar):**
```
"inteligencia artificial" AND "fiscalización tributaria"
"machine learning" AND "administración tributaria"
"transparencia algorítmica" AND "debido proceso"
"automatización" AND "actos administrativos" AND tributario
"protección de datos" AND "DIAN"
"analítica de datos" AND "evasión fiscal" AND Colombia
```

---

## 6. Bibliografía Sugerida (Categorizada)

### 6.1 Fuentes institucionales internacionales (ya tienes algunas — ampliar)

| Ref. | Fuente |
|---|---|
| ✅ Ya citada | OCDE (2020). *Tax Administration 3.0: The Digital Transformation of Tax Administration* |
| ✅ Ya citada | OCDE (2025). *Governing with Artificial Intelligence* |
| **Agregar** | OCDE (2023). *Tax Administration 2023: Comparative Information on OECD and Other Advanced and Emerging Economies* |
| **Agregar** | CEPAL (2026). *La inteligencia artificial en las administraciones tributarias: recomendaciones para implementarla.* LC/MEX/TS.2026/1 |
| **Agregar** | CIAT (2024-2025). Publicaciones sobre transformación digital y gestión del riesgo tributario |
| **Agregar** | Unión Europea (2024). *Reglamento de Inteligencia Artificial (AI Act)*. Reglamento (UE) 2024/1689 |
| **Agregar** | BID (2023-2025). Informes sobre modernización de la administración tributaria en América Latina |

### 6.2 Artículos académicos a buscar (por tema)

#### ML y Administración Tributaria
- Hemberg, E. et al. (2016). *Detecting tax evasion: A co-evolutionary approach.* Artificial Intelligence and Law.
- Rahimikia, E. & Pargoo, A.S. (2020). *Machine learning approaches in tax evasion detection.* Expert Systems with Applications.
- Vellutini, C. et al. (2022). *Using machine learning for tax compliance risk assessment.* IMF Working Paper.

#### Transparencia algorítmica y debido proceso
- Pasquale, F. (2015). *The Black Box Society.* Harvard University Press.
- Citron, D.K. & Pasquale, F. (2014). *The scored society: Due process for automated predictions.* Washington Law Review.
- Coglianese, C. & Lehr, D. (2017). *Regulating by robot: Administrative decision making in the machine-learning era.* Georgetown Law Journal.
- Zerilli, J. et al. (2019). *Transparency in algorithmic and human decision-making.* Philosophy & Technology.

#### Derecho tributario y tecnología en Colombia / América Latina
- Buscar en Redalyc/SciELO: artículos sobre facturación electrónica DIAN, información exógena, y modernización tecnológica tributaria
- Buscar en repositorios colombianos: tesis sobre IA y administración pública en Colombia

### 6.3 Normatividad colombiana relevante

| Norma | Contenido relevante |
|---|---|
| Constitución Política, Art. 15 | Derecho a la intimidad y Habeas Data |
| Constitución Política, Art. 29 | Debido proceso |
| Estatuto Tributario (arts. 684 y ss.) | Facultades de fiscalización de la DIAN |
| Ley 1581 de 2012 | Protección de datos personales |
| Ley 1266 de 2008 | Habeas Data financiero |
| Ley 2277 de 2022 | Reforma tributaria (ampliación información exógena) |
| Ley 2213 de 2022 | Virtualización de trámites judiciales y administrativos |
| CPACA (Ley 1437 de 2011) | Procedimiento administrativo, motivación de actos |
| Resolución DIAN 1255/2022 | Ampliación de información exógena |
| Resolución DIAN 162/2023 | Información exógena complementaria |
| CONPES 3975 de 2019 | Política Nacional de IA en Colombia |
| CONPES 3920 de 2018 | Política de explotación de datos (Big Data) |

---

## 7. Recomendaciones de Alto Nivel

### 7.1 Sobre la postura argumentativa

> [!IMPORTANT]
> **No escribas a favor ni en contra del ML en la DIAN.** El artículo debe ser descriptivo-analítico: identificar las tensiones jurídicas existentes y proponer condiciones mínimas para una implementación legítima. Un artículo que simplemente diga "el ML es bueno" o "el ML viola derechos" será débil académicamente.

La postura más sólida es: **"El ML es una herramienta con potencial transformador, pero su implementación en la administración tributaria colombiana presenta vacíos normativos y tensiones constitucionales que deben ser resueltas antes de su despliegue sistemático."**

### 7.2 Sobre la metodología

- **Tipo de investigación:** Jurídica dogmática, con enfoque analítico-descriptivo
- **Método:** Análisis documental + hermenéutica jurídica + derecho comparado
- **Declara explícitamente** qué NO vas a hacer: no es un artículo técnico sobre ML, no desarrolla un modelo algorítmico, no hace un análisis cuantitativo de la brecha fiscal

### 7.3 Sobre el derecho comparado (diferenciador clave)

Incluir al menos **tres jurisdicciones** para fortalecer el argumento:

| Jurisdicción | Qué aporta |
|---|---|
| **Unión Europea** | El AI Act (2024) clasifica como "alto riesgo" los sistemas de IA en administración pública. Exige transparencia, explicabilidad y supervisión humana. Es el referente regulatorio más avanzado del mundo |
| **Brasil** | La Receita Federal (RFB) ya usa ML para fiscalización. La Ley General de Protección de Datos (LGPD) y el Marco Legal de IA (2024) ofrecen un paralelo latinoamericano directo |
| **Chile** | El SII (Servicio de Impuestos Internos) es pionero en analítica de datos en América Latina. Tiene una estrategia de IA documentada |
| **México** | El SAT usa herramientas de ML. Marco regulatorio diferente pero con tensiones similares |

### 7.4 Sobre la originalidad

Para que el artículo aporte valor real, asegúrate de que responda al menos **una** de estas preguntas que nadie más ha contestado:

1. ¿Qué pasa hoy en Colombia cuando un contribuyente recibe un requerimiento de la DIAN basado (total o parcialmente) en un cruce algorítmico? ¿Cómo puede controvertirlo?
2. ¿El CONPES 3975 de 2019 (Política Nacional de IA) se aplica a la DIAN? ¿Es suficiente?
3. ¿Existen vacíos en el Estatuto Tributario (art. 684 y ss.) para fundamentar actos de fiscalización basados en modelos predictivos?

### 7.5 Sobre la redacción y estilo

- **Eliminar el arquetipo sistémico** de la Sección I o reducirlo a un párrafo. Es interesante pero ocupa demasiado espacio para un artículo jurídico
- **Agregar un párrafo de alcance y limitaciones** después de la pregunta de investigación
- **Definir conceptos técnicos** (ML, supervisado, caja negra) en un marco conceptual breve, pensado para lectores juristas
- **Cuidar las notas al pie**: pasar de 4 a mínimo 25-30 referencias para un artículo de este nivel

### 7.6 Sobre la estrategia de publicación (pensando a futuro)

> [!TIP]
> Si después de la especialización deseas publicar el artículo, considera estas revistas colombianas indexadas:

| Revista | Institución | Indexación |
|---|---|---|
| *Revista de Derecho Fiscal* | U. Externado | Scopus / SciELO |
| *Revista Instituto Colombiano de Derecho Tributario* | ICDT | Nacional |
| *Estudios Socio-Jurídicos* | U. del Rosario | Scopus |
| *Vniversitas* | PUJ | Scopus |
| *Revista de Derecho* | U. del Norte | Scopus / SciELO |

---

## 8. Checklist — Próximos Pasos

- [ ] Elegir una de las tres opciones de delimitación (A, B o C) y discutirla con el director
- [ ] Reformular la pregunta de investigación en máximo 3 líneas
- [ ] Ajustar el título del artículo
- [ ] Reducir la Sección I (formulación del problema) a máximo 1.5 páginas
- [ ] Definir explícitamente la metodología
- [ ] Buscar al menos 10-15 artículos académicos indexados en Scopus, WoS y SSRN
- [ ] Incorporar el informe CEPAL 2026 como referencia central
- [ ] Agregar sección de derecho comparado (UE, Brasil, Chile)
- [ ] Revisar y ampliar la normatividad colombiana citada (CONPES, Leyes de datos)
- [ ] Incluir un párrafo de alcance y limitaciones del artículo

---

> **Nota:** Este documento fue generado como apoyo analítico. Las decisiones finales sobre enfoque, estructura y contenido son responsabilidad de la autora y deben ser validadas con el director del trabajo de grado.
