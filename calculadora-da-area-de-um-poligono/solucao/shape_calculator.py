class Rectangle:

  def __init__(self, width, height):
    """
      Inicializa o objeto Rectangle
      Inicialize the object Rectangle
    """
    self.width = width
    self.height = height

  # setters
  def set_width(self, new_width):
    """
      Seta a largura do retangulo
      Set rectangle width
    """
    self.width = new_width

  def set_height(self, new_heigth):
    """
      Seta a altura do retangulo
      set rectangle heigth
    """
    self.height = new_heigth

  # getters
  def get_area(self):
    """
      Retorna a area do retangulo
      (get rectangle area)
    """
    return (self.width * self.height)

  def get_perimeter(self):
    """
      Retorna o perimetro do retangulo
      (get rectangle perimeter)
    """
    return (2 * self.width + 2 * self.height)

  def get_diagonal(self):
    """
      Retorna o valor da diagonal do retangulo
      (get the diagonal rectangle)
    """
    return ((self.width**2 + self.height**2)**(0.5))

  def get_picture(self):
    """
      Retorna uma string que é a representação do retangulo
      Returns a string rectangle representation

      Se um dos lados for maior que 50, a função retorna 
      "Too big for picture."
      (If one side bigger than 50, the method returns) 
      "Too big for picture"
    """
    if self.height > 50 or self.width > 50:
      return "Too big for picture."

    picture = ""
    for h in range(self.height):
      picture += "*" * self.width + "\n"

    return picture

  def get_amount_inside(self, other_polygon):
    """
      Retorna quantas vezes 'other_polygon' cabe em self
      returns how many times 'other_polygon' fits in self  
    """
    self_area = self.get_area()
    area_polygon = other_polygon.get_area()
    # Retorna quantas vezes self.Rectangle é maior que other_polygon
    return int(self_area / area_polygon)

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):

  def __init__(self, side):
    """
      Inicializa o objeto Square
      (Inicialize the object Square)
    """
    self.side = side
    super().__init__(side, side)

  # Setters
  def set_side(self, new_side):
    """
      Seta o lado do quadrado 
      (set side of the square)
    """
    self.side = new_side
    super().set_height(new_side)
    super().set_width(new_side)

  def set_width(self, new_side):
    """
      Seta o lado do quadrado 
      (set side of the square)
    """
    self.side = new_side
    super().set_height(new_side)
    super().set_width(new_side)

  def set_heigth(self, new_side):
    """
      Seta o lado do quadrado 
      (set side of the square)
    """
    self.side = new_side
    super().set_height(new_side)
    super().set_width(new_side)

  def __str__(self):
    """
      Retorna a representação do objeto Square
      Return the representation of the object Square
    """
    return f"Square(side={self.side})"


# test
if __name__ == "__main__":
  sq = Square(4)
  rect = Rectangle(3, 6)
  print(rect.get_picture())
  rect.set_width(7)
  rect.set_height(3)
  print(rect.get_picture())

  sq.set_side(2)
  print(sq)
