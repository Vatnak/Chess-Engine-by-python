# Chess Engine

A chess engine built from scratch in Python — board representation, legal move generation, and a minimax/alpha-beta search with a hand-crafted evaluation function. No external chess libraries used for the core logic; the goal is to implement the rules, search, and evaluation myself.

## Why this project

Built as a portfolio piece to demonstrate:
- Data structures and algorithmic thinking (board representation, move generation, tree search)
- Search optimization (minimax → alpha-beta pruning → move ordering → iterative deepening)
- Clean separation between core logic and interface (the engine has zero knowledge of the CLI or web layer)

## Project structure

```
chess_engine/     # core engine package — pure chess logic, no I/O
  constants.py     # piece values, square helpers, piece-square tables
  board.py         # Board: 64-square array + side to move, castling rights, en passant, clocks
  moves.py         # Move representation + pseudo-legal/legal move generation
  notation.py      # FEN and PGN import/export
  search.py        # minimax, alpha-beta pruning, iterative deepening
  evaluation.py    # material + positional scoring

tests/             # unit tests, including perft correctness tests for move generation

cli/               # terminal interface (first playable version)

web/               # web UI wrapping the engine (added later)
```

## Design decisions

- **Board storage**: flat list of 64 squares (`index = rank * 8 + file`), rather than a 2D grid — simpler index arithmetic for move generation.
- **Piece encoding**: single characters matching FEN convention (`P N B R Q K` white, lowercase black, empty for no piece) — keeps FEN import/export nearly free.
- **Move application**: board is copied on each move during search (not mutated in place with make/unmake). Simpler to get correct first; a make/unmake refactor is a planned future optimization.

## Status

🚧 In early planning/development. Board representation and file structure are designed; move generation, search, and evaluation are not yet implemented.

## Roadmap

- [ ] Board representation + initial position setup from FEN
- [ ] Pseudo-legal move generation per piece type
- [ ] Legal move filtering (check detection) + perft tests
- [ ] Game state tracking (castling rights, en passant, move clocks) + FEN/PGN
- [ ] Minimax search
- [ ] Alpha-beta pruning + move ordering + iterative deepening
- [ ] Evaluation function (material → piece-square tables → heuristics)
- [ ] CLI interface
- [ ] Web interface + deployment
- [ ] README write-up of algorithms for portfolio presentation

## Running it

_(To be filled in once the CLI is functional.)_

## License

MIT