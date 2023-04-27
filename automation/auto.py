import pandas as pd

simpsons = 'https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)'

pd.read_html(simpsons)
for _ in range(len(simpsons)):
    print(simpsons[1])