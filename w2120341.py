#Author:M.I.M.Injas
#Date:09/12/2024
#Student ID:w2120341

import tkinter as tk

# Task A: Input Validation
def validate_date_input():
    """
    Prompts the user for a date in DD MM YYYY format, validates the input for:
    - Correct data type
    - Correct range for day, month, and year
    """
    #Initialize variables
    day = 0
    month = 0
    year = 0

    while True:
        try:
            #Get valid date form the user
            day = input("Please enter the day of the survey in the format dd: ").strip()
            if not day:
                print("Input day can't be blank enter valid date")
                continue
            day = int(day)
            if day not in range(1,32):
                print("Out of range - values must be in the range 1 and 31.")
                continue
            break
        except ValueError:
            print("Integer required.")
            continue
                    
    while True:
        try:
            #Get valid month form the user
            month = input("Please enter the day of the survey in the format MM: ").strip()
            if not month:
                print("Input month can't be blank enter valid month")
                continue
            month = int(month)
            if month not in range(1,13):
                print("Out of range - values must be in the range 1 and 12.")
                continue
            break
        
        except ValueError:
            print("Integer required.")
            continue

    while True:
        try:
            #Get valid year form the user
            year = input("Please enter the day of the survey in the format yyyy: ").strip()
            if not year:
                print("Input year can't be blank enter valid year")
                continue
            year = int(year)
            if year not in range(2000,2025):
                print("Out of range - values must be in the range 2000 and 2024.")
                continue
            #Validate and handaling leap year
            if month ==2 and day> 29:
                print("February only has 29 days.")
                continue
            elif month == 2 and day == 29:
                if not((year % 4 ==0 and year % 100 != 0) or (year % 400 == 0)):
                    print(f"{year} is not a leap year,February has only 28 days in this year.")
                    continue
            break
                                        
        except ValueError:
            print("Integer required.")
            continue

    return day,month,year

def validate_continue_input():
    """
    Prompts the user to decide whether to load another dataset:
    - Validates "Y" or "N" input
    """
    while True:
        #Get the user input,remove trailing space and convert to lowercase
        select = input("Do you like to process an additional dataset? Enter ('Y' for Yes or 'N' for No):").strip().lower()
        if select in ["y","n"]:
            return select
        else:
            print("Invalid input,Enter ('Y'or 'N') ")

