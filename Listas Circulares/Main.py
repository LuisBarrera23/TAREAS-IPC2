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
  def __init__(self,estudiante=None,siguiente=None):
    self.estudiante=estudiante
    self.siguiente=siguiente

class lista_circular:
  def __init__(self):
    self.primero=None

  def insertar(self,estudiante):
    if self.primero is None:
      self.primero=nodo(estudiante=estudiante)
      self.primero.siguiente=self.primero
    else:
      actual=nodo(estudiante=estudiante,siguiente=self.primero.siguiente)
      self.primero.siguiente=actual

  def recorrer(self):
    if self.primero is None:
      return
    actual=self.primero
    print("Carne:",actual.estudiante.carne,"nombre:",actual.estudiante.nombre,"email:",actual.estudiante.email,"->")
    while actual.siguiente != self.primero:
      actual=actual.siguiente
      print("Carne:",actual.estudiante.carne,"nombre:",actual.estudiante.nombre,"email:",actual.estudiante.email,"->")

  def eliminar(self, carne):
    actual=self.primero
    anterior=None
    no_encontrado=False

    while actual and actual.estudiante.carne !=carne:
      anterior=actual
      actual=actual.siguiente
      if actual==self.primero:
        no_encontrado=True
        break

    if not no_encontrado:
      if anterior is not None:
        anterior.siguiente=actual.siguiente
      else:
        while actual.siguiente != self.primero:
          actual=actual.siguiente
        actual.siguiente=self.primero.siguiente
        self.primero=self.primero.siguiente

e1=estudiante(202010245,"Paola Carias",20,"siquinala",54645138,"paola@gmail.com","ingenieria en sistemas","programador jr")
e2=estudiante(202010254,"Gerson Quiroa",20,"masagua",546454486,"gerson@gmail.com","ingenieria en sistemas","programador jr")
e3=estudiante(202010033,"Jose Rodolfo",20,"santa rosa",5467826486,"rodolfo@gmail.com","ingenieria en sistemas","programador jr") 

lista_c=lista_circular()
lista_c.insertar(e1)
lista_c.insertar(e2)
lista_c.insertar(e3)

lista_c.recorrer()

lista_c.eliminar(202010245)
lista_c.recorrer()