from django.db import models
from django.db.models import Sum, Q
from django.core.validators import MaxValueValidator, MinValueValidator
import locale
from django.utils import timezone

# pricing model
class Pricing(models.Model):
    name = models.fields.CharField(
        max_length=100,
        unique=True
    )
    base_hours = models.fields.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    gross_time_rate = models.fields.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    additional_hours_cost =models.fields.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    bonus_hours_cost =models.fields.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    def __str__(self):
        return f'{self.name}'

# cost model
class Cost(models.Model):
    class Months(models.IntegerChoices):
        Janvier = 1
        Février = 2
        Mars = 3
        Avril = 4
        Mai = 5
        Juin = 6
        Juillet = 7
        Août = 8
        Septembre = 9
        Octobre = 10
        Novembre = 11
        Décembre = 12

    name = models.fields.CharField(
        max_length=20,
        unique=True
    )
    IE = models.fields.DecimalField(
          max_digits=5,
          decimal_places=2
    )
    meal = models.fields.DecimalField(
          max_digits=5,
          decimal_places=2
    )
    snack = models.fields.DecimalField(
         max_digits=5,
         decimal_places=2
    )
    paid_leave = models.fields.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    paid_leave_supp_frac = models.fields.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    paid_leave_supp_frac_month = models.IntegerField(
        choices=Months.choices, 
        validators=[MinValueValidator(1), MaxValueValidator(12)]
    )
    paid_leave_supp_frac_month_name = models.fields.CharField(
        max_length=10,
        editable=False
    )
    csg_rds = models.fields.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    csg_ded = models.fields.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    old1 = models.fields.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    old2 = models.fields.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    agff = models.fields.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    supplementary_pension = models.fields.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    personal_protection = models.fields.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    frac_factor = models.fields.DecimalField(
        max_digits=5,
        decimal_places=4,
        validators=[MinValueValidator(0), MaxValueValidator(1)]
    )
    div = models.fields.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(10)]
    )
    def save(self, *args, **kwargs):
        locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')
        self.paid_leave_supp_frac_month_name = timezone.datetime(2023, self.paid_leave_supp_frac_month,1).strftime("%B")
        super().save(*args, **kwargs)
    def __str__(self):
        return f'{self.name}'

# contrat model
class Contract(models.Model):
    name = models.fields.CharField(
        max_length=100,
        unique=True
    )
    week_hours = models.fields.DecimalField(
        max_digits=4,
        decimal_places=1,
        validators=[MinValueValidator(0), MaxValueValidator(50)]
    )
    weeks_number =models.fields.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(53)]
    )
    months_number = models.fields.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(12)]
    )
    supp_hours_number = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    week_hours_norms = models.fields.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(50)]
    )
    days_activity_number = models.fields.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(7)]
    )
    paid_vacation_number = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    pricing = models.ForeignKey(
        Pricing, 
        on_delete=models.CASCADE
    )
    monday_ie = models.BooleanField(
        default=True
    )
    tuesday_ie = models.BooleanField(
        default=True
    )
    wednesday_ie = models.BooleanField(
        default=True
    )
    thursday_ie = models.BooleanField(
        default=True
    )
    friday_ie = models.BooleanField(
        default=True
    )
    saturday_ie = models.BooleanField(
        default=False
    )
    sunday_ie = models.BooleanField(
        default=False
    )
    monday_meal = models.BooleanField(
        default=True
    )
    tuesday_meal = models.BooleanField(
        default=True
    )
    wednesday_meal = models.BooleanField(
        default=True
    )
    thursday_meal = models.BooleanField(
        default=True
    )
    friday_meal = models.BooleanField(
        default=True
    )
    saturday_meal = models.BooleanField(
        default=False
    )
    sunday_meal = models.BooleanField(
        default=False
    )
    monday_snack = models.BooleanField(
        default=True
    )
    tuesday_snack = models.BooleanField(
        default=True
    )
    wednesday_snack = models.BooleanField(
        default=True
    )
    thursday_snack = models.BooleanField(
        default=True
    )
    friday_snack = models.BooleanField(
        default=True
    )
    saturday_snack = models.BooleanField(
        default=False
    )
    sunday_snack = models.BooleanField(
        default=False
    )
    def __str__(self):
        return f'{self.name}'

