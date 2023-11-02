import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

results = []
for x in range(1):
    flow_file = f'pems_flow_{x}.xlsx'
    flow_data = pd.read_excel(flow_file)
    post_miles = flow_data.iloc[:, 0]
post_miles = np.array(post_miles)
# print(post_miles)

plt.figure(figsize=(10, 6))
# Using scatter to visualize each postmile along the horizontal line
plt.scatter(post_miles, [1]*len(post_miles), s=3, marker='o', c='b')  # `s` denotes the size of each point
plt.title("Position of Loop Detectors along the Highway")
plt.yticks([])  # Hide y-axis ticks
plt.xticks(np.arange(0, np.ceil(np.max(post_miles))+5, 5))
plt.xlabel("Postmile Value")
plt.ylabel("Highway")
plt.xlim(0, np.ceil(np.max(post_miles))+5)
plt.grid(True, which="both", axis="x")
plt.tight_layout()
plt.savefig('postmiles.png', dpi=300)


# Compute the differences
differences = np.diff(post_miles)
# Plot the differences
plt.figure(figsize=(10,6))
plt.plot(differences, marker='o', linestyle='-', color='b')
plt.title("Differences between Adjacent Postmile Values")
plt.xlabel("Index")
plt.ylabel("Difference Value")
plt.grid(True)
plt.tight_layout()
plt.savefig('differences.png')


# Plot the histogram
plt.figure(figsize=(10,6))
plt.hist(differences, bins='auto', edgecolor='k', alpha=0.7)
plt.title("Histogram of Differences between Adjacent Postmile Values")
plt.xlabel("Difference Value")
plt.ylabel("Frequency")
plt.grid(True)
plt.tight_layout()
plt.savefig('histogram.png')