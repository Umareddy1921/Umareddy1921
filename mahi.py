import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("C://Users/RK/Desktop/manu/matches.csv")
matches_per_stadium=data.groupby('Venue').size().reset_index(name='Match_Count')
print(matches_per_stadium)
plt.bar(matches_per_stadium['Venue'], matches_per_stadium['Match_Count'])
plt.xlabel('Venue')
plt.ylabel('Number of Matches')
plt.title('Number of Matches in each Venue')
plt.show()