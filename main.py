
import tcod

from Inputs.actions import EscapeAction, MovementAction
from Inputs.input_handlers import EventHandler

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
    
    event_handler = EventHandler()
    # This Builds the Screen, takes the Width and Hight and a Title and also a Tileset, wich is what we difined before
    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Gaming",
        vsync=True,
    ) as context:

        # This Creates Our "Console" which is what we’ll be drawing to
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:

            # This Prints the String in its X and Y Position of the Player on the "Console"
            root_console.print(x=player_x, y=player_y, string="@")

            # "context.present" is what actually updates the screen with what we’ve told it to display so far.
            context.present(root_console)

            # Clears the console
            root_console.clear()

            # This Entire Thing is for adding the stuff from Input_handlers.py/Actions.py or somth
            for event in tcod.event.wait():
                action = event_handler.dispatch(event)

                if action is None:
                    continue

                if isinstance(action, MovementAction):
                    player_x += action.dx
                    player_y += action.dy

                elif isinstance(action, EscapeAction):
                    raise SystemExit()


if __name__ == "__main__":
    main()