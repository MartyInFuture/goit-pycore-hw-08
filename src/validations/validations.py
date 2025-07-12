
class PhoneSizeException(Exception):
  def __init__(self, message = 'Phone number should be 10 digits!'):
    super().__init__(message)

class UserAlreadyExists(Exception):
  def __init__(self, message = 'Phone number should be 10 digits!'):
    super().__init__(message)

class required_args:
  def __init__(self, expected_args_count, optional_args_count=None):
    self.expected_args_count = expected_args_count
    self.optional_args_count = optional_args_count if optional_args_count is not None else expected_args_count

    if self.expected_args_count > self.optional_args_count:
      raise ValueError("optional_args_count must be ≥ expected_args_count")

  def __call__(self, func):
    def wrapper(instance, *args): 
      if len(args) < self.expected_args_count or len(args) > self.optional_args_count:
        args_count_range = self.expected_args_count if self.expected_args_count == self.optional_args_count else f"{self.expected_args_count}–{self.optional_args_count}"
        return f"Error: Expected {args_count_range} argument(s), but got {len(args)}."
      return func(instance, *args)
    return wrapper
