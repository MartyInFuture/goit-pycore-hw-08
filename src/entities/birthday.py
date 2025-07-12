from entities.field import Field
from datetime import datetime

BASE_FORMAT = '%d.%m.%Y'

class Birthday(Field):
  def __init__(self, value):
    try:
        datetime.strptime(value, BASE_FORMAT)
        self.value = value
    except ValueError:
        self.value = None
        raise ValueError("Invalid date or date format. Use DD.MM.YYYY")
  
  @staticmethod
  def should_congratulate_soon(contact):
    if not contact.birthday or not contact.birthday.value:
      return False

    try:
      today = datetime.today().date()
      birthdate = datetime.strptime(contact.birthday.value, BASE_FORMAT).date()
      birthdate_this_year = birthdate.replace(year=today.year)
      delta_days = (birthdate_this_year - today).days
      return 0 <= delta_days <= 7
    except Exception:
        return False

        

