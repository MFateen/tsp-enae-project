from Globals import *
import RandomWayPoint
import numpy as np


def compute_n(mean_x):
    n = ((100 * Z * STD_DEV) / (R * mean_x)) ** 2
    return math.ceil(n)


def simulate(n, p, filename):
    ret = 0
    # Opens the output file
    fo = open(filename, "w")

    fo.write("The %d vectors:\n" % n)
    fo.write("===============\n")

    total_mean_speed = RandomWayPoint.simulate_random_way_point()
    for i in range(1, n + 1):
        vector_minute_speed = RandomWayPoint.simulate_random_way_point()

        # Appends mean speeds of each minute to output file
        np.savetxt(fo, vector_minute_speed, fmt='%f', newline=' ')
        fo.write("\n")

        for j in range(0, len(total_mean_speed)):
            total_mean_speed[j] = (total_mean_speed[j] * i + vector_minute_speed[j])/(i+1)

    fo.write("\nThe mean vector:\n")
    fo.write("================\n")
    np.savetxt(fo, total_mean_speed, fmt='%f', newline=' ')
    fo.write("\n")

    if p:
        # Vector of computed n  for each mean
        vector_n = map(compute_n, total_mean_speed)

        fo.write("\nThe N vector:\n")
        fo.write("=============\n")
        np.savetxt(fo, vector_n, fmt='%d', newline=' ')
        fo.write("\n")

        largest_n = np.amax(vector_n)
        ret = largest_n

        fo.write("\n========================\n")
        fo.write("The Largest N value : %d\n" % largest_n)
        fo.write("========================\n")

    # Closes the output file
    fo.close()
    return ret

if __name__ == '__main__':
    l = simulate(30, True, "preliminary.txt")
    simulate(int(l), False, "Simulation.txt")
    e = Z * STD_DEV / math.sqrt(l)