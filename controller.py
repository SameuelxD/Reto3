#El Centro de Apoyo Tecnologico de CampusLands la ha contratado para Construir una Aplicacion que permita llevar la Gestion de Insidencias Tecnicas en cada una de las Salas de Entrenamiento y Review.El lider de IT desea que cada Trainer pueda reportar las insidencias ocurridas.
#El departamento de IT ha clasificado las Insidencias en las siguientes categorias: -Hardware y Software cada Trainer debe Ingresar la siguiente Informacion al momento de reportar la Insidencia: Categoria,Tipo Insidencia,Descripcion,Fecha Reportar,Area Insidencia,Lugar de Insidencia.
#CampusLands Cuenta con 4 Areas Generales en las cuales se encuentran los Equipos tecnologicos de uso diario de los Campers y Trainers. Las Areas son las siguientes: Area Training(Apolo,Artemis,Sputnik y Skylab),Area Reviews 1,Area Reviews 2.
#Las insidencias se pueden categorizar en Leve,Moderada y Critica.
#El sistema debe permitir Asignar computadores,Teclados,MOuse y DIademas en sonido en cada uno de los salones
#EL sistema debe permitir crear trainers(Id,NOmbre,Email Personal,Email Corporativo,telefono movil,telefono residencia,telefono empresa,telefono movil empresarial)
import os
import trainers
import insidencias
if __name__ == "__main__":
    Activate = True
    Trainers={'data':[]}
    Insidencias={'data':[]}
    opcion=None
    while(Activate):
        os.system("cls")
        print('+','-'*55,'+')
        print("|{:^20}{}{:^24}|".format(' ','Menu Pricipal',' '))
        print('+','-'*55,'+')
        print("1. Gestion de Insidencias")
        print("2. Gestion de Trainers")
        print("3. Gestion de Dispositivos Hardware")
        print("4. Salir")
        opcion=int(input("Digite la Opcion: "))
        if(opcion==1):
            insidencias.LoadInfoInsidencias()
            insidencias.MenuInsidencias()
        elif(opcion==2):
            trainers.LoadInfoTrainers()
            trainers.MenuTrainers()
        elif(opcion==3):
            pass
        elif(opcion==4):
            Activate=False
