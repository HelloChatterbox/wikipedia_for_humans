import wikipedia_for_humans

answer = wikipedia_for_humans.tldr_about("speed", "cheetah")
print(answer)
"""
In general, the speed of a hunting cheetah averages 64 km/h during a chase,
interspersed with a few short bursts when the speed varies between 104 and 
120 km/h
"""

answer = wikipedia_for_humans.tldr_about("speed", "light")
print(answer)
"""
The precise measurements yielded a speed of 299,796,000 m/s
"""

# results depend a lot on question, experiment with different keywords
answer = wikipedia_for_humans.tldr_about("distance", "jupiter")
print(answer)
"""
Because the eccentricity of its orbit is 0.048, Jupiter's distance from the 
Sun varies by 75 million km between its nearest approach and furthest distance
"""

answer = wikipedia_for_humans.tldr_about("distance", "venus")
print(answer)
"""
Venus orbits the Sun at an average distance of about 0.72 AU 108 million km
"""

answer = wikipedia_for_humans.tldr_about("distance sun", "mars")
print(answer)
"""
Mars's average distance from the Sun is roughly 230 million km , 
and its orbital period is 687 days
"""

answer = wikipedia_for_humans.tldr_about("distance", "neptune")
print(answer)
"""
The perihelion distance is 29.81 AU
"""

answer = wikipedia_for_humans.tldr_about("distance", "uranus")
print(answer)
"""
Its average distance from the Sun is roughly 20 AU 3 billion km
"""

# sometimes its hard to get the exact answer....
answer = wikipedia_for_humans.tldr_about("orbit", "pluto")
print(answer)
"""
Lowell had made a prediction of Planet X's orbit and position in 1915 that
was fairly close to Pluto's actual orbit and its position at that time
"""

# keep in mind automatic disambiguation
answer = wikipedia_for_humans.tldr_about("danger", "mercury")
print(answer)
"""
Environmental dangers have been a concern, particularly in the southern 
cities of Foshan and Guangzhou, and in Guizhou province in the southwest
"""

answer = wikipedia_for_humans.tldr_about("distance orbit", "mercury (planet)")
print(answer)
"""
its eccentricity is 0.21 with its distance from the Sun ranging 
from 46,000,000 to 70,000,000 km .
"""


answer = wikipedia_for_humans.tldr_about("gaul", "mercury god")
print(answer)
"""
Visucius was worshiped primarily in the frontier area of the empire in Gaul
and Germany
"""