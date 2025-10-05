import re

from rest_framework import serializers


class PasswordField(serializers.Field):
    default_error_messages = {
        'invalid_password': 'Invalid password format.',
        'too_short': 'Password is too short.',
        'empty_password': 'Password cannot be empty.',
        'no_letter': 'Password must contain at least one letter.',
        'no_digits': 'Password must contain at least one digit.',
        'non_latin_letters': 'Password can only contain Latin letters and digits.',
    }

    def to_representation(self, value):
        return value

    def to_internal_value(self, data):
        if not isinstance(data, str):
            self.fail('invalid_password')

        if not data:  # Check if password is empty
            self.fail('empty_password')

        if len(data) < 8:  # Checking minimum password length
            self.fail('too_short')

        if not any(char.isalpha() for char in data):  # Check for at least one letter
            self.fail('no_letter')

        if not any(char.isdigit() for char in data):  # Check for at least one digit
            self.fail('no_digits')

        if not re.match("^[a-zA-Z0-9]*$", data):  # Check for only Latin letters
            self.fail('non_latin_letters')

        return data