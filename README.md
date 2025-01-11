# Pygame Grid

The `Pygame Grid` module provides a utility function to draw customizable grids on the active Pygame screen. It simplifies the process of placing and aligning elements in Pygame applications, making it particularly useful for game development, UI design, and visualizations.

This module is a work in progress and will continue to evolve with additional features and enhancements over time. For detailed and advanced grid drawing capabilities, consider using the `GridDrawer` class.

---

## Installation and Usage

1. Install Python from [python.org](https://www.python.org/) if not already installed.

2. Open a terminal or command prompt and install Pygame:
   
   ```bash
   pip install pygame pygame-grid
   ```

---

### Example Usage

```python
import pygame
from grid_drawer import GridDrawer

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

Thank you for using the `Pygame Grid` module! Stay tuned for updates and feel free to contribute or provide feedback to help improve this tool further.
