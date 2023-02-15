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
cd goma
chmod +x goma.py # make executable
```
You can use goma with any board GUI that supports `GTP` For example, with [Sabaki](https://github.com/SabakiHQ/Sabaki), go to preferences -> engines -> add engine, and place `/{path to goma}/goma.py` in the path field.

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

Here's a recent game of GnuGo v goma, run in Sabaki:
```
GnuGo v. goma
------------
X : GnuGo
O : goma
$$ 
$$ +-------------------+
$$ | O O O O X . X O O |
$$ | . O X X X X X . O |
$$ | O O X O O . O O O |
$$ | O O X X O O X X O |
$$ | X X X . X X X . X |
$$ | O O X X X . X X X |
$$ | . X X . X X O . O |
$$ | O X . X O X O X O |
$$ | . O X . O . X . O |
$$ +-------------------+
```
The game continued until GnuGo passed, and goma passed the following move.

***

If you like this, you might also enjoy [dango](https://github.com/gsobell/dango).
For an very intresting overview of Computer Go and a bot in Rust: [rustygo](https://github.com/mratsim/rustygo).
