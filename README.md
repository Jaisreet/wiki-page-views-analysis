# Plotting Wikipedia Page Views
Python project analyzing Wikipedia page views and generating insightful plots. Explore distribution of views and compare data sets with scatterplots. Gain valuable insights into page popularity and trends.

GitHub Page: Plotting Wikipedia Page Views

**Introduction:**
In this project, we will be creating two plots to analyze the number of times individual Wikipedia pages were viewed in two particular hours. We will use data extracted from Wikipedia's page view counts.

**Instructions:**
To generate the plots, you will need to follow these steps:

1. Clone the repository: Start by cloning the repository to your local machine using the following command:
```
git clone https://github.com/your-username/wiki-page-views-analysis.git
```

2. Navigate to the project directory: Move into the project directory using the command:
```
cd plotting-wikipedia-page-views
```

3. Install dependencies: Ensure that you have the necessary dependencies installed by running the following command:
```
pip install -r requirements.txt
```

4. Run the Python script: Execute the Python script `create_plots.py` and provide the filenames of the two data files as command-line arguments. The command should look like this:
```
python3 create_plots.py pagecounts-20190509-120000.txt pagecounts-20190509-130000.txt
```
Replace `pagecounts-20190509-120000.txt` and `pagecounts-20190509-130000.txt` with the actual filenames of your data files.

**Note:** Make sure the data files are located in the same directory as the Python script.

5. View the plots: The script will generate two plots and save them as `wikipedia.png` in the project directory. You can view the plots by opening the file or use any image viewer.

**Additional Information:**
- The first plot, "Plot 1: Distribution of Views," represents the distribution of page views from the first data set. It assumes a Pareto distribution.
- The second plot, "Plot 2: Hourly Views," shows a scatterplot comparing the views from the first and second data files. The axes are displayed in a logarithmic scale.
- The plots will have relevant labels for clarity.
- You can customize the size of the plots by modifying the `plt.figure(figsize=(10, 5))` line in the script.

For further details and code implementation, please refer to the [GitHub repository](https://github.com/jaisreet/wiki-page-views-analysis)
