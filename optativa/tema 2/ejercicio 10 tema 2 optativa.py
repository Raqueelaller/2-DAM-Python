'''10.Escribe un programa que a partir de información de un donante determine si  puede donar sangre. Las condiciones para donar son: 
a. No se debe donar en ayunas. 
b. Edad: Comprendida entre los 18 y 65 años. 
c. Peso: Superior a 50kg. 
d. Tensión arterial: dentro de límites adecuados para la extracción. i. Tensión diastólica (baja): entre 50mm Hg y 100 mm Hg 
ii. Tensión sistólica (alta): entre 90mm y 180mm Hg 
e. Pulso (frecuencia cardiaca): entre 50 y 110 pulsaciones 
f. Valores de hemoglobina: 
i. En hombres: superior a 13,5 gramos por litro 
ii. En mujeres: superior a 12,5 gramos por litro. 
g. Plaquetas: más de 150.000 cc  
h. Proteínas totales: más de 6 gr/dl.
'''
ayunas=str(input("dime si estás en ayuna: "))
edad=int(input("dime tu edad: "))
peso=int(input("dime tu peso: "))
tensionD=int(input("dime tu tensión diastólica: "))
tensionS=int(input("dime tu tensión sistólica: "))
pulso=int(input("dime tu pulso: "))
sexo=str(input("dime si eres hombre o si eres mujer: "))
hemoglobina=int(input("dime tu hemogoblina: "))
plaqueta=int(input("dime las plaquetas que tienes: "))
proteina=int(input("dime las proteínas: "))

if ayunas=="si":
    if edad>= 18 and edad <= 65:
        if peso>50:
            if tensionD >= 50 and tensionD <= 100:
                if tensionS >= 90 and tensionS <= 180:
                    if pulso >= 50 and pulso <= 110:
                        if sexo == "hombre":
                            if hemoglobina<=13.5:
                                if plaqueta >= 150000:
                                    if proteina >=6:
                                        print("puedes donar sangre")
                                    else:
                                        print("no puedes donar")
                                else:
                                    print("no puedes donar")
                            else:
                                print("No puedes donar")
                        elif sexo=="mujer":
                            if hemoglobina>=12.5:
                                if plaqueta >= 150000:
                                    if proteina >=6:
                                        print("puedes donar sangre")
                                    else:
                                        print("no puedes donar")
                                else:
                                    print("no puedes donar")
                            else:
                                print("No puedes donar")
                        else:
                            print("Error")
                    else:
                        print("No puedes donar")
                else:
                    print("no puedes donar")
            else: 
                print("no puedes donar")
        else:
            print("no puedes donar")
    else: 
        print("no puedes donar")
else:
    print("No puedes donar")

            