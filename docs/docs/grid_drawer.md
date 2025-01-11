# GridDrawer Class

The `GridDrawer` class allows you to draw customizable grids on a Pygame screen. It includes options to control the appearance and spacing of both major and minor grid lines, as well as labels for the major grid lines.

## Constructor

Initializes the `GridDrawer` with customizable grid properties.

### Parameters

- `x_dist` (int, default=100): Distance between major vertical grid lines in pixels.
- `y_dist` (int, default=100): Distance between major horizontal grid lines in pixels.
- `color` (str, default="black"): Color of the major grid lines.
- `opacity` (float, default=0.5): Opacity of the major grid lines, between 0.0 and 1.0.
- `thickness` (int, default=3): Thickness of the major grid lines in pixels.
- `x_minor_dist` (int, default=20): Distance between minor vertical grid lines in pixels.
- `y_minor_dist` (int, default=20): Distance between minor horizontal grid lines in pixels.
- `minor_color` (str, default="black"): Color of the minor grid lines.
- `minor_opacity` (float, default=0.25): Opacity of the minor grid lines, between 0.0 and 1.0.
- `minor_thickness` (int, default=1): Thickness of the minor grid lines.

## Method: `draw_minor_vertical_lines`

Draws minor vertical grid lines on the screen.

### Parameters

- `screen` (pygame.Surface): The Pygame surface to draw on.
- `width` (int): Width of the screen.
- `height` (int): Height of the screen.

## Method: `draw_minor_horizontal_lines`

Draws minor horizontal grid lines on the screen.

### Parameters

- `screen` (pygame.Surface): The Pygame surface to draw on.
- `width` (int): Width of the screen.
- `height` (int): Height of the screen.

## Method: `draw_major_vertical_lines`

Draws major vertical grid lines with labels on the screen.

### Parameters

- `screen` (pygame.Surface): The Pygame surface to draw on.
- `width` (int): Width of the screen.
- `height` (int): Height of the screen.
- `font` (bool): The font used for labeling grid lines.

## Method: `draw_major_horizontal_lines`

Draws major horizontal grid lines with labels on the screen.

### Parameters

- `screen` (pygame.Surface): The Pygame surface to draw on.
- `width` (int): Width of the screen.
- `height` (int): Height of the screen.
- `font` (bool): The font used for labeling grid lines.

## Method: `draw_grid`

Draws the entire grid (minor and major lines with labels) on the current Pygame surface.

### Raises

- `RuntimeError`: If no Pygame screen is open.