# Task B: Processed Outcomes
def process_csv_data(day, month, year):
    """
    Processes the CSV data for the selected date and extracts:
    - Total vehicles
    - Total trucks
    - Total electric vehicles
    - Two-wheeled vehicles, and other requested metrics
    """
    try:
        # Open the csv file and read the csv file for the user given date
        traffic_csv_data = open(f"traffic_data{day:02d}{month:02d}{year}.csv", "r")
        traffic_data_set = traffic_csv_data.readlines()
        traffic_csv_data.close()
    except:
        print("Invalid date,Enter the correct date")
        return False
    else:
        # Split and clean data lines into a structured list
        for i in range(len(traffic_data_set)):
            traffic_data_set[i] = traffic_data_set[i].strip()
            traffic_data_set[i] = traffic_data_set[i].split(",")

        # Remove the header row in the csv file
        traffic_data_set.pop(0)

        # Initialize variables for metrics
        file_name = f"traffic_data{day:02d}{month:02d}{year}.csv"
        total_vehicles = 0
        total_trucks = 0
        total_electric_vehicles = 0
        total_two_wheeled_vehicles = 0
        total_busses_elm_rabbit_road_heading_north = 0
        total_vehicles_going_straight = 0
        percentage_of_trucks = 0
        total_bicycles = 0
        average_of_bikes = 0
        total_vehicles_over_speed = 0
        total_vehicles_elm_rabbit_road = 0
        total_vehicles_hanley_westway_road = 0
        scooter_percentage = 0
        total_scooter = 0
        total_rain_hours = 0
        hour_vehicle = {}
        results = []          
              
        # Iterate through each dataset record in traffic data and calculate metrics
        for i in traffic_data_set:
            total_vehicles += 1

            if i[8] == "Truck":
                total_trucks += 1
                   
            if i[9] == "TRUE":
                total_electric_vehicles += 1

            if i[8] in ["Bicycle", "Motorcycle", "Scooter"]:
                total_two_wheeled_vehicles += 1
              
            if i[8] =="Buss" and i[0] == "Elm Avenue/Rabbit Road" and i[4] == "N":
                    total_busses_elm_rabbit_road_heading_north +=1

            if i[3] == i[4]:
                total_vehicles_going_straight += 1

            if i[8] == "Bicycle":
                total_bicycles += 1

            if int(i[7]) > int(i[6]):
                total_vehicles_over_speed += 1

            #Check if the vehicle passed through Elm Avenue/Rabbit Road
            if i[0] == "Elm Avenue/Rabbit Road":
                total_vehicles_elm_rabbit_road += 1
                hour = i[2].split(":")[0]
                if hour not in hour_vehicle:
                    hour_vehicle[hour] = {"Elm Avenue/Rabbit Road": 0, "Hanley Highway/Westway": 0}
                hour_vehicle[hour]["Elm Avenue/Rabbit Road"] += 1

            #Check if the vehicle passed through Hanley Highway/Westway
            if i[0] == "Hanley Highway/Westway":
                total_vehicles_hanley_westway_road += 1
                hour = i[2].split(":")[0]
                if hour not in hour_vehicle:
                    hour_vehicle[hour] = {"Elm Avenue/Rabbit Road": 0, "Hanley Highway/Westway": 0}
                hour_vehicle[hour]["Hanley Highway/Westway"] += 1

            if i[8] == "Scooter" and i[0] =="Elm Avenue/Rabbit Road":
                total_scooter += 1

            if i[5] in ['Light Rain', 'Heavy Rain']:
                total_rain_hours += 1

        # Calculate the total vehicles and peak hour
        peak_hour = max(hour_vehicle.keys(), key=lambda hour: hour_vehicle[hour].get("Hanley Highway/Westway", 0))
        peak_vehicles = hour_vehicle[peak_hour].get("Hanley Highway/Westway", 0)
        peak_time = f"{peak_hour}:00 and {int(peak_hour)+1}:00"

        # Calculate percentage of the scooters and trucks
        scooter_percentage = int((total_scooter/total_vehicles_elm_rabbit_road)*100)              
        percentage_of_trucks = round((total_trucks / total_vehicles) * 100)
        average_of_bikes = round(total_bicycles / 24)

        return {
            "file_name": file_name,
            "total_vehicles": total_vehicles,
            "total_trucks": total_trucks,
            "total_electric_vehicles": total_electric_vehicles,
            "total_two_wheeled_vehicles": total_two_wheeled_vehicles,
            "total_busses_elm_rabbit_road_heading_north": total_busses_elm_rabbit_road_heading_north,
            "total_vehicles_going_straight": total_vehicles_going_straight,
            "percentage_of_trucks": percentage_of_trucks,
            "total_bicycles": total_bicycles,
            "average_of_bikes": average_of_bikes,
            "total_vehicles_over_speed": total_vehicles_over_speed,
            "total_vehicles_elm_rabbit_road": total_vehicles_elm_rabbit_road,
            "total_vehicles_hanley_westway_road": total_vehicles_hanley_westway_road,
            "scooter_percentage": scooter_percentage,
            "total_scooter": total_scooter,
            "total_rain_hours": total_rain_hours,
            "peak_vehicles": peak_vehicles,
            "peak_time": peak_time,
            "hour_vehicle": hour_vehicle,
            "results": results,
        }

