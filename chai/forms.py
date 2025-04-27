from django.db import migrations, models
from .models import ChaiVarity

class ChaiVarityMigration(migrations.Migration):
    dependencies = [
        ('chai', '0001_initial'),  # Adjust this to your actual initial migration file
    ]

    operations = [
        migrations.CreateModel(
            name='ChaiVarity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]

