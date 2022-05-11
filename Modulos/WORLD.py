def asig_world(age=None, answer=None, level=None):
    '''
      Parameters:
      ----------
      age: int
         La edad del usuario
      answer: bool
        La respuesta del usuario sobre si ha jugado ó no antes
      level: int
        El nivel evaluado del usuario  
      ----------
      Return
      ----------
      asig: str
         La asignación del Mundo después de evaluar los parámetros
   '''
    asig = ''
    if answer:
        if age > 12 and age <= 20 and level < 50:
            asig = f'Asignado a Mundo 2. Nivel: {level}'
        elif age > 12 and age <= 20 and level >= 50:
            asig = f'Asignado a Mundo 3. Nivel: {level}'
        elif age > 20 and level < 50:
            asig = f'Asignado a Mundo 5. Nivel: {level}'
        elif age > 20 and level >= 50:
            '''
                Creo que hay un error en las copias, y 
                en este caso debía ser asignado al Mundo
                6. Pero hago lo que está en las copias
            '''
            asig = f'Asignado a Mundo 5. Nivel: {level}'     
    else:
        if age > 12 and age <= 20:
            asig = f'Asignado a Mundo 1. Nivel: {level}'
        else:
            asig = f'Asignado a Mundo 4. Nivel: {level}'
    return asig