from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cleaning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('middlename', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('number', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('type', models.CharField(choices=[('3', '3 beds'), ('2', '2 beds'), ('1', '1 bed')], max_length=1)),
                ('price', models.IntegerField()),
                ('floor', models.IntegerField()),
                ('cleaners', models.ManyToManyField(through='hotel_app.Cleaning', to='hotel_app.Staff')),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passport_number', models.CharField(max_length=10, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('middlename', models.CharField(max_length=100)),
                ('from_location', models.CharField(max_length=100)),
                ('check_in_date', models.DateField(auto_now_add=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='guests', to='hotel_app.room')),
            ],
        ),
        migrations.AddField(
            model_name='cleaning',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cleaning', to='hotel_app.room'),
        ),
        migrations.AddField(
            model_name='cleaning',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cleaning', to='hotel_app.staff'),
        ),
    ]