Input deck created by FRIDGe
c ************************************Title************************************
c ************************Cell Cards for Assembly: 01A01*********************** 
100 10 0.04575 -100 u=101 imp:n=1 $Pin: Fuel
101 11 0.02428 100 -101 u=101 imp:n=1 $Pin: Bond
102 12 0.08599 101 -102 u=101 imp:n=1 $Pin: Clad
103 13 0.02428 102 u=101 imp:n=1 $Pin: Wirewrap + Coolant
104 14 0.02428 -103 u=102 imp:n=1 $Pin: Blank Pin Coolant
105 0 -104 lat=2 u=103 imp:n=1
     fill=-10:10 -10:10 0:0
      102 102 102 102 102 102 102 102 102 102
      102 102 102 102 102 102 102 102 102 102
      102 102 102 102 102 102 102 102 102 102 102
      101 101 101 101 101 101 101 101 101 101
      102 102 102 102 102 102 102 102 102 102 101
      101 101 101 101 101 101 101 101 101 101
      102 102 102 102 102 102 102 102 102 101 101
      101 101 101 101 101 101 101 101 101 101
      102 102 102 102 102 102 102 102 101 101 101
      101 101 101 101 101 101 101 101 101 101
      102 102 102 102 102 102 102 101 101 101 101
      101 101 101 101 101 101 101 101 101 101
      102 102 102 102 102 102 101 101 101 101 101
      101 101 101 101 101 101 101 101 101 101
      102 102 102 102 102 101 101 101 101 101 101
      101 101 101 101 101 101 101 101 101 101
      102 102 102 102 101 101 101 101 101 101 101
      101 101 101 101 101 101 101 101 101 101
      102 102 102 101 101 101 101 101 101 101 101
      101 101 101 101 101 101 101 101 101 101
      102 102 101 101 101 101 101 101 101 101 101
      101 101 101 101 101 101 101 101 101 101
      102 102 101 101 101 101 101 101 101 101 101
      101 101 101 101 101 101 101 101 101 102
      102 102 101 101 101 101 101 101 101 101 101
      101 101 101 101 101 101 101 101 102 102
      102 102 101 101 101 101 101 101 101 101 101
      101 101 101 101 101 101 101 102 102 102
      102 102 101 101 101 101 101 101 101 101 101
      101 101 101 101 101 101 102 102 102 102
      102 102 101 101 101 101 101 101 101 101 101
      101 101 101 101 101 102 102 102 102 102
      102 102 101 101 101 101 101 101 101 101 101
      101 101 101 101 102 102 102 102 102 102
      102 102 101 101 101 101 101 101 101 101 101
      101 101 101 102 102 102 102 102 102 102
      102 102 101 101 101 101 101 101 101 101 101
      101 101 102 102 102 102 102 102 102 102
      102 102 101 101 101 101 101 101 101 101 101
      101 102 102 102 102 102 102 102 102 102
      102 102 102 102 102 102 102 102 102 102 102
      102 102 102 102 102 102 102 102 102 102
      102
106 0 -106 u=100 fill=103 imp:n=1 $Assembly: Inner Portion of Assembly
110 20 0.02428  106 109 108 107 -110 u=100 imp:n=1 $Assembly: Assembly Duct
107 17 0.03364 -107 u=100 imp:n=1 $Assembly: plenum
108 18 0.07365 -108 u=100 imp:n=1 $Assembly: upper Reflector
109 19 0.07365 -109 u=100 imp:n=1 $Assembly: lower Reflector
112 22 0.02428 -112 u=100 imp:n=1 $Assembly: Lower Sodium
113 23 0.02428 -113 u=100 imp:n=1 $Assembly: Upper Sodium
111 0 -111 fill=100 imp:n=1 $Assembly
114 0 111 imp:n=0 $Assembly: Outside Assembly

