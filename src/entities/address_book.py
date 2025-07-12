from collections import UserDict
from entities.record import Record
from entities.birthday import Birthday
from validations.validations import required_args

class AddressBook(UserDict):

  @required_args(2, 3)
  def add_contact(self, name, phone, birthday = None):
    if(self.find(name)):
      return f"Contact with name {name} is already exists!"
    else:
      return self.create_contact(name, phone, birthday)

  @required_args(3)
  def change_phone(self, name, phone, new_phone):
    found_contact = self.find(name)
    if found_contact:
      return found_contact.edit_phone(phone, new_phone)
    else:
      return f"User with name {name} not found!"
    
  @required_args(2)
  def change_contact_name(self, name, new_name):
    found_contact = self.find(name)
    if found_contact:
      return found_contact.edit_name( new_name)
    else:
      return f"User with name {name} not found"

  @required_args(1)
  def get_contact_phone_list(self, name):
    found_contact = self.find(name)
    if found_contact:
      return found_contact.get_phones()
    else:
      return f"Contact with name {name} has not been found."

  @required_args(2, 3)
  def create_contact(self, name, phone, birthday = None):
    record = Record(name)
    self.__add_record(record)
    self.add_phone_to_record(name, phone)
    if birthday is not None:
      self.add_birthday_to_record(name, birthday)
    return f"Contact was created successfully: {record}"

  @required_args(1)
  def __add_record(self, record):
    self.data[record.name.value] = record  

  @required_args(2)
  def add_phone_to_record(self, name, phone):
    found_record = self.find(name)
    if found_record: 
      return found_record.add_phone(phone)
    else:
      return f"Contact with name {name} has not been found."
      
  @required_args(2)
  def add_birthday_to_record(self, name, birthday):
    found_record = self.find(name)
    if found_record:
      return found_record.add_birthday(birthday)
    else:
      return f"Contact with name - {name} was not found"

  @required_args(1)
  def show_birthday(self, name):
    found_record = self.find(name)
    if found_record:
      return found_record.birthday if found_record.birthday is not None else f"Birthday did not added to contact with name {name}"
    else:
      return f"Contact with name: {name} not found!"
    
  def get_upcoming_birthdays(self):
    return [str(contact) for contact in list(self.data.values()) if Birthday.should_congratulate_soon(contact)]



  def find(self, name):
    return self.data.get(name)
  
  def delete(self, name):
    if name in self.data:
      del self.data[name]

  @required_args(1)
  def get_record_by_name(self, name):
    output_record = None
    if self.find(name):
      output_record = self.find(name)
    else:
      self.create_contact(name)
      print(f"Record with name: {name} not found, created a new contact.")
      output_record = self.find(name)
    return output_record

  def get_all(self):
    return [str(record) for record in list(self.data.values())]