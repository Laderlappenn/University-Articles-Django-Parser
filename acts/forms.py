from django.forms import ModelForm
from django import forms
from .models import Table_1, Table_2, Table_3, Table_4, Table_5, Table_6


class Table_1_form(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['title'].widget.attrs.update({'class': 'special'})

    file = forms.FileField(required=False)

    class Meta:
        model = Table_1
        fields = '__all__'
        exclude = ('act_processing', 'user', 'executer')

    def __init__(self, *args, **kwargs):
        custom_info = kwargs.pop('custom_info', None)  # get the custom info from the kwargs
        super().__init__(*args, **kwargs)
        if custom_info:
            self.fields['custom_field'].initial = custom_info.get('custom_field',
                                                                  '')  # set the initial value for the custom field

class Table_2_form(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['title'].widget.attrs.update({'class': 'special'})

    file = forms.FileField(required=False)

    class Meta:
        model = Table_2
        fields = '__all__'
        exclude = ('user',)


class Table_3_form(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['title'].widget.attrs.update({'class': 'special'})

    file = forms.FileField(required=False)

    class Meta:
        model = Table_3
        fields = '__all__'
        exclude = ('user',)


class Table_4_form(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['title'].widget.attrs.update({'class': 'special'})

    file = forms.FileField(required=False)

    class Meta:
        model = Table_4
        fields = '__all__'
        exclude = ('user',)


class Table_5_form(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['title'].widget.attrs.update({'class': 'special'})

    file = forms.FileField(required=False)

    class Meta:
        model = Table_5
        fields = '__all__'
        exclude = ('user',)


class Table_6_form(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['title'].widget.attrs.update({'class': 'special'})

    file = forms.FileField(required=False)

    class Meta:
        model = Table_6
        fields = '__all__'
        exclude = ('user',)
