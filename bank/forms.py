from django.forms import ModelForm 
from django import forms
from .models import Expense
from users.models import CustomUser

class ExpenseForm(ModelForm):
    users = forms.ModelMultipleChoiceField(CustomUser.objects.none(), label='Utilisateurs')

    paid_with_my_card = forms.BooleanField(label="Payé avec ma carte", required=False)

    class Meta: 
        model = Expense
        fields = ['cost', 'description']
        labels = {
        	"cost": "Montant",
    	}

    def __init__(self, user, *args, **kwargs):
        super(ExpenseForm, self).__init__(*args, **kwargs)
        self.fields['users'].queryset = CustomUser.objects.filter(kot=user.kot).order_by('first_name', 'last_name')
        if user.kot.tricountOnly:
            self.fields['paid_with_my_card'] = forms.BooleanField(initial=True, widget=forms.HiddenInput())
        else:
            self.fields['paid_with_my_card'] = forms.BooleanField(label="Payé avec ma carte", required=False)
            


class ExpenseFormTCO(ModelForm): #TriCountOnly
    users = forms.ModelMultipleChoiceField(CustomUser.objects.none(), label='Utilisateurs')

    paid_with_my_card = forms.BooleanField(initial=True, widget=forms.HiddenInput())

    class Meta: 
        model = Expense
        fields = ['cost', 'description']
        labels = {
        	"cost": "Montant",
    	}

    def __init__(self, user, *args, **kwargs):
        super(ExpenseForm, self).__init__(*args, **kwargs)
        self.fields['users'].queryset = CustomUser.objects.filter(kot=user.kot).order_by('first_name', 'last_name')

class AddMoneyForm(ModelForm):
    user = forms.ModelChoiceField(CustomUser.objects.none(), label='Utilisateur')

    def __init__(self, user, *args, **kwargs):
        super(AddMoneyForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = CustomUser.objects.filter(kot=user.kot)

    class Meta:
    	model = Expense
    	fields = ['date', 'cost', 'description']
    	labels = {
        	"cost": "Montant",
	}
