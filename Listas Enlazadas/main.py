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

class lista_enlazada:
  def __init__(self):
    self.primero=None

  def insertar(self, estudiante):
    if self.primero is None:
        self.primero=nodo(estudiante=estudiante)
        return
    actual=self.primero
    while actual.siguiente:
      actual=actual.siguiente
    actual.siguiente=nodo(estudiante=estudiante)

  def recorrer(self):
    actual=self.primero
    while actual != None:
      print("carne:",actual.estudiante.carne,"nombre:",actual.estudiante.nombre,"email:",actual.estudiante.email,"->")
      actual=actual.siguiente
  
  def eliminar(self,carne):
    actual=self.primero
    anterior=None
    
    while actual and actual.estudiante.carne != carne:
      anterior=actual
      actual=actual.siguiente
    
    if anterior is None:
      self.primero=actual.siguiente
      actual.siguiente=None
    elif actual:
      anterior.siguiente=actual.siguiente
      actual.siguiente=None

  def buscar(self,carne):
    actual=self.primero

    while actual and actual.estudiante.carne !=carne and actual.siguiente:
      actual=actual.siguiente
    if actual.estudiante.carne is carne:
      print("encontrado")
      print("Carne:",actual.estudiante.carne)
      print("Nombre:",actual.estudiante.nombre)
      print("Edad:",actual.estudiante.edad)
      print("Dirección:",actual.estudiante.direccion)
      print("Telefono:",actual.estudiante.telefono)
      print("Email:",actual.estudiante.email)
      print("Carrera:",actual.estudiante.carrera)
      print("Puesto:",actual.estudiante.puesto)
    else:
      print("estudiante no encontrado")
    
    
e1=estudiante(202010245,"Paola Carias",20,"siquinala",54645138,"paola@gmail.com","ingenieria en sistemas","programador jr")
e2=estudiante(202010254,"Gerson Quiroa",20,"masagua",546454486,"gerson@gmail.com","ingenieria en sistemas","programador jr")
e3=estudiante(202010033,"Jose Rodolfo",20,"santa rosa",5467826486,"rodolfo@gmail.com","ingenieria en sistemas","programador jr")

lista_e=lista_enlazada()
lista_e.insertar(e1)
lista_e.insertar(e2)
lista_e.insertar(e3)

lista_e.recorrer()
lista_e.buscar(202010033)
lista_e.buscar(20201003)