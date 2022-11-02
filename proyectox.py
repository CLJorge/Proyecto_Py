


contraseña_reservada=""
contador_de_letras=0
def contraseña():
    global contraseña_reservada
    global contador_de_letras
    inicio()

    usuario_ingresecontraseña=str(input("Escriba una contraseña de 4 diguitos ---->"))
    contador_de_letras=len(usuario_ingresecontraseña)
    ii=0
    while ii != 2:
        if contador_de_letras !=4:
            print("Su contraseña en incorrecta")
            usuario_ingresecontraseña=str(input("Escriba una contraseña de 4 diguitos ---->"))
            contador_de_letras=len(usuario_ingresecontraseña)
            ii+=1 
            if ii ==2:
                print("Adios excediste el numero de intentos del principio")
            else:
                pass
        else:
            if contador_de_letras==4:  
                contraseña_reservada=usuario_ingresecontraseña
                comprobacion()   
                break

def comprobacion():
    i=0
    vereficador=str(input("Escriba su contraseña que elegio--->"))
    while i <=2:

        if contraseña_reservada==vereficador:
            print("                      ")
            print("--» BIENVENIDO :      ")
            menu()
            ejecucion()
            break
        else:
            if i==2:
                print("Esta no es tu cuenta")
                break
            else:
                print("Error escribio mal su contraseña")
                vereficador=str(input("Escriba su contraseña que elegio----> "))
        i+=1
lista=[]
nom=""        
sueldot=0
sueldo=0
bono1t=0
bono2t=0
def op1():
    global sueldot
    global nom
    global bono1t
    global bono2thola
    nom= str(input("Escriba su nombre: "))
    horas_trabajadas=int(input("Ingrese las horas trabajadas: "))
    sueldo_horas=int(input("Ingrese su sueldo por hora: "))

    extras = horas_trabajadas - 48    # Horas trabajadas menos 48 horas de jornada---pasando las 48 horas --2 primeras horas adicionales
    extrasb = horas_trabajadas - 50   # Horas trabajadas menos 50 -- pasando las 50 horas ya se contaria las demas horas extras

    if horas_trabajadas<=48 and horas_trabajadas>0:
        sueldo=horas_trabajadas*sueldo_horas
        sueldot=sueldo
        print ("------------------------------------------------------")
        print ("                                                      ")
        print ("    Nombre del empleado: ",nom)
        print ("    Su sueldo es: ",sueldot)
        print ("    No posee horas extras                             ")
        print ("                                                      ")
        print ("------------------------------------------------------")
        lista.append(" Nombre:   " + str(nom) + "   Sueldo Total   "+ str(sueldot))
        menu()
        ejecucion()
    elif horas_trabajadas>=49 and horas_trabajadas<=50:
        sueldo=horas_trabajadas*sueldo_horas
        bono=sueldo_horas*0.25
        bono1t=extras*bono      
        sueldot=sueldo+bono1t
        print ("------------------------------------------------------")
        print ("                                                      ")
        print ("    Nombre del empleado: ",nom)
        print ("    Su subsueldo es: ",sueldo)
        print ("    Bono por horas extras: ",bono1t)
        print ("    Su sueldo total es: ",sueldot)
        print ("                                                      ")
        print ("------------------------------------------------------")
        lista.append("  Nombre:   "+str(nom)+"   Sueldo Total=  "+str(sueldot)+"    1ers Extras    "+str(bono1t))
        menu()
        ejecucion()      
    elif horas_trabajadas>=51:
        sueldo = horas_trabajadas*sueldo_horas
        bono1=sueldo_horas*0.25
        bono1t=2*bono1
        bono2=sueldo_horas*0.35
        bono2t=extrasb*bono2
        sueldot = sueldo + bono1t + bono2t
        print ("------------------------------------------------------")
        print ("                                                      ")
        print ("    Nombre del empleado: ",nom)
        print ("    Su subsueldo es: ",sueldo)
        print ("    El bono de sus 2 primeras horas extras es: ",bono1t)
        print ("    El sueldo de sus demas horas extras es: ",bono2t)
        print ("    Su sueldo total es: ",sueldot)
        print ("                                                      ")
        print ("------------------------------------------------------")
        lista.append("  Nombre:  "+str(nom)+"   Sueldo Total=  "+str(sueldot)+"    1ers Extras    "+str(bono1t)+"    3er Extras   "+str(bono2t))
        menu()
        ejecucion()
    else:
        print("El numero que ingreso es incorrecto  ")
        menu()
        ejecucion()
def op2():
    if lista:     
        for i in lista:
            print(i)
        menu()
        ejecucion()
    else:
        print("No hay empleados registrados")
        menu()
        ejecucion()

def op3():
    exit()

def ejecucion():
    try:
        opcion = int(input("Elige una opcion: "))
        while opcion <1 or opcion >3:
            
                print("Ingrese un numero correcto porfavor: ")
                menu()
                ejecucion()
                
        else:
             pass

    except ValueError:
        print("No escriba letras please")
        menu()
        ejecucion()
    else:
        if opcion == 1:
            op1()
        else:
            if opcion == 2:
                op2()
            else:
                if opcion == 3:
                    op3()
                
def inicio():
    print('''
    
           \ \ \  MULTIFOODS  / / /
    ''')
                   

 
def menu():
    print('''
           EMPRESA MULTIFOODS :

           [1]_CONSULTA DE SUELDO DE EMPLEADOS
           [2]-ULTIMOS REGISTROS 
           [3]-SALIR
 
           SELECCIONE UNA OPCION:  
           ''')
if __name__ == '__main__':
    contraseña()