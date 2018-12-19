import addressbook_pb2

person = addressbook_pb2.Person()
person.id = 1234
person.name = "John Doe"
person.email = "jdoe@example.com"
phone = person.phones.add()
phone.number = "555-4321"
phone.type = addressbook_pb2.Person.HOME

print('Before serialize:')
print(person)

with open('person.bin', 'wb') as f:
    f.write(person.SerializeToString())

print('Read back:')

with open('person.bin', 'rb') as f:
    read_person = addressbook_pb2.Person()
    read_person.ParseFromString(f.read())
    print(read_person)
