from django.db import models

class Address(models.Model):
    post_code = models.CharField(max_length=20)
    street = models.CharField(max_length=255)
    neighborhood = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    street_number = models.CharField(max_length=20)
    complement = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.street}, {self.street_number} - {self.city}"


class Company(models.Model):
    cnpj = models.CharField(max_length=14)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    legal_name = models.CharField(max_length=100)
    trade_name = models.CharField(max_length=100)
    url_image = models.URLField(max_length=255)

    def __str__(self):
        return self.trade_names




class Person(models.Model):
    cpf = models.CharField(max_length=11, primary_key=True)
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

    gender = models.CharField(max_length=1, choices=[
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro')
    ], default='O')

    education_level = models.CharField(max_length=50, choices=[
        ('Ensino Fundamental', 'Ensino Fundamental'),
        ('Ensino Médio', 'Ensino Médio'),
        ('Ensino Superior', 'Ensino Superior'),
        ('Pós-graduação', 'Pós-graduação'),
        ('Mestrado', 'Mestrado'),
        ('Doutorado', 'Doutorado')
    ], default='Ensino Médio')

    marital_status = models.CharField(max_length=20, choices=[
        ('Solteiro(a)', 'Solteiro(a)'),
        ('Casado(a)', 'Casado(a)'),
        ('Divorciado(a)', 'Divorciado(a)'),
        ('Viúvo(a)', 'Viúvo(a)'),
        ('Separado(a)', 'Separado(a)')
    ], default='Solteiro(a)')

    total_income = models.IntegerField()
    current_occupation = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name} ({self.cpf})"

class BusinessHours(models.Model):
    # Dias da semana
    DAYS_OF_WEEK = [
        ('Segunda-feira', 'Segunda-feira'),
        ('Terça-feira', 'Terça-feira'),
        ('Quarta-feira', 'Quarta-feira'),
        ('Quinta-feira', 'Quinta-feira'),
        ('Sexta-feira', 'Sexta-feira'),
        ('Sábado', 'Sábado'),
        ('Domingo', 'Domingo'),
    ]

    day_of_week = models.CharField(max_length=20, choices=DAYS_OF_WEEK)
    initial_hour = models.TimeField()  # Armazena apenas hora
    end_hour = models.TimeField()      # Armazena apenas hora
    item = models.ForeignKey('Item', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.item} - {self.day_of_week}: {self.initial_hour} às {self.end_hour}"



class Item(models.Model):
    title = models.TextField(max_length=200)
    description = models.TextField()
    pickup_deadline = models.DateTimeField()
    
    pickup_type = models.CharField(
        max_length=50,
        choices=[
            ('Retirada no local', 'Retirada no local'),
            ('Entrega', 'Entrega')
])

    reservation_status = models.CharField(
        max_length=20,
        choices=[
            ('Available', 'Disponível'),
            ('Reserved', 'Reservado'),
            ('Collected', 'Coletado'),
            ('Expired', 'Expirado'),
            ('Cancelled', 'Cancelado')
        ],
        default='Available'
    )

    redemption_point = models.IntegerField()
    item_quantity = models.IntegerField()
    max_pickup = models.IntegerField()
    url_image = models.TextField(max_length=255)
    # transaction = models.ManyToManyField(Person, blank=True)  # Relacionamento M:N

    def __str__(self):
        return self.title

# class Transaction(models.Model):
#     pickup_time = models.DateTimeField()
#     person_id = models.ForeignKey(Item, on_delete=models.CASCADE)   # provavelmente invertido, veja abaixo
#     item_id = models.ForeignKey(Person, on_delete=models.CASCADE)   # provavelmente invertido, veja abaixo
#     pickup_quantity = models.IntegerField()

#     def __str__(self):
#         return f"{self.person.name} - {self.item.title} ({self.pickup_time})"
    
class Redemption_point(models.Model):
    id = models.IntegerField(primary_key=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.id
