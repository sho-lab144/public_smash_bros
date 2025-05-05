# matches/forms.py

from django import forms
from django_select2 import forms as s2forms
from .models import Match
from django.core.validators import MinValueValidator, MaxValueValidator
from .choices import CHARACTER_CHOICES

class MatchForm(forms.ModelForm):
    RESULT_CHOICES = [
        ('win', '勝利'),
        ('loss', '負け'),
        ('draw', '引き分け'),
    ]

    STAGE_CHOICES = [
        ('terminus', '1.終点'),
        ('battlefield', '2.戦場'),
        ('small_battlefield', '3.小戦場'),
    ]

    my_character_id = forms.ChoiceField(
        choices=CHARACTER_CHOICES,
        label="自分のキャラ",
        widget=s2forms.Select2Widget
    )
    opponent_character_id = forms.ChoiceField(
        choices=CHARACTER_CHOICES,
        label="相手のキャラ",
        widget=s2forms.Select2Widget
    )
    win_or_loss = forms.ChoiceField(choices=RESULT_CHOICES, label="勝敗")
    fighting_strength = forms.IntegerField(
        label='戦闘力',
        validators=[
            MinValueValidator(1000000),
            MaxValueValidator(16000000)
        ],
        help_text='100万から1600万の範囲で入力してください。'
    )
    stage = forms.ChoiceField(choices=STAGE_CHOICES, label="対戦ステージ")

    class Media:
        js = ('django_select2/django_select2.js',)

    class Meta:
        model = Match
        fields = ['my_character_id', 'opponent_character_id', 'win_or_loss', 'fighting_strength', 'stage']
        labels = {
            'fighting_strength': '戦闘力',
        }
