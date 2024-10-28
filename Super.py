import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta, norm

df = pd.read_csv('/Users/apolo13/Downloads/SuperMarketData.csv')

sales = np.array(df['Sales']) * 19.88
max_sales = max(sales)
min_sales = min(sales)
sales_norm = 1 / (max_sales - min_sales) * (sales - min_sales)

a, b, _, _ = beta.fit(sales)
mu_norm = a / (a + b)
var_norm = (a * b) / ((a + b) ** 2 * (a + b + 1))
desv_norm = np.sqrt(var_norm)

mu = (max_sales - min_sales) * mu_norm + min_sales
var = (max_sales - min_sales) * var_norm
sigma = np.sqrt(var)

fact = 1.15

sal_cajeros = 258.25
num_cajeros = 30
dias_t = 20

sal_conserjes = 5000
num_conserjes = 20

gerente = 100000

sub_gerente = 4500
num_subgerentes = 4

sal_almacenista = 262.13
almacenista = 40

g_pasillo = 264.65
num_pasillos = 60

sal_seguridad = 8000
num_seguridad = 5

sal_mantenimiento = 5500
num_mantenimiento = 5

total_cajeros = sal_cajeros * num_cajeros * dias_t * fact
total_conserjes = sal_conserjes * num_conserjes * fact
total_gerente = gerente
total_subgerentes = sub_gerente * num_subgerentes
total_almacenistas = sal_almacenista * almacenista * dias_t * fact
total_pasillos = g_pasillo * num_pasillos * dias_t * fact
total_seguridad = sal_seguridad * num_seguridad * fact
total_soporte = sal_mantenimiento * num_mantenimiento * fact

nomina_total = (total_cajeros + total_conserjes + total_gerente + total_subgerentes +
                total_almacenistas + total_pasillos)

print("Nómina total:", nomina_total)

cargo_fijo = 362.60
costo_kWh = 1.642
costo_distribucion_kW = 101.75
costo_capacidad_kW = 364.75

consumo_kWh_mensual = 120*2000*24
demanda_kW = 120*2000

gasto_fijo = cargo_fijo
gasto_variable_energia = consumo_kWh_mensual * costo_kWh
gasto_distribucion = demanda_kW * costo_distribucion_kW
gasto_capacidad = demanda_kW * costo_capacidad_kW

gasto_luz_total = gasto_fijo + gasto_variable_energia + gasto_distribucion + gasto_capacidad
print("Gasto total de luz mensual:", gasto_luz_total)

gasto_agua = 20757.36 + 102.49 * 3.8
print("Gasto de agua mensual:", gasto_agua)

gasto_total = nomina_total + gasto_luz_total + gasto_agua
print("Gasto total considerando luz (CFE) y agua:", gasto_total)

ingreso = gasto_total + 1500000

omega = norm.ppf(0.01)
a_ = mu ** 2
b_ = -2 * mu * gasto_total - omega ** 2 * sigma ** 2
c_ = gasto_total ** 2
N1 = (-b_ + np.sqrt(b_ ** 2 - 4 * a_ * c_)) / (2 * a_)
N2 = (-b_ - np.sqrt(b_ ** 2 - 4 * a_ * c_)) / (2 * a_)

print("N1 (Solución 1):", N1)
print("N2 (Solución 2):", N2)

if (ingreso / N1 - mu > 0):
    N = N1
else:
    N = N2

porc_pob = N / 160000
print("Porcentaje de la población necesario:", porc_pob)
