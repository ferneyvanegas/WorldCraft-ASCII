from datetime import date 
  
def calculateAge(birthDate): 
    today = date.today() 
    age = today.year - birthDate.year -((today.month, 
    today.day) < (birthDate.month, birthDate.day)) 
    return age 

# Función que recibe la edad en un formato, evalua si es correcto el formato y los valores, y entrega un array con año, mes y día
def format_age(birthDate):
    '''
        Parameters:
        ----------
        birthDate: str
            La fecha de nacimiento del usuario. En forma correcta debe venir con el formato DD/MM/AAAAA
        ----------
        Return:
        ----------
        array
            year: int
                El año de nacimiento del usuario
            month: int  
                El mes
            day: int
                El día
        False
            Si el formato de la fecha no es válido, ó los valores no están en el rango ó no son correctos
    '''
    # Verificar si la fecha tiene 10 caracteres y hay dos / dividiendo el día, el mes y el año
    if len(birthDate) == 10 and birthDate[2] == '/' and birthDate[5] == '/':
        # Extraer día, mes y año
        # =======================
        day = birthDate[0:2]
        month = birthDate[3:5]
        year = birthDate[6:]
        # =======================
        # Solo si son dígitos, se procede a aceptar la fecha ingresada
        if day.isdigit() and month.isdigit() and year.isdigit():
            day = int(day)
            month = int(month)
            year = int(year)
            # Evaluación de valores
            '''
                Existe una función con datetime llamada strptime, que me
                permitiría evaluar de hecho si la fecha en realidad existe. 
                Sin embargo, retorna una excepción, y creo que es un tema 
                algo avanzado.
                De modo que solo daré unos rangos a year, month y day para 
                que no se pasen de allí los usuarios
            '''
            if year > 1900 and 12 >= month > 0 and 31 >= day > 0:
                return [year, month, day]
            else:
                return False
        else:
            return False
    else:
        return False