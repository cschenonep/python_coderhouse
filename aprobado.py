import sys

if len(sys.argv) != 3:
    print("Solo ingresa dos valores")
else:
    if int(sys.argv[1] and int(sys.argv[2]))>=0 and int(sys.argv[1] and int(sys.argv[2]))<=10:
        if int(sys.argv[1] and int(sys.argv[2]))>=7:
            print("Promocionado")
        elif int(sys.argv[1] and int(sys.argv[2]))>=4:
            print("Aprobado, debe rendir el final")
    else:
        print("Debe ingresar valores menores o iguales a 10 y mayores que 0")