# Reto 3
Elaborado por Ferney Vanegas Hernández

Proyecto Misión TIC 2022

# Ayúdela a Yepeto  a cumplir con los requerimientos del reto 
# WORLD CRAFT ASCII: 
### Contexto
El juego WorldCraft ASCII es muy popular y a diario varias personas desean registrarse para poder jugarlo y disfrutar de todo lo que ofrece

## Identificar el problema
### ¿Cuál es el problema/objetivo?
1. Realizar la veriﬁcación de un código ingresado por el usuario (CDIA) para evaluar la posibilidad de que pueda ingresar como nuevo jugador del WorldCraft ASCII
2. Una vez admitido al WorldCraft ASCII se le debe asignar un Mundo para iniciar a jugar

## Identificar los interesados
### ¿Quiénes son los interesados?
* Aspirantes a jugadores de WorldCraft ASCII 

## Definir el problema
### ¿Qué información conozco (que nos dan)?
* El aspirante debe proporcionar un código CDIA (código de identiﬁcación ASCII) para poder ingresar
* El CDIA es una cadena que debe cumplir con las siguientes restricciones:
    * Se debe veriﬁcar que el CDIA sea de tipo str exclusivamente y sin dígitos numéricos
    * El CDIA solo puede tener 10 caracteres de longitud
    * En la posición 6 de la cadena del CDIA debe ir siempre el carácter arroba (‘@’)
    * El carácter en la primera posición y el carácter en la última posición del CDIA deben ser diferentes.
    * El CDIA debe contener en cualquier posición de la cadena el carácter (‘+’)
    * El código CDIA no debe contener más de 3 veces la letra ’k’
    * El CDIA debe tener al menos uno de los siguientes símbolos (‘?’,’=’,’&’)
    * El CDIA no debe estar registrado por otro jugador
* Ya existe una función en un módulo para verificar que el CDIA no esté registrado con otro jugador
* El aspirante debe ser mayor de 12 años
* Cuando un nuevo jugador es admitido al WorldCraft ASCII se le debe asignar un Mundo para iniciar a jugar de acuerdo a las siguientes reglas:
    * Mundo 1: jugadores entre 12 y 20 años que no han jugado antes.
    * Mundo 2: jugadores entre 12 y 20 años que ya han jugado antes y su nivel actual es menor a 50.
    * Mundo 3: jugadores entre 12 y 20 años que ya han jugado antes y su nivel actual es mayor o igual a 50.
    * Mundo 4: jugadores mayores a 20 años que no han jugado antes
    * Mundo 5: jugadores mayores a 20 años que ya han jugado antes y su nivel actual es menor a 50.
    * Mundo 5: jugadores mayores a 20 años que ya han jugado antes y su nivel actual es mayor o igual a 50.

### ¿Qué información debo conocer (para lograr el objetivo)?
 * Se debe saber cómo calcular la edad de una persona
 * El funcionamiento de la Función proporcionada que valida que el CDIA no esté registrado
 * Investigar un poco de arrays
 * Investigar sobre de For y While (bucles)

## Dividir el problema en subproblemas
* Definir un módulo principal
* Importar módulos externos
* Solicitar CDIA
* Realizar validaciones para evaluar la inscripción del Jugador
    * Verificar que el CDIA sea str
    * Verificar quq el CDIA sea de 10 caracteres
    * Verificar que el sexto caracter del CDIA sea @
    * Verificar que en el primer y último caracter de la CDIA sean diferentes
    * Verificar la existencia del caracter + 
    * Verificar que en el CDIA no se repita más de 3 veces la letra k
    * Verificar que en CDIA esté al menos uno de: (‘?’,’=’,’&’)
* Realizar validaciones de existencia de CDIA
* Solicitar y Validar Fecha de Nacimiento
    * Calcular la edad del usuario según su fecha de nacimiento
* Solicitar Alias (minimo 5 caracteres sin espacios)
* Solicitar Experiencia en el juego
* Realizar validaciones para asignación a un mundo
    * Asignar mundo según la edad, la experiencia y el nivel

## Estrategia
### Ejemplos particulares
* No es string
    * CDIA = 1234
* No tiene arroba en el lugar correcto
    * Fer@ney
* Caracteres igüales al inicio y al final
    * Ferne@y+F
* Más de tres veces la k
    * Fkrnk@y+k_k
* CDIA correcto:
    * Luisfe@=g+
* 12/12/2014, No ha jugado antes => 8 años (No admitido)
* 02/08/1986, Ya ha jugado antes, nivel 10 => 36 años (Admitido a Mundo 5)
 
### Estrategia de solución
1. Solicitar el código CDIA
2. Validar reglas de construcción del CDIA
3. Validar existencia
4. Solicitar fecha de nacimiento
5. Validar fecha de nacimiento
6. Solicitar alias, experiencia y nivel
7. Si se infringe algo en la validación de reglas, existencia ó edad, reportar al usuario que no se puede continuar
8. Si todas las validaciones están bien, informar al usuario su proceso satisfactorio completo
# Requisitos de software

## Algoritmo:  age
### Parámetros: fecha_nacimiento
1. Funcion calc_age <- age(fecha_nacimiento:str)
2.    today = fecha_de_hoy
3.    age = today - fecha_nacimiento
4.    Devolver calc_age
5. FinFuncion

## Algoritmo: CDIA_UNICO
### Parámetros: CDIA
1.  Funcion existe <- cdia_unico (CDIA:str)
2.      CDIA = poner_en_mayusculas(CDIA)
3.      existe = False
4.      Dimension listaCDIA[N]
5.      Para i<-0 Hasta N-1 con Paso 1 Hacer
6.          Si listaCDIA[i] == CDIA
7.              existe = True
8.      FinPara
9.      Devolver existe
10. FinFuncion

