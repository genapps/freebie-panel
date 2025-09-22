from django import forms
from django.contrib import admin
from .models import Person, Address, Company, BusinessHours, Item, RedemptionPoint, Transaction

# ===== Forms =====
class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in ['address', 'company']:
            if field_name in self.fields:
                widget = self.fields[field_name].widget
                widget.can_add_related = False
                widget.can_change_related = False
                widget.can_view_related = False
                widget.can_delete_related = False


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
            widget.can_delete_related = False


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
            widget.can_delete_related = False


class RedemptionPointForm(forms.ModelForm):
    class Meta:
        model = RedemptionPoint
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in ['address', 'company']:
            if field_name in self.fields:
                widget = self.fields[field_name].widget
                widget.can_add_related = False
                widget.can_change_related = False
                widget.can_view_related = False
                widget.can_delete_related = False


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if "redemption_point" in self.fields:
            widget = self.fields["redemption_point"].widget
            widget.can_add_related = False
            widget.can_change_related = False
            widget.can_view_related = False
            widget.can_delete_related = False


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in ['person', 'item']:
            if field_name in self.fields:
                widget = self.fields[field_name].widget
                widget.can_add_related = False
                widget.can_change_related = False
                widget.can_view_related = False
                widget.can_delete_related = False


# ===== Admin =====
@admin.register(Person)
class PessoaAdmin(admin.ModelAdmin):
    form = PersonForm
    list_display = ('cpf', 'name', 'birth_date', 'gender', 'company', 'phone')
    search_fields = ('cpf', 'name')
    list_filter = ('gender', 'education_level', 'marital_status', 'company')


@admin.register(Address)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('post_code', 'street', 'neighborhood', 'city', 'state', 'street_number', 'complement')
    search_fields = ('post_code', 'street', 'neighborhood', 'city', 'state')


@admin.register(Company)
class EmpresaAdmin(admin.ModelAdmin):
    form = CompanyForm
    list_display = ('cnpj', 'address', 'legal_name', 'trade_name', 'url_image')
    search_fields = ('cnpj', 'legal_name', 'trade_name')


@admin.register(BusinessHours)
class BusinessHoursAdmin(admin.ModelAdmin):
    form = BusinessHoursForm
    list_display = ('day_of_week', 'initial_hour', 'item', 'end_hour')
    search_fields = ('day_of_week', 'item__title')


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    form = ItemForm
    list_display = ('title', 'description', 'pickup_deadline', 'pickup_type',
                    'reservation_status', 'item_quantity', 'max_pickup',
                    'url_image', 'get_redemption_points')
    search_fields = ('title', 'description')
    list_filter = ('pickup_type', 'reservation_status')

    def get_redemption_points(self, obj):
        return ", ".join([str(rp) for rp in obj.redemption_point.all()])
    get_redemption_points.short_description = "Pontos de Resgate"


@admin.register(RedemptionPoint)
class PontoResgateAdmin(admin.ModelAdmin):
    form = RedemptionPointForm
    list_display = ('address', 'company')
    search_fields = ('company__trade_name', 'company__legal_name', 'address__street')


@admin.register(Transaction)
class TransacaoAdmin(admin.ModelAdmin):
    form = TransactionForm
    list_display = ('pickup_time', 'person', 'item', 'pickup_quantity')
    search_fields = ('person__name', 'item__title')
    list_filter = ('pickup_time', 'person')
