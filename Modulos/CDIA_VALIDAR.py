# Función que busca dígitos en un String
def exist_numbers(CDIA):
      '''
      Parameters:
      ----------
      CDIA: str
         Código del usuario
      ----------
      Return
      value: bool
         True si hay dígitos. False si no.
      '''
      value = False
      for i in CDIA:
         if i.isdigit():
            value = True
      return value

def validarCadena(CDIA):
   '''
      Parameters:
      ----------
      CDIA: str
         El código CDIA ingresado por el usuario
      ----------
      Return
      ----------
      valido: bool
         La evalucacion sobre si el CDIA evaluado es aceptado ó no
   '''
   # Valor inicial de valido es False. Solo cambia si se cumplen todos los requisitos
   valido = False 
   # Conversión a mayúsculas
   CDIA=CDIA.upper() 
   # ==========================================
   # INICIO DE VALIDACIONES
   # ==========================================
   # Validación si solo son letras y no hay números
   if exist_numbers(CDIA) == False:
      # Validacioń: la longitud es 10
      if len(CDIA)==10:
         # Validación: el sexto caracter @
         if CDIA.find("@")==6:
            # Se extrae el primer caracter de la cadena CDIA
            primer_caracter = CDIA[0]
            # El último caracter de la cadena CDIA está en la posición: longitud del strig - 1
            ultimo_caracter = CDIA[len(CDIA) - 1]
            # Validacion: no pueden ser iguales el primer y último caracter
            if primer_caracter != ultimo_caracter:
               # Validación: existe al menos 1 +
               if CDIA.count("+") > 0:
                  # Validacioń: máximo 3 veces k (En mayúscula)
                  if CDIA.count("K") <= 3:
                     # Validación: al menos 1 de los caracteres ?, = , &
                     if CDIA.count("?") > 0 or CDIA.count("=") > 0 or CDIA.count("&") > 0:
                        valido = True
   # ==========================================
   return  valido