import csv
from datetime import datetime
from matplotlib import pyplot as plt
filename = 'sitka_weather_2018_simple.csv'
# Add function to read file name & temperature type
def read_data(filename,temp_type):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        # Get dates and high temperatures from this file.
        # Formatted indents to match previously added code.
        dates, temps = [],[]
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            # Add If Elif statement to either return high or low temperatures
            if temp_type == 'high':
                temp = int(row[5])
            elif temp_type == 'low':
                temp = int(row[6])
            temps.append(temp)
    return dates,temps
# Plot the high temperatures.
#plt.style.use('seaborn')
def plot_data(dates,temps,temp_type):
    fig,ax = plt.subplots()
    # Add if elif statement for high & low temperatures 
    if temp_type == 'high':
        # Change highs to temps
        ax.plot(dates,temps,c='red')
        # Format plot.
        plt.title("Daily high temperatures - 2018", fontsize=24)
    elif temp_type == 'low':
        # Formatted similiar to highs then added blue for color instead of red
        ax.plot(dates,temps,c='blue')
        plt.title("Daily high temperatures - 2018", fontsize=24)
    plt.xlabel('',fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)",fontsize=16)
    plt.tick_params(axis='both',which='major',labelsize=16)
    plt.show()
# Create main loop that allows user to choose between high temps, low temps,
# or exiting the program. 
def main():
    while True:
        print('Welcome to Sitka Highs Weather Report Program!')
        print('This program has been updated my Liz Hinz for CSD325-A339')
        print('Choose an option:')
        print('1. View high temperatures')
        print('2. View low temperatures' )
        print('3. Exit')
        choice = input('Enter your choice (1/2/3):')
        # Added if elif else statement to read files for low or high temps
        # if neither temps are selected, the main function breaks 
        if choice == '1':
            dates, temps = read_data(filename,'high')
            plot_data(dates,temps,'high')
        elif choice == '2':
            dates,temps = read_data(filename,'low')
            plot_data(dates,temps,'low')
        # Add line telling the user the program is now exiting.
        elif choice == '3':
            print('Thanks for using the Sitka Highs Weather Report Program. See you next time!')
            break
        else:
            print('Invalid choice. Please enter a valid selection.')
# Call the main function
if __name__ == '__main__':
    main()
