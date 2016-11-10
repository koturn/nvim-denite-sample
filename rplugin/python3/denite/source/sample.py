# -*- coding: utf-8 -*-
# FILE: sample.py
# AUTHOR: koturn <jeak.koutan.apple@gmail.com>
# License: MIT License

from .base import Base
import glob
import itertools
import os


class Source(Base):
    def __init__(self, vim):
        #  このvimという引数はVimとPythonで相互にやりとりするためのインタフェース
        # :help pyth を参照すれば，おおよそのことが記述してある
        super().__init__(vim)
        # Denite xxx の xxx に相当する部分
        self.name = 'sample'
        # kind名を指定
        self.kind = 'sample'

    def on_init(self, context):
        '''
        このsourceが指定されて起動されたときに呼び出される．
        元のバッファのファイルタイプの取得などに利用する．
        今回は必要ないので，とりあえずechomsgしておく
        '''
        # print() は :echomsg と同等
        print('on_init')
        # filetypeなどの値は，以下のように context のキーとして生やす
        # selfのメンバにするのはよくない
        # context['__filetype'] = self.vim.eval('&filetype')

    def on_close(self, context):
        '''
        Denite終了時に呼び出される．
        '''
        # コンストラクタ以外では，self.vim を参照して，Vimインタフェースを利用する
        print('on_close')

    def gather_candidates(self, context):
        '''
        候補の取得を行う関数
        '''
        # sourceの引数context['args']はユーザがDenite実行時に以下のように : 区切りで指定する
        #   Denite sample:arg1:arg2:arg3
        dirpaths = ['~'] if len(context['args']) == 0 else context['args']
        print(dirpaths)
        candidates = filter(lambda path: os.path.isfile(path),
                        itertools.chain.from_iterable(
                            map(lambda dirpath: glob.glob(os.path.expanduser(dirpath) + '/*'), dirpaths)))
        # 辞書を返す
        #   word: 候補欄に表示される文字列
        #   アクション側で利用するための情報を増やしたい場合は 'action__xxx'
        #   という名前のキーを利用すること
        return list(map(
            lambda candidate: {
                'word': candidate},
            candidates))
