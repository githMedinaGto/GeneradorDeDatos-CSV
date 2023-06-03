import csv
from faker import Faker

fake = Faker()

# Generar datos aleatorios
with open('C:\\Users\\racie\\Downloads\\datos.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Nombre completo', 'Correo electrónico', 'Teléfono', 'Ciudad'])

    for i in range(10000):
        writer.writerow([fake.name(), fake.email(), fake.phone_number(), fake.city()])
