# Generated by Django 4.2.6 on 2023-10-22 10:41

from django.db import migrations, models
import petstagram.main.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_pet_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='PetPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='', validators=[petstagram.main.validators.image_max_size_validator])),
                ('description', models.TextField(blank=True, null=True)),
                ('publication_date', models.DateTimeField(auto_now_add=True)),
                ('likes', models.IntegerField(default=0)),
                ('tagged_pets', models.ManyToManyField(to='main.pet')),
            ],
        ),
    ]
