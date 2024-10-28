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

Se sigue una distribución normal, la cual presenta una gran simetría que podemos ver al comparar el comportamiento de la media con la mediana, ya que son valores muy similares, lo que indica una distribución simétrica de los datos. Por el otro lado el teorema del límite central establece que la suma o promedio de muchas variables aleatorias independientes tiende a seguir una distribución normal, independientemente de la distribución original de las variables. Esto hace que la normal sea una distribución esperada cuando muchos factores influyen en un resultado, como ocurre en casos en el mundo real como las calificaciones subjetivas, que tienden a estar influenciados por múltiples factores independientes. 

2)¿Cuál es la probabilidad de que en la sucursal que abramos, si los datos que usamos fue en una comunidad semejante a la de Juriquilla, de que en promedio tengan un rating de 8.5 o más?

Considerando que el promedio de los ratings es de 6.97 y la desviación es de 1.72, sobre una población como la de juriquilla de 160,000 habitantes, al aplicar el teorema del límite central, convirtiendo nuestro valor objetivo de 8.5 


Analisis mejorado

Luz: La tarifas para usuarios de alto consumo como un supermercado son la Tarifa OM, Tarifa GDMTO, o Tarifa DAC que se suelen aplicar para una gran demanda mayor a 100 kW. 

El costo por kilowatt-hora también depende del horario de consumo, es así que el costo puede variar dependiendo si son horarios pico o no. Por ejemplo, la tarifa GDMTO en Querétaro se divide en un cargo fijo que se cobra independientemente del consumo, es un costo fijo mensual de 362.60. igualmente hay un cargo variable que se basa en el consumo mensual de kWh el cual es de 1.642, y un cargo por distribución y capacidad que se cobran con base en la demanda de energía (en kWh) los cuales son de 101.75 y 364.75 respectivamente. Cabe resaltar que estas tarifas son adicionales al cargo variable y se aplican según la demanda máxima que tiene el supermercado.

Para este análisis consideraremos que el consumo de luz se da las 24 horas del día. 

Agua:  En general, se estima que un supermercado consume entre 1,500 y 2,500 litros de agua por día por cada 1,000 m² de superficie de venta. Es así que nuestro supermercado de 2000 m² debería consumir entre 3000 y 5000 litros de agua al día. En querétaro esto representaría un gasto que para empresas el cual es de alredor de $ 100 por metro cubico de agua consumido. 

Empleados: Vamos a considerar más puestos de trabajo cómo lo es la seguridad y quienes hacen el mantenimiento. De los cuales el sueldo promedio aquí en México es de $8,000 a $10,000 pesos al mes y el del personal de mantenimiento es similar, oscilando entre $7,500 y $12,000 pesos al mes. 

Visitas al supermercado: Estabamos asumiendo que una persona va en promedio 1 vez a la semana al supermercado, pero en muchos casos puede que hagan pequeñas compras dependiendo del día de la semana, considerando que hay días dodne ciertos productos son más baratos, o que si pensamos en que la mayor concentración de compras son en quincena.

semana... ¿esto es cierto? ¿Qué otra cosa podrías hacer/asumir?

