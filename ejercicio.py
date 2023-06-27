import funciones as fu

while True:
    fu.limpiar_pantalla()
    fu.menu()
    opcion=fu.validar_opcion()
    if opcion==1:
        rut=int(input("Ingrese rut de alumno:"))
        nombre=fu.validar_nombre()
        edad=fu.validar_edad()
        genero=fu.validar_genero()
        promedio=fu.validar_promedio()
        fechamatricula=fu.validar_fecha()
        nombreapoderado=input("Ingrese nombre del apoderado:")
        fu.registrar(nombre,edad,genero,promedio,fechamatricula,nombreapoderado)
    elif opcion==2:
        fu.buscar()
    elif opcion==3:
        rut=int(input("Ingrese rut:"))
        fu.certificado(rut)
    elif opcion==4:
        fu.printam("Saliendo del sistema")
        fu.printtitulo("Sebastian Gonzalez v.1")
        break
