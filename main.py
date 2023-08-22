import tcod

from engine import Engine
from Inputs.input_handlers import EventHandler
from procgen import generate_dungeon
import copy
import entity_factories
import color
import traceback


def main() -> None:
    # Screen Hight and Width
    screen_width = 80
    screen_height = 50
    map_width = 80
    map_height = 43

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    max_monsters_per_room = 2
    max_items_per_room = 2

    # Loads the Tileset file "dejavu10x10_gs_tc"
    tileset = tcod.tileset.load_tilesheet(
        "assets/tilesets/dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    player = copy.deepcopy(entity_factories.player)

    engine = Engine(player=player)

    engine.game_map = generate_dungeon(
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,
        max_monsters_per_room=max_monsters_per_room,
        max_items_per_room=max_items_per_room,
        engine=engine,
    )
    engine.update_fov()

    engine.message_log.add_message(
        "Real", color.welcome_text
    )

    # This Builds the Screen, takes the Width and Hight and a Title and also a Tileset, wich is what we difined before
    with tcod.context.new_terminal(
            screen_width,
            screen_height,
            tileset=tileset,
            title="Gaming",
            vsync=True,
    ) as context:
        # This Creates Our "Console" which is what we’ll be drawing to
        root_console = tcod.console.Console(screen_width, screen_height, order="F")
        while True:
            root_console.clear()
            engine.event_handler.on_render(console=root_console)
            context.present(root_console)
            try:
                for event in tcod.event.wait():
                    context.convert_event(event)
                    engine.event_handler.handle_events(event)
            except Exception:  # Handle exceptions in game.
                traceback.print_exc()  # Print error to stderr.
                # Then print the error to the message log.
                engine.message_log.add_message(traceback.format_exc(), color.error)

            # Clears the console
            root_console.clear()


if __name__ == "__main__":
    main()
