import tcod

from engine import Engine
from Inputs.input_handlers import EventHandler
from entity import Entity
from game_map import GameMap


def main() -> None:
    # Screen Hight and Width
    screen_width = 80
    screen_height = 50
    map_width = 80
    map_height = 45

    # Loads the Tileset file "dejavu10x10_gs_tc"
    tileset = tcod.tileset.load_tilesheet(
        "assets/tilesets/dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 255, 255))
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "@", (255, 255, 0))
    entities = {npc, player}

    game_map = GameMap(map_width, map_height)

    engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)

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
            engine.render(console=root_console, context=context)

            # "context.present" is what actually updates the screen with what we’ve told it to display so far.
            events = tcod.event.wait()

            # Clears the console
            root_console.clear()

            # This Entire Thing is for adding the stuff from Input_handlers.py/Actions.py or somth
            engine.handle_events(events)


if __name__ == "__main__":
    main()