# month model
class Month(models.Model):
    class Months(models.IntegerChoices):
        Janvier = 1
        Février = 2
        Mars = 3
        Avril = 4
        Mai = 5
        Juin = 6
        Juillet = 7
        Août = 8
        Septembre = 9
        Octobre = 10
        Novembre = 11
        Décembre = 12

    name = models.ForeignKey(
        Contract, 
        on_delete=models.CASCADE
    )
    cost = models.ForeignKey(
        Cost,
        on_delete=models.CASCADE,
    )
    month = models.IntegerField(
        choices=Months.choices, 
        validators=[MinValueValidator(1), MaxValueValidator(12)]
    )
    month_name =  models.fields.CharField(
        max_length=10,
        null=True,
        blank=True,
        editable=False
    )
    year =  models.fields.IntegerField(
        validators=[MinValueValidator(2000), MaxValueValidator(2100)]
    )
    IE_number = models.fields.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(31)],
        null=True,
        blank=True,
        editable=False
    )
    supp_hours_number = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        null=True,
        blank=True,
        editable=False
    )
    meal_number = models.fields.IntegerField(                                     
        validators=[MinValueValidator(0), MaxValueValidator(31)],
        null=True,
        blank=True,
        editable=False
    )
    snack_number = models.fields.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(31)],
        null=True,
        blank=True,
        editable=False
    )
    IE_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        editable=False
    )
    additional_hours_number = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        editable=False
    )
    bonus_hours_number = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        editable=False
    )
    additional_hours_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        editable=False
    )
    bonus_hours_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        editable=False
    )
    meal_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        editable=False
    )
    snack_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        editable=False
    )
    gross_base_salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        editable=False
    )
    base_salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        editable=False
    )
    paid_leave_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        editable=False
    )
    paid_leave_supp = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        editable=False
    )
    paid_leave_supp_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        editable=False
    )
    gross_salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        editable=False
    )
    gross_salary_cost_frac_factor = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        editable=False
    )
    csg_rds_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        editable=False
    )
    csg_ded_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        editable=False
    )
    old1_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        editable=False
    )
    old2_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        editable=False
    )
    agff_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        editable=False
    )
    supplementary_pension_cost =models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        editable=False
    )
    personal_protection_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        editable=False
    )
    salary_cost =models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        editable=False
    )
    net_salary_to_declare = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        editable=False
    )
    IE_cost_to_declare = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        editable=False
    )
    meal_cost_to_declare = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        editable=False
    )
    snack_cost_to_declare = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        editable=False
    )
    total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        editable=False
    )
    transfert = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        editable=False
    )
    transfert_wo_ie_meal_snack = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        editable=False
    )
    def compute(self, *args, **kwargs):
        contrat=Contract.objects.get(name=self.name)
        pricing=Pricing.objects.get(name=contrat.pricing)
        cost=Cost.objects.get(name=self.cost)
        days=Day.objects.all().filter(name=self)
        self.supp_hours_number = days.aggregate(value=Sum('supp_hours_number'))["value"] + contrat.supp_hours_number
        self.IE_number = days.aggregate(value=Sum('ie'))["value"] 
        self.meal_number = days.aggregate(value=Sum('meal'))["value"] 
        self.snack_number = days.aggregate(value=Sum('snack'))["value"] 
        self.IE_cost= self.IE_number*cost.IE
        self.additional_hours_number=0
        self.bonus_hours_number=0
        if self.supp_hours_number>0:
            self.additional_hours_number=self.supp_hours_number-(pricing.base_hours-contrat.week_hours)
            if self.additional_hours_number <=0:
                self.additional_hours_number = self.supp_hours_number
            else:
                self.additional_hours_number = pricing.base_hours - contrat.week_hours
                self.bonus_hours_number=self.supp_hours_number-self.additional_hours_number
        self.additional_hours_cost = self.additional_hours_number*pricing.additional_hours_cost
        self.bonus_hours_cost=self.bonus_hours_number*pricing.bonus_hours_cost
        self.meal_cost=self.meal_number*cost.meal
        self.snack_cost = self.snack_number*cost.snack
        self.gross_base_salary = ((pricing.gross_time_rate*contrat.week_hours*contrat.weeks_number)+(contrat.supp_hours_number*pricing.bonus_hours_cost*contrat.weeks_number))/contrat.months_number
        self.base_salary = self.gross_base_salary/cost.div
        self.paid_leave_cost = (self.base_salary*cost.paid_leave/100)
        self.paid_leave_supp=Month.objects.all().filter(
            Q(name_id = self.name) &
            (
                Q(year = self.year-1, month__gte=cost.paid_leave_supp_frac_month) |
                Q(year = self.year, month__lt=cost.paid_leave_supp_frac_month)
            )
        ).aggregate(value=Sum('paid_leave_cost'))["value"]
        self.paid_leave_supp_cost = 0
        if self.month==cost.paid_leave_supp_frac_month :
            self.paid_leave_supp_cost= self.paid_leave_supp * cost.paid_leave_supp_frac/100
        self.gross_salary = self.base_salary +  self.additional_hours_cost + self.bonus_hours_cost + self.paid_leave_cost + self.paid_leave_supp_cost
        self.gross_salary_cost_frac_factor=self.gross_salary*cost.frac_factor
        self.csg_rds_cost = self.gross_salary_cost_frac_factor*cost.csg_rds/100
        self.csg_ded_cost = self.gross_salary_cost_frac_factor*cost.csg_ded/100
        self.old1_cost = self.gross_salary*cost.old1/100
        self.old2_cost = self.gross_salary*cost.old2/100
        self.agff_cost = self.gross_salary*cost.agff/100
        self.supplementary_pension_cost = self.gross_salary*cost.supplementary_pension/100
        self.personal_protection_cost = self.gross_salary*cost.personal_protection/100
        self.salary_cost = self.csg_rds_cost+self.csg_ded_cost+self.old1_cost+self.old2_cost+self.agff_cost+self.supplementary_pension_cost+self.personal_protection_cost
        self.net_salary_to_declare = self.gross_salary-self.salary_cost
        self.IE_cost_to_declare = self.IE_cost/cost.div
        self.meal_cost_to_declare = self.meal_cost/cost.div
        self.snack_cost_to_declare = self.snack_cost/cost.div
        self.total = self.net_salary_to_declare + self.IE_cost_to_declare + self.meal_cost_to_declare + self.snack_cost_to_declare
        self.transfert = self.total*cost.div
        self.transfert_wo_ie_meal_snack = self.transfert - (self.IE_cost + self.meal_cost + self.snack_cost)
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.name} - {self.cost} - {self.month_name} - {self.year}"

