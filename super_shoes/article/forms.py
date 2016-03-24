#!/usr/bin/python
# -*- coding: utf-8 -*-
from article.models import Article
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (Submit,
                                 ButtonHolder, Div, Field)
from django.conf import settings
from django import forms
from django.utils.translation import ugettext as _

def v_number(value):
    try:
        if not int(value):
            raise forms.ValidationError(_('must be a valid number'),
                                        code='invalid')
    except ValueError:
        raise forms.ValidationError(
            _('Invalid value. Must be numeric'),
            code='invalid',
        )


class ArticleModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ArticleModelForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)

        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('save', 'save'))

    def clean(self):
        super(ArticleModelForm, self).clean()
        try:
            article = Article(**self.cleaned_data)
            article.save()
        except Exception:
            raise forms.ValidationError(_("Correct the form below"))
        return self.cleaned_data

    class Meta:
        model = Article
        fields = ('name', "description", 'price', 'total_in_vault',
                  'total_in_shelf', 'store')

