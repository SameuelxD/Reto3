"""categoria=""
            for i in CategoriaInsidencias:
                while(i!=categoria):
                    categoria=input("Digite la Categoria de la Insidencia: ").upper()
            tipo=""
            for i in TipoInsidencias:
                while(i!=categoria):
                    tipo=input("Digite el Tipo de Insidencia: ")
            area=input("Digite el Area donde se dio la Insidencia: ").upper()
            while(AreasGenerales.get(area)):
                salon=""
                for i in AreasGenerales[area]:
                    while(i!=lugar):
                        lugar=input("Digite el Lugar donde se dio la Insidencia: ").upper()"""

mi_diccionario = {
    "clave1": [1, 2, 3],
    "clave2": [4, 5, 6],
    "clave3": [7, 8, 9]
}

for clave, lista in mi_diccionario.items():
    print(f"Clave: {clave}")
    print("Elementos de la lista:")
    for elemento in lista:
        print(elemento)
    print()
