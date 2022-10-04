from django import forms
from .models import Santa, SantaMember


class SantaForm(forms.ModelForm):
    class Meta:
        model = Santa
        fields = (
            'label',
            'description',
            'draw_date',
        )


class SantaMemberForm(forms.ModelForm):
    class Meta:
        model = SantaMember
        fields = (
            'member',
            'target',
            'santa',
        )


class SantaMemberUpdateForm(forms.ModelForm):
    class Meta:
        model = SantaMember
        fields = (
            'target',
        )
