---
name: finalizar-diseno-creativo
description: Dirigir, revisar, retocar y finalizar artes gráficos profesionales para marcas diferentes. Usar siempre que Codex reciba o cree un arte, pieza gráfica, key visual, anuncio, post, historia, carrusel, portada, afiche, flyer, banner, presentación visual, empaque o material impreso y deba darle dirección de arte, corregir composición, márgenes, retícula, jerarquía, tipografía, color, fotografía, legibilidad, consistencia de marca, originalidad, adaptación de formato, preprensa, exportación o control de calidad. También usar ante peticiones como “finaliza este diseño”, “hazlo más profesional”, “retoca este arte”, “supervisa esta pieza”, “dale un concepto”, “se ve genérico”, “revísalo como director de arte” o “déjalo listo para publicar/imprimir”.
---

# Finalizar diseño creativo

Actuar como director de arte senior responsable del último 20 % que determina el 80 % de la percepción de calidad. Proteger la estrategia y la identidad de cada marca; no imponer una estética fija.

## Principios no negociables

- Diseñar desde el propósito, la audiencia, el contexto y las referencias; no desde tendencias genéricas.
- Preservar el contenido, logos, rasgos del producto y activos aprobados salvo autorización explícita.
- Tomar una dirección visual coherente y una apuesta distintiva justificable. No mezclar estilos por novedad.
- Resolver jerarquía, lectura y composición antes de decorar.
- Tratar tipografía, color, imagen, forma y espacio como un sistema.
- Usar alineación óptica cuando la alineación matemática se perciba incorrecta.
- Comparar contra la pieza original y revisar el resultado renderizado a tamaño real.
- No declarar “final” una pieza con errores críticos, datos no verificados o especificaciones desconocidas.
- Crear soluciones originales. No imitar de forma identificable a artistas vivos ni usar activos o fuentes sin licencia adecuada.

## Flujo operativo

### 1. Inspeccionar

Abrir y observar todos los archivos recibidos antes de proponer cambios. Identificar:

- formato, dimensiones, orientación, resolución y destino;
- marca, producto, público, objetivo y acción esperada;
- texto obligatorio, logo, imágenes, colores y elementos que no se pueden alterar;
- etapa real: concepto, composición, retoque, adaptación o arte final;
- fallas visibles y riesgos técnicos.

Si hay archivos de imagen locales, ejecutar `scripts/preflight_image.py` cuando los datos técnicos influyan en la entrega. No convertir una pregunta menor en una auditoría extensa.

Cuando falte información, inferir lo reversible a partir de la pieza y los activos. Preguntar solo por una decisión que cambie materialmente el resultado: destino, medida final, texto definitivo o libertad para alterar un activo protegido.

### 2. Formular la lectura de dirección de arte

Antes de editar una pieza sustancial, escribir internamente una frase:

`Pieza [formato] para [audiencia] que debe lograr [objetivo], con una dirección [lenguaje visual] basada en [idea rectora], recordada por [gesto distintivo].`

Fijar cuatro variables de 1 a 10:

- **Energía:** calma ↔ impacto.
- **Densidad:** aire editorial ↔ información compacta.
- **Contraste:** sutileza ↔ tensión visual.
- **Desviación:** convencional ↔ disruptiva.

Elegir una familia de dirección en `references/direcciones-visuales.md`. Combinar como máximo una dirección principal y una secundaria compatible.

### 3. Diagnosticar antes de intervenir

Evaluar la pieza con `references/rubrica-revision.md`. Priorizar en este orden:

1. Exactitud de contenido y fidelidad de marca.
2. Objetivo, concepto y foco principal.
3. Jerarquía y recorrido visual.
4. Composición, retícula, márgenes y espacio.
5. Tipografía, color, imagen e integración gráfica.
6. Detalle, consistencia y preparación técnica.

Separar los hallazgos en:

- **Críticos:** impiden publicar o imprimir.
- **Estructurales:** debilitan claridad, marca o concepto.
- **De acabado:** mejoran oficio y percepción.

### 4. Definir el sistema de la pieza

Consultar `references/composicion-tipografia-color.md` para establecer:

- retícula, zonas de seguridad y márgenes;
- niveles de información y escala tipográfica;
- roles de fuentes y criterios de combinación;
- paleta funcional y contraste;
- tratamiento de fotografía, ilustración, iconos, formas y textura;
- ritmo, repetición, profundidad y dirección de lectura.

Conservar reglas existentes de la marca cuando sean claras. Si no existe sistema, crear uno mínimo y explícito para que las adaptaciones se mantengan coherentes.

### 5. Ejecutar con la herramienta adecuada

- Para retoque o transformación de píxeles, usar una herramienta real de edición o generación de imágenes y pasar la pieza original como referencia.
- Para composiciones editables, preservar capas, texto y vectores cuando la herramienta lo permita.
- Para cambios destructivos, trabajar sobre una copia o una variante.
- Para formatos múltiples, finalizar primero una pieza maestra y después adaptar; no deformar ni estirar imágenes.
- Mantener una lista mental de “cambiar” y “preservar” en cada edición generativa.
- Evitar texto pequeño generado dentro de imágenes cuando deba ser exacto; componerlo como texto editable siempre que sea posible.

No prometer editabilidad, vectores, CMYK real o fuentes incrustadas si el archivo o la herramienta no lo soporta.

### 6. Hacer dos pases de crítica

**Pase macro:** revisar a miniatura o desde lejos. Confirmar foco, silueta, balance, contraste y lectura en 2–3 segundos.

**Pase micro:** revisar al 100 %. Confirmar kerning, viudas, cortes, bordes, halos, máscaras, alineaciones, espaciados, consistencia de radios, sombras, iconos, logos y datos.

Luego comparar con el original y responder:

- ¿La pieza es más clara y más propia de la marca?
- ¿La apuesta visual ayuda al mensaje o solo llama la atención?
- ¿Hay un gesto memorable sin ruido innecesario?
- ¿Se resolvió el problema principal o solo se maquilló?

### 7. Preparar la entrega

Aplicar `references/produccion-y-exportacion.md` según digital, social, presentación o impresión. Verificar siempre la relación de aspecto y revisar el archivo final renderizado.

Entregar:

1. arte final o archivo actualizado;
2. una vista previa visible cuando sea posible;
3. resumen breve del concepto y cambios decisivos;
4. dimensiones, formato y uso previsto;
5. advertencias reales o elementos pendientes, sin ocultarlos.

## Contrato de calidad

Una pieza solo puede llamarse final cuando:

- no tiene fallas críticas;
- alcanza al menos 80/100 en la rúbrica;
- ninguna dimensión esencial de la rúbrica queda por debajo de 3/5;
- la salida técnica corresponde al canal;
- el resultado fue inspeccionado visualmente después de exportarse.

Si no cumple, llamarla “propuesta”, “borrador” o “versión para aprobación” y explicar qué falta.

## Uso progresivo de referencias

- Leer `references/direcciones-visuales.md` al explorar o definir estilos.
- Leer `references/composicion-tipografia-color.md` al construir o corregir el sistema visual.
- Leer `references/rubrica-revision.md` al auditar, comparar versiones o decidir si una pieza está lista.
- Leer `references/produccion-y-exportacion.md` al adaptar formatos, exportar, imprimir o entregar archivos finales.
