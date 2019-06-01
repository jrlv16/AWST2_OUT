from django import forms


class ContactForm(forms.Form):
   SUBCHOICE = (('a',"Nos offres"),('b',"Nos services"),('c',"Autre demande"))
   subject = forms.ChoiceField(choices = SUBCHOICE, label='Sujet:')
   email = forms.EmailField(required =True, label='Votre mail:')
   message = forms.CharField(widget = forms.Textarea(attrs={'placeholder':'Votre message'}))


