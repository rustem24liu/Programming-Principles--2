from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

# ---------- FREE API KEY examples ---------------------

owm = OWM('591b26325a13da9c5edfcda8c7a83ac8')
mgr = owm.weather_manager()
place = input("What city do you want to know?")

observation = mgr.weather_at_place(place)
w = observation.weather
print(w)