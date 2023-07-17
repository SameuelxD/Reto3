import core
import os

infoTrainers= {"data":[]}
def LoadInfoTrainers():
    global infoTrainers
    if (core.CheckFile("trainers.json")):
        infoTrainers = core.LoadInfo("trainers.json")
    else:
        core.AddInfo("trainers.json",infoTrainers)
def MenuTrainers():
    os.system("cls")
    Passive=True 
    print('+','-'*55,'+')
    print("|{:^16}{}{:^15}|".format(' ','GESTION DE TRAINERS',' '))
    print('+','-'*55,'+')
    print("1. Agregar Trainer")
    print("2. Buscar Trainer")
    print("3. Editar Trainer")
    print("4. Eliminar Trainer")
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
            print("|{:^16}{}{:^15}|".format(' ','AGREGAR TRAINER',' '))
            print('+','-'*49,'+')
            Pause=True
            while(Pause):
                try:
                    id=int(input("Digite el Id del Trainer"))
                except ValueError:
                    print("El Id Digitado no es Valido")
                else:
                    id=str(id)
                    Pause=False
            Pause=True
            while(Pause):
                try:
                    nombre=input("Digite el Nombre del Trainer: ").upper()
                    personal=input("Digite el Correo Electronico Personal del Trainer: ")
                    corporativo=input("Digite el Correo Electronico Corporativo del Trainer: ")
                    nombre=int(nombre)
                    personal=int(personal)
                    corporativo=int(corporativo)
                except ValueError:
                    nombre=str(nombre)
                    personal=str(personal)
                    corporativo=str(corporativo)
                    if((len(nombre)!=0)and(len(personal)!=0)and(len(corporativo)!=0)):
                        Pause=False
                    else:
                        print("Digitos Invalidos,Solo se aceptan Strings para las opciones")
                else:
                    print("Digitos Invalidos,Solo se aceptan Strings para las opciones") 
            Pause=True
            while(Pause):
                try:
                    movil=int(input("Digite el Telefono Movil del Trainer: "))
                    residencia=int(input("Digite el Telefono de Residencia del Trainer: "))
                    empresa=int(input("Digite el Telefono de Empresa del Trainer: "))
                    movilEmpresa=int(input("Digite el Telefono Movil Empresarial del Trainer: "))
                except ValueError:
                    print("Digitos Invalidos,Solo se aceptan Enteros para las opciones")
                else:
                    Pause=False
            trainer ={
                "Id":id,
                "Nombre":nombre,
                "Email-Personal":personal,
                "Email-Corporativo":corporativo,
                "Telefono-Movil":movil,
                "Telefono-Residencia":residencia,
                "Telefono-Empresa":empresa,
                "Telefono-Movil-Empresarial":movilEmpresa
            }
            infoTrainers["data"].append(trainer)
            core.AddInfo("trainers.json",trainer)
            Passive=bool(input("Digite un valor Alphanumerico para volver a Ingresar un Trainer o Presione Enter para Salir al Menu Principal --> "))
    
    elif (opcion == 2):
        while(Passive):
            os.system("cls")
            print('+','-'*49,'+')
            print("|{:^16}{}{:^15}|".format(' ','BUSCAR TRAINERS',' '))
            print('+','-'*49,'+')
            id = input("Digite el Id del Trainer a Buscar:")
            for i,item in enumerate(infoTrainers["data"]):
                if id in item["Id"]:
                    print(f'Id Trainer : {item["Id"]}')
                    print(f'Nombre Trainer : {item["Nombre"].upper()}')
                    print(f'Email Personal : {item["Email-Personal"]}')
            Passive=bool(input("Digite un valor Alphanumerico para volver a Buscar un Camper o Presione Enter para Salir al Menu Principal --> "))

    elif (opcion == 3):
        while(Passive):
            os.system("cls")
            print('+','-'*49,'+')
            print("|{:^16}{}{:^15}|".format(' ','EDITAR TRAINERS',' '))
            print('+','-'*49,'+')
            id = input("Digite el Id del Trainer a Editar: ")
            for i,item in enumerate(infoTrainers["data"]):
                if id in item["Id"]:
                    item["Nombre"] = input("Digite un Nuevo Nombre para el Trainer o Presione Enter para Omitir: ") or item["Nombre"]
                    item["Email-Personal"] = input("Digite un Nuevo Email Personal para el Trainer o Presione Enter para Omitir: ") or item["Email-Personal"]
                    core.EditarData("trainers.json",infoTrainers)
            Passive=bool(input("Digite un valor Alphanumerico para volver a Editar un Camper o Presione Enter para Salir al Menu Principal --> "))

    elif (opcion == 4):
        while(Passive):
            os.system("cls")
            print('+','-'*49,'+')
            print("|{:^16}{}{:^15}|".format(' ','ELIMINAR TRAINERS',' '))
            print('+','-'*49,'+')
            id = input("Digite el Id del Trainer a Eliminar: ")
            for i,item in enumerate(infoTrainers["data"]):
                if id in item["Id"]:
                    itemDel = infoTrainers["data"].pop(i)
                    core.EditarData("trainers.json",infoTrainers)
            Passive=bool(input("Digite un valor Alphanumerico para volver a Eliminar un Camper o Presione Enter para Salir al Menu Principal --> "))

    elif (opcion == 5):
        Passive = False
    if Passive:
        MenuTrainers()
    else:
        print("OPCION INEXISTENTE")
        input("Digite una tecla para continuar...")