# uppercase = white piece
# lowercase = black piece

class Board:
    def __init__(self):
        # Flat 64-square list representing the board.
        # Index 0 = a1, index 7 = h1, index 56 = a8, index 63 = h8.
        # Index formula: row * 8 + col (see index() below).
        self.squares = [
            "R", "N", "B", "Q", "K", "B", "N", "R",
            "P", "P", "P", "P", "P", "P", "P", "P",  
            ".", ".", ".", ".", ".", ".", ".", ".", 
            ".", ".", ".", ".", ".", ".", ".", ".",  
            ".", ".", ".", ".", ".", ".", ".", ".",  
            ".", ".", ".", ".", ".", ".", ".", ".",
            "p", "p", "p", "p", "p", "p", "p", "p", 
            "r", "n", "b", "q", "k", "b", "n", "r"   
        ]

        self.side_to_move = "w"  # "w" = White to move, "b" = Black to move
        self.castling_rights = {"K": True, "Q": True, "k": True, "q": True}
        self.en_passant_target = None
        self.halfmove_clock = 0
        self.fullmove_number = 1

    def index(self, row, col):
        # Converts a (row, col) pair INTO a single flat-list index.
        # Example: index(2, 3) -> 19 (just the position number, not the piece).
        return row * 8 + col

    def row_col(self, index):
        # Converts a flat-list index BACK INTO a (row, col) pair.
        # This is the reverse of index() above.
        # Example: row_col(19) -> (2, 3)
        return divmod(index, 8)

    def get(self, index):
        # Returns the piece (or ".") actually stored at this index.
        # e.g. get(19) -> "." if that square is empty.
        return self.squares[index]

    def set(self, index, piece):
        # Places a piece (or ".") at this index.
        self.squares[index] = piece

    def is_empty(self, index):
        # True if this square has no piece on it.
        if self.squares[index] == ".":
            return True
        else: 
            return False

    def is_white(self, piece):
        # White pieces are uppercase letters.
        return piece.isupper()

    def is_black(self, piece):
        # Black pieces are lowercase letters (excluding "." for empty squares).
        return piece.islower() and piece != "."

    def copy(self):
        # Returns a new Board with the same state, for search to branch on
        # without mutating the original (no make/unmake yet, per design).
        new_board = Board.__new__(Board)  # skip __init__, avoid rebuilding start pos
        new_board.squares = self.squares.copy()
        new_board.side_to_move = self.side_to_move
        new_board.castling_rights = self.castling_rights.copy()
        new_board.en_passant_target = self.en_passant_target
        new_board.halfmove_clock = self.halfmove_clock
        new_board.fullmove_number = self.fullmove_number
        return new_board

    # --- display ---
    def print_board(self):
        # Prints the board top-down (row 7 = Black's back rank first),
        # matching how a chessboard is normally viewed.
        for row in range(7, -1, -1):
            start = row * 8
            print(" ".join(self.squares[start:start + 8]))


if __name__ == "__main__":
    # Quick manual check: run this file directly to see the starting position.
    board = Board()
    board.print_board()