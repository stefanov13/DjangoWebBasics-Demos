from django import forms
from .models import Person

'''
ModelTestForm:

Форма със модел - използва полета от зададения модел в 
Meta класа, могат да се подадат като списък и в него се 
подават имената на полетата от модела в кавички, 
може и да се вземат всичките с '__all__', 
може и да се изключат полета като начина е 
същия като със списъка, но вместо 'fields' се ползва 'exclude'
'''


class ModelTestForm(forms.ModelForm):
    # Disabled form fields

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.__set_disabeld_fields()

    # def __set_disabeld_fields(self):
    #     for field in self.fields.values():
    #         field.widget.attrs['disabled'] = 'disabled'

    class Meta:
        model = Person
        fields = '__all__'


'''
TestForm:
Форма без зададен модел - дефинираме полетата като атрибути както във моделите.
'''


class TestForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    age = forms.IntegerField()
