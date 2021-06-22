import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('light.csv')

fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(x=df['Phase'], y=df['Mag'], s=10, c='b', marker="+", label='5 Nights of Magnitude')
plt.plot(df['Phase'], df['Curve'], label='6th order curve')
plt.gca().invert_yaxis()
plt.xlabel("Phase")
plt.ylabel("Magnitude")
plt.title('1998 TU3 Light Curve')
plt.legend(loc='upper right')
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)

plt.show()
