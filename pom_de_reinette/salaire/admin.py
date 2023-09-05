from django.contrib import admin
from salaire.models import Contract, Cost, Pricing, Month, Day, Summary, ContractEnd

class ContractAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "week_hours",
        "weeks_number",
        "months_number",
        "pricing",
        "supp_hours_number",
        "week_hours_norms",
        "days_activity_number",
        "paid_vacation_number",
        "monday_ie",
        "tuesday_ie",
        "wednesday_ie",
        "thursday_ie",
        "friday_ie",
        "saturday_ie",
        "sunday_ie",
        "monday_meal",
        "tuesday_meal",
        "wednesday_meal",
        "thursday_meal",
        "friday_meal",
        "saturday_meal",
        "sunday_meal",
        "monday_snack",
        "tuesday_snack",
        "wednesday_snack",
        "thursday_snack",
        "friday_snack",
        "saturday_snack",
        "sunday_snack"
    )

admin.site.register(Contract, ContractAdmin)

class CostAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "IE",
        "meal",
        "snack",
        "paid_leave",
        "paid_leave_supp_frac",
        "paid_leave_supp_frac_month",
        "csg_rds",
        "csg_ded",
        "old1",
        "old2",
        "agff",
        "supplementary_pension",
        "personal_protection",
        "frac_factor", 
        "div"
    )

admin.site.register(Cost, CostAdmin)

class PricingAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "base_hours",
        "gross_time_rate",
        "additional_hours_cost",
        "bonus_hours_cost"
    )

admin.site.register(Pricing, PricingAdmin)

class MonthAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "cost",
        "month",
        "month_name",
        "year",
        "IE_number",
        "supp_hours_number",
        "meal_number",
        "snack_number",
        "IE_cost",
        "additional_hours_number",
        "bonus_hours_number",
        "additional_hours_cost",
        "bonus_hours_cost",
        "meal_cost",
        "snack_cost",
        "gross_base_salary",
        "base_salary",
        "paid_leave_cost",
        "paid_leave_supp",
        "paid_leave_supp_cost",
        "gross_salary",
        "csg_rds_cost",
        "csg_ded_cost",
        "old1_cost",
        "old2_cost",
        "agff_cost",
        "supplementary_pension_cost",
        "personal_protection_cost",
        "salary_cost",
        "net_salary_to_declare",
        "IE_cost_to_declare",
        "meal_cost_to_declare",
        "snack_cost_to_declare",
        "total",
        "transfert",
        "transfert_wo_ie_meal_snack"
    )

admin.site.register(Month, MonthAdmin)

class DayAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "day_name",
        "day",
        "ie",
        "supp_hours_number",
        "meal",
        "snack"
    )

admin.site.register(Day, DayAdmin)

class SummaryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "month",
        "year",
        "mam",
        "cost",
        "total",
        "IE_cost",
        "meal_cost",
        "snack_cost",
        "total_wo_ie_meal_snack",
        "remaining_costs",
        "assmat_salary"
    )

admin.site.register(Summary, SummaryAdmin)

class ContractEndAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "month",
        "year",
        "factor",
        "salary",
        "remaining_paid_leave_cost",
        "assmat_salary"
    )

admin.site.register(ContractEnd, ContractEndAdmin)
