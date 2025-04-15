The library takes input in ...uH and converts it into ...e-6 and vice versa. The library can convert voltage(V), current(A), inductance(H), capacitance(F), resistance($\Omega$) and frequency(Hz). 

Call unit_to_val() to convert string to float.
Call res(), cap(), ind(), volts(), amps() and freq() to convert float to string.

The library can convert in the range of Terra to femto.
If "M" is entered it is considered mega(10e6) and "m" is entered it is considered mili(10e-3).
