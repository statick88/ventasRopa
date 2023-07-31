# Generated by Django 4.2.3 on 2023-07-31 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.CharField(choices=[('cédula', 'Cédula'), ('ruc', 'RUC'), ('pasaporte', 'Pasaporte')], max_length=20)),
                ('documento_detalle', models.PositiveIntegerField()),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('dirección', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripción', models.TextField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='productos')),
                ('marca', models.CharField(choices=[('nike', 'Nike'), ('adidas', 'Adidas'), ('puma', 'Puma'), ('reebok', 'Reebok')], max_length=50)),
                ('talla', models.CharField(choices=[('s', 'S'), ('m', 'M'), ('l', 'L'), ('xl', 'XL')], max_length=50)),
                ('color', models.CharField(choices=[('negro', 'Negro')], max_length=50)),
                ('material', models.CharField(choices=[('poliester', 'Poliester')], max_length=50)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.IntegerField()),
                ('fecha', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtotal', models.FloatField(verbose_name='Costo de la prenda')),
                ('observaciones', models.CharField(max_length=50)),
                ('iva', models.FloatField(choices=[(0.12, '12%')])),
                ('descuento', models.FloatField(choices=[(0.1, '10%'), (0.2, '20%'), (0.3, '30%')])),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.cliente')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.producto')),
            ],
        ),
    ]
