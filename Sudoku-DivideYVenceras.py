import time  # Importa el módulo para medir el tiempo

sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def imprimirSudoku(su): #Define una función que recibe el tablero (su)
    for i in range(len(su)): #Recorre las filas del tablero.
        if i % 3 == 0: #Cada 3 filas, imprime una línea horizontal para separar las subcuadrículas.
            print("- - - - - - - - - - - - - - -")
        for j in range(len(su[0])):#Recorre las columnas de la fila actual.
            if j % 3 == 0: #cada 3 columnas, imprime un borde vertical (|) para separar las subcuadrículas.
                print(" | ", end="")
            if j == 8: #Si estamos en la última columna, imprime el número seguido de un borde vertical (|).
                print(str(su[i][j]) + " | ")
            else:
                print(str(su[i][j]) + " ", end="")
    print("- - - - - - - - - - - - - - -")

def encontrarVacio(su): #Define una función para encontrar la primera celda vacía del tablero.
    """Encuentra la primera celda vacía en el tablero."""
    for i in range(len(su)):
        for j in range(len(su[0])):
            if su[i][j] == 0: #Si encuentra una celda vacía (valor 0), retorna su posición como una tupla (i, j).
                return (i, j)
    return False #Si no hay celdas vacías, retorna False.

def esValido(su, num, pos): #Define una función para verificar si el número num es válido en la posición pos.
    """Comprueba si 'num' es válido en la posición 'pos'."""
    # Revisar fila
    for i in range(len(su[0])):
        if su[pos[0]][i] == num and pos[1] != i: #Si el número ya existe en la fila (excepto en la columna actual), retorna False.
            return False
    # Revisar columna
    for i in range(len(su)):
        if su[i][pos[1]] == num and pos[0] != i: #Si el número ya existe en la columna (excepto en la fila actual), retorna False.
            return False
    # Revisar subcuadrícula
    cajaX = pos[1] // 3 #Calcula la columna inicial de la subcuadrícula.
    cajaY = pos[0] // 3 #Calcula la fila inicial de la subcuadrícula.
    for i in range(cajaY * 3, cajaY * 3 + 3): #Recorre las filas de la subcuadrícula.
        for j in range(cajaX * 3, cajaX * 3 + 3): #Recorre las columnas de la subcuadrícula.
            if su[i][j] == num and (i, j) != pos: #Si el número ya existe en la subcuadrícula, retorna False.
                return False
    return True #Si ninguna restricción falla, el número es válido.

def resolverPorRegion(su, regiones):
    """Resuelve el Sudoku dividiéndolo en regiones."""
    if not regiones: #Si no quedan regiones por resolver, retorna True.
        return True  # Caso base: todas las regiones están completas
    
    # Trabajar en la primera región
    region = regiones[0] #Toma la primera región para resolver.
    for i in range(1, 10): #Prueba números del 1 al 9.
        if esValido(su, i, region): #Verifica si el número es válido en la región actual.
            fila, col = region
            su[fila][col] = i #Coloca el número en la celda.
            if resolverPorRegion(su, regiones[1:]): #Llama recursivamente para resolver el resto del tablero.                                       
                return True
            su[fila][col] = 0  #Si falla, retrocede y elimina el número
    
    return False

def resolverSudoku(su):
    """Divide el problema por regiones (celdas vacías) y aplica recursividad."""
    #crea una lista llamada celdas_vacias que contiene las posiciones de todas las celdas vacías del tablero.
    celdas_vacias = [(i, j) for i in range(len(su)) for j in range(len(su[0])) if su[i][j] == 0] #Verifica si la celda en la posición (i, j) está vacía (tiene un valor 0).Si es así, añade la posición (i, j) a la lista
    return resolverPorRegion(su, celdas_vacias) #Llama a la función resolverPorRegion, que es la encargada de resolver el Sudoku aplicando el paradigma de divide y vencerás.

# Medir tiempo de ejecución
start_time = time.time()  # Registra el tiempo de inicio

# Ejecución
print("\nTablero inicial:")
imprimirSudoku(sudoku)

if resolverSudoku(sudoku):
    print("\nSudoku resuelto:")
else:
    print("\nNo se encontró solución.")

imprimirSudoku(sudoku)

end_time = time.time()  # Registra el tiempo de finalización

# Calcular y mostrar el tiempo de ejecución
execution_time = end_time - start_time
print(f"\nTiempo de ejecución: {execution_time:.6f} segundos")
