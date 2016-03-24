#!/usr/bin/python
# -*- coding: utf-8 -*-
from store.models import Store
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (Submit,
                                 ButtonHolder, Div, Field)
from django import forms
from django.utils.translation import ugettext as _

class StoreModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StoreModelForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)

        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('save', 'save'))

    def clean(self):
        super(StoreModelForm, self).clean()
        try:
            store = Store(**self.cleaned_data)
            store.save()
        except Exception:
            raise forms.ValidationError(_("Correct the form below"))
        return self.cleaned_data

    class Meta:
        model = Store
        fields = ('name', "address")