def display_outcomes(outcomes):
    """
    Displays the calculated outcomes in a clear and formatted way.
    """
    #The results in to list of string
    results =[
        f"\n************************************\n"
        f"data file selected is {outcomes['file_name']}\n"
        f"*********************************\n"
        f"The total number of vehicles recorded for this date is: {outcomes['total_vehicles']}\n"
        f"The total of trucks recorded for this data is: {outcomes['total_trucks']}\n"
        f"The total number of electric vehicles for this data is: {outcomes['total_electric_vehicles']}\n"
        f"The total number of two-wheeled vehicles for this data is: {outcomes['total_two_wheeled_vehicles']}\n"
        f"The total number of Buss leaving Elm Avenue/Rabbit Road heading North is: {outcomes['total_busses_elm_rabbit_road_heading_north']}\n"
        f"The total number of vehicles through both junctions not turning left or right is: {outcomes['total_vehicles_going_straight']}\n"
        f"The Percentage of total vehicles recorded that are trucks for this date is: {outcomes['percentage_of_trucks']}%\n"
        f"The average number of Bikes per hour for this date is: {outcomes['average_of_bikes']}\n"    
        f"\nThe total number of Vehicles recorded as over the speed limit for this date is: {outcomes['total_vehicles_over_speed']}\n" 
        f"The total number of Vehicles recorded through Elm Avenue/Rabbit Road junction is: {outcomes['total_vehicles_elm_rabbit_road']}\n"
        f"The total number of Vehicles recorded through Hanley Highway/Westway Road junction is: {outcomes['total_vehicles_hanley_westway_road']}\n"
        f"{outcomes['scooter_percentage']}% of vehicles recorded through Elm Avenue/Rabbit Road are scooters.\n"
        f"\nThe highest number of vehicles in an hour on Hanley Highway/Westway junction is {outcomes['peak_vehicles']}\n"
        f"The most vehicles through Hanley Highway/Westway were recorded between {outcomes['peak_time']}\n"               
        f"The number of hours of rain for this date is: {outcomes['total_rain_hours']}\n"
        
    ]
    
    return results

# Task C: Save Results to Text File
def save_results_to_file(results):
    """
    Saves the processed outcomes to a text file and appends if the program loops.
    """
    try:
        with open ("results.txt","a") as file:
            for line in results:
                print(line)
                file.write(line+"\n")
        print("Results saved to results.txt ")
    except PermissionError:
        print("Unable to write to results.txt check the file permissions.")
    except FileNotFoundError:
        print("File or directory not found.")

# Task D: Histogram Display
class HistogramApp:
    def __init__(self, traffic_data, date):
        """
        Initializes the histogram application with the traffic data and selected date.
        """
        self.traffic_data = traffic_data
        self.date = date
        self.root = tk.Tk()#Create the main Tkinter window
        self.canvas = None #Will hold the canvas for drawing

    def setup_window(self):
        """
        Sets up the Tkinter window and canvas for the histogram.
        """
        self.root.title("Histogram")#Create the title of the window
        self.canvas = tk.Canvas(self.root, width=1000, height=600, bg="#E5E4E2")
        self.canvas.pack()
        
    def draw_axes(self):
        """
        Draws the axes and labels for the histogram.
        """
        self.canvas.create_line(100, 500, 800, 500, width=2)#Draw x-axis using this instructions

        #X-axis labels (hours)
        for i in range(24):
            x = 100 + (i * 30)
            self.canvas.create_line(x, 500, x, 495, width=2)#Draw tick marks using this instructions
            self.canvas.create_text(x, 510, text=str(i), font=("Arial", 10))#Draw Hour labels using this instructions

        #Drwa y-axis labels (vehicle count)
        for i in range(0, 101, 10):
            y = 500 - (i * 4)

    def draw_bars(self):
        """
        Draws the bars for the histogram based on the traffic data.
        """
        bar_width = 12
        #Draw bars for each hour
        for hour, values in self.traffic_data.items():
            x_base = 100 + (int(hour) * 30)

            #Junction 1 (Elm Avenue/Rabbit Road) and draw the bars uisng below instructions
            elm_height = values.get("Elm Avenue/Rabbit Road", 0) * 4
            self.canvas.create_rectangle(
                x_base - bar_width, 500 - elm_height, x_base, 500, fill="Light green"
            )
            self.canvas.create_text(
                x_base - bar_width / 2, 500 - elm_height - 10, text=str(values.get("Elm Avenue/Rabbit Road", 0)), font=("Arial", 8),fill="Light green"
            )

            #Junction 2 (Hanley Highway/Westway) and draw the bars uisng below instructions
            hanley_height = values.get("Hanley Highway/Westway", 0) * 4
            self.canvas.create_rectangle(
                x_base, 500 - hanley_height, x_base + bar_width, 500, fill="#FF8080"
            )
            self.canvas.create_text(
                x_base + bar_width / 2, 500 - hanley_height - 10, text=str(values.get("Hanley Highway/Westway", 0)), font=("Arial", 8),fill="#FF8080"
            )

    def add_legend(self):
        """
        Adds a legend to the histogram to indicate which bar corresponds to which junction.
        """
        #Adding legend as create rectangle box using Elm Avenue/Rabbit Road junction and Hanley Highway/Westway
        self.canvas.create_rectangle(50, 120, 70, 140, fill="Light green")
        self.canvas.create_text(80, 130, text="Elm Avenue/Rabbit Road", anchor="w", font=("Arial", 12))

        self.canvas.create_rectangle(50, 150, 70, 170, fill="#FF8080")
        self.canvas.create_text(80, 160, text="Hanley Highway/Westway", anchor="w", font=("Arial", 12))

        #Adding title and x-axis label
        self.canvas.create_text(500, 50, text=f"Histogram of Vehicle Frequency per Hour ({self.date})", font=("Arial", 16, "bold"))
        self.canvas.create_text(500, 550, text="Hours 00:00 to 24:00", font=("Arial", 12))

    def draw_histogram(self):
        """
        Draws the histogram with axes, labels, and bars.
        """
        self.draw_axes()
        self.draw_bars()
        self.add_legend()

    def run(self):
        """
        Runs the Tkinter main loop to display the histogram.
        """
        self.setup_window()
        self.draw_histogram()
        self.root.mainloop()

