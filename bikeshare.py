import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
   
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs     
    city = input("Write the city name: ").lower()

    while city not in ['chicago', 'new york city', 'washington']:
          city = input("Your input is not valid. Type in: chicago, new york city or washington: ").lower()
    
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Now write the month: ").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("& please write day of the week: ").lower()
   
    print ('-'*40)
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
    df = pd.read_csv("{}.csv".format(city.replace(" ","_")))

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].apply(lambda x: x.month) 
    df['day_of_week'] = df['Start Time'].apply(lambda x: x.strftime('%A').lower())

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df.loc[df['month'] == month,:]
    if day != 'all':
        df = df.loc[df['day_of_week'] == day,:]
    return df

 

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...')
    start_time = time.time()

    # TO DO: display the most common month
    monthindex = df.month.mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    common_month = months[monthindex - 1]
    print('\n * Most popular month: \n' + common_month)


    # TO DO: display the most common day of week
    weekindex = df['day_of_week'].mode()[0]
    print('\n * Most popular day of the week: \n' + weekindex)

    
    # TO DO: display the most common start hour
    print('\n * Most popular start hour:')
    df['hour'] = df['Start Time'].dt.hour
    print (df.hour.mode()[0])
  

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print(" * Most popular start station: \n" + start_station)
   
    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts().reset_index()['index'][0]
    print("\n * Most popular end station:\n" + end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popular_station = df[['Start Station', 'End Station']].groupby(['Start Station', 'End Station']).size().nlargest(1)
    print('\n * Most popular combination of start&end station: ')
    print (popular_station)
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # TO DO: display total travel time
    trip_sum = df['Trip Duration'].sum()
    print(" * Total travel time: ")
    print(trip_sum)
    

    # TO DO: display mean travel time
    trip_avg = df['Trip Duration'].mean()
    print(" * Mean travel time:")
    print(trip_avg)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\n * This is the counts of user types:')
    print (df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if city != 'washington':
        print("\n * This is the counts of gender:")
        print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
        
        print(" \n * The earliest year of birth:")
        print(df['Birth Year'].min())
        
        print("The latest year of birth:")
        print(df['Birth Year'].max())
        
        print("The most common year of birth:")
        print(df['Birth Year'].mode().values[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
