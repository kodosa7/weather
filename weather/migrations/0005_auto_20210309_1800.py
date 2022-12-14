# Generated by Django 3.1.5 on 2021-03-09 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0004_auto_20210125_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='cityName',
            field=models.CharField(choices=[('Prague', 'Praha'), ('Brno', 'Brno'), ('Liberec', 'Liberec'), ('Ostrava', 'Ostrava'), ('České Budějovice', 'České Budějovice'), ('Karlovy Vary', 'Karlovy Vary'), ('Litoměřice', 'Litoměřice'), ('Cheb', 'Cheb'), ('Mladá Boleslav', 'Mladá Boleslav'), ('Olomouc', 'Olomouc'), ('Hradec Králové', 'Hradec Králové'), ('Plzeň', 'Plzeň'), ('Doksy', 'Doksy'), ('Roudnice nad Labem', 'Roudnice nad Labem'), ('Ústí nad Labem', 'Ústí nad Labem'), ('Děčín', 'Děčín'), ('Snědovice', 'Snědovice'), ('London', 'London'), ('Oxford', 'Oxford'), ('Liverpool', 'Liverpool'), ('Glasgow', 'Glasgow'), ('Dublin', 'Dublin'), ('Berlin', 'Berlin'), ('Munchen', 'Munchen'), ('Paris', 'Paris'), ('Warsaw', 'Warsaw'), ('Moscow', 'Moscow'), ('Budapest', 'Budapest'), ('Roma', 'Roma'), ('Cairo', 'Cairo'), ('New York', 'New York'), ('Tokyo', 'Tokyo'), ('Sydney', 'Sydney'), ('Adamov', 'Adamov'), ('Edinburgh', 'Edinburgh')], max_length=30, verbose_name='City Name'),
        ),
    ]
