from heroes import lista_heroes
#  CONSTANTES

EMPRESAS_VALIDAS     = ["DC Comics", "Marvel Comics"]
GENEROS_VALIDOS      = ["M", "F", "NB"]
INTELIGENCIAS_VALIDAS = ["low", "average", "good", "high", "genius"]

INDICE_NOMBRE      = 0
INDICE_IDENTIDAD   = 1
INDICE_EMPRESA     = 2
INDICE_ALTURA      = 3
INDICE_PESO        = 4
INDICE_GENERO      = 5
INDICE_COLOR_OJOS  = 6
INDICE_COLOR_PELO  = 7
INDICE_FUERZA      = 8
INDICE_INTELIGENCIA = 9

#  FUNCIONES DE PRESENTACIÓN

def imprimir_separador():
    #Imprime una línea separadora 
    print("-" * 30)


def imprimir_heroe(heroe: list):
    # Muestra la información de un héroe 
    imprimir_separador()
    print(f"   Nombre       : {heroe[INDICE_NOMBRE]}")
    print(f"   Identidad    : {heroe[INDICE_IDENTIDAD]}")
    print(f"   Empresa      : {heroe[INDICE_EMPRESA]}")
    print(f"   Altura       : {heroe[INDICE_ALTURA]:.2f} cm")
    print(f"   Peso         : {heroe[INDICE_PESO]:.2f} kg")
    print(f"   Género       : {heroe[INDICE_GENERO]}")
    print(f"   Color ojos   : {heroe[INDICE_COLOR_OJOS]}")
    print(f"   Color pelo   : {heroe[INDICE_COLOR_PELO]}")
    print(f"   Fuerza       : {heroe[INDICE_FUERZA]}")
    print(f"   Inteligencia : {heroe[INDICE_INTELIGENCIA]}")
    imprimir_separador()


def imprimir_menu():
    #Muestra el menú principal de la aplicación
    imprimir_separador()
    print("        STARK INDUSTRIES - GESTIÓN DE HÉROES         ")
    imprimir_separador()
    print("  1. Listar todos los héroes")
    print("  2. Agregar héroe")
    print("  3. Eliminar héroe por nombre")
    print("  4. Ordenar héroes por nombre (A → Z)")
    print("  5. Ver héroe más alto")
    print("  6. Ver héroe más fuerte")
    print("  7. Ver héroe menos pesado")
    print("  0. Salir")
    imprimir_separador()

#  FUNCIONES DE VALIDACIÓN

def validar_string_no_vacio(mensaje: str) -> str:
    #Solicita un string no vacío al usuario.
    valor = input(mensaje).strip()
    if valor == "":
        print("El campo no puede estar vacío. Intentá de nuevo.")
        return validar_string_no_vacio(mensaje)   # recursión
    return valor


def validar_empresa() -> str:
    #Solicita y valida la empresa del héroe.
    print(f"  Empresas válidas: {', '.join(EMPRESAS_VALIDAS)}")
    empresa = input("  Empresa: ").strip()
    if empresa not in EMPRESAS_VALIDAS:
        print("Empresa inválida. Intentá de nuevo.")
        return validar_empresa()                   # recursión
    return empresa


def validar_numero_positivo(mensaje: str) -> float:
    #Solicita un número mayor a 0.#
    try:
        valor = float(input(mensaje))
        if valor <= 0:
            raise ValueError
        return valor
    except ValueError:
        print("Debe ser un número mayor a 0. Intentá de nuevo.")
        return validar_numero_positivo(mensaje)    # recursión


def validar_genero() -> str:
    #Solicita y valida el género del héroe.
    print(f"  Géneros válidos: {', '.join(GENEROS_VALIDOS)}")
    genero = input("  Género: ").strip().upper()
    if genero not in GENEROS_VALIDOS:
        print("Género inválido. Intentá de nuevo.")
        return validar_genero()                    # recursión
    return genero


def validar_inteligencia() -> str:
    #Solicita y valida el nivel de inteligencia del héroe.
    print(f"  Niveles válidos: {', '.join(INTELIGENCIAS_VALIDAS)}")
    intel = input("  Inteligencia: ").strip().lower()
    if intel not in INTELIGENCIAS_VALIDAS:
        print("Nivel de inteligencia inválido. Intentá de nuevo.")
        return validar_inteligencia()              # recursión
    return intel

#  FUNCIONES DE BÚSQUEDA RECURSIVA

def buscar_maximo_recursivo(lista: list, indice_campo: int, indice_actual: int, indice_maximo: int) -> int:
    
    #Retorna el índice del héroe con el valor máximo en el campo dado
    #Función recursiva pura.
    
    if indice_actual == len(lista):
        return indice_maximo
    if lista[indice_actual][indice_campo] > lista[indice_maximo][indice_campo]:
        return buscar_maximo_recursivo(lista, indice_campo, indice_actual + 1, indice_actual)
    return buscar_maximo_recursivo(lista, indice_campo, indice_actual + 1, indice_maximo)


def buscar_minimo_recursivo(lista: list, indice_campo: int, indice_actual: int, indice_minimo: int) -> int:
    #Retorna el índice del héroe con el valor mínimo en el campo dado
    #Función recursiva pura
    if indice_actual == len(lista):
        return indice_minimo
    if lista[indice_actual][indice_campo] < lista[indice_minimo][indice_campo]:
        return buscar_minimo_recursivo(lista, indice_campo, indice_actual + 1, indice_actual)
    return buscar_minimo_recursivo(lista, indice_campo, indice_actual + 1, indice_minimo)


