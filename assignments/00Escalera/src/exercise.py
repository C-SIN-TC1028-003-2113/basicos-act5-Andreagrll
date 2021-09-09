import math

def main():
    h = float (input ("Altura de la casa: "))
    a = int (input ("Angulo en grados: "))

    radianes = math.radians(a)

    largo = round(h/math.sin(radianes))

    print ("Largo de la escalera: "+ str (largo))

if __name__ == '__main__':
    main()
