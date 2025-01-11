# About GridDrawer

The `GridDrawer` class is a Python utility designed to assist developers in creating customizable grid patterns within Pygame applications. It provides options to control the appearance, spacing, and labeling of both major and minor grid lines, making it ideal for game development, simulations, or visual design tools.

---

## Features

### Customizable Grid Lines

The `GridDrawer` class allows users to define the:

- Distance between major grid lines (`x_dist`, `y_dist`)
- Thickness, color, and opacity of major lines (`thickness`, `color`, `opacity`)
- Distance between minor grid lines (`x_minor_dist`, `y_minor_dist`)
- Thickness, color, and opacity of minor lines (`minor_thickness`, `minor_color`, `minor_opacity`)

### Labels for Major Lines

Major grid lines can include labels to enhance usability, making it easy to reference positions within the grid.

### Fully Integrated with Pygame

The class is built for Pygame, seamlessly working with Pygame surfaces for rendering.

---

## Use Cases

1. **Game Development**:
   
   - Implementing tiled-based games like strategy or puzzle games.
   - Creating map editors.

2. **Visualizations**:
   
   - Drawing grids for data visualization or simulations.

3. **UI/UX Design**:
   
   - Designing interfaces with precise alignment.

---

## Getting Started

### Installation

Ensure you have Pygame installed. If not, install it using:

```bash
pip install pygame
```

### Example Usage

```python
import pygame
from pygame_grid import GridDrawer

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("GridDrawer Example")

# Create GridDrawer instance
grid = GridDrawer()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # Fill screen with white

    # Draw grid
    grid.draw_grid(screen, width=800, height=600)

    pygame.display.flip()

pygame.quit()
```

---

## Contributions

Contributions to the `GridDrawer` project are welcome! Feel free to submit pull requests or raise issues on the repository.

---

## License

The `GridDrawer` class is licensed under the MIT License. See the `LICENSE` file for details.
