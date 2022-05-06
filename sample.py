# import pandas as pd 



# df = pd.read_csv("C:/Users/ibnja/example.csv")
# print(df)
# df.columns
# print(df.columns)

# print(df.dtypes)

# df.timeTaken = df.timeTaken.astype(int)

# df['endTime'] = pd.to_datetime(df['endTs'], format='%Y-%m-%d %H:%M:%S.%f')
# df['startTime'] = df.apply(lambda x: get_starttime(x.endTime, x.timeTaken), axis=1)
# df.drop(columns='endTs')


# df['requestActiveAtTestTime'] = df.apply(lambda x: between_two_times(x.startTime, x.endTime, test_time), axis=1)

# #df['startTime'] = df['endTime'] - pd.Timedelta(milliseconds=df['timeTaken'])


# def get_starttime(endtime,delta_in_ms):
#     return endtime - pd.Timedelta(milliseconds=delta_in_ms)

# def between_two_times(startTime, endTime, checkTime):
#     return startTime < checkTime <= endTime


# from datetime import datetime
# test_time = datetime.strptime('2017-10-23T12:00:00.000', '%Y-%m-%dT%H:%M:%S.%f')


# count_active_request = len(df[df.requestActiveAtTestTime==True])


import sys

print ("the name of the program is ", sys.argv[0])
time_input = sys.argv[1]
print(time_input, " time_input")
if '[' and ']' not in time_input :
    print("its a list")
    time_input_list = time_input.replace("[", "").replace("]", "").split(",")
    global parset_times_list
    parset_times_list = [ input.replace(" ", "").lstrip("\'").rstrip("\'") for input in time_input_list]
    print(parset_times_list)
else:
    print([time_input])

