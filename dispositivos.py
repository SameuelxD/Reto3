import core
import os
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
    print("1. Agregar Insidencia.")
    print("2. Buscar Insidencia.")
    print("3. Editar Insidencia.")
    print("4. Eliminar Insidencia.")
    print("5. Regresar menu principal")
    opcion =int(input("Digite Opcion: "))
    if (opcion == 1):
        while(Passive):
            os.system("cls")
            print('+','-'*49,'+')
            print("|{:^16}{}{:^15}|".format(' ','AGREGAR DISPOSITIVOS',' '))
            print('+','-'*49,'+')
            Pause=True
            while(Pause):
                try:
                    id=int(input("Digite el Id de la Insidencia a Agregar: "))
                except ValueError:
                    print("El Id Digitado para la Insidencia no es Valido...")
                else:
                    id=str(id)
                    Pause=False
            Pause=True
            while(Pause):
                os.system("cls")
                print("---CATEGORIA INSIDENCIAS---\n -LEVE.\n -MODERADA.\n -CRITICA.")
                categoria=input("Digite la Categoria de la Insidencia: ").upper()
                for i,item in enumerate(CategoriaInsidencias):
                    if categoria==item:
                        Pause=False
            Pause=True
            while(Pause):
                os.system("cls")
                print("---TIPOS INSIDENCIAS---\n -HARDWARE.\n -SOFTWARE.")
                tipo=input("Digite el Tipo de Insidencia: ").upper()
                for i,item in enumerate(TipoInsidencias):
                    if tipo==item:
                        Pause=False
            Pause=True
            while(Pause):
                os.system("cls")
                print("---AREAS GENERALES---\n -AREA TRAINING.\n -AREA REVIEWS.")
                area=input("Digite el Area donde sucedio la Insidencia: ").upper()
                for i,item in AreasGenerales.items():
                    if area==i:
                        while(Pause):
                            os.system("cls")
                            print("---AREA TRAINING---\n -APOLO.\n -ARTEMIS.\n -SPUTNIK.\n -SKYLAB.")
                            print("---AREA REVIEWS---\n -AREA REVIEWS1.\n -AREA REVIEWS2.")
                            print("Recuerde que el Lugar varia en opciones por el Area que marco...")
                            lugar=input("Digite el Lugar donde sucedio la Insidencia: ").upper()
                            for elemento in item:
                                if lugar==elemento:
                                    Pause=False        
            insidencia ={
                "Id-Insidencia":id,
                "Categoria-Insidencia":categoria,
                "Tipo-Insidencia":tipo,
                "Descripcion":input("Digite una Descripcion de la Insidencia: "),
                "Fecha-Reporte":input("Digite la Fecha del Reporte de la Insidencia: "),
                "Area-Insidencia":area,
                "Lugar-Insidencia":lugar
            }
            infoInsidencias["data"].append(insidencia)
            core.AddInfo("insidencias.json",insidencia)
            Passive=bool(input("Digite un valor Alphanumerico para volver a Ingresar una Insidencia o Presione Enter para Salir al Menu Principal --> "))
    
    elif (opcion == 2):
        while(Passive):
            os.system("cls")
            print('+','-'*49,'+')
            print("|{:^16}{}{:^15}|".format(' ','BUSCAR INSIDENCIA',' '))
            print('+','-'*49,'+')
            id = input("Digite el Id de la Insidencia a Buscar:")
            for i,item in enumerate(infoInsidencias["data"]):
                if id in item["Id-Insidencia"]:
                    print(f'Id Insidencia : {item["Id-Insidencia"]}')
                    print(f'Categoria Insidencia : {item["Categoria-Insidencia"]}')
                    print(f'Fecha Reporte : {item["Fecha-Reporte"]}')
                    print(f'Area Insidencia : {item["Area-Insidencia"]}')
                    print(f'Lugar Insidencia : {item["Lugar-Insidencia"]}')
            Passive=bool(input("Digite un valor Alphanumerico para volver a Buscar una Insidencia o Presione Enter para Salir al Menu Principal --> "))

    elif (opcion == 3):
        while(Passive):
            os.system("cls")
            print('+','-'*49,'+')
            print("|{:^16}{}{:^15}|".format(' ','EDITAR INSIDENCIA',' '))
            print('+','-'*49,'+')
            id = input("Digite el Id de la Insidencia a Editar: ")
            for i,item in enumerate(infoInsidencias["data"]):
                if id in item["Id-Insidencia"]:
                    item["Descripcion"] = input("Digite una Nueva Descripcion para la Insidencia o Presione Enter para Omitir: ") or item["Descripcion"]
                    item["Fecha-Reporte"] = input("Digite una Nueva Fecha de Reporte de la Insidencia o Presione Enter para Omitir: ") or item["Fecha-Reporte"]
                    core.EditarData("insidencias.json",infoInsidencias)
            Passive=bool(input("Digite un valor Alphanumerico para volver a Editar una Insidencia o Presione Enter para Salir al Menu Principal --> "))

    elif (opcion == 4):
        while(Passive):
            os.system("cls")
            print('+','-'*49,'+')
            print("|{:^16}{}{:^15}|".format(' ','ELIMINAR INSIDENCIA',' '))
            print('+','-'*49,'+')
            id = input("Digite el Id de la Insidencia a Eliminar: ")
            for i,item in enumerate(infoInsidencias["data"]):
                if id in item["Id-Insidencia"]:
                    itemDel = infoInsidencias["data"].pop(i)
                    core.EditarData("insidencias.json",infoInsidencias)
            Passive=bool(input("Digite un valor Alphanumerico para volver a Eliminar una Insidencia o Presione Enter para Salir al Menu Principal --> "))
    elif (opcion == 5):
        Passive = False
    if Passive:
        MenuInsidencias()