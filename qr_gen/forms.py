from django import forms

class QRcodeForm(forms.Form):
    rest_name = forms.CharField(max_length=50,
                                label='Restaurant name',
                                widget = forms.TextInput(
                                    attrs={
                                        'class':'form-control',
                                        'placeholder':'restaurant name'
                                    }
                                ))
    url = forms.URLField(max_length=300,label='Menu URL',
                         widget=forms.URLInput(
                             attrs={
                                 'class':'form-control',
                                 'placeholder':'Enter URl'
                             }
                         ))