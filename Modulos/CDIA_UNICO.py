def CDIA_UNICO(CDIA):
  listaCDIA={"Luisfe@=g+","Lui?fe@=g+","Luikf&@=g+"}
  for n in listaCDIA:
    if n.upper() == CDIA.upper():
      return True
  return False
