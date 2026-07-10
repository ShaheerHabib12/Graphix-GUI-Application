# Patchwork Quilt Generator

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-blue)
![Status](https://img.shields.io/badge/Status-Coursework%20Project-success)
![License](https://img.shields.io/badge/License-Educational-lightgrey)

A Python program that procedurally generates a patchwork-quilt-style grid of graphical patches, with an interactive mode for adding, deleting, and moving individual patches. Built with `graphix`, a Tkinter-based teaching graphics library, as coursework for the M30299 Programming module at the University of Portsmouth.

---

## Project Overview

This project generates a square grid of quilt "patches," where each patch is drawn using one of three custom shape designs and coloured according to the diagonal/triangle region it falls into within the grid. The pattern (which design and colour a given row/column position receives) is entirely rule-based, driven by the cell's position relative to the grid's diagonal and edges, producing a symmetrical, quilt-like visual.

The project was developed to demonstrate procedural 2D graphics generation using an object-oriented graphics library, along with user input validation, coordinate geometry, and event-driven interaction (mouse clicks and key presses) for a "challenge" extension that turns the static quilt into an editable grid.

The main programming concepts demonstrated are: use of an external object-oriented graphics API, coordinate/geometry calculations to programmatically place shapes, conditional logic to implement a positional design rule set, input validation loops, and a Tkinter event loop driving interactive state (selection, creation, deletion, and movement of grid elements).

---

## Assignment Information

| Item | Details |
|---|---|
| University | University of Portsmouth |
| Module | M30299 – Programming |
| Assignment | Assignment #1 (Student ID: 2601143) |
| Language | Python 3 |
| Project Type | University Coursework |
| Academic Level | Undergraduate – BSc (Hons) Computer Science |

---

## Project Objectives

- Use an object-oriented graphics library (`graphix`) to programmatically draw and position custom shapes on a canvas.
- Implement multiple distinct patch designs built from primitive shapes (`Rectangle`, `Circle`, `Oval`).
- Apply positional/geometric rules to determine which design and colour is drawn at each grid cell, based on the cell's row and column.
- Validate user input from the console (grid size and colour selection) against a fixed set of allowed values.
- Extend the static drawing into an interactive application that responds to mouse clicks and keyboard input to edit the grid at runtime.

---

## Features

**Console Input & Validation**
- Prompts the user for a grid size, restricted to `5, 7, 9, 11, 13`.
- Prompts the user for three distinct colours, restricted to `red, green, blue, purple, magenta, orange`, re-prompting until three different valid colours are entered.

**Procedural Patchwork Grid**
- Generates an `size × size` grid of 100×100 pixel patches in a Tkinter window sized to fit the grid exactly.
- Three patch designs, each built from `graphix` primitives:
  - **Solid patch** – a single filled rectangle.
  - **"Last digit" patch** – a 10-step staircase built from stacked rectangles.
  - **"Penultimate" patch** – a 5×4 grid of alternating circles and ovals.
- Deterministic placement rule based on each cell's row/column position: the main diagonal, top row/right column, left column/bottom row, upper triangle, and lower triangle each receive a distinct combination of design and colour from the three chosen colours.

**Interactive Editing (Challenge Extension)**
- Click any cell to select it; a black border highlights the current selection.
- Press `Escape` to clear the current selection.
- Press keys `1`–`9` on an empty selected cell to create a new patch (mapping each of the three designs to each of the three chosen colours).
- Press `x` on an occupied cell to erase its patch.
- Use the arrow keys (`Up`, `Down`, `Left`, `Right`) to move the selected patch to an adjacent empty cell, provided the destination is within the grid bounds and unoccupied.
- Internal state for every placed patch (design type and colour) is tracked in a dictionary keyed by `(row, column)`, allowing patches to be looked up, erased, and redrawn during moves.

---

## Technologies Used

| Category | Details |
|---|---|
| Language | Python 3 |
| Graphics Library | `graphix` (a Tkinter-based object-oriented graphics module, adapted from John Zelle's `graphics.py`, provided for the M30299 module) |
| GUI Backend | Tkinter (via `graphix.Window`, which subclasses `tk.Canvas`) |
| Core Concepts | Procedural/rule-based graphics generation, coordinate geometry, event-driven programming (mouse and keyboard polling), input validation loops, dictionary-based state tracking |

---

## Project Structure

```text
Patchwork-Quilt-Generator/
│
├── main.py    # Main program: input handling, patch design functions, and the interactive main loop
├── graphix.py    # Supplied graphics library (Window, Point, shapes, Text, Entry)
└── README.md
```

---

## Code Architecture

### `graphix.py`
A supplied teaching library, not authored as part of this assignment, that wraps Tkinter's `Canvas` to provide an object-oriented drawing API. It exposes a `Window` class (mouse/keyboard polling via `check_mouse()` / `check_key()`) and drawable `GraphixObject` subclasses (`Point`, `Line`, `Circle`, `Oval`, `Rectangle`, `Polygon`, `Text`, `Entry`), each with settable `fill_colour`, `outline_colour`, and `outline_width` properties. `main.py` is built entirely on top of this API via `from graphix import *`.

### `main.py`
Contains all assignment logic, organised into four groups of functions:

- **User input** (`input_three_colour`, `input_colour`, `input_size`) – console-based prompts that validate the grid size and the three chosen colours against fixed allow-lists, re-prompting on invalid input.
- **Patch design functions** (`draw_solid_patch`, `draw_last_digit_patch`, `draw_penultimate_patch`) – each takes a window, an `(x, y)` origin, and a colour, and draws one of the three 100×100 patch designs using primitive `graphix` shapes.
- **Grid placement logic** (`draw_patch`) – given a cell's row and column, applies a positional rule set (diagonal, edges, upper/lower triangle) to decide which design and which of the three colours to draw, and records the result in the `patch_states` dictionary.
- **Interactive/challenge functions** (`click_to_cell`, `draw_border`, `erase_patch`, `create_patch_here`, `move_patch`) – translate pixel coordinates to grid cells, draw the selection border, and create, delete, or relocate patches in response to user input, keeping `patch_states` in sync with what is drawn.
- **`main()`** – collects user input, draws the background and initial patchwork grid, then runs a polling loop (`while win.is_open()`) that reads mouse clicks and key presses each frame to drive the interactive editing features.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ShaheerHabib12/Patchwork-Quilt-Generator.git
   ```
2. Navigate into the project folder:
   ```bash
   cd Patchwork-Quilt-Generator
   ```
3. Ensure `graphix.py` is present in the same directory as `main.py` (it is imported directly via `from graphix import *`).

No `pip install` step is required, as the project has no external dependencies beyond the supplied `graphix` module and the Python standard library.

---

## Requirements

- Python 3.8 or later (the codebase uses `from __future__ import annotations` and modern type hints)
- Tkinter (included with most standard Python installations; on some Linux distributions install via `sudo apt-get install python3-tk`)
- The `graphix.py` file must be located in the same directory as the main script

---

## How to Run

From the project's root directory:

```bash
python main.py
```

The program will first ask for input in the terminal before opening the graphics window.

---

## Usage

1. When prompted in the terminal, enter a grid size from `5, 7, 9, 11, 13`.
2. Enter three different colours, one at a time, each chosen from `red, green, blue, purple, magenta, orange`.
3. A Tkinter window opens showing the generated patchwork grid, sized to the chosen dimensions.
4. To edit the grid interactively:
   - **Click** a cell to select it (a black border appears around it).
   - Press **Escape** to deselect.
   - Press **1–9** on an empty selected cell to add a patch (each number maps to one of the three designs in one of the three chosen colours).
   - Press **x** on an occupied selected cell to remove its patch.
   - Use the **arrow keys** to move the selected patch into an adjacent empty cell.
5. Closing the window ends the program.

---

## Learning Outcomes

This project demonstrates practical experience with:

- Using a third-party object-oriented graphics API to draw and style shapes programmatically.
- Translating coordinate/geometry calculations (cell size, offsets, radii) into correctly positioned graphical output.
- Implementing conditional, position-based logic to generate a deterministic, rule-driven visual pattern across a grid.
- Writing robust console input validation loops that reject and re-prompt on invalid values.
- Handling Tkinter-style event polling (`check_mouse`, `check_key`) to build an interactive, stateful application loop.
- Maintaining an external state structure (a dictionary keyed by grid coordinates) that stays synchronised with what is currently drawn on screen.
- Working within the constraints of a supplied library (`graphix`) rather than a general-purpose GUI framework.

---

## Challenges

- Calculating correct pixel offsets for the circle/oval grid pattern in `draw_penultimate_patch`, so that alternating rows and columns of circles and ovals tile consistently within a fixed 100×100 patch.
- Keeping the `patch_states` dictionary consistent with what is actually drawn on the canvas across create, erase, and move operations, since `graphix` does not track object placement by grid coordinate itself.
- Constraining interactive patch movement to valid, unoccupied grid cells while reusing the same design/colour rendering logic used for the initial static grid.
- Structuring input validation so that the three required colours are guaranteed to be distinct without duplicating validation code for each prompt.

---

## Future Improvements

- Add error handling around patch-type dispatch in the move logic to guard against unrecognised patch types.
- Allow the patch design used for the "create" shortcuts (keys 1–9) to be chosen independently of the three colours picked at startup.
- Support saving and reloading a custom-edited grid layout (e.g. via JSON), similar in spirit to state persistence in other coursework projects.
- Add an on-screen legend or status bar showing the current selection, grid size, and colour key.
- Allow the grid size and colours to be adjusted without restarting the program.

---

## Screenshots

> Screenshots of the running application should be added here to showcase the generated patchwork and interactive editing.

- `docs/screenshots/patchwork-grid.png` — Initial generated patchwork grid
- `docs/screenshots/patch-selected.png` — A selected patch with border highlight
- `docs/screenshots/patch-editing.png` — Adding/moving a patch interactively

---

## Author

**Muhammad Shaheer Habib**
BSc (Hons) Computer Science
University of Portsmouth

GitHub: [https://github.com/ShaheerHabib12](https://github.com/ShaheerHabib12)

---

## Acknowledgements

This project was developed as part of the **M30299 Programming** module at the **University of Portsmouth** for educational purposes. The `graphix` module is a supplied teaching library adapted from John Zelle's `graphics.py`, provided for use on the module and not authored as part of this assignment.

---

## License

This repository is intended for educational and portfolio purposes.
© Muhammad Shaheer Habib
