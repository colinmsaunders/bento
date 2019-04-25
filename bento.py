# bento.py -- simulation for tram problem

# You live in a town with a light rail tram on a loop. 
# You are dropped off at a random point on that loop.
# You want to get home as soon as possible.
# Trains go clockwise.
# Do you start walking clockwise or anticlockwise?


DEFAULT_CONSTANTS = {
    'num_stops'         : 10,
    'num_trains'        : 2,
    'speed_human'       : 5.0,
    'speed_train'       : 20.0,
    'loop_length'       : 10,
}


import random, sys


def do_sim_dir(constants, is_clockwise):

    # init
    #
    human = random.random() * constants['loop_length']
    trains = [0.0, ] * constants['num_trains']
    trains[0] = random.random() * constants['loop_length']
    for i in range(1, constants['num_trains']):
        trains[i] = (trains[i - 1] + (constants['loop_length'] / constants['num_trains'])) % constants['loop_length']
    ticks = 0
    is_on_train = False
    tick_length = constants['loop_length'] / constants['num_stops']
    clock_time = 0.0

    # tick routine
    #
    while 1:
        old_clock_time = clock_time
        clock_time += tick_length
        ticks += 1

        # TODO: do stuff

        x = random.randint(0, 100)
        if is_clockwise and 0 == x:
            break
        if not is_clockwise and 1 == x:
            break
    # return total elapsed wall clock time
    #
    return clock_time


def do_sim(constants):
    rand_state = random.getstate()
    clockwise_score = do_sim_dir(constants, True)
    random.setstate(rand_state)
    anticlockwise_score = do_sim_dir(constants, False)
    return (clockwise_score, anticlockwise_score)


def do_sim_many(constants, n):
    a, b = 0.0, 0.0
    for i in range(n):
        x = do_sim(constants)
        a += x[0]
        b += x[1]
    return (a, b)


def main(argv):
    c = argv[0]
    constants = DEFAULT_CONSTANTS.copy()
    if 0:
        pass
    elif 'do_sim_dir' == c:
        random.seed(argv[1])
        x = do_sim_dir(constants, '0' != argv[2])
        print(x)
    elif 'do_sim' == c:
        random.seed(argv[1])
        x = do_sim(constants)
        print('%f\t%f' % (x[0], x[1]))
    elif 'do_sim_many' == c:
        random.seed(argv[1])
        n = int(argv[2])
        x = do_sim_many(constants, n)
        print('%f\t%f' % (x[0] / n, x[1] / n))
    else:
        raise Exception('I don\'t know how to "%s".' % c)


if __name__ == '__main__':
    main(sys.argv[1:])
