#enter times frames as military times
class Timeframe:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time


def time_overlap(time_1, time_2):
    if time_1.end_time < time_2.start_time:
        raise ValueError('No time conflict')
        
    return(time_2.start_time, time_1.end_time)

def main():
    time1 = Timeframe(12, 16)
    time2 = Timeframe(14, 16)

    print(time_overlap(time1, time2))

if __name__ == '__main__':
    main()