---
name: web-inventario-conciliacion
description: Conciliar inventarios y catálogos con fuentes vigentes, identidades verificadas, ubicaciones y protección frente a cambios concurrentes.
---

# Inventario y catálogo multicliente
Identifica cliente, plataforma, catálogo, fuente de verdad, fecha, ubicación y alcance de actualización. Usa las instrucciones particulares del cliente para bodegas, cálculo objetivo, excepciones, SKU y estado de producto. No heredes reglas de Bikexperts o de otra marca a todos los clientes. Distingue conciliación, propuesta, importación iniciada y resultado verificado.

Antes de modificar, conserva exportación actual con variantes, opciones, identificadores y ubicación; actualízala inmediatamente antes de importar cuando exista protección por valor anterior. Separa disponible, comprometido, no disponible y existencias físicas según la plataforma; no los sustituyas entre sí. No uses la suma visible del catálogo como inventario de una ubicación específica.

Cruza por identidad exacta. Normaliza prefijos o códigos únicamente cuando las reglas del cliente lo indiquen. Títulos, tallas, colores y opciones sirven para corroborar; una coincidencia aproximada no autoriza cambios. Detecta colisiones: varios registros apuntando a una variante con cantidades contradictorias se excluyen y reportan; no elijas ni sumes arbitrariamente. Distingue faltante confirmado, posible faltante y no conciliado.

Calcula cantidades con la fuente y fórmula autorizadas; preserva reservas o compromisos que corresponda. En CSV parte de la exportación nativa y conserva estructura, handles, opciones, ubicación y estados requeridos; no construyas imports solo con SKU y cantidad. La importación de inventario no equivale a actualizar SKU. Para APIs verifica versión, permisos y control de concurrencia; una operación de fijar cantidades requiere una fuente de verdad y comparación adecuada, no desactivar controles para forzar el cambio.

Gestiona estados de producto por separado de cantidades. Producto y variante no tienen necesariamente el mismo alcance de estado. No ocultes un producto con una variante vigente, excepción protegida o identidad ambigua. No elimines ni reactives productos ni cambies precio, descripción, medios o políticas fuera del encargo. Un faltante en una hoja no significa automáticamente discontinuado; decide según regla y evidencia del cliente.

Prepara lista de cambios con valores anteriores y objetivo, excluidos y motivos. Si se autoriza importar o editar, verifica resumen de la plataforma y luego lectura posterior: cada objetivo, ausencia de cambios fuera del lote y preservación de otras ubicaciones y campos. Un mensaje de recepción no prueba todas las cantidades. Si el valor anterior ya cambió, reexporta y concilia; no sobrescribas cambios concurrentes.

Entrega cantidades modificadas, casos sin cambio, productos posibles por montar, estados modificados, identidades pendientes y errores. Marca fecha y fuente. Las excepciones sin resolver permanecen intactas. No declares toda la tienda conciliada por haber completado un lote. Sin conexión real, produce el informe o instrucciones; no afirmes que se aplicó inventario.
