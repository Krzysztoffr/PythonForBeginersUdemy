
isAutomaticMode = True
# is the level of day-lighr above 80%
is80PercentLight = True
# is the Sun ligthing directly into the driver's face
isDirectLight = False
# is it rainy, foggy or other weather conditions are present
isRainy = False

turnLightsOn = (
                isAutomaticMode
                and
                (not is80PercentLight
                or isDirectLight
                or isRainy)
                )
print("Automatic mode:   ",isAutomaticMode)
print("Is the light good:",is80PercentLight)
print("Is sun low:       ",isDirectLight)
print("Is it rainy:      ",isRainy)
print("TURN LIGHTS ON:   ",turnLightsOn)

def should_turn_lights_on(isAutomaticMode, is80PercentLight, isDirectLight, isRainy):
    return (
        isAutomaticMode
        and
        (not is80PercentLight
         or isDirectLight
         or isRainy)
    )

# Test the function with different conditions
print("testAutomaticModeOnLightGoodSunNotLowNotRainy: ", should_turn_lights_on(True, True, False, False))
print("testAutomaticModeOnLightNotGoodSunNotLowNotRainy: ", should_turn_lights_on(True, False, False, False))
print("testAutomaticModeOnLightGoodSunNotLowRainy: ", should_turn_lights_on(True, True, False, True))
print("testAutomaticModeOnLightGoodSunLowNotRainy: ", should_turn_lights_on(True, True, True, False))
print("testAutomaticModeOnLightNotGoodSunNotLowRainy: ", should_turn_lights_on(True, False, False, True))
print("testAutomaticModeOffLightGoodSunNotLowRainy: ", should_turn_lights_on(False, True, False, True))