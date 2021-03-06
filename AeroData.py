import numpy as np
import matplotlib.pyplot as plt

def CL(alpha='sweep'):

    CLa=np.array(
    [
        [-3.999818368,    -0.153],
        [-2.999434058,    -0.076],
        [-1.999622705,    0.001],
        [-0.999811353,    0.078],
        [0           ,    0.155],
        [0.999811353 ,    0.232],
        [2.000195663 ,    0.309],
        [3.000007015 ,    0.386],
        [3.999818368 ,    0.463],
        [5.000202678 ,    0.54],
        [6.000014031 ,    0.617],
        [6.999825383 ,    0.694],
        [8.000209693 ,    0.771],
        [9.000021046 ,    0.848],
        [9.999832398 ,    0.925],
        [11.00021671 ,    1.002],
        [12.00002806 ,    1.079],
        [12.99983941 ,    1.156],
        [14.00022372 ,    1.233],
        [15.00003508 ,    1.28],
        [15.99984643 ,    1.3],
        [17.00023074 ,    1.3],
        [18.00004209 ,    1.23],
    ])

    z = np.polyfit(CLa[:,0], CLa[:,1], 4)
    f = np.poly1d(z)

    if not isinstance(alpha,str):

        return f(alpha)
    else:
        # calculate new x's and y's
        x_new = np.linspace(-4, 60, 50)
        y_new = f(x_new)
        plt.plot(CLa[:,0],CLa[:,1],'o',x_new,y_new)
        plt.xlim([-4, 20])
        plt.show()

def CD(alpha='sweep'):

    CDa=np.array(
    [
    [    -3.999818368  ,  0.031  ],
    [    -2.999434058  ,  0.03   ],
    [    -1.999622705  ,  0.03   ],
    [    -0.999811353  ,  0.031  ],
    [    0             ,  0.033  ],
    [    0.999811353   ,  0.035  ],
    [    2.000195663   ,  0.038  ],
    [    3.000007015   ,  0.042  ],
    [    3.999818368   ,  0.046  ],
    [    5.000202678   ,  0.051  ],
    [    6.000014031   ,  0.056  ],
    [    8.000209693   ,  0.069  ],
    [    9.000021046   ,  0.076  ],
    [    9.999832398   ,  0.084  ],
    [    11.00021671   ,  0.093  ],
    [    12.00002806   , 0.102  ],
    [    12.99983941   , 0.112  ],
    [    14.00022372   , 0.115  ],
    [    15.00003508   ,  0.12   ],
    [    15.99984643   ,  0.13   ],
    [    17.00023074   ,  0.138  ],
    [    18.00004209   ,  0.145  ],
    [    18.99985344   ,  0.15   ],
    [    20.00023775   ,  0.165  ]
    ])

    z = np.polyfit(CDa[:,0], CDa[:,1], 2)
    f = np.poly1d(z)

    if not isinstance(alpha,str):
        
        return f(alpha)
    else:
        # calculate new x's and y's
        x_new = np.linspace(-4, 60, 50)
        y_new = f(x_new)
        plt.plot(CDa[:,0],CDa[:,1],'o',x_new,y_new)
        plt.xlim([-4, 20])
        plt.show()
