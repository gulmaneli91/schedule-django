
from django import forms
from django.core.exceptions import ValidationError

from . import models

class ContactForm(forms.ModelForm):
    first_name= forms.CharField(
        widget=forms.TextInput(
            attrs={
             'class':'classe-a classe-b',
             'placeholder':'Type here third time',  
            }
        ),
        label='First Name',
        help_text=' user help text',
        
    )
    
    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)  
      
    #   self.fields ['first_name'].widget.attrs.update({
    #     'class':'classe-a classe-b',
    #     'placeholder':'Type here ',
    #   })
      
    class Meta:
        model = models.Contact
        fields = (
            'first_name','last_name','phone', 'email','description', 'category',
        )
        # widgets ={
        #     'first_name': forms.TextInput(
        #         attrs={
        #             'class':'classe-a classe-b',
        #             'placeholder':'Type here'
        #         }
        #     )
        # }
        
    def clean(self):
        #cleaned_data = self.cleaned_data
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')

        if first_name == last_name:
            msg= ValidationError(            
                'first name can not be equal the last one.',
                code='invalid'
            )
            self.add_error('last_name', msg)
            
        # self.add_error(
        #     'first_name',
        #     ValidationError(
        #         'error message',
        #         code='invalid'
        #     )
        # )
        
        # self.add_error(
        #   'first_name',
        #   ValidationError(
        #     'litle Billy',
        #     code='invalid'
        #   )
        # )
        
        return super().clean()
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        
        if first_name == 'ABC':
          self.add_error(
            'first_name', 
            ValidationError(
                'Do not be silly',
                code='invalid'
            )
          )
        return first_name
        