c ********************Surface Cards for Fuel Assembly: 01A01*******************
100 RCC 0.0 0.0 0.0 0 0 60.0 0.19745 $Pin: Fuel
101 RCC 0.0 0.0 0.0 0 0 60.6 0.228 $Pin: Bond - 1% higher than fuel
102 RCC 0.0 0.0 0.0 0 0 60.6 0.265 $Pin: Clad - 1% higher than fuel
103 RHP 0.0 0.0 0.0 0 0 60.6 0 0.66144 0 $Pin: Coolant - 1% higher than fuel
104 RHP 0.0 0.0 0.0 0 0 60.6 0 0.33072 0 $Pin: Blank Pin - 1% higher than fuel
106 RHP 0.0 0.0 0.0 0 0 60.6 5.505 0 0 $Assembly: Duct Inner Surface
107 RHP 0.0 0.0 60.6 0 0 60.0 5.505 0 0 $Assembly: plenum
108 RHP 0.0 0.0 120.6 0 0 60.0 5.505 0 0 $Assembly: upper Reflector
109 RHP 0.0 0.0 -60.0 0 0 60.0 5.505 0 0 $Assembly: lower Reflector
110 RHP 0.0 0.0 -60.0 0 0 240.6 6.10531 0 0 $Assembly:Duct Outer Surface
111 RHP 0.0 0.0 -99.7 0 0 320.0 6.105 0 0 $Assembly: Full Assembly Surface
112 RHP 0.0 0.0 -99.8 0 0 39.8 6.10531 0 0 $Assembly: Lower Sodium
113 RHP 0.0 0.0 180.6 0 0 39.7 6.10531 0 0 $Assembly: Upper Sodium

c **********************************Data Cards*********************************
c ******************************k-code Information*****************************
kcode 10000000000 1.0 300 2300
ksrc 0 0 80 
PRDMP 100 10 100 1 
kopts BLOCKSIZE=10 KINETICS=YES PRECURSOR=Yes 
c *****************************Material Information****************************
c Material: 5Pu22U10Zr; Density: 0.04575 atoms/bn*cm 
m10 92235.82C 1.9146E-1 92238.82C 5.4143E-1 94239.82C 4.0222E-2
     94240.82C 2.5566E-3 40090.82C 1.1707E-1 40091.82C 2.5250E-2
     40092.82C 3.8175E-2 40094.82C 3.7862E-2 40096.82C 5.9725E-3
c Material: Liquid Sodium; Density: 0.02428 atoms/bn*cm 
m11 11023.82C 1.0000E+0
c Material: HT9; Density: 0.08599 atoms/bn*cm 
m12 6000.82C 9.1823E-3 14028.82C 7.2709E-3 14029.82C 3.5663E-4
     14030.82C 2.2753E-4 15031.82C 5.3409E-4 16032.82C 3.2768E-4
     16033.82C 2.5087E-6 16034.82C 1.3799E-5 16036.82C 3.0663E-8
     23050.82C 8.2802E-6 23051.82C 3.2392E-3 24050.82C 5.5167E-3
     24052.82C 1.0230E-1 24053.82C 1.1381E-2 24054.82C 2.7805E-3
     25055.82C 6.0224E-3 26054.82C 5.0761E-2 26056.82C 7.6841E-1
     26057.82C 1.7434E-2 26058.82C 2.2802E-3 28058.82C 3.2398E-3
     28060.82C 1.2064E-3 28061.82C 5.1586E-5 28062.82C 1.6184E-4
     28064.82C 3.9894E-5 42092.82C 8.7178E-4 42094.82C 5.3731E-4
     42095.82C 9.2035E-4 42096.82C 9.5849E-4 42097.82C 5.4627E-4
     42098.82C 1.3737E-3 42100.82C 5.4201E-4 74180.82C 1.8386E-6
     74182.82C 4.0157E-4 74183.82C 2.1566E-4 74184.82C 4.5925E-4
     74186.82C 4.2153E-4
c Material: Liquid Sodium; Density: 0.02428 atoms/bn*cm 
m13 11023.82C 1.0000E+0
c Material: Liquid Sodium; Density: 0.02428 atoms/bn*cm 
m14 11023.82C 1.0000E+0
c Material: ['LiquidNa', 'Void', 'HT9']; Density: 0.03364 atoms/bn*cm 
m17 11023.82C 1.2141E-2 6000.82C 1.9740E-4 14028.82C 1.5631E-4
     14029.82C 7.6667E-6 14030.82C 4.8915E-6 15031.82C 1.1482E-5
     16032.82C 7.0445E-6 16033.82C 5.3931E-8 16034.82C 2.9664E-7
     16036.82C 6.5919E-10 23050.82C 1.7801E-7 23051.82C 6.9635E-5
     24050.82C 1.1860E-4 24052.82C 2.1992E-3 24053.82C 2.4466E-4
     24054.82C 5.9774E-5 25055.82C 1.2947E-4 26054.82C 1.0913E-3
     26056.82C 1.6519E-2 26057.82C 3.7480E-4 26058.82C 4.9020E-5
     28058.82C 6.9649E-5 28060.82C 2.5935E-5 28061.82C 1.1090E-6
     28062.82C 3.4791E-6 28064.82C 8.5764E-7 42092.82C 1.8741E-5
     42094.82C 1.1551E-5 42095.82C 1.9786E-5 42096.82C 2.0605E-5
     42097.82C 1.1744E-5 42098.82C 2.9532E-5 42100.82C 1.1652E-5
     74180.82C 3.9527E-8 74182.82C 8.6329E-6 74183.82C 4.6362E-6
     74184.82C 9.8729E-6 74186.82C 9.0621E-6
