def on_b_pressed():
    game.splash("You should try", Swimming_Array._pick_random())
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_pressed():
    game.splash("You should try", Running_Array._pick_random())
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

Swimming_Array: List[str] = []
Running_Array: List[str] = []
game.splash("Do you like running(A) or swimming(B)? Press A, then your selection.")
Running_Array = ["Marathon Running", "Sprinting", "Soccer"]
Swimming_Array = ["Water Polo", "Scuba Diving", "Surfing"]