def buscar_heroe_por_nombre_recursivo(lista: list, nombre: str, indice: int) -> int:    
    #Busca un héroe por nombre (insensible a mayúsculas) de forma recursiva
    #Retorna el índice encontrado o -1 si no existe
    
    if indice == len(lista):
        return -1
    if lista[indice][INDICE_NOMBRE].lower() == nombre.lower():
        return indice
    return buscar_heroe_por_nombre_recursivo(lista, nombre, indice + 1)

#  ORDENAMIENTO BURBUJA

def ordenar_por_nombre_burbuja(lista: list) -> list:
    #Ordena la lista de héroes alfabéticamente por nombre
    #usando el algoritmo de burbuja 
    #Retorna una nueva lista ordenada para no modificar el original
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j][INDICE_NOMBRE].lower() > lista[j + 1][INDICE_NOMBRE].lower():
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

#  OPCIONES DEL MENÚ

def listar_heroes(lista: list):
    #Opción 1 — Lista todos los héroes.
    if len(lista) == 0:
        print("\n La lista de héroes está vacía.")
        return
    print(f"\n Total de héroes registrados: {len(lista)}\n")
    for heroe in lista:
        imprimir_heroe(heroe)


def agregar_heroe(lista: list):
    #Opción 2 — Agrega un nuevo héroe con validaciones.
    print("\n  ── Ingresá los datos del nuevo héroe ──\n")
    nombre     = validar_string_no_vacio("  Nombre      : ")
    identidad  = validar_string_no_vacio("  Identidad   : ")
    empresa    = validar_empresa()
    altura     = validar_numero_positivo("  Altura (cm) : ")
    peso       = validar_numero_positivo("  Peso (kg)   : ")
    genero     = validar_genero()
    color_ojos = validar_string_no_vacio("  Color ojos  : ")
    color_pelo = validar_string_no_vacio("  Color pelo  : ")
    fuerza     = int(validar_numero_positivo("  Fuerza (0-100): "))
    inteligencia = validar_inteligencia()

    nuevo_heroe = [nombre, identidad, empresa, altura, peso,
                   genero, color_ojos, color_pelo, fuerza, inteligencia]

    lista.append(nuevo_heroe)
    print(f"\n ¡{nombre} fue agregado correctamente!")


def eliminar_heroe(lista: list):
    #Opción 3 — Elimina un héroe por nombre.#
    if len(lista) == 0:
        print("\n La lista de héroes está vacía.")
        return

    nombre = input("\n  Ingresá el nombre del héroe a eliminar: ").strip()
    indice = buscar_heroe_por_nombre_recursivo(lista, nombre, 0)

    if indice == -1:
        print(f"\n No se encontró ningún héroe con el nombre '{nombre}'.")
    else:
        confirmacion = input(f"\n  ¿Confirmar eliminación de '{lista[indice][INDICE_NOMBRE]}'? (s/n): ").strip().lower()
        if confirmacion == "s":
            eliminado = lista.pop(indice)
            print(f"\n '{eliminado[INDICE_NOMBRE]}' fue eliminado de la lista.")
        else:
            print("  Operación cancelada.")


def ordenar_heroes(lista: list):
    #Opción 4 — Ordena la lista alfabéticamente por nombre.
    if len(lista) == 0:
        print("\n La lista de héroes está vacía.")
        return
    ordenar_por_nombre_burbuja(lista)
    print("\n Lista ordenada alfabéticamente (A → Z).")
    for heroe in lista:
        print(f"     • {heroe[INDICE_NOMBRE]}")


def ver_heroe_mas_alto(lista: list):
    #Opción 5 — Muestra el héroe con mayor altura.
    if len(lista) == 0:
        print("\n La lista de héroes está vacía.")
        return
    indice = buscar_maximo_recursivo(lista, INDICE_ALTURA, 1, 0)
    print(f"\n El héroe más alto es:\n")
    imprimir_heroe(lista[indice])


def ver_heroe_mas_fuerte(lista: list):
    #Opción 6 — Muestra el héroe con mayor fuerza.
    if len(lista) == 0:
        print("\n  La lista de héroes está vacía.")
        return
    indice = buscar_maximo_recursivo(lista, INDICE_FUERZA, 1, 0)
    print(f"\n El héroe más fuerte es:\n")
    imprimir_heroe(lista[indice])


def ver_heroe_menos_pesado(lista: list):
    #Opción 7 — Muestra el héroe con menor peso.
    if len(lista) == 0:
        print("\n La lista de héroes está vacía.")
        return
    indice = buscar_minimo_recursivo(lista, INDICE_PESO, 1, 0)
    print(f"\n El héroe menos pesado es:\n")
    imprimir_heroe(lista[indice])

#  FUNCIÓN PRINCIPAL — MENÚ

def menu_principal():
    #Punto de entrada de la aplicación. Gestiona el ciclo del menú.#
    heroes = lista_heroes   # lista importada de heroes.py

    continuar = True
    while continuar:
        imprimir_menu()
        opcion = input("  Elegí una opción: ").strip()

        if opcion == "1":
            listar_heroes(heroes)
        elif opcion == "2":
            agregar_heroe(heroes)
        elif opcion == "3":
            eliminar_heroe(heroes)
        elif opcion == "4":
            ordenar_heroes(heroes)
        elif opcion == "5":
            ver_heroe_mas_alto(heroes)
        elif opcion == "6":
            ver_heroe_mas_fuerte(heroes)
        elif opcion == "7":
            ver_heroe_menos_pesado(heroes)
        elif opcion == "0":
            print("\n Hasta la próxima.")
            continuar = False
        else:
            print("\nOpción inválida. Ingresá un número del 0 al 7.")

        if continuar:
            input("\n  Presioná Enter para continuar...")

#  PUNTO DE ENTRADA

if __name__ == "__main__":
    menu_principal()
