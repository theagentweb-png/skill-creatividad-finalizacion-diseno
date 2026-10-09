# QA y puerta de ejecucion

## Antes del lanzamiento

- Confirmar cliente, cuenta, mercado, moneda, zona horaria y objetivo.
- Confirmar presupuesto diario/total, fechas, limites y metodo de puja.
- Probar URL, carga movil, formulario/checkout, mensaje y oferta.
- Probar conversion primaria, valor, moneda, deduplicacion y diagnosticos.
- Confirmar UTMs, autoetiquetado, nomenclatura y fuente de verdad.
- Revisar geografia, idioma, exclusiones, audiencias y first-party data.
- Revisar formatos, recortes, textos, audio, subtitulos, identidad y CTA.
- Revisar politicas, categoria especial/regulada, consentimiento y derechos.
- Confirmar que no se optimiza hacia una microconversion de bajo valor por error.
- Guardar configuracion previa y definir rollback.

## Manifiesto de cambio

Registrar:

- Cliente, plataforma, account/campaign ID parcial y objeto exacto.
- Estado y valor anterior.
- Cambio propuesto y valor nuevo.
- Evidencia y objetivo.
- Impacto y riesgo esperados.
- Hora y responsable.
- Ventana sin nuevas ediciones.
- KPI y guardrails de monitorizacion.
- Condicion y pasos de rollback.

## Puerta de mutacion

Ejecutar solo si:

1. El usuario pidio ejecucion, no solo analisis.
2. La cuenta exacta y el alcance estan confirmados.
3. El tracking y la economia necesarios son suficientemente confiables.
4. El cambio esta respaldado por datos y reglas oficiales vigentes.
5. El manifiesto permite revertir y verificar.
6. Existe aprobacion explicita para ese cambio o un alcance previamente aprobado que lo cubre claramente.

Si falta una condicion, entregar borrador y pedir la decision necesaria. No borrar; pausar o archivar. No pegar secretos en archivos, prompts o reportes.

## Despues del cambio

- Verificar que la plataforma acepto exactamente la mutacion prevista.
- Revisar entrega, tracking, presupuesto, rechazos y URL.
- Registrar el cambio en el historial de la cuenta.
- Evitar cambios adicionales durante la ventana acordada salvo guardrail roto.
- Comparar contra baseline equivalente y considerar conversion lag.
- Cerrar con mantener, ampliar, revertir o iterar, indicando evidencia.
