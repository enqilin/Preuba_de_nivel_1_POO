import os 
import vehiculos.vehiculo as db

def iniciar():
    while True:
        helpers.limpiar_pantalla()


        print("==============================")
        print("  Bienvenida al Gestor        ")
        print("==============================")
        print("[1] Listar los vehiculos      ")
        print("[2] Buscar un vehiculo        ")
        print("[3] Buscar con otro carárectes")
        print("[4] Añadir un vehiculo        ")
        print("[5] Modificar un vehiculo     ")
        print("[6] Borrar un vehiculo        ")
        print("[7] Cerrar el Gestor          ")
        print("==============================")

        option=input("> ")
        helpers.liampiar_pantalla()

        if option==" 1 ":
            print("Listando los vehiculos...\n")
            for vehiculos in db.Vehiculos.vehiculo:
                print(vehiculos)
        
        elif option=="2":
            print("Buascando un vehiculo...\n")
            vehiculos=helpers.leer_texto(3,3,"Bastidor (2 int y 1 char)").upper()
            vehiculos=db.Vehiculos.buscar(bastidor)
            if vehiculos:
                print(vehiculos)
            else:
                print("El vehiculo no existe")

        elif option =="4":

            bastidor = None
            while True:
                Bastidor=helpers.leer_texto(3,3, "bastidor(2 int y 1 cahr)").upper()
                if helpers.bastidor_valido(bastidor,db.Vehiculos.vehiculo):
                    break
            
            ruedas= helpers.leer_texto(2,10,"El numero de ruedas(2 o 4)")
            color= helpers.leer_texto(2,30,"El color (de 2 a 30)").capitalize()
            db.Vehiculos.crear((bastidor,ruedas,color))
            print("El vehiculo añadido correctamente")

        elif  option== "5":
            print(" Modificando el vehiculo...\n")

            bastidor=helpers.leer_texto(3,3, "Bastidor(2 int y 1 cahr)").upper()
            if vehiuclos:
                ruedas=helpers.leer_texto(
                    2,10,f"El numero de ruedas(2 o 4))[{vehiculos.ruedas}]"
                )
                color=helpers.leer_texto(
                    2,30,f"El color (de 2 a 30)[{vehiculos.color}]").capitalize()
                db.Vehiculo.modificar(vehiculos.bastidor,vehiculos.ruedas,vehiculos.color)
                print("Vehiculo modificado correctamente")
            else:
                print("Vehiculo no encontrado")
    
            

        elif option=="6":
            print("Borrando el vehiculo...\n")
            bastidor=helpers.leer_texto(3,3, "Bastidor (2int y 1 char)").upper()
            if db.vehiculos.Borrar(bastidor):
                print("Vehiculo borrado correctamente.")
            else:
                print("Vehiculo no existe.")

        elif option=="7":
            print("Salir del gestor...\n")
            break

    input("\n Presiona el ENTER para continuar...")





        