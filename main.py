#enter times frames as military times
class Timeframe:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time


def time_overlap(time_1, time_2):
    if time_1.end_time < time_2.start_time:
        raise ValueError('No time conflict')
    else:
        overlap_start = time_1.end_time - time_2.start_time + 10 #add 10 to remain in military time
        counter = overlap_start
        while counter < time_1.end_time:
            counter += 1
    return(overlap_start, counter)

def main():
    time1 = Timeframe(12, 15)
    time2 = Timeframe(14, 16)

    print(time_overlap(time1, time2))

if __name__ == '__main__':
    main()