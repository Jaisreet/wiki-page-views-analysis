# Plotting Wikipedia Page Views

## Problem Statement

The task is to create two plots based on the provided data of the number of times individual Wikipedia pages were viewed in two specific hours. The goal is to visualize the distribution of page views and examine the relationship between views from two different data files.

## Approach and Methods

1. **Plot 1: Distribution of Views**

   - Sort the data from the first input file based on the number of views in descending order using the `sort_values` function.
   - Create a plot using `plt.plot` with the sorted views data. Matplotlib will automatically generate the x-coordinates as a range from 0 to n-1.
   - Use a Pareto distribution to model the distribution of page views based on statistical knowledge.

2. **Plot 2: Hourly Views**

   - Read the two data files and extract the views data into separate Pandas Series objects.
   - Create a DataFrame using the two Series, where the page names serve as the index.
   - Plot a scatterplot using `plt.plot` with the views from the first data file as the x-coordinate and the corresponding views from the second data file as the y-coordinate.
   - Adjust the axes to log scale using `plt.xscale` and `plt.yscale` for better visualization due to the distribution of values.

3. **Final Output**

   - Use `plt.savefig` to save the figure as a PNG file named "wikipedia.png".
   - Add labels to the plots using `plt.title`, `plt.xlabel`, and `plt.ylabel` to provide useful information.
   - To view the figure during testing, use `plt.show()`, but exclude it in the final version.

A sample "wikipedia.png" file is included in the ZIP file for reference.

To run the program, execute the following command in the command line:

```
python3 create_plots.py pagecounts-20190509-120000.txt pagecounts-20190509-130000.txt
```

Make sure to replace "pagecounts-20190509-120000.txt" and "pagecounts-20190509-130000.txt" with the actual filenames you want to process.
