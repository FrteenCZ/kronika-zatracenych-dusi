data_start_hour: int = int(input())
data_start_min: int = int(input())
data_lenght_hour: int = int(input())
data_lenght_min: int = int(input())
stream_start_hour: int = int(input())
stream_start_min: int = int(input())
stream_lenght_hour: int = int(input())
stream_lenght_min: int = int(input())


def convert_to_uniks(days: int, hours: int, minutes: int) -> int:
    """
        Combines days, hours and minutes into a uniks time stamp
        epoch starts at 00:00 the first day

        returns minutes since 00:00 first day
    """
    timestamp: int = (days*24 + hours)*60 + minutes

    return timestamp

data_start_day: int = 0

if data_start_hour < 14:
    data_start_day = 1

stream_start_day: int = 0

if stream_start_hour < 14:
    stream_start_day = 1

data_start_uniks: int = convert_to_uniks(data_start_day, data_start_hour, data_start_min)
data_end_uniks: int = data_start_uniks + convert_to_uniks(0, data_lenght_hour, data_lenght_min)

stream_start_uniks: int = convert_to_uniks(stream_start_day, stream_start_hour, stream_start_min)
stream_end_uniks: int = stream_start_uniks + convert_to_uniks(0, stream_lenght_hour, stream_lenght_min)


if data_end_uniks <= stream_start_uniks:
    print("v pohode")

elif data_end_uniks <= stream_end_uniks:
    print(f"neuvidis {data_end_uniks - stream_start_uniks} minut")

else:
    print("to nedas")
