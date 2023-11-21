<br/>
<p align="center">
  <h3 align="center">Unveil the Power of Your Sales: Multi-Channel Mastery Through Data Analytics</h3>

  <p align="center">
    Navigate the Nexus of Sales Channels - Analyze, Strategize, and Maximize!
    <br/>
    <br/>
  </p>
</p>



## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
* [Contributing](#contributing)
* [License](#license)
* [Authors](#authors)
* [Acknowledgements](#acknowledgements)

## About The Project

### Problem Statement:

A retail company has been collecting sales data from various channels, including Online, In-Store, and Direct sales. They have this data stored in a CSV file, 'sales_data_extended_sample.csv', with sales figures recorded by date. The company needs to perform a time-series analysis to understand the monthly trends and the contribution of each sales channel to total sales over time. Specifically, they want to visualize:

1. The total sales per month to observe overall business performance and identify any seasonality.
2. The breakdown of monthly sales by channel to assess the performance of each channel.
3. A comparative analysis across months and channels to pinpoint which combinations are most successful.

The company is looking for a way to visualize this data in a clear, informative manner to aid in strategic decision-making.

### Solution:

To address the company's needs, a Python script was developed using libraries like Pandas, NumPy, Matplotlib, and Seaborn to analyze and visualize the sales data. Here is how the solution was implemented:

1. **Data Loading and Indexing**:
   - The script starts by loading the data with `pandas.read_csv`, parsing the 'Date' column into datetime objects to facilitate time-series analysis.
   - The 'Date' column is then set as the DataFrame index, which allows for easy slicing and resampling of the data based on time periods.

2. **Data Resampling**:
   - The `resample('M').sum()` function is used to aggregate the data on a monthly basis. This step simplifies the dataset into a more manageable form by consolidating daily sales into monthly figures.

3. **Sales Aggregation**:
   - A new column 'Total_Sales' is computed by summing the sales from the three channels. This gives a quick overview of the total sales performance for each month.

4. **Visualization with Subplots**:
   - A figure is created to host three subplots, one for each analysis requirement. This allows the company to view all relevant trends and comparisons in a single comprehensive visualization.

5. **Plot 1 - Total Monthly Sales**:
   - The first subplot is a bar chart showing total sales for each month. It serves to highlight overall trends and potential seasonality in sales.

6. **Plot 2 - Sales Breakdown by Channel**:
   - The second subplot is a stacked bar chart. It shows the contribution of each sales channel to the monthly sales, allowing for a direct comparison of channel performance.

7. **Plot 3 - Heatmap of Sales by Channel and Month**:
   - The third subplot is a heatmap which offers a detailed view of the sales performance of each channel across different months. It uses color intensity to represent the sales volume, making it easier to spot which channel-month combinations are performing best or worst.

8. **Layout Optimization**:
   - `plt.tight_layout()` is utilized to automatically adjust the subplots so that they fit into the figure area nicely, preventing any overlap of titles or labels.

9. **Result Display**:
   - The `plt.show()` function is called to display the figure with all the subplots. This provides the company with a clear, visual representation of their sales data, facilitating informed decision-making.

This solution enables the company to effectively visualize their sales data, understand underlying patterns, and make data-driven decisions to optimize their sales strategy.

This script is a comprehensive example of data analysis and visualization using Python's popular libraries: Pandas, NumPy, Matplotlib, and Seaborn. It demonstrates how to load, process, and visualize a dataset of sales data. Here's a breakdown of its logic and functionality:

1. **Import Libraries**:
   - `pandas`: A powerful data manipulation and analysis library.
   - `numpy`: Adds support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions.
   - `matplotlib.pyplot`: A plotting library that provides a MATLAB-like interface.
   - `seaborn`: A statistical data visualization library based on matplotlib.
   - `DateFormatter`, `AutoDateLocator`: Modules from matplotlib for handling date formatting in plots.

2. **Load Data**:
   - The script reads a CSV file, `sales_data_extended_sample.csv`, into a Pandas DataFrame.
   - The `parse_dates` argument in `pd.read_csv` function is used to parse the 'Date' column as a datetime object.
   - A custom date parser is defined using a lambda function that specifies the date format ('%Y-%m-%d').

3. **Data Preparation**:
   - The 'Date' column is set as the index of the DataFrame using `set_index`.
   - The data is resampled to monthly frequency using `resample('M')`, and the sales are summed up for each month.

4. **Data Aggregation**:
   - A new column, 'Total_Sales', is created by summing up sales from different channels: 'Online_Sales', 'InStore_Sales', and 'Direct_Sales'.

5. **Data Visualization Setup**:
   - A figure of size 15x15 is initialized for plotting multiple subplots.
   - Three subplots are created within this figure.

6. **First Plot - Total Monthly Sales**:
   - This is a bar chart displaying total sales for each month.
   - The x-axis is labeled with formatted dates (Month and Year), and the y-axis shows total sales.

7. **Second Plot - Sales Breakdown by Channel**:
   - This plot is a stacked bar chart showing the breakdown of monthly sales by different sales channels.
   - Each stack segment represents sales from a different channel.

8. **Third Plot - Heatmap of Sales by Channel and Month**:
   - This is a heatmap representing sales data.
   - Rows represent sales channels, and columns represent months.
   - The `sns.heatmap` function from Seaborn is used, with data transposed for appropriate visualization.

9. **Layout Adjustments and Display**:
   - `plt.tight_layout()` is called to adjust the layout and avoid overlapping of labels and titles.
   - Finally, `plt.show()` displays the plotted graphs.

This script efficiently demonstrates the process of loading a time-series dataset, aggregating the data, and visualizing the aggregated data in different formats, including bar charts and a heatmap, to provide insightful views into the sales trends and channel performance over time.

The output of this script would consist of three distinct visualizations, each offering a different perspective on the sales data:

1. **Total Monthly Sales Bar Chart**:
   - This chart displays the total sales for each month as bars.
   - The x-axis represents months, formatted as 'Month Year' (e.g., Jan 2020), while the y-axis represents the total sales values.
   - Each bar represents the total sales for a specific month, providing a clear view of how total sales have varied month over month.

2. **Monthly Sales Breakdown by Channel Stacked Bar Chart**:
   - This chart breaks down the monthly sales into different channels (Online, InStore, Direct) and presents them as stacked bars.
   - Similar to the first chart, the x-axis represents months, and the y-axis represents sales values.
   - Each bar is segmented into different colors, with each segment representing sales from a particular channel. This visualization helps in understanding the contribution of each sales channel to the total monthly sales.

3. **Heatmap of Sales by Channel and Month**:
   - The heatmap offers a more detailed breakdown of sales by channel and month.
   - The x-axis lists the months, and the y-axis lists the sales channels.
   - Each cell in the heatmap corresponds to the sales figure for a particular channel in a specific month.
   - The color intensity in each cell represents the magnitude of sales, with darker colors typically indicating higher sales figures. 
   - This format is particularly useful for quickly identifying patterns or anomalies in sales across different channels and months.

Overall, these visualizations collectively provide a comprehensive view of the sales trends over time, the performance of different sales channels, and the monthly distribution of sales. This kind of analysis is crucial for businesses to understand their sales dynamics and to make informed decisions based on sales performance trends. The use of different types of charts (bar chart, stacked bar chart, heatmap) allows for the examination of the data from various angles, enhancing the ability to derive meaningful insights.

Here is a detailed explanation of each chart:

1. **Total Monthly Sales Bar Chart (Top Chart)**:
   - This chart shows the total sales for each month. The bars are uniformly colored.
   - The x-axis labels represent the months, denoted in the format 'MMM YYYY' (e.g., Jan 2020). The y-axis shows sales figures, scaled to 1e6 (which likely represents the sales in millions for clarity).
   - The highest sales seem to occur in March 2020, with a notable decrease in May 2020. This trend can indicate seasonal effects, promotional impacts, or other market influences.

2. **Monthly Sales Breakdown by Channel Stacked Bar Chart (Middle Chart)**:
   - Here, each month's total sales are broken down by sales channel: Online, InStore, and Direct.
   - The x-axis maintains the same monthly labels. The y-axis also scales to 1e6 for consistency with the first chart.
   - The colors represent different channels: blue for Online Sales, orange for InStore Sales, and green for Direct Sales.
   - This chart allows us to see the contribution of each channel to the total sales. For instance, Online Sales appears to be the largest contributor in most months, while Direct Sales is the smallest. The substantial part of InStore Sales in March, followed by a sharp drop in May, could suggest a specific event or change in consumer behavior.

3. **Heatmap of Sales by Channel and Month (Bottom Chart)**:
   - The heatmap provides a matrix view where each cell's color intensity indicates the sales volume.
   - The x-axis has the same monthly intervals, while the y-axis lists the sales channels vertically.
   - Color intensity varies according to the legend on the right, indicating sales volume, with darker colors showing higher sales figures.
   - Numeric annotations within each cell give the exact sales figure for that channel and month. For example, Online Sales in January 2020 were 582,380, which is the highest single value visible on the heatmap, indicated by the darkest color.
   - The heatmap quickly reveals which channel-month combinations had the highest and lowest sales. It is instantly noticeable that Direct Sales in May 2020 had a low value of 67,355, indicated by a much lighter color.

These visualizations collectively provide an insightful look into the sales performance over time, showing not only the overall trend but also the distribution of sales across different channels. They would be particularly useful for identifying seasonal trends, the effectiveness of sales strategies across different channels, and the impact of external factors on consumer behavior.


## Built With

The Multi-channel Sales Data Analysis project leverages a stack of high-powered, open-source Python libraries, each contributing its robust features to facilitate comprehensive data analysis and visualization. Below is a detailed description of the main components used in building this project:

- **Pandas**: At the core of data manipulation in this project, Pandas offers fast, flexible, and expressive data structures designed to work with structured data intuitively. It provides the essential DataFrame object, enabling sophisticated indexing and reshaping of datasets, and is used here for reading the CSV data, parsing dates, indexing, and resampling the sales data by month.
  
- **NumPy**: This fundamental package for scientific computing with Python is used for its array object and its capability to handle a vast array of numerical operations. NumPy supports the project by enabling efficient computations and data aggregations that are integral when dealing with large datasets.

- **Matplotlib**: A plotting library for the Python programming language and its numerical mathematics extension, NumPy. It provides an object-oriented API for embedding plots into applications. In this project, Matplotlib is utilized to create a variety of visual representations of the data, including bar charts and configurations for the plotting areas.

- **Seaborn**: Built on top of Matplotlib, Seaborn is a statistical data visualization library that offers a higher-level interface for drawing attractive and informative statistical graphics. In this codebase, Seaborn is used to generate an advanced heatmap visualization that elegantly represents the data's complexity in an accessible form.

- **DateFormatter & AutoDateLocator**: These are submodules from Matplotlib that specialize in formatting date values into a readable format and locating dates on an axis, respectively. They are part of the toolkit used to ensure that dates are presented in a clear and coherent style on the plots.

The combination of these tools provides a robust environment for performing detailed and insightful data analysis. With a focus on efficiency and aesthetics, the project is structured to harness the strengths of each library, ensuring that the visualization of sales data is not only analytical but also engaging.

---

Each of these components is well-documented and supported by a community of developers and data scientists, ensuring that the project remains sustainable and extensible for future enhancements or customization.

## Getting Started

Welcome to the Sales Data Visualization project! This repository contains a Python script that enables you to visualize sales data from multiple channels over time using libraries such as Pandas, NumPy, Matplotlib, and Seaborn. Below is a step-by-step guide to help you set up and run the script.

### Prerequisites

- Ensure you have Python installed on your system. Python 3.7 or above is recommended.
- Basic knowledge of Python and libraries such as Pandas and Matplotlib will be beneficial.

### Installation and Setup

1. **Clone the Repository:**
   Begin by cloning the repository to your local machine. Use the following command in your terminal or command prompt:
   ```
   git clone https://github.com/<username>/<repository-name>.git
   ```
   Replace `<username>` and `<repository-name>` with the appropriate GitHub username and the repository name.

2. **Navigate to the Repository Directory:**
   After cloning, move into the project directory with:
   ```
   cd <repository-name>
   ```

3. **Create a Virtual Environment (Recommended):**
   It's a good practice to create a virtual environment for your project to manage dependencies:
   ```
   python -m venv venv
   ```
   Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

4. **Install Required Packages:**
   With your virtual environment activated, install the required Python packages using pip:
   ```
   pip install pandas numpy matplotlib seaborn
   ```

### Running the Script

1. **Prepare Your Dataset:**
   Ensure you have a CSV file named `sales_data_extended_sample.csv` with sales data and dates. The script is configured to parse dates in the 'YYYY-MM-DD' format.

2. **Run the Script:**
   Execute the Python script to generate the visualizations:
   ```
   python <script-name>.py
   ```
   Replace `<script-name>` with the name of the Python script in the repository.

### Understanding the Code

- The script begins by importing necessary Python libraries for data handling and visualization.
- It loads the CSV file, parsing the 'Date' column into `datetime` objects, and sets it as the DataFrame index for time-series analysis.
- The script resamples the data by month and calculates the sum of sales, followed by the computation of total sales for each channel.
- Three plots are generated: a bar chart for total monthly sales, a stacked bar chart for sales by channel, and a heatmap for a detailed view of sales by channel and month.
- Finally, it improves the plot layout and displays the visualizations.

### Contributing

If you'd like to contribute to the project, your contributions are welcome! Please feel free to fork the repository, make changes, and submit a pull request.

### Issues

Should you encounter any issues while setting up or running the script, please open an issue on the GitHub repository with a detailed description of the problem.

### License

This project is licensed under the MIT License - see the LICENSE file in the repository for details.

---

Get started with this guide, and you'll be visualizing sales data in no time. If you have any questions or need further assistance, don't hesitate to reach out. Happy coding!

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.
* If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com//Multi-channel-Sales-Data-Analysis/issues/new) to discuss it, or directly create a pull request after you edit the *README.md* file with necessary changes.
* Please make sure you check your spelling and grammar.
* Create individual PR for each suggestion.
* Please also read through the [Code Of Conduct](https://github.com//Multi-channel-Sales-Data-Analysis/blob/main/CODE_OF_CONDUCT.md) before posting your first idea as well.

### Creating A Pull Request

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See [LICENSE](https://github.com//Multi-channel-Sales-Data-Analysis/blob/main/LICENSE.md) for more information.

## Authors

* **Robbie** - *PhD Computer Science Student* - [Robbie](https://github.com/TribeOfJudahLion) - **

## Acknowledgements

* []()
* []()
* []()
