# Rubik's Cube Solver

This is a Python-based Rubik's Cube Solver that uses the Kociemba algorithm to find a solution for any valid 3x3 Rubik's Cube configuration. The project includes a graphical user interface (GUI) built with `tkinter` to visualize the cube and interactively solve it.

## Features

- **Interactive GUI**: Visualize the Rubik's Cube and input your own cube configuration.
- **Step-by-Step Solution**: Solve the cube step-by-step with the ability to move forward and backward through the solution.
- **Color Picker**: Easily set the colors of each face using a color picker.
- **Reset Functionality**: Reset the cube to its initial state or redesign it.

## Requirements

- Python 3.x
- `tkinter` (usually comes pre-installed with Python)
- `kociemba` library (`pip install kociemba`)

## How to Use

1. **Clone the Repository**:
    git clone https://github.com/your-username/rubiks-cube-solver.git
    cd rubiks-cube-solver
3. **Install Dependencies** :
    pip install kociemba
4. **Run the programme** :
    python gui.py


## Using the GUI:
1. Use the color picker to set the colors of each face.
2. Click "Submit" to solve the cube.
3. Use the "Next" and "Prev" buttons to navigate through the solution steps.
4. Click "Reset" to clear the cube and start over.
