import string

matriz_adyacencia = []


def crear_grafo():
    global matriz_adyacencia

    matriz_adyacencia = []  # Reinicializar la lista matriz_adyacencia

    confirmacion = input("Crear un nuevo grafo borrará el anterior. ¿Estás seguro de continuar? (y/n): ")

    if confirmacion.lower() == "y":
        # Lógica para crear un grafo
        n = int(input("Ingrese el número de nodos: "))

        for _ in range(n):
            fila = []
            for _ in range(n):
                valor = input("Ingrese el valor (0 o 1) para la matriz de adyacencia: ")
                while valor != "0" and valor != "1":
                    print("Valor inválido. Por favor, ingrese 0 o 1.")
                    valor = input("Ingrese el valor (0 o 1) para la matriz de adyacencia: ")
                fila.append(int(valor))
            matriz_adyacencia.append(fila)

        print("¡Grafo creado!")

    elif confirmacion.lower() == "n":
        print("Creación de grafo cancelada.")
    else:
        print("Opción inválida. Por favor, selecciona 'y' para continuar o 'n' para cancelar.")


def visualizar_grafo():
    # Lógica para visualizar el grafo
    if len(matriz_adyacencia) == 0:
        print("No hay ningún grafo creado aun...")
    else:
        print("Visualizando el grafo...")
        print("Matriz de adyacencia:")
        for fila in matriz_adyacencia:
            print(fila)


def agregar_nodo():
    # Logica para agregar un nodo
    global matriz_adyacencia

    if len(matriz_adyacencia) == 0:
        print("No hay ningún grafo creado aún. Primero crea un grafo.")
        return

    n = len(matriz_adyacencia)  # Obtener el número de nodos en el grafo

    if n == 0:
        print("El grafo no tiene nodos. Agrega nodos al grafo primero.")
        return

    nueva_fila = []
    nueva_columna = []

    for i in range(n):
        conexion_fila = input(f"Ingrese 1 si hay conexión entre el nuevo nodo y {string.ascii_uppercase[i]} (fila), o 0 si no hay conexión: ")
        conexion_columna = input(f"Ingrese 1 si {string.ascii_uppercase[i]} tiene conexión con el nuevo nodo (columna), o 0 si no hay conexión: ")

        # Validar que la conexión ingresada sea 0 o 1
        if conexion_fila != "0" and conexion_fila != "1":
            print(f"El valor de conexión ingresado para la fila {string.ascii_uppercase[i]} no es válido. Se asumirá que no hay conexión.")
            conexion_fila = "0"

        if conexion_columna != "0" and conexion_columna != "1":
            print(f"El valor de conexión ingresado para la columna {string.ascii_uppercase[i]} no es válido. Se asumirá que no hay conexión.")
            conexion_columna = "0"

        nueva_fila.append(int(conexion_columna))
        nueva_columna.append(int(conexion_fila))

    nueva_fila.append(0)  # Agregar conexión del nuevo nodo consigo mismo en la fila

    for i in range(n):
        matriz_adyacencia[i].append(nueva_fila[i])  # Agregar nueva fila a cada columna existente

    nueva_columna.append(0)  # Agregar conexión del nuevo nodo consigo mismo en la columna
    matriz_adyacencia.append(nueva_columna)  # Agregar nueva columna como última fila

    print("Nodo agregado correctamente y conexiones actualizadas.")


def buscar_camino():
    # Logica para buscar el camino entre dos puntos
    global matriz_adyacencia

    if len(matriz_adyacencia) == 0:
        print("No hay ningún grafo creado aún. Primero crea un grafo.")
        return

    n = len(matriz_adyacencia)  # Obtener el número de nodos en el grafo

    if n == 0:
        print("El grafo no tiene nodos. Agrega nodos al grafo primero.")
        return

    print("------------!!!ATENCION!!!------------")
    print("")
    print("Aqui vas a ingresar los dos puntos para buscar el camino entre ellos...")
    print("")
    print("Cuando vayas a ingresar un punto, solo se admitira letras en orden alfabetico escritas en mayusculas, (A,B,C,D,E,F,G,H.....)")
    print("")
    print("Y como sabes que letra poner?")
    print("")
    print("La matriz estara organizada de forma alfabetica, entonces segun la posicion como lo tomes, supongamos:")
    print("Si tomas la posicion 0 en la matriz esta sera A, si es la posicion 1 sera B, asi con el resto....")
    print("Puedes pedir visualizar el grafo para que tengas una vista de cuales letras estarian supuestamente para que el sistema no falle porque tienes letras que no existen")
    print("")

    origen = input("Ingrese el nodo de origen: ")
    destino = input("Ingrese el nodo de destino: ")

    # Validar que los nodos ingresados sean válidos
    if not origen.isalpha() or origen.islower() or not destino.isalpha() or destino.islower():
        print("Los nodos ingresados no son válidos. Ingrese letras mayúsculas válidas.")
        return

    # Convertir nodos a índices en la matriz
    origen_index = ord(origen) - ord('A')
    destino_index = ord(destino) - ord('A')

    # Validar que los índices estén dentro del rango válido
    if origen_index < 0 or origen_index >= n or destino_index < 0 or destino_index >= n:
        print("Los nodos ingresados están fuera del rango válido.")
        return

    # Realizar búsqueda en profundidad (DFS) para encontrar los caminos entre origen y destino
    visitados = [False] * n  # Lista para rastrear los nodos visitados
    camino = []  # Lista para almacenar el camino actual
    caminos_encontrados = []  # Lista para almacenar todos los caminos encontrados

    # Función auxiliar de DFS
    def dfs(nodo_actual):
        visitados[nodo_actual] = True  # Marcar el nodo actual como visitado
        camino.append(chr(nodo_actual + ord('A')))  # Agregar el nodo actual al camino

        # Verificar si se ha alcanzado el nodo de destino
        if nodo_actual == destino_index:
            caminos_encontrados.append(" -> ".join(camino))  # Agregar el camino encontrado a la lista

        # Recorrer los nodos adyacentes no visitados
        for i in range(n):
            if matriz_adyacencia[nodo_actual][i] == 1 and not visitados[i]:
                dfs(i)  # Llamada recursiva a DFS para el nodo adyacente

        # Retroceder: eliminar el nodo actual del camino y marcarlo como no visitado
        camino.pop()
        visitados[nodo_actual] = False

    # Iniciar la búsqueda en profundidad (DFS) desde el nodo de origen
    dfs(origen_index)

    # Mostrar los caminos encontrados
    if len(caminos_encontrados) > 0:
        print(f"Camino(s) encontrado(s) entre {origen} y {destino}:")
        for i, camino in enumerate(caminos_encontrados):
            print(f"{i+1}. {camino}")
    else:
        print(f"No hay un camino entre el nodo {origen} y el nodo {destino}.")


while True:
    print("¡Bienvenido al menú de grafos!")
    print("Opciones:")
    print("1. Crear grafo")
    print("2. Visualizar grafo")
    print("3. Agregar nodo al grafo")
    print("4. Buscar camino de un nodo A a un nodo B")
    print("0. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        crear_grafo()
    elif opcion == "2":
        visualizar_grafo()
    elif opcion == "3":
        agregar_nodo()
    elif opcion == "4":
        buscar_camino()
    elif opcion == "0":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
