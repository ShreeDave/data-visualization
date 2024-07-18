# Import the 'pandas' and 'matplotlib.pyplot' modules and load dataset
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("https://s3-student-datasets-bucket.whjr.online/whitehat-ds-datasets/project-3/sample_csv_file.csv")
# Display the first and last 5 rows
df.head()
df.tail()
# Display the number of rows and columns, and check for null values
df.shape
df.isnull().sum()

# Scatter plots
plt.scatter(df['y'],df['x1'])
plt.show()

plt.figure(figsize=(16,4))
plt.scatter(df['y'],df['x2'])
plt.show()

plt.figure(figsize=(16,4))
plt.scatter(df['y'],df['x3'])
plt.show()

plt.figure(figsize=(16,4))
plt.scatter(df['y'],(2*df['x1'] + 3 *df['x2'] + 4 * df['x3'] + 5 * df['x4']))
plt.show()

# Line plots
plt.plot(df['y'],df['x1'])
plt.show()

plt.figure(figsize=(16,4))
plt.plot(df['y'],df['x2'])
plt.show()

plt.figure(figsize=(16,4))
plt.plot(df['y'],df['x3'])
plt.show()

plt.figure(figsize=(16,4))
plt.plot(df['y'],(2*df['x1']+3*df['x2']+4*df['x3']+5*df['x4']))
plt.show()

# Cumulative Frequency
cum_freq_x1 = []
cum = 0
for i in range(df.shape[0]):
  # Calculate the cumulative frequency of 'x1' column using 'cum + df['x1'][i]'
  cum = cum + df['x1'][i]
  # Append the value of 'cum' 
  cum_freq_x1.append(cum)
 # Convert the 'cum_freq_x1' list into a pandas series
cum_freq_x1 = pd.Series(cum_freq_x1)
print(type(cum_freq_x1))
cum_freq_x1.head(10)

# Min, max, mean, median
print("Minimum:", cum_freq_x1.min())
print("Maximum:", cum_freq_x1.max())
print("Mean:", cum_freq_x1.mean())
print("Median:", cum_freq_x1.median())









