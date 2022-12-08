import phonenumbers

text = input()
numbers = phonenumbers.PhoneNumberMatcher(text, "IN")

for number in numbers:
      print('Valid')