# goma
goma is a stochastic Go engine written in python

> **go•ma** [ごま]
> noun
> 1. *Sesamum indicum* Sesame plant, produces small oval seeds.

>small seed of far reach <br>
>white flower in summer blooms <br>
>from oval take oil

### Project Motivation:
This project is an outgrowth of [dango](https://github.com/gsobell/dango), with hope of being integrated back it at a later date, when both are functional. The goal isn't to compete with neural-net Go engines, rather to write a passably decent knowledge based engine from scratch.

## Usage
### Installation
To download and launch, run the following:
```shell
git clone https://github.com/gsobell/goma.git
cd goma
chmod +x goma.py # make executable
```
You can use goma with any board GUI that supports `GTP` For example, with [Sabaki](https://github.com/SabakiHQ/Sabaki), go to preferences -> engines -> add engine, and place `/{path to goma}/goma.py` in the path field.

## Features

### Current
* Places stones on the board randomly
* Conforms to [`GTP`](https://www.lysator.liu.se/~gunnar/gtp/) protoccol
* Nigiri pre-game (similar to coin toss)

### Future
* Basic game logic (including keeping track of captures)
* Basic joseki (openings)
* Basic shape (group) library
* Game status estimation
* Moderate to heavy refactoring
* Use interpolation to make game heatmap

### Moonshots
* Monte Carlo Search Tree (MCST) Life/Death readouts

goma is already better than most humans (most humans don't know how to play go)

## Examples

Here's a recent game of GnuGo v goma, run in Sabaki:
```
GnuGo v goma
------------
X : goma
O : GnuGo
$$ +---------------------------------------+
$$ | . . . . . . . . . . . . . . . . . . . |
$$ | . . . . . . . . . . . . . . . . . . . |
$$ | . . . X . . . O . . . O . . X . O . . |
$$ | . . . , X . . O X O . . O . . , . . . |
$$ | . . O . . X . O O . X . . . O . O . . |
$$ | . . . . . . X . . . . . . . . . . . . |
$$ | . . . . . X . . . X . . . . . . . . X |
$$ | . . . . . . . . . . X . . . . . . . . |
$$ | . X X . . . . . . . . . . . X . . . . |
$$ | . . . , . . . . . , . . . . . , . O . |
$$ | . . . . . . . . . . . . . . . . O X . |
$$ | . . . . . . . . . O . . . . . O . . X |
$$ | . . . . . . . . O . X . . . . . . . . |
$$ | . . . . . . . X . . . . . . . . . . . |
$$ | . . . . . X . . . O . O . . . . . X . |
$$ | . . X , . . . . . , . . . . O , O O . |
$$ | . X . . . . O . . O . X . . . O X . . |
$$ | . . X . . . . X . . . O . . . . . . . |
$$ | . . . . X . . . . . . . . . . . . . . |
$$ +---------------------------------------+
```
The game continued until goma made an illegal move and GnuGo crashed.

***

If you like this, you might also enjoy [dango](https://github.com/gsobell/dango), [cbonsai](https://gitlab.com/jallbrit/cbonsai), [sabaki](https://github.com/SabakiHQ/Sabaki), [baduk-fortune](https://github.com/gsobell/baduk-fortune), and [haikunator](https://github.com/usmanbashir/haikunator).
