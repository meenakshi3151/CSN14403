# Create a scatter plot with two numerical columns from a DataFrame, customizing markers, colors, and labels.
import pandas as pd
import matplotlib.pyplot as plt
data = {'column1': [1, 2, 3, 4, 5],
        'column2': [5, 4, 3, 2, 1]}
df = pd.DataFrame(data)
marker_style = input("Enter the marker style") 
marker_size = int(input("Enter the marker size"))
marker_color = input("Enter the marker color") 
line_color = input("Enter the line color")   
df.plot(kind="scatter",x='column1', y="column2", marker=marker_style, s=marker_size, c=marker_color)
plt.title('Scatter Plot of column1 vs column2')

plt.show()