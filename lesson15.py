#Lesson 15 task 1
#Task 1
"""Create a class method named `validate`, which should be called from
the `__init__` method to validate parameter email,
passed to the constructor. The logic inside the `validate`
method could be to check if the passed email parameter is a valid email string.
Email validations:
https://help.xmatters.com/ondemand/trial/valid_email_format.htm
https://en.wikipedia.org/wiki/Email_address
"""

class Validate:

    def __init__(self, email):
        self.email = email

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self,email):
        if self.check_email(email):
            self._email=email
        else:
            self.email = None
            raise Exception ('Не правильный имейл')

    @staticmethod
    def check_email(email):
        regex = ''
