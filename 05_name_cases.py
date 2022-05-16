name="eric"
message=f"Hello {name.title()},would you like to learn some python today?"
print(message)
message=f"Hello {name.upper()},would you like to learn some python today?"
print(message)
message=f"Hello {name.lower()},would you like to learn some python today?"
print(message)

message='Albert Einstein said,"A person who never made a mistake never tried anyting new"'
print(message)

famous_person="albert einstein"
message=f'{famous_person.title()} said,"A person who never made a mistake never tried anyting new"'
print(message)

famous_person=" albert einstein "
print(famous_person.lstrip())

famous_person=" albert einstein "
print(famous_person.rstrip())

famous_person=" albert einstein "
print(famous_person.strip())

famous_person=" albert einstein "
message=f"{famous_person}"
print(f"{message.strip()}\t\n{message.title()}")