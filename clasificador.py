# Con esta biblioteca vamos a importar los cálculos a un csv
import pandas as pd

# Necesitamos poblar los diccionarios con sus respectivos términos
elementos = {
    "activo circulante":{"efectivo":0.0,"documentos por cobrar":0.0,"cuentas por cobrar":0.0,"seguros pagados por anticipado":0.0,"suministros":0.0,"renta pagada por anticipado":0.0,"inventarios":0.0},
    "activo no circulante":{"terreno":0.0, "maquinaria y equipo":0.0,"depreciacion acumulada":0.0,"construccion en proceso":0.0,"edificio":0.0},
    "pasivo corto plazo":{"ingresos diferidos":0.0,"cuentas por pagar":0.0,"sueldos por pagar":0.0},
    "pasivo largo plazo":{"documentos por pagar":0.0,"prestamos bancarios":0.0},
    "gastos":{"gastos por suministros":0.0,"gastos por sueldos":0.0,"gastos por renta":0.0,"gastos por depreciacion":0.0, "gastos por servicios":0.0},
    "otros gastos":{"gastos por impuestos":0.0},
    "head resultados":{"ingresos por renta":0.0,"ingresos por servicios":0.0,"costo de ventas":0.0,"ingresos por ventas":0.0},
    "capital contable":{"resultados acumulados":0.0,"capital social":0.0},
    "utilidades":{"ingresos por intereses":0.0,"gastos por impuestos":0.0}
}

# Función para saber qué clasificación tiene un elemento
def obtenerClasificacion(elemento):
    for i in elementos:
        if(elemento in elementos[i]):
            return i

#Función que realiza la suma de todos los valores para los elementos
def sumaElementos(diccionario):
    suma = 0
    for k in diccionario:
        if(k.lower() == "depreciacion acumulada"):
            suma = suma - diccionario[k]
        else:
            suma = suma + diccionario[k]
    return suma


# Vamos a darle la estructura a Balance Sheet
'''
                           Nombre de la Empresa
                               Balance Sheet
                                  fecha
    Activos                                             Pasivos

   Activos Circulantes                        Pasivos a Corto Plazo
       a) Efectivo                               a) Cuentas por pagar
       b) Cuentas por cobrar                     b) Ingresos Diferidos
       c) Suministros                         Total pasivos corto plazo
       d) Rentas pagadas por anticipado
   Activos no Circulantes                     Pasivos a Largo Plazo
       a) Terreno                                a) Documentos por pagar
       b) Maquinaria y equipo
       c) Depreciación Acumulada              Capital Contable
                                                 a) Capital Social
                                                 b) Resiltados Acumulados
   Total Activos                              Total Capital Contable

'''
# Función para obtener el reporte

# Pedimos el nombre del archivo
nombre = input("Ingresa el archivo: ")
# Pedimos el nombre de la empresa
empresa = input("Ingresa el nombre de la empresa: ")
# Pedimos la fecha para la cual se realiza el informe
fecha = input("Ingresa la fecha para la que se realiza: ")

f = open(nombre,"r")
lectura = f.read()
contenido = lectura.split("\n")

#Diccionarios que mantendrán la clasificación


for linea in contenido:
    elem = linea.lower()
    elems = elem.split(",")
    cl = obtenerClasificacion(elems[0])
    # Procedemos a agregar los elementos a sus respectivas clasificaciones
    if(type(cl) == str):
        elementos[cl][elems[0]] = float(elems[1])

# Realizamos las sumas
sumaActivoC  = sumaElementos(elementos["activo circulante"])
sumaActivoNC = sumaElementos(elementos["activo no circulante"])
sumaPasivoL  = sumaElementos(elementos["pasivo largo plazo"])
sumaPasivoC  = sumaElementos(elementos["pasivo corto plazo"])

# Vamos a darle la estructura a un Reporte de Resultados
'''

                         Nombre de la Empresa
                         Multiple Step Income
                          for the year date

   Net Sales/ Ingresos por Servicios   A
   Costo de ventas                     B

   Utilidad Bruta                   C =  A-B

   Gastos por Venta                    D
   Gastos por Suministros              E
   Gastos por Sueldos                  F
   Gastos por Renta                    G
   Gastos por Depreciación             H

   Total Gastos                I =  D + E + F + G + H

   Utilidad de Operación           J = C - I

   Ingresos por Intereses              K
   Utilidad antes de Impuestos      L = J + K
   Gastos por Impuestos                M

   Utilidad Neta                  N =  L - M

'''

