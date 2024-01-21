# 9. Generate 1000 random samples from a standard normal distribution and plot their histogram using Matplotlib.
import numpy
import pandas
import matplotlib.pyplot as plt
random_array=numpy.random.randn(1000)

# arr_freq=numpy.zeros(1000,dtype=int)
# for i in range(1000):
#     arr_freq[int(random_array[i]*100)]+=1
# mydata={"random_array":random_array,
# "arr_freq":arr_freq}    
# inDataframe=pandas.DataFrame(mydata)
# inDataframe.plot(kind="scatter",x="random_array",y="arr_freq")
# plt.show()
df = pandas.DataFrame({'random_array': random_array})
plt.hist(df['random_array'], bins=30, density=True, alpha=0.7, color='blue', edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of 1000 Random Samples from Standard Normal Distribution')
