
import pandas as pd 
from datetime import datetime
import sys

def read_csv(fileName):
    df = pd.read_csv(fileName)
    return df

# Helper function. For lambda.
def get_start_time(endtime,delta_in_ms):
    return endtime - pd.Timedelta(milliseconds=delta_in_ms)

#helper function. For lambda.
def between_two_times(startTime, endTime, checkTime):
    return startTime < checkTime <= endTime

# Convert endTime into datetime object Calucate Start Time.
def format_input_data(df):
    df.timeTaken = df.timeTaken.astype(int)
    df['endTime'] = pd.to_datetime(df['endTs'], format='%Y-%m-%d %H:%M:%S.%f')
    df['startTime'] = df.apply(lambda x: get_start_time(x.endTime, x.timeTaken), axis=1)
    return df.drop(columns='endTs')


# for test_time figure out if it falls between start and endtime. Return number of rows where it falls between start and endtime.
def count_between_time(df, test_time):
    df['requestActiveAtTestTime'] = df.apply(lambda x: between_two_times(x.startTime, x.endTime, test_time), axis=1)
    #print(df)
    count_active_request = len(df[df.requestActiveAtTestTime==True])
    print(count_active_request, " total active requests during : ", test_time)
    return count_active_request


# If input is intended to be list of timestamp. Parse it create a python list with input strings
def parse_input(time_input):
    # print(time_input, " time_input")
    if '[' and ']' in time_input :
        # print("its a list")
        time_input_list = time_input.replace("[", "").replace("]", "").split(",")
        global parset_times_list
        parset_times_list = [ input.replace(" ", "").lstrip("\'").rstrip("\'") for input in time_input_list]
        return parset_times_list
    else:
        return [time_input]

def main():
    file_name = sys.argv[1]
    test_time_string  = sys.argv[2]

    test_time_list = parse_input(test_time_string)
    df = read_csv(file_name)
    df = format_input_data(df)

    # Reuse the above result datafraome for multiple test_time
    for test_time in test_time_list:
        #convert test_time into datetime
        test_time = datetime.strptime(test_time, '%Y-%m-%dT%H:%M:%S.%f')
        count_between_time(df, test_time)


if __name__ == "__main__":
    main()



# sample execution :  python LogExplorerTripathiJay.py C:/Users/ibnja/example.csv 2017-10-23T12:00:00.000
# sample output : 
# 7  total active requests during :  2017-10-23 12:00:00

# Sample Execution with list :  python LogExplorerTripathiJay.py C:/Users/ibnja/example.csv  "['2017-10-23T12:00:00.000', '2017-10-23T12:00:00.400']"
# Sample output : 
# 7  total active requests during :  2017-10-23 12:00:00
# 1  total active requests during :  2017-10-23 12:00:00.400000