# Necesitamos leer los datos para que nos genere el Reporte de Resultados

print("-----------------------------------------------------------")
print("                Empresa  "+ empresa)
print("           Multiple Step Income-Estado de Resultados")
print("                   Fecha: "+fecha)
print("\n-----------------------------------------------------------")
a = b = 0

if(elementos["head resultados"]["ingresos por ventas"] > 0.0):
    a = elementos["head resultados"]["ingresos por ventas"]
elif(elementos["head resultados"]["ingresos por servicios"] > 0.0):
    a = elementos["head resultados"]["ingresos por servicios"]
b = elementos["head resultados"]["costo de ventas"]
c = elementos["utilidades"]["ingresos por intereses"]
d = elementos["otros gastos"]["gastos por impuestos"]
z = elementos["head resultados"]["ingresos por renta"]
# Operaciones con los datos
sumaGastos = sumaElementos(elementos["gastos"])
utilidadOperacion = (a+z-b)-sumaGastos
utilidadAntesImpuestos = utilidadOperacion+c
utilidadNeta = utilidadAntesImpuestos - d

print("Ingresos por Ventas: "+str(a))
print("Ingresos por Renta: "+str(z))
print("Costos de Ventas:    "+str(b))
print("---------------")
print("Utilidad Bruta: "+str((a+z) - b))
print("---------------")
print("Gastos de Operación: ")
for k in elementos["gastos"]:
    print(k+ "    "+str(elementos["gastos"][k]))
print("Suma total de gastos: "+str(sumaGastos))
print("---Utilidad de Operación----")
print("total: "+str(utilidadOperacion))
print("---------------")
print("Ingresos por intereses  "+str(c))

print("Utilidad antes de impuestos: "+str(utilidadAntesImpuestos))
print("gastos por impuestos "+str(d))
print("\nUtilidad Neta: "+str(utilidadNeta)+"\n\n")


# Realizamos la suma de los totales
sumaActivos = sumaActivoC + sumaActivoNC


# Vamos a imprimir el informe
print("-----------------------------------------------------------")
print("                Empresa  "+ empresa)
print("                   Balance Sheet")
print("                   Fecha: "+fecha)
print("\n-----------------------------------------------------------")
print("        Activos Circulantes ")
for k in elementos["activo circulante"]:
    print(k + "    " + str(elementos["activo circulante"][k]))
print("Total Activos Circulantes: "+str(sumaActivoC))
print("\n\n       Activos no Circulantes")
for k in elementos["activo no circulante"]:
    print(k + "    " + str(elementos["activo no circulante"][k]))
print("Total Activos No Circulantes: "+str(sumaActivoNC))
print("--------------")
print("Total de Activos: "+str(sumaActivos))
print("------------------------------------------------------------")
print("\n\n       Pasivos a Corto Plazo")
for k in  elementos["pasivo corto plazo"]:
    print(k + "    " + str(elementos["pasivo corto plazo"][k]))
print("Total Pasivos a corto plazo: "+str(sumaPasivoC))
print("\n\n       Pasivos a largo plazo")
for k in elementos["pasivo largo plazo"]:
    print(k + "    " + str(elementos["pasivo largo plazo"][k]))
print("Total Pasivos a largo plazo: "+str(sumaPasivoL))
print("--------------")
print("Total de Pasivos: "+str(sumaPasivoC+sumaPasivoL))
print("\n\n       Capital Contable")
for k in elementos["capital contable"]:
    if(k == "resultados acumulados"):
        elementos["capital contable"][k] = elementos["capital contable"][k] + utilidadNeta
    print(k + "    " + str(elementos["capital contable"][k]))
print("Utilidad neta: "+str(utilidadNeta))
#Realizamos las sumas y restas debidas
sumaCapitC = sumaElementos(elementos["capital contable"])
sumaPasivos = sumaPasivoL + sumaPasivoC + sumaCapitC

print("Total Capital Contable: "+str(sumaCapitC))
print("--------------")
print("Total Capital Contable + Pasivos: "+str(sumaPasivos))
print("------------------------------------------------------------")
