# -*- coding: utf-8 -*-
# FILE: sample.py
# AUTHOR: koturn <jeak.koutan.apple@gmail.com>
# License: MIT License

from .base import Base

class Kind(Base):
    def __init__(self, vim):
        super().__init__(vim)
        # kindの名前．この名前をsourceで指定することにより，関連付けられる
        self.name = 'sample'
        # デフォルトのアクション(候補上で<CR>を押下したときに実行するアクション)を指定する．
        # self.default_action = 'xxx' と指定すると，このクラスのメソッド:
        # action_xxx() が呼び出される
        self.default_action = 'sample'

    def action_sample(self, context):
        '''
        コンストラクタで指定したように，デフォルトのアクションを記述する関数
        '''
        for target in context['targets']:
            filepath = target['word']
            print(filepath + ' has ' + str(sum(1 for line in open(filepath, encoding='utf-8'))) + ' lines')

    def action_preview(self, context):
        '''
        候補上にカーソルが移動する度に呼び出される関数
        :Denite -auto-preview ... のように -auto-preview オプションを付加すると，previewモードになる
        付加しない場合でも，以下のキーを押下することでpreview動作を行うことは可能
          insertモード: <C-v>
          normalモード: p
        return Trueとしないと，deniteが終了する
        '''
        # context['targets'] に source側のgether_candidatesの返り値が格納されている
        filepath = context['targets'][0]['word']
        print(filepath + ' has ' + str(sum(1 for line in open(filepath, encoding='utf-8'))) + ' lines')
        return True
