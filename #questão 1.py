 #questão 1
segundos= int(input("Quantos segundos?"))

horas = segundos // 3600
segundos_resto = segundos % 3600
minutos = segundos_resto // 60
segundos_resto = segundos_resto % 60

print (horas, " horas, ", minutos, "minutos e ", segundos_resto, " segundos ")

# transforma segundos em horas e minutos
