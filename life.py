# The following code is based on an example from Python Playground

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

vals = ON, OFF = 255, 0
DEFAULT_SIZE = 100

def random_grid(size):
    return np.random.choice(vals, size * size, p=[.2, .8]).reshape(size, size)

def update(frameNum, img, grid, size):
    new_grid = grid.copy()
    for i in xrange(size):
        for j in xrange(size):
            total = int(grid[(i - 1) % size, (j - 1) % size] + grid[i, (j - 1) % size] + grid[(i + 1) % size, (j - 1) % size] +
                        grid[(i - 1) % size, j] + grid[(i + 1) % size, j] +
                        grid[(i - 1) % size, (j + 1) % size] + grid[i, (j + 1) % size] + grid[(i + 1) % size, (j + 1) % size]) / 255

            if grid[i, j] == ON:
                if total < 2 or total > 3:
                    new_grid[i, j] = OFF
            else:
                if total == 3:
                    new_grid[i, j] = ON
    img.set_data(new_grid)
    grid[:] = new_grid[:]
    return img,

def main():
    grid = random_grid(DEFAULT_SIZE)
    update_interval = 50

    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    ani = animation.FuncAnimation(fig,
                                  update,
                                  fargs=(img, grid, DEFAULT_SIZE),
                                  frames=10,
                                  interval=update_interval,
                                  save_count=50)
    plt.show()


if __name__ == '__main__':
    main()
