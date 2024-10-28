Estimación de Ganancias para una Nueva Sucursal de supermercado en Juriquilla

En este análisis, asumimos el rol de analistas trabajando para una empresa multinacional como Walmart, que busca expandirse abriendo una nueva sucursal en una comunidad semejante a Juriquilla, la cual cuenta con aproximadamente 40,000 habitantes. Nuestro objetivo es estimar el porcentaje de personas que necesitaríamos convencer para que realicen compras en la nueva sucursal, de manera que podamos generar una ganancia neta mensual de al menos $1,500,000.

El análisis se basa en un archivo .csv proporcionado que contiene información sobre las ganancias por transacción en comunidades similares en términos de nivel socioeconómico. En este contexto, la ganancia por transacción ya incluye la fórmula:

𝐺𝑎𝑛𝑎𝑛𝑐𝑖𝑎 = 𝑇𝑟𝑎𝑛𝑠𝑎𝑐𝑐𝑖ó𝑛 − 𝑃𝑎𝑔𝑜 𝑑𝑒 𝐼𝑚𝑝𝑢𝑒𝑠𝑡𝑜𝑠 − 𝐶𝑜𝑠𝑡𝑜𝑠 𝑑𝑒 𝐶𝑜𝑚𝑝𝑟𝑎 𝑑𝑒 𝑃𝑟𝑜𝑑𝑢𝑐𝑡𝑜𝑠

Para alcanzar el objetivo propuesto, utilizaremos la estimación de parámetros como la base de nuestro análisis. En particular, aplicaremos el método de Maximum Likelihood Estimation (Estimación por Máxima Verosimilitud), que es ampliamente utilizado para encontrar los parámetros que mejor se ajustan a los datos observados.

Además, emplearemos la distribución beta como la función de densidad de probabilidad para modelar los datos. Esta distribución es altamente flexible y nos permite ajustar su forma al comportamiento de los datos variando sus parámetros α y β. Esta flexibilidad nos permitirá adaptar el modelo a diferentes posibles escenarios de distribución de las ganancias, mejorando así la precisión de nuestras estimaciones.


Análisis incial basado en datos promedio en juriquilla:

Ventas mínima necesarias para $1,500,000 en ganancias: 35740
Porcentje de la población que sean consumidores necesario: 22%

Ratings:

Media: 6.97
Desviación: 1.72

Distribución del modelo

Se sigue una distribución uniforme y continua, ya que como se puede ver en el histograma, todos los rangos de valores parecen tener la misma probabilidad de ocurrir, 

2)¿Cuál es la probabilidad de que en la sucursal que abramos, si los datos que usamos fue en una comunidad semejante a la de Juriquilla, de que en promedio tengan un rating de 8.5 o más?

Considerando que el promedio de los ratings es de 6.97 y la desviación es de 1.72, en esta muestra de 1000, al aplicar el teorema del límite central, podemos encontrar nuestra z tomando en cuenta que la media que estamos buscando es de 8.5, por lo que la probabilidad de que los ratings en promedio sean de 8.5, es prácticamente nula. 

Lo que se le podría recomendar al area de atención al cliente en este caso es mejorar el sistema con el que se evalúan los ratings, ya que no te da la suficiente información saber la calificación que le da un consumidor a un día en el supermercado para mejorar algún area, por lo que deberían enfocarse en analizar los días en los ratings más altos, para ver que patrones siguen, así mismo se debe de encontrar la forma de establecer una relación de los ratings con las ventas en el día, ya que se le da la misma importancia a un promedio de ratings en un día con bajas ventas en comparación a los que más ventas concentran. 


Analisis mejorado

Luz: La tarifas para usuarios de alto consumo como un supermercado son la Tarifa OM, Tarifa GDMTO, o Tarifa DAC que se suelen aplicar para una gran demanda mayor a 100 kW. 

El costo por kilowatt-hora también depende del horario de consumo, es así que el costo puede variar dependiendo si son horarios pico o no. Por ejemplo, la tarifa GDMTO en Querétaro se divide en un cargo fijo que se cobra independientemente del consumo, es un costo fijo mensual de 362.60. igualmente hay un cargo variable que se basa en el consumo mensual de kWh el cual es de 1.642, y un cargo por distribución y capacidad que se cobran con base en la demanda de energía (en kWh) los cuales son de 101.75 y 364.75 respectivamente. Cabe resaltar que estas tarifas son adicionales al cargo variable y se aplican según la demanda máxima que tiene el supermercado.

Para este análisis consideraremos que el consumo de luz se da las 24 horas del día. 

Agua:  En general, se estima que un supermercado consume entre 1,500 y 2,500 litros de agua por día por cada 1,000 m² de superficie de venta. Es así que nuestro supermercado de 2000 m² debería consumir entre 3000 y 5000 litros de agua al día. En querétaro esto representaría un gasto que para empresas el cual es de alredor de $ 100 por metro cubico de agua consumido. 

Empleados: Vamos a considerar más puestos de trabajo cómo lo es la seguridad y quienes hacen el mantenimiento. De los cuales el sueldo promedio aquí en México es de $8,000 a $10,000 pesos al mes y el del personal de mantenimiento es similar, oscilando entre $7,500 y $12,000 pesos al mes. 

Visitas al supermercado: Estabamos asumiendo que una persona va en promedio 1 vez a la semana al supermercado, pero en muchos casos puede que hagan pequeñas compras dependiendo del día de la semana, considerando que hay días dodne ciertos productos son más baratos, o se gasta más los días que son quincena, para modelar el número de visitas semanales al supermercado con una media de 1.5 visitas por semana, que se puede ajustar según los datos disponibles, podemos utilizar una distribución de Poisson. De esta forma consideramos que cada cliente podría visitar el supermercado de manera independiente de otros clientes, y la frecuencia media de visitas puede estar bien representada por un número constante de 1.5 visitas por semana, entonces las ventas totales se ajustan multiplicando las ventas históricas por el número de visitas generadas por la distribución de Poisson.

Nuevos resultados:

Nómina total: 1017569.0999999999
Gasto total de luz mensual: 121418282.6
Gasto de agua mensual: 21146.822
Gasto total considerando luz (CFE) y agua: 122456998.52199998
N1 (Solución 1): 21912.708120768093
N2 (Solución 2): 21909.218233039912
Porcentaje de la población necesario: 0.13695442575480057

