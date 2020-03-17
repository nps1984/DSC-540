import matplotlib.pyplot as plt
import pandas as pd

pop_file = 'world-population.xlsm'
world_pop = pd.read_excel(pop_file)

world_pop.head()
world_pop.plot(x='Year',y='Population')
plt.show()