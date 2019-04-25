# bento.py -- simulation for tram problem

# You live in a town with a light rail tram on a loop.
# You are dropped off at a random point on that loop.
# You want to get home as soon as possible.
# Trains go clockwise.
# Do you start walking clockwise or anticlockwise?

# constants are in meters & seconds

DEFAULT_CONSTANTS = {
    'loop_length'       : 10 * 1000,
    'stop_count'        : 5,
    'train_count'       : 2,
    'human_speed'       : (5.0 * 1000) / (60 * 60),
    'train_speed'       : (10.0 * 1000) / (60 * 60),
}


import random, sys


def do_sim(constants, is_clockwise, verbose):

    def log(s):
        if verbose:
            sys.stdout.write(s + '\n')

    # init
    #
    log('setting up ...')
    human = random.random() * constants['loop_length']
    trains = [0.0, ] * constants['train_count']
    trains[0] = random.random() * constants['loop_length']
    for i in range(1, constants['train_count']):
        trains[i] = (trains[i - 1] + (constants['loop_length'] / constants['train_count'])) % constants['loop_length']
    ticks = 0
    on_train = None     # or index of train
    tick_time = (constants['loop_length'] / constants['stop_count']) / constants['train_speed']
    log('tick_time: %f' % tick_time)
    clock_time = 0.0

    # tick routine
    #
    log('starting ticks ...')
    while 1:
        old_clock_time = clock_time
        clock_time += tick_time
        ticks += 1

        # TODO: do stuff

        x = random.randint(0, 100)
        if is_clockwise and 0 == x:
            break
        if not is_clockwise and 1 == x:
            break
    log('all done.')
    log('ticks: %d, clock_time: %f' % (ticks, clock_time))

    # return total elapsed wall clock time
    #
    return clock_time


def do_sim_both(constants):
    rand_state = random.getstate()
    clockwise_score = do_sim(constants, True, False)
    random.setstate(rand_state)
    anticlockwise_score = do_sim(constants, False, False)
    return (clockwise_score, anticlockwise_score)


def do_sim_many(constants, n):
    a, b = 0.0, 0.0
    for i in range(n):
        x = do_sim_both(constants)
        a += x[0]
        b += x[1]
    return (a, b)


def main(argv):
    c = argv[0]
    constants = DEFAULT_CONSTANTS.copy()
    if 0:
        pass
    elif 'do_sim' == c:
        random.seed(argv[1])
        x = do_sim(constants, '0' != argv[2], True)
        print(x)
    elif 'do_sim_both' == c:
        random.seed(argv[1])
        x = do_sim_both(constants)
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
