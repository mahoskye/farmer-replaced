# Game Snippets

Each of these snippets is a function window within the game. Since each window within the game is in the same code space, they don't require anything special to reference one another.

## Snippet Relationships

### Main Loop

This is the core loop I use when I want to farm a wide variety of crops.

- main.py
- action_controller.py
- do_trade.py
- make_move.py
- plant_controller.py
- sunflowers.py

### Pumpkin Loop

For when you just want a bunch of pumpkins.

- pumpkin_farmin.py
- do_trade.py
- make_move.py
- plant_controller.py

### Flower Power

For when you just want a bunch of sunflowers.

- flower_power.py
- do_trade.py
- make_move.py
- plant_controller.py
- sunflowers.py

### Maze Loop

Creating and solving the maze is a very different problem from the farming aspect of the game. This is a separate loop that I run when I want to solve the maze.

- maze_main.py

### Scratch Pads

These are just snippets of code that I use to test out ideas.

- f0.py - used this to check if an unlock was available
- f1.py - testing out general ideas and primarily a todo list.
- f2.py - this snippet floods the map with cactus in order to build up the required amount to unlock Dinosaurs.
- carrots.py - early attempt at a carrot farming loop.
- tree.py - early attempt at a tree farming loop.
- pumpkins.py - early attempt at a pumpkin farming loop.
- sunflower_mania.py - [broken] early attempt at a sunflower farming loop.
