class estudiante:
  def __init__(self,carne,nombre,edad,direccion,telefono,email,carrera,puesto):
    self.carne=carne
    self.nombre=nombre
    self.edad=edad
    self.direccion=direccion
    self.telefono=telefono
    self.email=email
    self.carrera=carrera
    self.puesto=puesto

class nodo:
  def __init__(self,estudiante=None,siguiente=None,anterior=None):
    self.estudiante=estudiante
    self.siguiente=siguiente
    self.anterior=anterior

class lista_doble:
  def __init__(self):
    self.primero=None

  def insertar(self,estudiante):
    if self.primero is None:
      self.primero=nodo(estudiante=estudiante)

    else:
      actual=nodo(estudiante=estudiante,siguiente=self.primero)
      self.primero.anterior=actual
      self.primero=actual

  def recorrer(self):
    if self.primero is None:
      return
    actual=self.primero
    print("Carne:",actual.estudiante.carne,"nombre:",actual.estudiante.nombre,"email:",actual.estudiante.email,"->")
    while actual.siguiente !=None:
      actual=actual.siguiente
      print("Carne:",actual.estudiante.carne,"nombre:",actual.estudiante.nombre,"email:",actual.estudiante.email,"->")

  def eliminar(self, carne):
    actual=self.primero
    while actual:
      if actual.estudiante.carne==carne:
        if actual.anterior:
          if actual.siguiente:
            actual.anterior.siguiente=actual.siguiente
            actual.siguiente.anterior=actual.anterior
          else:
            actual.anterior.siguiente=None
            actual.anterior=None
        else:
          if actual.siguiente:
            self.primero=actual.siguiente
            actual.siguiente.anterior=None
          else:
            self.primero=None
        return True
      else:
        actual=actual.siguiente
    return False

  def buscar(self,carne):
    actual=self.primero
    while actual.siguiente:
        if actual.estudiante.carne==carne:
            print("Carne:",actual.estudiante.carne,"nombre:",actual.estudiante.nombre,"email:",actual.estudiante.email,"->")
            return
        actual=actual.siguiente
    if actual.estudiante.carne is carne:
        print("Carne:",actual.estudiante.carne,"nombre:",actual.estudiante.nombre,"email:",actual.estudiante.email,"->")
        return
    print("Estudiante no encontrado")
    

e1=estudiante(202010245,"Paola Carias",20,"siquinala",54645138,"paola@gmail.com","ingenieria en sistemas","programador jr")
e2=estudiante(202010254,"Gerson Quiroa",20,"masagua",546454486,"gerson@gmail.com","ingenieria en sistemas","programador jr")
e3=estudiante(202010033,"Jose Rodolfo",20,"santa rosa",5467826486,"rodolfo@gmail.com","ingenieria en sistemas","programador jr") 

lista_d=lista_doble()
lista_d.insertar(e1)
lista_d.insertar(e2)
lista_d.insertar(e3)

lista_d.recorrer()

# lista_d.eliminar(202010033)
# lista_d.eliminar(202010254)
# lista_d.eliminar(202010245)

lista_d.buscar(20210245)