# Task E: Code Loops to Handle Multiple CSV Files
class MultiCSVProcessor:
    def __init__(self):
        """
        Initializes the application for processing multiple CSV files.
        """
        self.current_data = None

    def load_csv_file(self, day, month, year):
        """
        Loads a CSV file and processes its data.
        """
        outcomes = process_csv_data(day, month, year)# Process the CSV file
        if outcomes:
            results = display_outcomes(outcomes)
            save_results_to_file(results)#Display the outcomes and saved to the file
            return outcomes
        else:
            print("Failed to process the CSV file.")# Display an error message
            return None
            

    def clear_previous_data(self):
        """
        Clears data from the previous run to process a new dataset.
        """
        self.current_data = None #Initialize current_data as None

    def handle_user_interaction(self):
        """
        Handles user input for processing multiple files.
        """
        while True:
            select = validate_continue_input()# Prompt user to continue or exit
            if select == "n":
                print("Exiting the program.")
                break
            elif select == "y":
                day, month, year = validate_date_input()# Get new date input from user
                self.clear_previous_data()
                self.current_data = self.load_csv_file(day, month, year)
                if self.current_data:
                    # Prepare data for histogram
                    hour_vehicle = self.current_data["hour_vehicle"]
                    traffic_data = {
                        hour: {
                            "Elm Avenue/Rabbit Road": hour_vehicle[hour]["Elm Avenue/Rabbit Road"],
                            "Hanley Highway/Westway": hour_vehicle[hour]["Hanley Highway/Westway"],
                        }
                        for hour in hour_vehicle.keys()
                    }

                    # Create and display the histogram
                    histogram_app = HistogramApp(traffic_data, f"{day:02d}/{month:02d}/{year}")
                    histogram_app.run()
            else:
                print("Invalid input. Please enter 'Y' or 'N'.")

    def process_files(self):
        """
        Main loop for handling multiple CSV files until the user decides to quit.
        """
        self.handle_user_interaction()

#The main program
if __name__ == "__main__":
    first_time = False
    while True:
        #Get the date input from the user
        if not first_time:
            day, month, year = validate_date_input()
            first_time = True
        else:
            #Ask the user if they want to process another dataset
            select = validate_continue_input()
            if select == "n":
                print("Exiting the program")
                break  #Exit the loop if the user chooses "n"
            elif select == "y":
                day, month, year = validate_date_input()

        #Process the CSV data for the given date
        outcomes = process_csv_data(day, month, year)
        if outcomes:
            results = display_outcomes(outcomes)
            save_results_to_file(results)

            #Prepare data for histogram
            hour_vehicle = outcomes["hour_vehicle"]
            traffic_data = {
                hour: {
                    "Elm Avenue/Rabbit Road": hour_vehicle[hour]["Elm Avenue/Rabbit Road"],
                    "Hanley Highway/Westway": hour_vehicle[hour]["Hanley Highway/Westway"],
                }
                for hour in hour_vehicle.keys()
            }

            #Create and display the histogram
            histogram_app = HistogramApp(traffic_data, f"{day:02d}/{month:02d}/{year}")
            histogram_app.run()
        else:
            first_time = False
