# bmsgens
Generates 32 order-6 binary magic square generators

Using Euler's method to compose order 2n magic square, we can work backward and produce binary magic square generators. These order-2n matrices are binary in the sense each cell contains one of two values; and they can be used, with the arbitrary selection of n+1 numbers (a1, a2, a3, ..., a(n-1), a(n), a(n+1)), to produce infinitely many magic squares. Magic constants so produced will be independent of numbers a1 ... a(n); a(n+1) varying the magic constant by a(n+1) n^2.

Still needs to sample CW, transpose and transpose with both rotations. Python times out at 2n > 6. Perhaps fortran.
