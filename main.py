from machine import Pin, RTC
from time import sleep_ms
from k155id1 import Decoder, NixieDot
SAVER_PERIOD = 2#in minutes; default = 10
SAVER_DELAY_TIME = 300#in ms; default = 300
SAVER_ITERATION_COUNT = 1
current_state = None
def debug_dc_to_dec(val):
    if val['a0'] is not None or val['a1'] is not None or val['a2'] is not None or val['a3'] is not None:
        return int(f'''{str(val["a3"]) + str(val["a2"]) + str(val["a1"]) + str(val["a0"])}''', 2)
    else:
        return('None')
def state():
    print('state() был вызван')
    if current_state is None:
        return True
    else:
        return current_state


def main():
    hour1 = Decoder({'a0': Pin(0, Pin.OUT, Pin.PULL_DOWN), 'a1': Pin(1, Pin.OUT, Pin.PULL_DOWN), 'a2': Pin(14, Pin.OUT, Pin.PULL_DOWN), 'a3': Pin(12, Pin.OUT, Pin.PULL_DOWN)})
    hour2 = Decoder({'a0': Pin(16, Pin.OUT, Pin.PULL_DOWN), 'a1': Pin(17, Pin.OUT, Pin.PULL_DOWN), 'a2': Pin(26, Pin.OUT, Pin.PULL_DOWN), 'a3': Pin(27, Pin.OUT, Pin.PULL_DOWN)})
    min1 = Decoder({'a0': Pin(2, Pin.OUT, Pin.PULL_DOWN), 'a1': Pin(3, Pin.OUT, Pin.PULL_DOWN), 'a2': Pin(4, Pin.OUT, Pin.PULL_DOWN), 'a3': Pin(5, Pin.OUT, Pin.PULL_DOWN)})
    min2 = Decoder({'a0': Pin(6, Pin.OUT, Pin.PULL_DOWN), 'a1': Pin(7, Pin.OUT, Pin.PULL_DOWN), 'a2': Pin(8, Pin.OUT, Pin.PULL_DOWN), 'a3': Pin(9, Pin.OUT, Pin.PULL_DOWN)})
    
    saver = NixieSaver([hour1, hour2, min1, min2])
    clock = Clock(hour1, hour2, min1, min2, saver)
    while True:
        current_state = state()
        if current_state:
            clock.show_time()
            print(current_state)
            print(f'HOUR1 Time:{clock.ct}, current:{hour1.current}, verbose: {debug_dc_to_dec(min1.current)}')
            print(f'HOUR2 Time:{clock.ct}, current:{hour2.current}, verbose: {debug_dc_to_dec(min1.current)}')
            print(f'MIN1 Time:{clock.ct}, current:{min1.current}, verbose: {debug_dc_to_dec(min1.current)}')
            print(f'MIN2 Time:{clock.ct}, current:{min2.current}, verbose: {debug_dc_to_dec(min1.current)}\n{"---"*3}')
            #print(clock.ct, min2.current, '\n')
            sleep_ms(1000)
            


class Clock:
    def __init__(self, hour1, hour2, minute1, minute2, saver, second1=None, second2=None):
        if second1 is not None or second2 is not None:
            if not isinstance(hour1, Decoder) or not isinstance(hour2, Decoder) or not isinstance(minute1, Decoder) or not isinstance(minute2, Decoder) or not isinstance(second1, Decoder) or not isinstance(second2, Decoder):
                raise TypeError('Args must be Decoder')
        self.saver = saver
        self.rtc = RTC()
        self.rtc.datetime(self.get_new_time())
        self.hour1 = hour1
        self.hour2 = hour2
        self.minute1 = minute1
        self.minute2 = minute2
        self.second1 = second1
        self.second2 = second2
        self.old_time = -1
    def get_new_time(self):
        #TODO
        year = 2022
        month = 1
        day = 3
        weekday = 1
        hour = 10 # fake data
        minute = 20
        second = 30
        return (year, month, day, weekday, hour, minute, second, 0)
    
    def show_time(self):
        global current_state
        print(self.rtc.datetime())
        current_time = self.rtc.datetime()[4:]
        if current_time[1] != self.old_time and current_time[1] % SAVER_PERIOD == 0:
            current_state = 'enum_nixies'
            self.saver.run()
            self.old_time = current_time[1]
        print('old time:', self.old_time)
        self.ct = current_time
        #set hours
        if current_time[0] < 10:
            self.hour1.set_num(0)
            self.hour2.set_num(current_time[0])
        else:
            self.hour1.set_num(current_time[0]//10)
            self.hour2.set_num(current_time[0]%10)
        #set minutes
        if current_time[1] < 10:
            self.minute1.set_num(0)
            self.minute2.set_num(current_time[1])
        else:
            self.minute1.set_num(current_time[1]//10)
            self.minute2.set_num(current_time[1]%10)
        #set seconds
        if self.second1 is not None or self.second2 is not None:
            if current_time[2] < 10:
                self.second1.set_num(0)
                self.second2.set_num(current_time[2])
            else:
                self.second1.set_num(current_time[2]//10)
                self.second2.set_num(current_time[2]%10)
class NixieSaver:
    def __init__(self, nixies):
        self.nixies = nixies
    def run(self):
        print('NixieSaver.run() был вызван')
        global current_state
        for i in range(SAVER_ITERATION_COUNT):
            for nixie in self.nixies:
                nixie.set_num(0)
                sleep_ms(SAVER_DELAY_TIME)
                print(i, '0 is ok')
                nixie.set_num(1)
                sleep_ms(SAVER_DELAY_TIME)
                print(i, '1 is ok')
                nixie.set_num(2)
                sleep_ms(SAVER_DELAY_TIME)
                print(i, '2 is ok')
                nixie.set_num(3)
                sleep_ms(SAVER_DELAY_TIME)
                print(i, '3 is ok')
                nixie.set_num(4)
                sleep_ms(SAVER_DELAY_TIME)
                print(i, '4 is ok')
                nixie.set_num(5)
                sleep_ms(SAVER_DELAY_TIME)
                print(i, '5 is ok')
                nixie.set_num(6)
                sleep_ms(SAVER_DELAY_TIME)
                print(i, '6 is ok')
                nixie.set_num(7)
                sleep_ms(SAVER_DELAY_TIME)
                print(i, '7 is ok')
                nixie.set_num(8)
                sleep_ms(SAVER_DELAY_TIME)
                print(i, '8 is ok')
                nixie.set_num(9)
                sleep_ms(SAVER_DELAY_TIME)
                print(i, '9 is ok')
        current_state = None
        return print('DEBUG:SAVER: RUN OK')
if __name__ == '__main__':
    #main()
    pass