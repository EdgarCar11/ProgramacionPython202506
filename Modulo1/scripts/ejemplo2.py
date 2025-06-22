1








PRECIO_PAN =3.49
DESCUENTO = 0.6



cantidad_barras =int(input('Ingrese el numero de barras de pan vendidas que no son del dia'))
descuento_aplicado= DESCUENTO*cantidad_barras*PRECIO_PAN
precio_pagado=cantidad_barras*PRECIO_PAN*(1-DESCUENTO)

print(f'Precio barra pan{PRECIO_PAN}')
print(f'Precio aplicado pan{descuento_aplicado}')
print(f'Precio pagado por el cliente{precio_pagado:.2f}')