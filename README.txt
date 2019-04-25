Bento -- the tram problem
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
    * spherical cows

                      _
                     / \
                    |   |
                    |___|
               *------*----A-*
               |             |
               |             |
               |             |
               *-B----*----H-*
                        <- ? ->

In the above, Human H is at a point in the southeast, he lives
at the north end of town. Trams A & B are moving clockwise.
Should Human H walk with the traffic or against it?

(Again, he doesn't know where he is in town, nor can he see
the trams nor the stops.)

-----------------------------------------

To run a simulation, type:

    % python bento.py do_sim MY_SEED 1

    [ snip ]

    6480.00000

This means, do a clockwise simulations with "MY_SEED" to seed
the random number generator. Do "0" for anti-clockwise. Total
time was 6480 seconds, or about 108 minutes.

    % python bento.py do_sim_both MY_SEED
    15120.000000   26640.000000

This means, do a simulation for both directions  using "MY_SEED"
to see the random number generator. The clockwise run took 15,120
seconds, the anti-clockwise run took 26,640 seconds.

To run 100 simulatins, type:

    % python bento.py do_sim_many MY_SEED 100
    75942.000000   71439.120000

This means, after 100 simulations, the average clockwise time
was 75942 seconds, the average anti-clockwise time was 71439
seconds.

Edit the code to change the following constants:

DEFAULT_CONSTANTS = {
    'loop_length'       : 10 * 1000,
    'stop_count'        : 5,
    'train_count'       : 2,
    'human_speed'       : (5.0 * 1000) / (60 * 60),
    'train_speed'       : (10.0 * 1000) / (60 * 60),
}

Distances are in meters, time is in seconds.
(not that it matters).

