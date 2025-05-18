# Lista de ventas
ventas = [
    {"fecha": "2024-01-01", "producto": "Laptop", "cantidad": 2, "precio": 1200.50},
    {"fecha": "2024-01-01", "producto": "Mouse", "cantidad": 5, "precio": 25.00},
    {"fecha": "2024-01-02", "producto": "Laptop", "cantidad": 1, "precio": 1150.00},
    {"fecha": "2024-01-02", "producto": "Monitor", "cantidad": 3, "precio": 300.00},
    {"fecha": "2024-01-03", "producto": "Mouse", "cantidad": 7, "precio": 20.00},
    {"fecha": "2024-01-03", "producto": "Monitor", "cantidad": 2, "precio": 310.00}
]

# 1. Cálculo de ingresos totales
ingresos_totales = 0
for venta in ventas:
    ingresos_totales += venta["cantidad"] * venta["precio"]

# 2. Análisis del producto más vendido
ventas_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    if producto in ventas_por_producto:
        ventas_por_producto[producto] += cantidad
    else:
        ventas_por_producto[producto] = cantidad

producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)
cantidad_mas_vendida = ventas_por_producto[producto_mas_vendido]

# 3. Promedio de precio por producto
precios_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    total_precio = venta["precio"] * venta["cantidad"]
    cantidad = venta["cantidad"]
    if producto in precios_por_producto:
        precios_por_producto[producto] = (
            precios_por_producto[producto][0] + total_precio,
            precios_por_producto[producto][1] + cantidad
        )
    else:
        precios_por_producto[producto] = (total_precio, cantidad)

precios_promedio = {}
for producto, (suma_precios, cantidad_total) in precios_por_producto.items():
    precios_promedio[producto] = round(suma_precios / cantidad_total, 2)

# 4. Ingresos por día
ingresos_por_dia = {}
for venta in ventas:
    fecha = venta["fecha"]
    ingreso = venta["cantidad"] * venta["precio"]
    if fecha in ingresos_por_dia:
        ingresos_por_dia[fecha] += ingreso
    else:
        ingresos_por_dia[fecha] = ingreso

# 5. Resumen de ventas
resumen_ventas = {}
for producto in ventas_por_producto:
    cantidad_total = ventas_por_producto[producto]
    ingresos_totales_producto = precios_por_producto[producto][0]
    precio_promedio = precios_promedio[producto]
    resumen_ventas[producto] = {
        "cantidad_total": cantidad_total,
        "ingresos_totales": round(ingresos_totales_producto, 2),
        "precio_promedio": precio_promedio
    }

# --- Presentación de resultados ---
print("==== LISTA DE VENTAS ====")
for venta in ventas:
    print(venta)

print("\n==== INGRESOS TOTALES ====")
print(f"${ingresos_totales:.2f}")

print("\n==== PRODUCTO MÁS VENDIDO ====")
print(f"{producto_mas_vendido} con {cantidad_mas_vendida} unidades")

print("\n==== PRECIO PROMEDIO POR PRODUCTO ====")
for producto, promedio in precios_promedio.items():
    print(f"{producto}: ${promedio}")

print("\n==== INGRESOS POR DÍA ====")
for fecha, ingreso in ingresos_por_dia.items():
    print(f"{fecha}: ${round(ingreso, 2)}")

print("\n==== RESUMEN DE VENTAS ====")
for producto, resumen in resumen_ventas.items():
    print(f"{producto}:")
    for clave, valor in resumen.items():
        print(f"  {clave}: {valor}")
