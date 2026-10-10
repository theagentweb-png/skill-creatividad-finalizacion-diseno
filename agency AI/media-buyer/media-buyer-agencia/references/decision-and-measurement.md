# Decision, economia y medicion

## Calcular el limite economico

Usar los datos reales del cliente y declarar el horizonte.

- Ecommerce, primera compra: `CPA_equilibrio = ingreso neto por pedido - COGS - costos variables - devoluciones esperadas`.
- Ecommerce, margen porcentual: `ROAS_equilibrio = 1 / margen_de_contribucion`, cuando el margen excluye pauta y usa la misma base de ingresos.
- Leads: `CPL_equilibrio = tasa lead-a-venta x contribucion esperada por venta`.
- LTV: usar contribucion, no ingresos brutos; descontar churn, devoluciones, costo de servicio y tiempo. Presentar escenario conservador, base y alto.

Aplicar un margen de seguridad acordado. No convertir el punto de equilibrio en meta operativa sin considerar caja, capacidad e incertidumbre.

## Establecer una fuente de verdad

Conciliar cuatro capas cuando existan:

1. Plataforma publicitaria: entrega y conversiones atribuidas.
2. Analitica: sesiones, eventos y rutas.
3. Sistema transaccional o CRM: ventas, margen, estado y calidad.
4. Finanzas: ingreso neto, devoluciones, costos y caja.

Reportar diferencias; no sumarlas como si fueran conversiones unicas. Para leads, devolver a la plataforma estados de calidad y venta cuando sea viable y permitido.

## Evitar reglas universales de pausa

No pausar automaticamente por "2x" o "3x CPA", frecuencia, CTR, numero de conversiones o dias transcurridos. Evaluar conjuntamente:

- Gasto respecto al CPA/CPL limite y presupuesto total.
- Conversion lag y ventana de atribucion.
- Volumen y varianza historica.
- Calidad del tracking y cambios recientes.
- Rol de la campaña en el funnel e incrementalidad.
- Riesgo de oportunidad y reversibilidad.

Permitir accion inmediata ante URL rota, gasto fuera de alcance, tracking duplicado grave, incumplimiento, mercado equivocado o configuracion claramente contraria al brief. Documentar la excepcion.

## Optimizar presupuesto

Comparar eficiencia marginal: cuanto resultado adicional produce el siguiente peso invertido. No reasignar solo por ROAS promedio. Considerar saturacion, volumen, calidad, contribucion, capacidad, dependencia de marca y solapamiento entre canales.

Clasificar:

- Mantener: cumple meta y necesita estabilidad.
- Escalar con prueba: cumple meta y conserva oportunidad marginal.
- Reparar: tiene demanda pero falla tracking, oferta, creativo o pagina.
- Reducir: eficiencia marginal inferior con evidencia suficiente.
- Pausar/revertir: riesgo material o perdida confirmada, con aprobacion.

## Diseñar pruebas

Definir hipotesis, unidad experimental, variante, KPI primario, guardrails, presupuesto, duracion minima, conversion lag y regla de decision antes de lanzar. Evitar cambiar audiencia, creativo, puja y landing simultaneamente si se busca aprendizaje causal.

Presentar uplift y rango de incertidumbre cuando los datos lo permitan. Si no hay potencia suficiente, calificar el resultado como direccional.

## Pacing

Comparar gasto acumulado real contra presupuesto acumulado esperado y ajustar por estacionalidad, dia de semana y horas activas. Investigar antes de corregir. No perseguir un pacing perfecto si obliga a comprar trafico marginal de mala calidad.
