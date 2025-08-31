import os

class ControladorLibros:
    def __init__(self, archivo="libros.txt"):
        self.archivo = archivo
        if not os.path.exists(self.archivo):
            with open(self.archivo, "w") as f:
                pass

    def agregar_libro(self, titulo, autor):
        with open(self.archivo, "a") as f:
            f.write(f"{titulo},{autor}\n")

    def listar_libros(self):
        with open(self.archivo, "r") as f:
            lineas = f.readlines()
        if not lineas:
            print("No hay libros registrados.")
        else:
            for i, linea in enumerate(lineas, 1):
                titulo, autor = linea.strip().split(",")
                print(f"{i}. {titulo} - {autor}")


def menu():
    controlador = ControladorLibros()

    while True:
        print("\n===== MENÚ LIBRERÍA =====")
        print("1. Agregar libro")
        print("2. Listar libros")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            titulo = input("Título del libro: ")
            autor = input("Autor del libro: ")
            controlador.agregar_libro(titulo, autor)
            print("Libro agregado correctamente.")
        elif opcion == "2":
            controlador.listar_libros()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    menu()
