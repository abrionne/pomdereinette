# Generated by Django 4.2.3 on 2023-09-18 09:53

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('week_hours', models.DecimalField(decimal_places=1, max_digits=4, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(50)])),
                ('weeks_number', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(53)])),
                ('months_number', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(12)])),
                ('supp_hours_number', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('week_hours_norms', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(50)])),
                ('days_activity_number', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(7)])),
                ('paid_vacation_number', models.DecimalField(decimal_places=2, max_digits=10)),
                ('monday_ie', models.BooleanField(default=True)),
                ('tuesday_ie', models.BooleanField(default=True)),
                ('wednesday_ie', models.BooleanField(default=True)),
                ('thursday_ie', models.BooleanField(default=True)),
                ('friday_ie', models.BooleanField(default=True)),
                ('saturday_ie', models.BooleanField(default=False)),
                ('sunday_ie', models.BooleanField(default=False)),
                ('monday_meal', models.BooleanField(default=True)),
                ('tuesday_meal', models.BooleanField(default=True)),
                ('wednesday_meal', models.BooleanField(default=True)),
                ('thursday_meal', models.BooleanField(default=True)),
                ('friday_meal', models.BooleanField(default=True)),
                ('saturday_meal', models.BooleanField(default=False)),
                ('sunday_meal', models.BooleanField(default=False)),
                ('monday_snack', models.BooleanField(default=True)),
                ('tuesday_snack', models.BooleanField(default=True)),
                ('wednesday_snack', models.BooleanField(default=True)),
                ('thursday_snack', models.BooleanField(default=True)),
                ('friday_snack', models.BooleanField(default=True)),
                ('saturday_snack', models.BooleanField(default=False)),
                ('sunday_snack', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Cost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('IE', models.DecimalField(decimal_places=2, max_digits=5)),
                ('meal', models.DecimalField(decimal_places=2, max_digits=5)),
                ('snack', models.DecimalField(decimal_places=2, max_digits=5)),
                ('paid_leave', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('paid_leave_supp_frac', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('paid_leave_supp_frac_month', models.IntegerField(choices=[(1, 'Janvier'), (2, 'Février'), (3, 'Mars'), (4, 'Avril'), (5, 'Mai'), (6, 'Juin'), (7, 'Juillet'), (8, 'Août'), (9, 'Septembre'), (10, 'Octobre'), (11, 'Novembre'), (12, 'Décembre')], validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)])),
                ('paid_leave_supp_frac_month_name', models.CharField(editable=False, max_length=10)),
                ('csg_rds', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('csg_ded', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('old1', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('old2', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('agff', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('supplementary_pension', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('personal_protection', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('frac_factor', models.DecimalField(decimal_places=4, max_digits=5)),
                ('div', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
            ],
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('base_hours', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0)])),
                ('gross_time_rate', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0)])),
                ('additional_hours_cost', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0)])),
                ('bonus_hours_cost', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.IntegerField(choices=[(1, 'Janvier'), (2, 'Février'), (3, 'Mars'), (4, 'Avril'), (5, 'Mai'), (6, 'Juin'), (7, 'Juillet'), (8, 'Août'), (9, 'Septembre'), (10, 'Octobre'), (11, 'Novembre'), (12, 'Décembre')], validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)])),
                ('month_name', models.CharField(blank=True, editable=False, max_length=10, null=True)),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(2000), django.core.validators.MaxValueValidator(2100)])),
                ('mam', models.DecimalField(decimal_places=2, default=1400, max_digits=6)),
                ('total', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True)),
                ('IE_cost', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True)),
                ('meal_cost', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True)),
                ('snack_cost', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True)),
                ('total_wo_ie_meal_snack', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True)),
                ('remaining_costs', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True)),
                ('assmat_salary', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True)),
                ('cost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salaire.cost')),
            ],
        ),
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.IntegerField(choices=[(1, 'Janvier'), (2, 'Février'), (3, 'Mars'), (4, 'Avril'), (5, 'Mai'), (6, 'Juin'), (7, 'Juillet'), (8, 'Août'), (9, 'Septembre'), (10, 'Octobre'), (11, 'Novembre'), (12, 'Décembre')], validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)])),
                ('month_name', models.CharField(blank=True, editable=False, max_length=10, null=True)),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(2000), django.core.validators.MaxValueValidator(2100)])),
                ('IE_number', models.IntegerField(blank=True, editable=False, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(31)])),
                ('supp_hours_number', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('meal_number', models.IntegerField(blank=True, editable=False, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(31)])),
                ('snack_number', models.IntegerField(blank=True, editable=False, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(31)])),
                ('IE_cost', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True)),
                ('additional_hours_number', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True)),
                ('bonus_hours_number', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True)),
                ('additional_hours_cost', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True)),
                ('bonus_hours_cost', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True)),
                ('meal_cost', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True)),
                ('snack_cost', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True)),
                ('gross_base_salary', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True)),
                ('base_salary', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True)),
                ('paid_leave_cost', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True)),
                ('paid_leave_supp', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True)),
                ('paid_leave_supp_cost', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True)),
                ('gross_salary', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True)),
                ('gross_salary_cost_frac_factor', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True)),
                ('csg_rds_cost', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True)),
                ('csg_ded_cost', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True)),
                ('old1_cost', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True)),
                ('old2_cost', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True)),
                ('agff_cost', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True)),
                ('supplementary_pension_cost', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True)),
                ('personal_protection_cost', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True)),
                ('salary_cost', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True)),
                ('net_salary_to_declare', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True)),
                ('IE_cost_to_declare', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True)),
                ('meal_cost_to_declare', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True)),
                ('snack_cost_to_declare', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True)),
                ('total', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True)),
                ('transfert', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True)),
                ('transfert_wo_ie_meal_snack', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True)),
                ('cost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salaire.cost')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salaire.contract')),
            ],
        ),
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_name', models.CharField(max_length=100)),
                ('day', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(31)])),
                ('supp_hours_number', models.DecimalField(decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(0)])),
                ('ie', models.BooleanField(default=False)),
                ('meal', models.BooleanField(default=False)),
                ('snack', models.BooleanField(default=False)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salaire.month')),
            ],
        ),
        migrations.CreateModel(
            name='ContractEnd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.IntegerField(choices=[(1, 'Janvier'), (2, 'Février'), (3, 'Mars'), (4, 'Avril'), (5, 'Mai'), (6, 'Juin'), (7, 'Juillet'), (8, 'Août'), (9, 'Septembre'), (10, 'Octobre'), (11, 'Novembre'), (12, 'Décembre')], validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)])),
                ('year', models.IntegerField(validators=[django.core.validators.MinValueValidator(2000), django.core.validators.MaxValueValidator(2100)])),
                ('factor', models.DecimalField(decimal_places=2, default=80, max_digits=10)),
                ('salary', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True)),
                ('assmat_salary', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True)),
                ('remaining_paid_leave_cost', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True)),
                ('assmat_remaining_paid_leave', models.DecimalField(blank=True, decimal_places=2, editable=False, max_digits=10, null=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salaire.contract')),
            ],
        ),
        migrations.AddField(
            model_name='contract',
            name='pricing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salaire.pricing'),
        ),
    ]