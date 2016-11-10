vim-denite-sample
=================

Sample denite-source.


## Usage

```vim
:Denite sample
```

Preview action is also available.

```vim
:Denite -auto-preview sample
```


## Installation

### With [dein.vim](https://github.com/Shougo/neobundle.vim)

Write following code to your `.vimrc` and execute `:call dein#install()` in
your Vim.

```vim
call dein#add('koturn/vim-denite-sample', {
      \ 'on_source': 'denite.nvim'
      \})
```

### With [NeoBundle](https://github.com/Shougo/neobundle.vim)

Write following code to your `.vimrc` and execute `:NeoBundleInstall` in your
Vim.

```vim
NeoBundle 'koturn/vim-denite-sample'
```

If you want to use `:NeoBundleLazy`, write following code in your .vimrc.

```vim
NeoBundle 'koturn/vim-denite-sample', {
      \ 'on_source': 'denite.nvim'
      \}
```

### With [Vundle](https://github.com/VundleVim/Vundle.vim)

Write following code to your `.vimrc` and execute `:PluginInstall` in your Vim.

```vim
Plugin 'koturn/vim-denite-sample'
```

### With [vim-plug](https://github.com/junegunn/vim-plug)

Write following code to your `.vimrc` and execute `:PlugInstall` in your Vim.

```vim
Plug 'koturn/vim-denite-sample'
```

### With [vim-pathogen](https://github.com/tpope/vim-pathogen)

Clone this repository to the package directory of pathogen.

```
$ git clone https://github.com/koturn/vim-denite-sample.git ~/.vim/bundle/vim-denite-sample
```

### With packages feature

In the first, clone this repository to the package directory.

```
$ git clone https://github.com/koturn/vim-denite-sample.git ~/.vim/pack/koturn/opt/vim-denite-sample
```

Second, add following code to your `.vimrc`.

```vim
packadd vim-denite-sample
```

### With manual

If you don't want to use plugin manager, put files and directories on
```~/.vim/```, or ```%HOME%/vimfiles/``` on Windows.


## Dependent plugins

### Required

- [Shougo/denite.nvim](https://github.com/Shougo/denite.nvim)


## LICENSE

This software is released under the MIT License, see [LICENSE](LICENSE).
