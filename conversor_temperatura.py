# Programa coversor de temperatura
print ("---------------------------------------")
print ("------VALOR EN GRADOS CENTIGRADOS------")
print ("---------------------------------------")

#input

c = int(input("Digite el valor de grados centígrados:"))

#processing
f =(c+273.15)
k =(c*1.8+32)

#output
print("----------------------------------")
print("------------RESULTADOS------------")
print("----------------------------------")

print("Resultado grados farenheit " + str(f))
print("Resultados grados kelvin " + str(k))
