from django.db import models
from django.utils import timezone
import uuid
from .choices import CHARACTER_CHOICES

class Match(models.Model):
    match_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    match_time = models.DateTimeField(default=timezone.now, verbose_name="対戦時間")
    my_character_id = models.IntegerField(choices=CHARACTER_CHOICES, verbose_name="自分のキャラ")
    opponent_character_id = models.IntegerField(choices=CHARACTER_CHOICES, verbose_name="相手のキャラ")
    win_or_loss = models.CharField(max_length=10, verbose_name="勝敗")
    fighting_strength = models.IntegerField(verbose_name="戦闘力")
    stage = models.CharField(max_length=100, verbose_name="対戦ステージ")

    def my_character_name(self):
        # このメソッド内でキャラクター名を直接取得
        character_dict = dict(CHARACTER_CHOICES)
        my_character_id = int(self.my_character_id)
        return character_dict.get(my_character_id, "不明なキャラクター")

    def opponent_character_name(self):
        # このメソッド内でキャラクター名を直接取得
        character_dict = dict(CHARACTER_CHOICES)
        opponent_character_id = int(self.opponent_character_id)
        return character_dict.get(opponent_character_id, "不明なキャラクター")

    def __str__(self):
        # 文字列表現の更新
        return f"{self.my_character_name()} vs {self.opponent_character_name()} at {self.match_time.strftime('%Y-%m-%d %H:%M')}"
    

    def get_win_or_loss_display(self):
      result_dict = {
        'win': '勝利',
        'loss': '負け',
        'draw': '引き分け',
    }
      return result_dict.get(self.win_or_loss, '不明')

    def get_stage_display(self):
      stage_dict = {
        'terminus': '1.終点',
        'battlefield': '2.戦場',
        'small_battlefield': '3.小戦場',
    }
      return stage_dict.get(self.stage, '不明')
