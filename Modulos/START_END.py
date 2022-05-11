'''
    Las funciones de este módulo no tienen algoritmo en metodoideal.md
    La razón es poque fueron hechas solo para darle un estilo al programa
    Fueron creadas una vez el programa funcionaba y cumplía con lo requerido
'''

def start():
    print(
        '********************************************\n'
        '       _   _      _    _  _   _   _ _ _  \n'
        '|   | | | | / |  | \\  |  | / |_| |_  |  \n'
        '|_|_| |_| | \\ |_ |_/  |_ | \\ | | |   |  \n'
        '                                      ASCII\n'
        '********************************************\n'
        '   Developed by: Ferney Vanegas Hernández\n'
        '   MinTic 2022\n'
        '********************************************\n'
    )

def bad_end(msn):
    '''
    Parameters:
    -----------
    msn: str
        Mensaje de error
    '''
    print(
        '\n'
        '********************************************\n'
        'Programa terminado\n'
        f'** {msn} **\n'
        'GRACIAS POR JUGAR WORLDCRAFT ASCII!\n'
        '********************************************\n'
    )

def good_end(alias, asig_world):
    '''
    Parameters:
    ----------
    alias: str
        El alias ingresado por el usuario
    asig_world: str
        La frase se asignación al Mundo y Nivel
    '''
    print(
        '_______________________________________\n'
        f'{alias}:'
        f'Bienvenido a WorldCraft ASCII!\n'
        f'{asig_world}\n'
        '_______________________________________\n'
    )