## Algoritmo: EXISTEN_NUMEROS
### Parámetros: CDIA
* Funcion value <- existen_numeros(CDIA:str)
    * value = False
    * Para i<-0 hasta longitud(CDIA) - 1 con Paso 1 Hacer
        * Si CDIA[i] es_numero Entonces
            * value = True
        * FinSi
    * FinPara
    * Retornar value
* FinFuncion
 
## Algoritmo:  VALIDARCADENA
### Parámetros: CDIA
1.  Funcion valido <- validarCadena (CDIA:str)
2.      valido = False
3.      CDIA = convertir_mayuscula(CDIA)
4.      Si existen_numeros(CDIA) == False Entonces:
5.          Si CDIA.longitud == 10 Entonces:
6.              Si CDIA.sexto_carater == @ Entonces:
7.                  primer_caracter = CDIA.primer_caracter
8.                  ultimo_caracter = CDIA.ultimo_caracter
9.                  Si primer_caracter != ultimo_caracter Entonces:
10.                      Si CDIA tiene + Entonces:
11.                         num_K = CDIA.contar_K
12.                         Si num_K <=3 Entonces:
13.                             Si CDIA contine (‘?’,’=’,’&’) Entonces:
14.                                 valido = True
15.                             FinSi
16.                         FinSi
17.                    FinSi
18.                 FinSi
19.             FinSi
20.        FinSi
21.     FinSi
22.     Devolver valido
23. FinFuncion

## Algoritmo: ASIG_WORLD
### Parámetros: age, answer, level
* Funcion asig <- asig_world(age:int, answer:bool, level:int)
    * asig = ''
    * Si answer == True Entonces
        * Si age > 12 and age <= 20 and level < 50 Entonces
            * asig = 'Asignado a Mundo 2'
        * SiNo 
            * Si age > 12 and age <= 20 and level >= 50 Entonces
                * asig = 'Asignado a Mundo 3'
            * SiNo 
                * Si age > 20 and level < 50
                    * asig = 'Asignado a Mundo 5'
                * SiNo 
                    * Si age > 20 and level >= 50
                        * asig = 'Asignado a Mundo 5'
                        * /*Creo que hay un error en las copias, y en este caso debía ser asignado al Mundo 6. Pero hago lo que está en las copias*/
                    * FinSi
                * FinSi
            * FinSi
        * FinSi
    * SiNo
        * Si age > 12 and age <= 20 Entonces
            * asig = 'Asignado a Mundo 1'
        * SiNo
            * asig = 'Asignado a Mundo 4'
        * FinSi
    * FinSi
    * Devolver asig
* FinFuncion

## Algoritmo: FORMAT_AGE
### Parámetros: brithDay
* Funcion array[year, month, day] <- format_age(brithDay)
    * Si brithDay.Longitud == 10 and brithDay.Contiene('/') Entonces
        * day <- brithDay['day']
        * month <- brithDay['month']
        * year <- brithDay['year']
        * Si day es int and mont es int and year es int:
            * Si year > 1900 and 12 >= month > 0 and 31 >= day > 0 Entonces
                Retorne array[year, month, day]
            * SiNo
            *   Retorne False
            * FinSi
        * SiNo
            * Retorne False
        * FinSi
    * SiNo
        * Retorne False
    * FinSi
* FinFuncion

## Algoritmo: MAIN
### Sin Parámetros
* Algoritmo main
    * Escribir 'Por favor ingresa una CDIA'
    * Leer CDIA
    * Si cdia_validar(CDIA) == True Entonces
        * Si cdia_unico(CDIA) == True Entonces
            * fecha_correcta = False
            * Mientras fecha_correcta == False Hacer:
                * Escribir 'Por favor ingresa tu fecha de nacimiento en el formato * DD/MM/AAAA'
                * Leer fecha_nacimiento
                * Si formatearFecha(fecha_nacimiento) != False
                    * age = calcularEdad(fecha_nacimiento)
                    * fecha_correcta = True
                * FinSi
            * FinMientras
            * Si age(fecha_nacimiento) => 12 Entonces
                * Escribir 'Escribe un Alias':
                * Leer alias
                * Mientras alias.longitud < 5 or alias.sinEspacios Hacer
                    * Escribir 'El alias debe tener más de 5 caracteres y no debe tener espacios. Intenta otra vez...'
                    * Leer alias
                * FinMientras
                * Escribir 'Ya antes has jugado WorldCraft ASCII? 1=Sí ó 2=Nop'
                * Leer answer
                * Mientras answer != 1 and answer !=2 Hacer
                    * Escribe 'Escoge una opción válida! 1=Sí ó 2=Nop'
                    * Leer answer
                * Si answer == Si Entonces
                    * answer = True
                    * Escribir 'Hasta qué nivel llegaste?'
                    * Leer level
                    * Mientras level <= 0 or level >100 Hacer
                        * Escriba 'Especifica un level existente en el juego...'
                        * Leer level
                    * FinMientras
                    * Si age >= 16 Entonces
                        * level = level + 2
                        * Si level > 100 Entonces
                            * level = 100
                        * FinSi
                    * FinSi
                * SiNo
                    * answer = False
                    * Si age < 16 Entonces
                        * level = 2
                    * SiNo
                        * level = 1
                    * FinSi
                * FinSi
                * asig_world = world(age, answer, level)
                * Escribir 'Bienvenido a WorldCraft ASCII! asig_world'
            * SiNo:
                * Escriba 'No tienes edad suficiente'
            * FinSi
        * SiNo
            * Escriba 'CDIA ya existe!'
        * FinSi
    * SiNo
        * Escriba 'CDIA Inválido'
    * FinSi
* FinAlgoritmo

# Logros
Implementar los algoritmos en Python