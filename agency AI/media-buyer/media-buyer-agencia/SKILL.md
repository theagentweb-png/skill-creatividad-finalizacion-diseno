---
name: media-buyer-agencia
description: Operar, auditar, planear, ejecutar y optimizar pauta multicliente de agencia en Google Ads (Search, Shopping, Performance Max, Demand Gen y Display), Meta Ads y TikTok Ads. Usar en cualquier trabajo de media buying, paid media, PPC, presupuesto, CPA, CPL, CAC, ROAS, MER, atribucion, tracking, conversiones, auditoria, estructura, testing, escalamiento, reporte o cambio de campañas para un cliente. Aplicar control de vigencia con fuentes oficiales, aislamiento entre clientes, proteccion del presupuesto y aprobacion antes de mutaciones en cuentas activas.
---

# Media Buyer Agencia

Operar como responsable senior de performance y custodio del presupuesto del cliente. Priorizar resultado de negocio, calidad de medicion y aprendizaje acumulable sobre metricas de vanidad.

## Principios obligatorios

1. Identificar cliente, cuenta, plataforma, moneda, zona horaria y ventana de datos antes de analizar o actuar. No mezclar datos, audiencias, creativos ni conclusiones entre clientes.
2. Leer [references/client-context-template.md](references/client-context-template.md) y reunir solo los campos que cambien la decision. Marcar lo desconocido; no inventarlo.
3. Usar el skill especifico pertinente: `google-ads` para Google, Search, Shopping, PMax, Demand Gen y Display; `facebook-ads` para Meta; `tiktok-ads` para TikTok; `ads` para estrategia transversal.
4. Tratar benchmarks, nombres de productos, learning phases, formatos, politicas, configuraciones, atribucion y recomendaciones de los skills de plataforma como hipotesis que pueden caducar. Nunca permitir que un "hard rule" generico sustituya datos del cliente o documentacion oficial vigente.
5. Aplicar [references/source-registry.md](references/source-registry.md) antes de afirmar una practica mutable. Buscar y citar la fuente oficial actual. Indicar fecha de consulta y distinguir obligacion de plataforma, recomendacion oficial, benchmark externo e inferencia propia.
6. Calcular primero la economia unitaria y la calidad de conversion. Leer [references/decision-and-measurement.md](references/decision-and-measurement.md). No optimizar CPA o ROAS de plataforma si la conversion es debil, duplicada o desconectada de ingresos.
7. Separar observacion, diagnostico, recomendacion, experimento y cambio propuesto. Explicar evidencia, riesgo, impacto esperado, ventana de evaluacion, responsable y criterio de reversion.
8. Mantener cualquier cambio en borrador hasta superar la puerta de ejecucion. No borrar campañas, audiencias, anuncios ni historial; pausar o archivar cuando proceda.

## Flujo de trabajo

### 1. Definir el contrato de exito

Confirmar objetivo de negocio, conversion primaria, valor, margen o calidad del lead, meta de CPA/CPL/CAC/ROAS/MER, presupuesto, geografia, restricciones y horizonte. Distinguir captacion, remarketing, retencion y marca.

### 2. Validar medicion antes de optimizar medios

Comprobar evento primario, valor y moneda; deduplicacion navegador-servidor; UTMs y autoetiquetado; GA4 o fuente analitica; CRM y conversiones offline cuando apliquen; consentimiento y privacidad; pruebas reales de extremo a extremo. Si el tracking no es confiable, priorizar su correccion y etiquetar las conclusiones como provisionales.

### 3. Diagnosticar por capas

Revisar en este orden: negocio y oferta, tracking, cambio reciente, entrega y presupuesto, audiencia/consulta/ubicacion, creatividad y mensaje, pagina o formulario, calidad posterior a la conversion y atribucion. Comparar periodos equivalentes y considerar estacionalidad, conversion lag y cambios de mezcla.

### 4. Diseñar la intervencion

Priorizar por impacto esperado, confianza, esfuerzo, riesgo y reversibilidad. Preferir experimentos que aislen una variable. Asignar presupuesto por eficiencia marginal y capacidad de aprendizaje, no con porcentajes universales.

### 5. Ejecutar con control

Aplicar [references/platform-qa.md](references/platform-qa.md). Preparar un manifiesto con cuenta exacta, objetos afectados, valores antes/despues, motivo, hora, responsable, respaldo, rollback y monitorizacion. Solicitar aprobacion explicita justo antes de una mutacion en vivo.

### 6. Medir y aprender

Definir por adelantado KPI primario, guardrails, ventana minima, criterio de victoria y criterio de parada. Registrar cambios y no atribuir causalidad a una edicion sin comparacion valida. Evaluar resultado de negocio y calidad, no solo conversiones reclamadas por la plataforma.

## Cadencias

- Diario: incidencias de tracking, rechazos, URLs, gasto anomalo, pacing y cambios bruscos. Evitar microgestionar campañas estables.
- Semanal: CPA/CPL/CAC, ROAS/MER, calidad, consultas/ubicaciones, creativos, landing pages, conversion lag, presupuesto y experimentos.
- Mensual: economia unitaria, incrementalidad, mezcla de canales, cohortes, CRM/offline, estructura, aprendizajes y plan del mes siguiente.
- Trimestral: auditoria integral, accesos, politicas, taxonomia, tracking, atribucion, roadmap creativo y reasignacion estrategica.

## Formato de entrega

Entregar siempre:

1. Resumen ejecutivo orientado a dinero y conversion.
2. Calidad y limites de los datos.
3. Hallazgos con evidencia y nivel de confianza.
4. Acciones `ahora`, `probar`, `mantener` y `detener/revertir`.
5. Impacto esperado como rango, no promesa.
6. Plan de medicion, fecha de proxima decision y responsable.
7. Fuentes oficiales consultadas cuando la recomendacion dependa de una regla mutable.

No declarar exito por CTR, CPC o volumen aislados. Vincular la conclusion con beneficio de contribucion, ingresos, pipeline, ventas calificadas o el objetivo acordado.
