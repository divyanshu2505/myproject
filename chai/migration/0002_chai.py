from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('chai', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chaivarity',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='chaivarity',
            name='image',
            field=models.ImageField(upload_to='chai_varity_images/'),
        ),
        migrations.AlterField(
            model_name='chaivarity',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='chaivarity',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='chaivarity',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]