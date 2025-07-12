from entities.field import Field
from validations.validations import PhoneSizeException

class Phone(Field):
  def __init__(self, value):
    if len(value) == 10: 
      self.value = value
    else:
      raise PhoneSizeException