# days model
class Day(models.Model):
    name = models.ForeignKey(
        Month, 
        on_delete=models.CASCADE,
    )
    day_name = models.fields.CharField(
        max_length=100,
    )
    day = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(31)],
    )
    supp_hours_number = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        default=0
    )
    ie = models.BooleanField(
        default=False
    )

    meal = models.BooleanField(
        default=False
    )
    snack = models.BooleanField(
        default=False
    )
    def __str__(self):
        return f"{self.name} - {self.day_name} - {self.day}"

# month summary
class Summary(models.Model):
    class Months(models.IntegerChoices):
        Janvier = 1
        Février = 2
        Mars = 3
        Avril = 4
        Mai = 5
        Juin = 6
        Juillet = 7
        Août = 8
        Septembre = 9
        Octobre = 10
        Novembre = 11
        Décembre = 12
    month = models.IntegerField(
        choices=Months.choices, 
        validators=[MinValueValidator(1), MaxValueValidator(12)]
    )
    month_name =  models.fields.CharField(
        max_length=10,
        null=True,
        blank=True,
        editable=False
    )
    year =  models.fields.IntegerField(
        validators=[MinValueValidator(2000), MaxValueValidator(2100)]
    )
    mam = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        default=1400
    )
    cost = models.ForeignKey(
        Cost, 
        on_delete=models.CASCADE
    )
    total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        editable=False
    )
    IE_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        editable=False
    )
    meal_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        editable=False
    )
    snack_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        editable=False
    )
    total_wo_ie_meal_snack = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        editable=False
    )
    remaining_costs= models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        editable=False
    )
    assmat_salary= models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        editable=False
    )
    def save(self, *args, **kwargs):
        locale.setlocale(locale.LC_TIME, 'fr_FR.UTF-8')
        obj=Month.objects.all().filter(month=self.month,year=self.year)
        cost=Cost.objects.get(name=self.cost)
        self.month_name = timezone.datetime(self.year, self.month,1).strftime("%B")
        self.total = obj.aggregate(value=Sum('transfert'))["value"] 
        self.IE_cost = obj.aggregate(value=Sum('IE_cost'))["value"] 
        self.meal_cost = obj.aggregate(value=Sum('meal_cost'))["value"] 
        self.snack_cost = obj.aggregate(value=Sum('snack_cost'))["value"]
        self.total_wo_ie_meal_snack = obj.aggregate(value=Sum('transfert_wo_ie_meal_snack'))["value"]
        self.remaining_costs = self.mam - self.IE_cost
        self.assmat_salary = (self.total_wo_ie_meal_snack - self.remaining_costs) / cost.div
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.month} - {self.year}"

