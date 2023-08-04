from django.db import models

class Cliente(models.Model):
    documento = models.CharField(max_length=20, choices=[('cédula', 'Cédula'), ('ruc', 'RUC'), ('pasaporte', 'Pasaporte')])  # Adjust the max_length for the documento field
    documento_detalle = models.IntegerField(default=1000000000, verbose_name='Número de cédula')
    nombre = models.CharField(max_length=50, verbose_name='Nombre del cliente')
    apellido = models.CharField(max_length=50, verbose_name='Apellido del cliente')
    dirección = models.CharField(max_length=50, verbose_name='Dirección del cliente')
    telefono = models.CharField(max_length=10,verbose_name='Teléfono del cliente')
    email = models.CharField(max_length=50, verbose_name='Correo electrónico del cliente')

    def __str__(self):
        return self.nombre + ' ' + self.apellido

class Producto(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre del producto')
    descripción = models.TextField(verbose_name='Descripción del producto')
    imagen = models.ImageField(upload_to='productos', null=True, blank=True, verbose_name='Imagen del producto')
    marca = models.CharField(max_length=50, choices=[('nike', 'Nike'), ('adidas', 'Adidas'), ('puma', 'Puma'), ('reebok', 'Reebok')])  # Add max_length for marca field
    talla = models.CharField(max_length=50, choices=[('s', 'S'), ('m', 'M'), ('l', 'L'), ('xl', 'XL')])  # Add max_length for talla field
    color = models.CharField(max_length=50, choices=[('negro', 'Negro')])
    material = models.CharField(max_length=50, choices=[('poliester', 'Poliester')])
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(verbose_name='Stock del producto')
    fecha = models.DateField(auto_now=True)
        
    def __str__(self):
        return self.nombre + ' ' + self.marca

class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    subtotal = models.FloatField(verbose_name='Costo de la prenda')
    observaciones = models.CharField(max_length=50, verbose_name='Observaciones de la venta')
    iva = models.FloatField(choices=[(0.12, '12%')])
    total = models.FloatField()
    descuento = models.FloatField(choices=[(0.1, '10%'), (0.2, '20%'), (0.3, '30%')])  # Add choices for discount percentages

    @property
    def total(self):
        total = self.subtotal + self.iva - (self.subtotal * self.descuento)  # Calculate total amount after discount
        return total

    def __str__(self):
        return f"{self.cliente} - {self.producto} por el costo tota de: {self.total}"