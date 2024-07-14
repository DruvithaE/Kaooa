README

kaooa.py:

colour codes:
vulture: yellow
crow: Blue
default: red

- The game starts by displaying a star-shaped board on the screen. Each vertex of the star contains a circle representing a possible position for placing either a crow or a vulture.
- The first player to make a move is the crow. The player selects a circle on the board (i.e., a vertex of the star) to place the crow by clicking the mouse.
- After the crow's move, it's the vulture's turn. The vulture selects an empty circle (vertex) to place itself. If the move is invalid, it keeps waiting until its a valid move
- The game continues with players taking turns until one of the following conditions is met:
    - If the number of deaths of crows reaches 4 or more, the vulture wins.
    - If the vulture cannot make any valid move, the crow wins.
- Once all 7 crows have been placed, the crow to move is selected. Once selected, there's no option to change, and only that crow can be moved. To place it in a new position it should click on an empty vertex.
- If an invalid move is attempted during the crow's turn, it keeps waiting until a valid move is made.