from datetime import datetime, timedelta

def count_sundays_on_first_of_month(start_date, end_date):
    # Convert the input dates to datetime objects
    start = datetime.strptime(start_date, '%Y-%m-%d')
    end = datetime.strptime(end_date, '%Y-%m-%d')

    # Define a timedelta of one day
    one_day = timedelta(days=1)

    # Initialize a counter for Sundays on the first day of the month
    sunday_count = 0

    # Iterate through the dates between start and end
    current_date = start
    while current_date <= end:
        # Check if the current date is a Sunday and the first day of the month
        if current_date.weekday() == 6 and current_date.day == 1:  # Sunday is represented by 6
            sunday_count += 1

        # Move to the next day
        current_date += one_day

    return sunday_count


# Example usage
start_date = '1901-01-01'
end_date = '2000-12-31'
sunday_count = count_sundays_on_first_of_month(start_date, end_date)
print("Number of Sundays that fell on the first day of the month:", sunday_count)