# contrat end
class ContractEnd(models.Model):
    class Months(models.IntegerChoices):
        Janvier = 1
        Février = 2
        Mars = 3
        Avril = 4
        Mai = 5
        Juin = 6
        Juillet = 7
        Août = 8
        Septembre = 9
        Octobre = 10
        Novembre = 11
        Décembre = 12
    name = models.ForeignKey(
        Contract, 
        on_delete=models.CASCADE
    )
    month = models.IntegerField(
        choices=Months.choices, 
        validators=[MinValueValidator(1), MaxValueValidator(12)]
    )
    year =  models.fields.IntegerField(
        validators=[MinValueValidator(2000), MaxValueValidator(2100)]
    )
    factor = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default= 80
    )
    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        editable=False
    )
    assmat_salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        editable=False
    )
    remaining_paid_leave_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        editable=False
    )
    assmat_remaining_paid_leave = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        editable=False
    )
    def save(self, *args, **kwargs):
        months=Month.objects.all().filter(name_id=self.name)
        cost=months.values_list("cost",flat=True).distinct().first()
        cost=Cost.objects.get(id=cost)
        self.salary = months.aggregate(value=Sum('net_salary_to_declare'))["value"] 
        self.assmat_salary = self.salary / self.factor
        if self.month >= cost.paid_leave_supp_frac_month:
            self.remaining_paid_leave_cost =months.filter(
                year=self.year, month__gte=cost.paid_leave_supp_frac_month
            ).aggregate(value=Sum('paid_leave_cost'))["value"]
        else:
            self.remaining_paid_leave_cost=months.filter(
                Q(year = self.year-1, month__gte=cost.paid_leave_supp_frac_month) |
                Q(year = self.year)
            ).aggregate(value=Sum('paid_leave_cost'))["value"]
        self.assmat_remaining_paid_leave = self.remaining_paid_leave_cost / cost.paid_leave_supp_frac
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.name}"
