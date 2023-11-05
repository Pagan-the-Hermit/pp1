car_speed = int(input('enter car speed: '))
speed_limit_min = 40
speed_limit_max = 140
if car_speed in range(speed_limit_min, speed_limit_max):
    print('ok')
else:
    print('Warning: invalid car speed!!')