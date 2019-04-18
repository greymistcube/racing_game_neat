# Racing Game with NEAT

![Game Screen](./docs/img/racing_game_ai_peek.gif)

More information about this project can be found on
[this github page.](https://greymistcube.github.io/racing_game_ai/)

## Dependencies

[![pygame][pygame_img]][pygame_url]
[![numpy][numpy_img]][numpy_url]

This project only requires numpy and pygame packages to run.
To install the required packages, run the following commands.
```
pip install numpy
pip install pygame
```

## Usage Examples

Run with
```
python game.py
```
to start the game normally in a playable mode with the default settings.
Various command line arguments may be passed on to change the settings.
For example,
```
python game.py -z3 -n200 neat
```
will start the game with 3x display zoom and 200 cars per generation for
the AI to train on. For more help, run the program with `-h` as its argument.

## Controls
Use <kbd>&uarr;</kbd>, <kbd>&darr;</kbd>, <kbd>&larr;</kbd>, and <kbd>&rarr;</kbd>
keys to control the car. Number keys <kbd>0</kbd>, ..., <kbd>9</kbd>
may be used to change the game speed. This is mainly used to speed up
the training process for the AI.
Use <kbd>i</kbd> to toggle the information overlay and <kbd>d</kbd>
to show the debug screen.

<!-- Markdown link & image definitions -->
[pygame_img]: https://img.shields.io/badge/pygame-1.9.4-brightgreen.svg
[pygame_url]: https://www.pygame.org/
[numpy_img]: https://img.shields.io/badge/numpy-1.16.2-brightgreen.svg
[numpy_url]: https://www.numpy.org/
