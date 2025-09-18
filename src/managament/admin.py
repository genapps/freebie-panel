from django import forms
from django.contrib import admin
from .models import Person, Address, Company, BusinessHours, Item, RedemptionPoint, Transaction

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if "address" in self.fields:
            widget = self.fields["address"].widget
            widget.can_add_related = False
            widget.can_change_related = False
            widget.can_view_related = False
            widget.can_delete_related = False

        if "company" in self.fields:
            widget = self.fields["company"].widget
            widget.can_add_related = False
            widget.can_change_related = False
            widget.can_view_related = False   
            widget.can_delete_related = False 


@admin.register(Person)
class PessoaAdmin(admin.ModelAdmin):
    form = PersonForm  # ← aplica o form sem ícones
    list_display = ('cpf', 'name', 'birth_date', 'gender', 'company', 'phone')
    search_fields = ('cpf', 'name')
    list_filter = ('gender', 'education_level', 'marital_status', 'company')


@admin.register(Address)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('post_code', 'street', 'neighborhood', 'city', 'state', 'street_number', 'complement')
    search_fields = ('post_code', 'street', 'neighborhood', 'city', 'state')



class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if "address" in self.fields:
            widget = self.fields["address"].widget
            widget.can_add_related = False
            widget.can_change_related = False
            widget.can_view_related = False

@admin.register(Company)
class EmpresaAdmin(admin.ModelAdmin):
    form = CompanyForm   # ← aplica o form sem ícones
    list_display = ('cnpj', 'address', 'legal_name', 'trade_name', 'url_image')
    search_fields = ('cnpj', 'legal_name', 'trade_name')


# ===== BusinessHours sem ícones de relação no campo "item" =====
class BusinessHoursForm(forms.ModelForm):
    class Meta:
        model = BusinessHours
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if "item" in self.fields:
            widget = self.fields["item"].widget
            widget.can_add_related = False
            widget.can_change_related = False
            widget.can_view_related = False


@admin.register(BusinessHours)
class BusinessHoursAdmin(admin.ModelAdmin):
    form = BusinessHoursForm
    list_display =('day_of_week', 'initial_hour', 'item', 'end_hour')
    search_fields = ('day_of_week', 'item__title')


class RedemptionPointForm(forms.ModelForm):
    class Meta:
        model = RedemptionPoint
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if "redemptionPoint" in self.fields:
            widget = self.fields["redemptionPoint"].widget
            widget.can_add_related = False
            

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    form = RedemptionPointForm
    list_display = ('title', 'description', 'pickup_deadline', 'pickup_type',
                    'reservation_status', 'item_quantity', 'max_pickup',
                    'url_image', 'get_redemption_points')
    search_fields = ('title', 'description')
    list_filter = ('pickup_type', 'reservation_status')

    def get_redemption_points(self, obj):
        return ", ".join([str(rp) for rp in obj.redemption_point.all()])
    get_redemption_points.short_description = "Pontos de Resgate"



class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if "person" in self.fields:
            widget = self.fields["person"].widget
            widget.can_add_related = False
            widget.can_change_related = False
            widget.can_view_related = False
            widget.can_delete_related = False

        if "item" in self.fields:
            widget = self.fields["item"].widget
            widget.can_add_related = False
            widget.can_change_related = False
            widget.can_view_related = False   
            widget.can_delete_related = False


@admin.register(Transaction)
class TransacaoAdmin(admin.ModelAdmin):
    form = TransactionForm
    list_display = ('pickup_time', 'person', 'item', 'pickup_quantity')
    search_fields = ('person__name', 'item__title')
    list_filter = ('pickup_time', 'person')



class RedemptionPointForm(forms.ModelForm):
    class Meta:
        model = RedemptionPoint
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if "address" in self.fields:
            widget = self.fields["address"].widget
            widget.can_add_related = False
            widget.can_change_related = False
            widget.can_view_related = False
            widget.can_delete_related = False

        if "company" in self.fields:
            widget = self.fields["company"].widget
            widget.can_add_related = False
            widget.can_change_related = False
            widget.can_view_related = False   
            widget.can_delete_related = False

@admin.register(RedemptionPoint)
class PontoResgateAdmin(admin.ModelAdmin):
    form = PersonForm  # ← aplica o form sem ícones
    list_display = ('address', 'company')
    search_fields = ('company__trade_name', 'company__legal_name', 'address__street')
