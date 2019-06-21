import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new_york_city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Select city. \n Type in either 'chicago', 'new_york_city', or 'washington'. >> ").lower()

    while city not in ['chicago', 'new_york_city', 'washington']:
        print("That's not a valid selection.  Check spelling and include underscores where shown.")
        city = input("Type in either 'chicago', 'new_york_city', or 'washington'. >> ").lower()
    """(Refactoring change 1: improved parameter input method"""
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Select month. \n Type in a month from January to June, or enter 'all'. >> ").lower()
    
    while month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
        print("That's not a valid selection.  Be sure to spell out the month name.")
        month = input("Type in a month from January to June, or enter 'all'. >> ").lower()
   
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Select weekday. \n Type in 'Sunday', 'Monday', etc. or enter 'all'. >> ").lower()
    
    while day not in ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']:
        print("That's not a valid selection.  Check your spelling.")
        day = input("Type in 'Sunday', 'Monday', etc. or enter 'all'. >> ").lower()
    
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
      
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # extract start hour for stats
    df['start hour'] = df['Start Time'].dt.hour
    
    # create concatenated field for trip
    df['trip'] = df['Start Station'] + " to " + df['End Station']
   
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def scroll_through(df):

    scroll_choice = input('\nWould you like to view some raw data? (yes or no) >> ').lower()
    if scroll_choice in ('yes'):
        i = 0
        while True:
            # the '-4' removes the columns that were added 
            print(df.iloc[i,1:-4]) 
            print(df.iloc[i+1,1:-4])
            print(df.iloc[i+2,1:-4])
            print(df.iloc[i+3,1:-4])
            print(df.iloc[i+4,1:-4])
            i += 5
            continue_scrolling = input('Would you like to see more data? (yes or no) >> ').lower()
            if continue_scrolling not in ('yes'):
                break
    
    print('-'*40)

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    most_common_month_number = df['month'].mode()[0]
    most_common_month_name = months[most_common_month_number - 1]
    print("The most common month is: ", most_common_month_name.title())

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print("The most common day is: ", most_common_day)

    # TO DO: display the most common start hour
    most_common_start_hour = df['start hour'].mode()[0]
    if most_common_start_hour < 13:
        print("The most common start hour is: ", most_common_start_hour, "am")
    else:
        print("The most common start hour is: ", most_common_start_hour-12, "pm")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("The most common start station is: ", most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("The most common end station is: ", most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_common_trip = df['trip'].mode()[0]
    print("The most common trip is: ", most_common_trip)   
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    duration_hours = (int(df['Trip Duration'].sum() // 60))
    duration_minutes = (int(df['Trip Duration'].sum() % 60))
    print("The duration total is: ", duration_hours, "hours and", duration_minutes, "minutes.")
            
    # TO DO: display mean travel time
    mean_hours = (int(df['Trip Duration'].mean()))
    print("The mean trip duration is: ", mean_hours, "minutes.")   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("User types:")
    print(user_types)

    # TO DO: Display counts of gender
    columns_list = df.columns
    if 'Gender' not in (columns_list):
        print("Gender counts not surveyed.")
    else:
        print("Gender type counts:\n", (df['Gender'].value_counts()))

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in (columns_list):
        print("Birth years not surveyed.")
    else:
        print("The earliest birth year is: ", (int(df['Birth Year'].min())))
        print("The most recent birth year is: ", (int(df['Birth Year'].max())))
        print("The most common birth year is: ", (int(df['Birth Year'].mode())))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        scroll_through(df)
            
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()