controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    game.splash("You should try", Swimming_Array._pickRandom())
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    game.splash("You should try", Running_Array._pickRandom())
})
let Swimming_Array: string[] = []
let Running_Array: string[] = []
game.splash("Do you like running(A) or swimming(B)? Press A, then your selection.")
Running_Array = ["Marathon Running", "Sprinting", "Soccer"]
Swimming_Array = ["Water Polo", "Scuba Diving", "Surfing"]
