from entities.name import Name
from entities.phone import Phone
from entities.birthday import Birthday
from validations.validations import PhoneSizeException

class Record():
  def __init__(self, name):
    self.name = Name(name)
    self.phones = []
    self.birthday = None

  def __str__(self):
    return str({'name': self.name.value, 'birthday': self.birthday.value if self.birthday else None, 'phones': self.get_phones()})

  def add_phone(self, new_phone):
    try:
      self.phones.append(Phone(new_phone))
      return f"{new_phone} has been successfully added"
    except PhoneSizeException as e:
      return 

  def add_birthday(self, birthdate):
    try:
      self.birthday = (Birthday(birthdate))
      return f"Birthday added successfully - {birthdate}"
    except Exception:
      return print(f"wrong birthdate format") 

  def remove_phone(self, phone):
    phone_to_remove = self.find_phone(phone)

    if phone_to_remove:
      self.phones.remove(phone_to_remove)
      return f"{phone_to_remove} has been successfully removed."
    else:
      return f"{phone} has not been found."
  
  def edit_phone(self, phone, new_phone):
    found_phone = self.find_phone(phone)

    if found_phone:
      phone_index = self.phones.index(found_phone)
      self.phones[phone_index] = Phone(new_phone)
      return f"{new_phone} has been successfully added to contact {self.name.value}"
    else:
      return f"{phone}not founded in {self.name.value} contact list!"

  def edit_name(self, new_name):
    prev_name = self.name
    self.name = Name(new_name)
    return f"{prev_name.value} successfully changed to {new_name}"
  
  def find_phone(self, phone):
    found_phone = next(p for p in self.phones if p.value == phone)
    if found_phone:
      return found_phone
    else:
      return f"{phone} has not been found."
  
  def get_phones(self):
    return [p.value for p in self.phones]
