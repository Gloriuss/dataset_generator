# Random Server Hostnames Dataset Generator

This project is a practice exercise from the “Advanced Python Programming” module, demonstrating the creation of a dataset of random server hostnames. Using Python, we generate and analyze the dataset by creating a Pandas DataFrame and visualizing data with Matplotlib.

## Features

	•	Random Hostname Generation: A function generates random hostnames based on specified rules for operating system type, environment, and country.
	•	Data Storage in DataFrame: Generated data is stored in a Pandas DataFrame for easy manipulation and analysis.
	•	Visualization: Multiple graphs provide insight into the distribution of server hostnames by country, environment, and operating system.

## Prerequisites

	•	Python 3.7+
	•	Libraries: pandas, matplotlib, seaborn

## Installation

### 1.	Clone the repository:
git clone https://github.com/Gloriuss/dataset_generator.git
### 2.	Navigate to the project directory:
cd dataset_generator
### 3.	Create a virtual environment:
python3 -m venv .venv
### 4.	Activate the virtual environment:
- On macOS/Linux:
source .venv/bin/activate
- On Windows:
.venv\Scripts\activate
### 5.	Install dependencies:
pip install -r requirements.txt

## Usage
### 1.	Launch the generator:
python main.py

### 2.	View the generated CSV file:
A hosts.csv file will be created, containing the generated server data.

## Code Breakdown

### 1. set_hostnames(number_of_hosts:int)->None

Generates random hostnames according to specified rules:

	•	Operating System: First character represents the OS (Linux, Solaris, AIX, or HP-UX).
	•	Environment: Second character indicates the environment (Development, Integration, Testing, etc.).
	•	Country: Third to fifth characters represent the country (Norway, France, etc.).
	•	Each hostname ends with a unique node ID.

### 2. get_os(hostname:str)->str

Returns the operating system name based on the hostname prefix.

### 3. get_enviroment(hostname:str)->str

Determines the environment name based on the second character of the hostname.

### 4. get_country(hostname:str)->str

Returns the country name by interpreting characters 3-5 in the hostname.

### 5. set_dataframe(count:int)->None

Creates a Pandas DataFrame from the generated hostnames. It assigns columns for hostname, OS, environment, country, and node ID.

### 6. Data Visualization

	•	Country & Environment Distribution: A bar chart showing the number of hosts by country and environment.
	•	Type of OS grouped by country: Horizontal bar chart visualizing OS types by country.
	•	Total Operating Systems: Pie chart displaying the percentage distribution of operating systems.
	•	Total Hosts by Country: Horizontal bar chart showing the number of hosts by country.
	•	Hosts by Country and Environment: Bar chart of hosts by country and environment.

### Example Output

1.	DataFrame:
hostname    os    environment    country    node
LDIRL003    Linux      Development    Ireland    3
...

3.	CSV: Saved as hosts.csv, viewable with any CSV reader or using Pandas.
4.	Visualizations:
Several bar charts and a pie chart representing the data distribution.

## License

This project is for educational purposes and does not include a specific license.

## Credits

Developed by Diego Gloria Salamanca as part of a programming practice module for his master’s degree.
