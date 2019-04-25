bento -- the tram problem
=========================

You live in an imaginary town called "Bento". Bento is served
by a light rail system that operates on a loop. There are
several trams the run clockwise and stop at each of several
stops. You live on a stop.

Imagine you are dropped at a random point along the loop,
should you start walking clockwise or anti-clockwise, to get
home fastest?

Assume:

    * trams are evenly spaced
    * stations are evenly spaced
    * trams stop for 0 time
    * trams have infinite acceleration & decceleration
    * trams are faster than humans
    * humans stop at first stop they encounter
    * humans can't see trams or stops before they reach them

-----------------------------------------

to run a simulation, type:

	% python bento.py do_sim MY_SEED
    210.000000   205.000000

This means, do a simulation, using "MY_SEED" to see the random
number generator. The clockwise run took 210 seconds, the anti-
clockwise run took 205 seconds.

to run 100 simulatins, type:

	% python bento.py run_many MY_SEED 100
    774.80000   1161.60000

This means, after 100 simulatins, the average clockwise time
was 774.8 seconds, the average anti-clockwise time was 1161.6
seconds.

Edit the code to change the following constants:

    DEFAULT_CONSTANTS = {
        'num_stops'         : 10,
        'num_trains'        : 2,
        'speed_human'       : 5.0,
        'speed_train'       : 20.0,
        'loop_length'       : 10,
    }

Distances are in kilometers, speeds are in kilometers an hour
(not that it matters).

