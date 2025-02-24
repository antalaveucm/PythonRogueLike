import copy
import tcod
from input_handlers import EventHandler
import entity_factories
from engine import Engine
from procgen import generate_dungeon

def main() -> None:
    screen_width = 160
    screen_height = 100

    map_width = 160
    map_height = 100

    room_max_size = 15
    room_min_size = 6
    max_rooms = 30

    max_monsters_per_room = 2

    tiles = "assets/dejavu10x10_gs_tc.png"

    tileset = tcod.tileset.load_tilesheet(
        tiles, 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    player = copy.deepcopy(entity_factories.player)

    game_map = generate_dungeon(
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,
        max_monsters_per_room=max_monsters_per_room,
        player=player
    )
    engine = Engine(event_handler=event_handler, game_map=game_map, player=player)
    
    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Yet Another Roguelike Tutorial",
        vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:
            engine.render(console=root_console, context=context)

            events = tcod.event.wait()

            engine.handle_events(events)

if __name__ == "__main__":
    main()