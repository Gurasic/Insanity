
import tcod


def main() -> None:
    # Screen Hight and Width
    screen_width = 80
    screen_height = 50

    # Player X and Y Position
    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    # Loads the Tileset file "dejavu10x10_gs_tc"
    tileset = tcod.tileset.load_tilesheet(
        "assets/tilesets/dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    # This Builds the Screen, takes the Width and Hight and a Title and also a Tileset, wich is what we difined before
    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Yet Another Roguelike Tutorial",
        vsync=True,
    ) as context:

        # This Creates Our "Console" which is what we’ll be drawing to
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:

            # This Prints the String in its X and Y Position of the Player on the "Console"
            root_console.print(x=player_x, y=player_y, string="@")

            # "context.present" is what actually updates the screen with what we’ve told it to display so far.
            context.present(root_console)

            # This allows for an Exit (Pressing the X button to close the Program)
            for event in tcod.event.wait():
                if event.type == "QUIT":
                    raise SystemExit()


if __name__ == "__main__":
    main()