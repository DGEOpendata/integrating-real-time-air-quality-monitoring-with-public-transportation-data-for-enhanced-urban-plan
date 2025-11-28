# Integrating Real-Time Air Quality Monitoring with Public Transportation Data

## Overview
This project aims to integrate real-time air quality monitoring data with public transportation usage data to enhance urban planning and environmental policy-making in Abu Dhabi. By correlating these datasets, we can identify zones with high pollution and traffic congestion to optimize transport routes and improve air quality.

## Prerequisites
- Python 3.x
- Pandas
- Matplotlib
- Seaborn

## Installation
1. Clone the repository:
   bash
   git clone https://github.com/username/air-quality-transport.git
   cd air-quality-transport
   
2. Install the required packages:
   bash
   pip install pandas matplotlib seaborn
   

## Datasets
The project uses two main datasets:
1. **Public Transport Usage Data**: Contains date, location, and transport usage metrics.
2. **Real-Time Air Quality Data**: Contains date, location, and air quality indicators such as PM2.5.

Ensure both datasets are stored in CSV format and placed in the project directory.

## Running the Analysis
Execute the Python script to analyze and visualize the data:
bash
python analyze_data.py


## Outputs
- **Correlation Matrix**: Shows the correlation between transport usage and air quality indicators.
- **Visualization**: Line plot showing public transport usage against PM2.5 levels over time.
- **High Pollution and Usage Areas**: Identifies locations and dates with high pollution and transport usage.

## Contribution
Feel free to submit issues or pull requests to enhance the analysis or visualization features.

## License
This project is licensed under the MIT License.