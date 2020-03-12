import matplotlib.pyplot as plt

import numpy as np
from mpl_toolkits import mplot3d


def plot_3D_coordinates(datalist, name_list):

    colour_list = ['b', 'r', 'k']

    plt.figure()
    ax = plt.axes(projection='3d')
    for idx, data in enumerate(datalist):
        ax.scatter3D([x[0] for x in data], [x[1] for x in data], [x[2] for x in data],
                     c=colour_list[idx],
                     label=name_list[idx])

    ax.set_xlabel("x (m)")
    ax.set_ylabel("y (m)")
    ax.set_zlabel("z (m)")

    ax.set_xticks(np.linspace(-0.1, 0.1, 5))
    ax.set_yticks(np.linspace(-0.1, 0.1, 5))
    ax.set_zticks(np.linspace(0, 0.2, 5))

    ax.legend(loc='best')





