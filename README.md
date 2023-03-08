# goma
goma is a stochastic Go engine written in python

> **go•ma** [ごま]
> noun
> 1. *Sesamum indicum* Sesame plant, produces small oval seeds.

### Project Motivation:
This project is an outgrowth of [dango](https://github.com/gsobell/dango), with hope of being integrated back in the future. The goal isn't to compete with neural-net Go engines, rather to write a passably decent engine from scratch. It is very much a work in progress, and should be handled as such.

## Usage
### Installation
To download and launch, run the following:
```shell
git clone https://github.com/gsobell/goma.git
cd goma && chmod +x goma.py
./goma.py
```

To install on Arch-based distros, use the [PKGBUILD](https://github.com/gsobell/goma/blob/home/PKGBUILD):
```shell
curl -O https://raw.githubusercontent.com/gsobell/goma/home/PKGBUILD
makepkg -i
```


You can use goma with any board GUI that supports `GTP` For example, with [Sabaki](https://github.com/SabakiHQ/Sabaki), go to preferences -> engines -> add engine, and place `/{path to goma}/goma.py` in the path field.

There is also the `asciiboard()` function, uncommented by default, that provides an ascii terminal interface similar to GnuGo's `--mode ascii`.

## Features

### Current
* Places stones on the board randomly
* Only makes legal moves; passes at end of game
* Full [`GTP`](https://www.lysator.liu.se/~gunnar/gtp/) protocol

### Future
* Basic game logic
* Basic joseki (openings)
* Basic shape (group) library
* Help flag and information
* Game status estimation
* Moderate to heavy refactoring
* Use interpolation to make game heatmap

### Moonshots
* Monte Carlo Search Tree (MCST) Life/Death readouts

goma is already better than most humans (most humans don't know how to play go)

## Examples

Here's a recent game of goma v goma, run in Sabaki:
```
goma v. goma
------------
 ● : goma
 ○ : goma
 +---------------------------------------+
 | ● ● ● ● ● ○ ○ ● ● ● ● ● ○ · ● ● ● ● ● |
 | ● ● ● ● ○ · ○ ● ● ● ● ● ● ○ ● ● ○ ○ ● |
 | ● ● ● ● ○ ○ ○ ○ ● ● ● ● ● ● ○ ○ ○ ● ● |
 | ● ● ● ○ ○ ● ● ● ● ● ● ○ ○ ○ ○ ○ ● ● ● |
 | ● ● ● ● ○ ● ● ● ● ● ○ · ○ ○ ○ ○ ○ ○ ● |
 | · ● ○ ○ ● ● ● ● ● ● ○ ○ ○ ○ ○ ○ ○ ○ ● |
 | ● ○ ○ ○ ○ ● ● ● ● ● ● ○ ○ ○ ○ ○ ○ ○ ○ |
 | ● ○ ○ ○ ○ ○ ● ● ● ● ● ● ○ ● ○ ○ ○ ○ ○ |
 | ● ● ○ ○ ○ ○ ○ ● ● ● ● ● ● ● ● ○ ○ ○ ○ |
 | ○ ○ ○ ○ ● ● ● ● ● ● ● ● ● ○ ○ ○ ○ ○ ○ |
 | ○ ○ ○ ○ ● ● ○ ○ ● ● ● ● ● ○ ○ ○ ○ ○ ○ |
 | ○ ○ ○ ○ ○ ○ ○ ○ ● ● ● ● ● ○ ○ ○ ○ ○ ● |
 | ○ ○ ○ ○ ○ ○ ○ ○ ● ● ● ● ● ● ● ● ● ● ● |
 | ○ ○ ○ ○ ○ ○ ● ● ● ● ● ● ○ ○ ● ● ● ● ● |
 | ○ ○ ○ · ○ ● ● ● ● ● ● ● ○ ○ ● ● ● ● ● |
 | ○ ○ ○ ● ○ ● ● ● ● ● ● ● ○ · ● ● ● ● ● |
 | ○ ○ ○ ○ ○ ○ ● ● ● ● ● ● ● ○ ● ● ● ● ● |
 | ○ ○ ○ ○ ○ ● ● ● ● ● ● ● ● ● ● ● ● ● ● |
 | ○ ○ ○ ○ ○ ● ● ● ● ● ● ● ● ● ● ● ● ● ● |
 +---------------------------------------+
```
Currently all games goma plays against itself end in seki.

***

If you like this, you might also enjoy [dango](https://github.com/gsobell/dango).

For a very interesting overview of Computer Go and a bot in Rust: [rustygo](https://github.com/mratsim/rustygo).
