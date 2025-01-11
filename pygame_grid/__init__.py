import pygame

class GridDrawer:
    """
    A class for drawing a customizable grid on a Pygame screen.

    Attributes:
        x_dist ( int ): Distance between major vertical grid lines in pixels.
        y_dist ( int ): Distance between major horizontal grid lines in pixels.
        color ( str ): Color of the major grid lines.
        opacity ( float ): Opacity of the major grid lines, between 0.0 and 1.0.
        thickness ( int ): Thickness of the major grid lines in pixels.
        x_minor_dist ( int ): Distance between minor vertical grid lines in pixels.
        y_minor_dist ( int ): Distance between minor horizontal grid lines in pixels.
        minor_color ( str ): Color of the minor grid lines.
        minor_opacity ( float ): Opacity of the minor grid lines, between 0.0 and 1.0.
        minor_thickness ( int ): Thickness of the minor grid lines in pixels.
    """

    def __init__(self, 
                 x_dist: int = 100, 
                 y_dist: int = 100, 
                 color: str = "black", 
                 opacity: float = 0.5, 
                 thickness: int = 3, 
                 x_minor_dist: int = 20, 
                 y_minor_dist: int = 20, 
                 minor_color: str = "black", 
                 minor_opacity: float = 0.25, 
                 minor_thickness: int = 1) -> None:
        """
        Initializes the GridDrawer with customizable grid properties.
        
        """
        self.x_dist = x_dist
        self.y_dist = y_dist
        self.color = color
        self.opacity = opacity
        self.thickness = thickness
        self.x_minor_dist = x_minor_dist
        self.y_minor_dist = y_minor_dist
        self.minor_color = minor_color
        self.minor_opacity = minor_opacity
        self.minor_thickness = minor_thickness

    def draw_minor_vertical_lines(self, screen: pygame.Surface, width: int, height: int) -> None:
        """
        Draws minor vertical grid lines on the screen.

        Args:
            screen ( pygame.Surface ): The Pygame surface to draw on.
            width ( int ): Width of the screen.
            height ( int ): Height of the screen.
        """
        for x in range(self.x_minor_dist, width, self.x_minor_dist):
            if x % self.x_dist != 0:
                line_surface = pygame.Surface((self.minor_thickness, height), pygame.SRCALPHA)
                line_surface.fill(self.minor_color)
                line_surface.set_alpha(int(self.minor_opacity * 255))
                screen.blit(line_surface, (x - self.minor_thickness // 2, 0))

    def draw_minor_horizontal_lines(self, screen: pygame.Surface, width: int, height: int) -> None:
        """
        Draws minor horizontal grid lines on the screen.

        Args:
            screen ( pygame.Surface ): The Pygame surface to draw on.
            width ( in t): Width of the screen.
            height ( int ): Height of the screen.
        """
        for y in range(self.y_minor_dist, height, self.y_minor_dist):
            if y % self.y_dist != 0:
                line_surface = pygame.Surface((width, self.minor_thickness), pygame.SRCALPHA)
                line_surface.fill(self.minor_color)
                line_surface.set_alpha(int(self.minor_opacity * 255))
                screen.blit(line_surface, (0, y - self.minor_thickness // 2))

    def draw_major_vertical_lines(self, screen: pygame.Surface, width: int, height: int, font: bool = False) -> None:
        """
        Draws major vertical grid lines with labels on the screen.

        Args:
            screen ( pygame.Surface ): The Pygame surface to draw on.
            width ( int ): Width of the screen.
            height ( int ): Height of the screen.
            font ( True | False ): The font used for labeling grid lines.
        """
        font_a = pygame.font.SysFont("Arial", 12)
        for x in range(self.x_dist, width, self.x_dist):
            line_surface = pygame.Surface((self.thickness, height), pygame.SRCALPHA)
            line_surface.fill(self.color)
            line_surface.set_alpha(int(self.opacity * 255))
            screen.blit(line_surface, (x - self.thickness // 2, 0))
            if font:
                label = font_a.render(str(x), True, self.color)
                label.set_alpha(int(self.opacity * 255))
                label = pygame.transform.rotate(label, -90)
                screen.blit(label, (x - 13, 1))

    def draw_major_horizontal_lines(self, screen: pygame.Surface, width: int, height: int, font: bool = False) -> None:
        """
        Draws major horizontal grid lines with labels on the screen.

        Args:
            screen ( pygame.Surface ): The Pygame surface to draw on.
            width ( int ): Width of the screen.
            height ( int): Height of the screen.
            font : The font used for labeling grid lines.
        """
        font_a = pygame.font.SysFont("Arial", 12)
        for y in range(self.y_dist, height, self.y_dist):
            line_surface = pygame.Surface((width, self.thickness), pygame.SRCALPHA)
            line_surface.fill(self.color)
            line_surface.set_alpha(int(self.opacity * 255))
            screen.blit(line_surface, (0, y - self.thickness // 2))
            if font:
                label = font_a.render(str(y), True, self.color)
                label.set_alpha(int(self.opacity * 255))
                screen.blit(label, (1, y - 13))

    def draw_grid(self) -> None:
        """
        Draws the entire grid (minor and major lines with labels) on the current Pygame surface.

        Raises:
            RuntimeError: If no Pygame screen is open.
        """
        screen = pygame.display.get_surface()
        if screen is None:
            raise RuntimeError("There is no pygame screen open!")
        
        width, height = screen.get_size()
        font = pygame.font.SysFont("Arial", 12)

        self.draw_minor_vertical_lines(screen, width, height)
        self.draw_minor_horizontal_lines(screen, width, height)
        self.draw_major_vertical_lines(screen, width, height, font)
        self.draw_major_horizontal_lines(screen, width, height, font)
