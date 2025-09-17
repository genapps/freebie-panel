from django.contrib import admin
from .models import Person, Address, Company, BusinessHours, Item, RedemptionPoint, Transaction

@admin.register(Person)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'birth_date', 'gender', 'education_level', 'marital_status', 'total_income', 'current_occupation', 'name', 'phone', 'company', 'address')
    search_fields = ('cpf', 'name')

@admin.register(Address)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('post_code', 'street', 'neighborhood', 'city', 'state', 'street_number', 'complement')
    search_fields = ('post_code', 'street', 'neighborhood', 'city', 'state')

@admin.register(Company)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('cnpj', 'address', 'legal_name', 'trade_name', 'url_image')
    search_fields = ('cnpj', 'legal_name', 'trade_name')

@admin.register(BusinessHours)
class HorarioFuncionamentoAdmin(admin.ModelAdmin):
    list_display =('day_of_week', 'initial_hour', 'item', 'end_hour')
    search_fields = ('day_of_week', 'item__title')

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'pickup_deadline', 'pickup_type', 'reservation_status', 'item_quantity', 'max_pickup', 'url_image',  'get_redemption_points',)
    search_fields = ('title', 'description')
    def get_redemption_points(self, obj):
        return ", ".join([str(rp) for rp in obj.redemption_point.all()])
    get_redemption_points.short_description = "Pontos de Resgate"

@admin.register(Transaction)
class TransacaoAdmin(admin.ModelAdmin):
    list_display = (
        'pickup_time',
        'person',
        'item',
        'pickup_quantity',
        # Se quiser mostrar mais info do item ou pessoa, pode criar métodos abaixo
    )
    search_fields = ('person__name', 'item__title')


@admin.register(RedemptionPoint)
class PontoResgateAdmin(admin.ModelAdmin):
    list_display = ('address', 'company')  
    search_fields = ('company__name', 'address__street')