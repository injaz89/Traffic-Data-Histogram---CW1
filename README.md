# 🚦 Traffic Data Analysis Application

A Python-based application designed to analyze daily traffic data from CSV files. It processes traffic volume, vehicle types, and flow at specific junctions, generates a comprehensive text report, and visualizes the peak traffic hours using an interactive Tkinter histogram.

## ✨ Features

- **Date Validation (Task A)**: Prompts the user for a survey date (DD, MM, YYYY) and rigorously validates the input, including leap year checks.
- **Traffic Data Processing (Task B)**: Reads from specifically formatted CSV files (e.g., `traffic_data15062024.csv`) and calculates key metrics:
  - Total vehicles, trucks, electric vehicles, and two-wheelers.
  - Number of vehicles exceeding the speed limit.
  - Traffic flow at specific junctions (Elm Avenue/Rabbit Road and Hanley Highway/Westway).
  - Peak traffic hours and specific vehicle percentages (like scooters).
- **Report Generation (Task C)**: Automatically saves the processed outcomes and metrics into a `results.txt` file for permanent record-keeping.
- **Data Visualization (Task D)**: Generates a histogram using `tkinter`, visualizing the hourly vehicle frequency at the two main junctions side-by-side.
- **Multi-Dataset Processing (Task E)**: Allows the user to seamlessly load and analyze multiple datasets in a single session without restarting the program.

## 🛠️ Technologies Used

- **Python 3.x**: Core programming language.
- **Tkinter**: Standard GUI library in Python used for rendering the interactive histogram.
- **File I/O**: For reading CSV datasets and appending results to text files.

## 📂 Project Structure

```text
w2120341/
│
├── w2120341.py                 # Main Python application script
├── w2120341.pdf                # Project documentation/assignment brief
├── results.txt                 # Auto-generated text file storing processed outcomes
├── traffic_data15062024.csv    # Sample traffic dataset (June 15, 2024)
├── traffic_data16062024.csv    # Sample traffic dataset (June 16, 2024)
└── traffic_data21062024.csv    # Sample traffic dataset (June 21, 2024)
```

## 🚀 Getting Started

### Prerequisites

- **Python 3.6+** installed on your system.
- Tkinter (usually comes pre-installed with standard Python distributions).

### How to Run

1. **Navigate to the project directory:**
   Ensure you are in the folder containing `w2120341.py` and the corresponding `traffic_dataDDMMYYYY.csv` files.

2. **Run the script:**
   Open a terminal or command prompt and execute:
   ```bash
   python w2120341.py
   ```

3. **Follow the on-screen prompts:**
   - Enter the **Day** (e.g., `15`)
   - Enter the **Month** (e.g., `06`)
   - Enter the **Year** (e.g., `2024`)

4. **View the Results:**
   - The application will output the traffic statistics in the console.
   - The results will also be saved automatically to `results.txt`.
   - A **Histogram window** will pop up showing the hourly breakdown of traffic at the two main junctions. Close the window to proceed.

5. **Load another dataset:**
   - When prompted with `Do you like to process an additional dataset? (Y/N)`, enter `Y` to load another file (like the 16th or 21st of June) or `N` to exit.

## 📝 Author

- **Name:** M.I.M.Injas
- **Student ID:** w2120341
- **Date:** 09/12/2024
