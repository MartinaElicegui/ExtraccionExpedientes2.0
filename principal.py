import sys
from funciones import *
from easygui import *

def main():
    driver = generarDriver()
    loguearProfesional(driver)
    # La función buscarExpediente llama a: leerCUIJ(), cargarCUIJ(driver, cuijs) y navegar(driver)
    # A su vez, cuando entra en la función cargarCUIJ(driver, cuijs) llama a extraerInformación(driver)
    # Dentro de la función navegar(driver) llama a extraerSegundoAdjunto(driver) (SÓLO SI EL ARCHIVO EXISTE)
    buscarExpediente(driver)
    #formatearResultado(driver)
    
if __name__ == "__main__":
    sys.exit(main())


