import Modulos.CDIA_UNICO as unico
import Modulos.age as edad
import Modulos.CDIA_VALIDAR as validar
import Modulos.WORLD as world
import Modulos.START_END as start_end
from datetime import date 

''' 
    Códigos para hacer pruebas:
    Correcto
        Lukkke@=g+
    Incorrectos
        (Existente)
            Luisfe@=g+
        (4K)
            Lukkkk@=g+
        (@ fuera de posición)
            Lukkk@e=g+
        (9 caracteres)
            Lukkke@=g
        (1er y Último caracteres igüales)
            +ukkke@=g+
        (Sin +)
            Lukkke@=g-
        (Sin ‘?’,’=’,’&’)
            Lukkke@g+
        (Con números)
            Luk1ke@=g+
    
    Notas al profesor: 
        1) Utilizo while (sí, sé que es avanzado pero lo investigué) para controlar lo que el usuario ingresa
        2) Investigué isdigit. Valida si en un string hay dígitos
        3) Para print uso print(f'texto {variables}') con el fin de que sea más legible el código
        4) Uso arrays (lo investigué) para formatear la fecha ingresada por el usuario
        5) Utilizo for para recorrer el CDIA y evaluar cada caracter y ver si hay un número
        
        Por tanto: Uso temas que aún no se han visto, pero es porque los investigué para cumplir con lo requerido
'''
start_end.start()
# Solicitud del CDIA al usuario
CDIA = input('Ingresa un CDIA\n') # Uso \n para hacer saltos de línea
# Validación de los requisistos del CDIA ingresado
if validar.validarCadena(CDIA):
    # Validacioń de la no existencia del CDIA ingresado
    if unico.CDIA_UNICO(CDIA) == False:
        correct_birthDate = False # Será falso a menos que ingresen un formato correcto de fecha
        while correct_birthDate == False:
            birthDate = input('Por favor ingresa tu fecha de nacimiento(Ej: 02/08/1986)\n')
            birthDate = edad.format_age(birthDate)
            if birthDate != False:
                # Cambio del valor correct_birthDate para salir del while
                correct_birthDate = not correct_birthDate
        # Se entregan los parámetros correctos a calculteAge, para obtener la edad
        age = edad.calculateAge(date(birthDate[0],birthDate[1],birthDate[2]))
        # Verificacioń: Edad
        if age > 12:
            # Se requerirá un Alias de al menos 5 dígitos. Para no acabar el programa, se solicitará hasta que el usurio ingrese un valor válido
            # ==================================
            alias = input('Escribe un Alias (Mínimo 5 dígitos)\n')
            while len(alias) < 5 or alias.count(' ') > 0:
                alias = input('Escribe un Alias (Mínimo 5 dígitos)\n')
            # ==================================

            # Se pregunta al usuario sobre su experiencia en el juego. Para no acabar el programa, se solicitará hasta que el usurio ingrese un valor válido
            # ==================================
            answer = int(input('Ya antes has jugado WorldCraft ASCII? 1=Sí ó 2=No\n'))
            while answer != 1 and answer!=2:
                answer = int(input('Ingresaste opción inválida. Ya antes has jugado WorldCraft ASCII? 1=Sí ó 2=No\n'))
            # ==================================

            # Validación experiencia del usuario
            # Se actualiza el valor de answer según respuesta numérica y se solicita ó asigna un level
            if answer == 1:
                answer = True
                level = int(input('Hasta qué nivel llegaste?(0 - 100)\n'))
                while level <= 0 or level >100:
                    level = int(input('Nivel incorrecto! Hasta qué nivel llegaste?(0 - 100)\n'))
                if age > 16:
                    level = level + 2
                    # Como solo hay 100 niveles, se hace validación de ello
                    if level > 100:
                        level = 100
            else:
                answer = False
                if age > 16:
                    level = 2
                else:
                    level = 1
            # Se llama a la función asig_word para obtener el mundo al que será asignado, entregándole los parámetros requeridos
            asig_world = world.asig_world(age, answer, level)
            start_end.good_end(alias, asig_world)
        else:
            msn = 'No tienes edad suficiente'
            start_end.bad_end(msn)
    else:
        msn = 'CDIA ya existe!'
        start_end.bad_end(msn)
else:
    msn = 'CDIA Inválido' 
    start_end.bad_end(msn)