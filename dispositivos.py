import core
import os
CategoriaDispositivos=["COMPUTADORES","TECLADOS","MOUSE","DIADEMAS"]
MarcaDispositivos=["LENOVO","APPLE","ACER","DELL"]
AreasGenerales={
    "AREA TRAINING":["APOLO","ARTEMIS","SPUTNIK","SKYLAB"],
    "AREA REVIEWS":["AREA REVIEWS1","AREA REVIEWS2"]
}
infoDispositivos= {"data":[]}
def LoadInfoDispositivos():
    global infoDispositivos
    if (core.CheckFile("dispositivos.json")):
        infoDispositivos = core.LoadInfo("dispositivos.json")
    else:
        core.AddInfo("dispositivos.json",infoDispositivos)
def MenuDispositivos():
    os.system("cls")
    Passive=True 
    print('+','-'*55,'+')
    print("|{:^16}{}{:^15}|".format(' ','GESTION DE DISPOSITIVOS',' '))
    print('+','-'*55,'+')
    print("1. Agregar y Asignar Dispositivos.")
    print("2. Buscar Dispositivos.")
    print("3. Reasignar Dispositivos.")
    print("4. Eliminar Dispositivos.")
    print("5. Regresar menu principal")
    Continue=True
    while(Continue):
        try:
            opcion=int(input("Digite la Opcion: "))
        except ValueError:
            print("Digito Invalido, Solo se aceptan Enteros")
        else:
            Continue=False
    if (opcion == 1):
        while(Passive):
            os.system("cls")
            print('+','-'*49,'+')
            print("|{:^16}{}{:^15}|".format(' ','AGREGAR DISPOSITIVOS',' '))
            print('+','-'*49,'+')
            Pause=True
            while(Pause):
                try:
                    id=int(input("Digite el Id del Dispositivo a Agregar: "))
                except ValueError:
                    print("El Id Digitado para el Dispositivo no es Valido...")
                else:
                    id=str(id)
                    Pause=False
            Pause=True
            while(Pause):
                os.system("cls")
                print("---CATEGORIA DISPOSITIVOS---\n -COMPUTADORES.\n -TECLADOS.\n -MOUSE.\n -DIADEMAS.")
                categoria=input("Digite la Categoria del Dispositivo a Agregar: ").upper()
                for i,item in enumerate(CategoriaDispositivos):
                    if categoria==item:
                        Pause=False
            Pause=True
            while(Pause):
                os.system("cls")
                print("---MARCA DISPOSITIVOS---\n -LENOVO.\n -APPLE.\n -ACER.\n -DELL.")
                marca=input("Digite la Marca del Dispositivo: ").upper()
                for i,item in enumerate(MarcaDispositivos):
                    if marca==item:
                        Pause=False
            Pause=True
            while(Pause):
                os.system("cls")
                print("---AREAS GENERALES---\n -AREA TRAINING.\n -AREA REVIEWS.")
                area=input("Digite el Area donde quiere Agregar y Asignar Dispositivos: ").upper()
                for i,item in AreasGenerales.items():
                    if area==i:
                        while(Pause):
                            os.system("cls")
                            print("---AREA TRAINING---\n -APOLO.\n -ARTEMIS.\n -SPUTNIK.\n -SKYLAB.")
                            print("---AREA REVIEWS---\n -AREA REVIEWS1.\n -AREA REVIEWS2.")
                            print("Recuerde que el Lugar varia en opciones por el Area que marco...")
                            lugar=input("Digite el Lugar donde quiere Asignar los Dispositivos: ").upper()
                            for elemento in item:
                                if lugar==elemento:
                                    Pause=False        
            dispositivo ={
                "Id-Dispositivo":id,
                "Categoria-Dispositivo":categoria,
                "Marca-Dispositivo":marca,
                "Area-Dispositivo":area,
                "Lugar-Dispositivo":lugar
            }
            infoDispositivos["data"].append(dispositivo)
            core.AddInfo("dispositivos.json",dispositivo)
            Passive=bool(input("Digite un valor Alphanumerico para volver a Ingresar un Dispositivo o Presione Enter para Salir al Menu Principal --> "))
    
    elif (opcion == 2):
        while(Passive):
            os.system("cls")
            print('+','-'*49,'+')
            print("|{:^16}{}{:^15}|".format(' ','BUSCAR DISPOSITIVO',' '))
            print('+','-'*49,'+')
            id = input("Digite el Id del Dispositivo a Buscar:")
            for i,item in enumerate(infoDispositivos["data"]):
                if id==item["Id-Dispositivo"]:
                    print(f'Id Dispositivo : {item["Id-Dispositivo"]}')
                    print(f'Categoria Dispositivo : {item["Categoria-Dispositivo"]}')
                    print(f'Marca Dispositivo : {item["Marca-Dispositivo"]}')
                    print(f'Area dispositivo : {item["Area-Dispositivo"]}')
                    print(f'Lugar dispositivo : {item["Lugar-Dispositivo"]}')
            Passive=bool(input("Digite un valor Alphanumerico para volver a Buscar una dispositivo o Presione Enter para Salir al Menu Principal --> "))

    elif (opcion == 3):
        while(Passive):
            os.system("cls")
            print('+','-'*49,'+')
            print("|{:^16}{}{:^15}|".format(' ','REASIGNAR DISPOSITIVO',' '))
            print('+','-'*49,'+')
            id = input("Digite el Id del Dispositivo a Reasignar: ")
            for i,item in enumerate(infoDispositivos["data"]):
                if id in item["Id-Dispositivo"]:
                    Pause=True
                    while(Pause):
                        os.system("cls")
                        print("---AREAS GENERALES---\n -AREA TRAINING.\n -AREA REVIEWS.")
                        area=input("Digite el Area donde quiere Reasignar el Dispositivo o Presione Enter para Omitir: ").upper()
                        for i,item in AreasGenerales.items():
                            if area==i:
                                while(Pause):
                                    os.system("cls")
                                    print("---AREA TRAINING---\n -APOLO.\n -ARTEMIS.\n -SPUTNIK.\n -SKYLAB.")
                                    print("---AREA REVIEWS---\n -AREA REVIEWS1.\n -AREA REVIEWS2.")
                                    print("Recuerde que el Lugar varia en opciones por el Area que marco...")
                                    lugar=input("Digite el Lugar donde quiere Reasignar los Dispositivos: ").upper()
                                    
                                    for elemento in item:
                                        if  lugar==elemento:
                                            for i,item in enumerate(infoDispositivos["data"]):
                                                if id in item["Id-Dispositivo"]:
                                                    item["Area-Dispositivo"]=area
                                                    item["Lugar-Dispositivo"]=lugar
                                            core.EditarData("dispositivos.json",infoDispositivos)
                                            Pause=False 
            Passive=bool(input("Digite un valor Alphanumerico para volver a Reasignar un Dispositivo o Presione Enter para Salir al Menu Principal --> "))

    elif (opcion == 4):
        while(Passive):
            os.system("cls")
            print('+','-'*49,'+')
            print("|{:^16}{}{:^15}|".format(' ','ELIMINAR DISPOSITIVO',' '))
            print('+','-'*49,'+')
            id = input("Digite el Id de la Dispositivo a Eliminar: ")
            for i,item in enumerate(infoDispositivos["data"]):
                if id in item["Id-Dispositivo"]:
                    itemDel = infoDispositivos["data"].pop(i)
                    core.EditarData("dispositivos.json",infoDispositivos)
            Passive=bool(input("Digite un valor Alphanumerico para volver a Eliminar una dispositivo o Presione Enter para Salir al Menu Principal --> "))
    elif (opcion == 5):
        Passive = False
    if Passive:
        MenuDispositivos()
    else:
        print("OPCION INEXISTENTE")
        input("Digite una tecla para continuar...")