c Material: ['LiquidNa', 'HT9']; Density: 0.07365 atoms/bn*cm 
m18 11023.82C 4.8565E-3 6000.82C 6.3168E-4 14028.82C 5.0019E-4
     14029.82C 2.4534E-5 14030.82C 1.5653E-5 15031.82C 3.6742E-5
     16032.82C 2.2542E-5 16033.82C 1.7258E-7 16034.82C 9.4926E-7
     16036.82C 2.1094E-9 23050.82C 5.6962E-7 23051.82C 2.2283E-4
     24050.82C 3.7951E-4 24052.82C 7.0374E-3 24053.82C 7.8291E-4
     24054.82C 1.9128E-4 25055.82C 4.1430E-4 26054.82C 3.4920E-3
     26056.82C 5.2862E-2 26057.82C 1.1994E-3 26058.82C 1.5686E-4
     28058.82C 2.2288E-4 28060.82C 8.2992E-5 28061.82C 3.5488E-6
     28062.82C 1.1133E-5 28064.82C 2.7445E-6 42092.82C 5.9973E-5
     42094.82C 3.6963E-5 42095.82C 6.3314E-5 42096.82C 6.5937E-5
     42097.82C 3.7580E-5 42098.82C 9.4502E-5 42100.82C 3.7286E-5
     74180.82C 1.2649E-7 74182.82C 2.7625E-5 74183.82C 1.4836E-5
     74184.82C 3.1593E-5 74186.82C 2.8999E-5
c Material: ['LiquidNa', 'HT9']; Density: 0.07365 atoms/bn*cm 
m19 11023.82C 4.8565E-3 6000.82C 6.3168E-4 14028.82C 5.0019E-4
     14029.82C 2.4534E-5 14030.82C 1.5653E-5 15031.82C 3.6742E-5
     16032.82C 2.2542E-5 16033.82C 1.7258E-7 16034.82C 9.4926E-7
     16036.82C 2.1094E-9 23050.82C 5.6962E-7 23051.82C 2.2283E-4
     24050.82C 3.7951E-4 24052.82C 7.0374E-3 24053.82C 7.8291E-4
     24054.82C 1.9128E-4 25055.82C 4.1430E-4 26054.82C 3.4920E-3
     26056.82C 5.2862E-2 26057.82C 1.1994E-3 26058.82C 1.5686E-4
     28058.82C 2.2288E-4 28060.82C 8.2992E-5 28061.82C 3.5488E-6
     28062.82C 1.1133E-5 28064.82C 2.7445E-6 42092.82C 5.9973E-5
     42094.82C 3.6963E-5 42095.82C 6.3314E-5 42096.82C 6.5937E-5
     42097.82C 3.7580E-5 42098.82C 9.4502E-5 42100.82C 3.7286E-5
     74180.82C 1.2649E-7 74182.82C 2.7625E-5 74183.82C 1.4836E-5
     74184.82C 3.1593E-5 74186.82C 2.8999E-5
c Material: Liquid Sodium; Density: 0.02428 atoms/bn*cm 
m20 11023.82C 1.0000E+0
c Material: Liquid Sodium; Density: 0.02428 atoms/bn*cm 
m21 11023.82C 1.0000E+0
c Material: Liquid Sodium; Density: 0.02428 atoms/bn*cm 
m22 11023.82C 1.0000E+0
c Material: Liquid Sodium; Density: 0.02428 atoms/bn*cm 
m23 11023.82C 1.0000E+0