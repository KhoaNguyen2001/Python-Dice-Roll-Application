import matplotlib.pyplot as plt

def draw_die(n: int, size=1.0, pip_size=900):
    if n not in range(1, 7):
        raise ValueError("n phải trong [1..6]")

    layout = {
        1: [(1,1)],
        2: [(0,0),(2,2)],
        3: [(0,0),(1,1),(2,2)],
        4: [(0,0),(0,2),(2,0),(2,2)],
        5: [(0,0),(0,2),(1,1),(2,0),(2,2)],
        6: [(0,0),(0,2),(1,0),(1,2),(2,0),(2,2)],
    }

    step = size/4
    centers = {0: size-3*step, 1: size/2, 2: 3*step}
    xs, ys = [], []
    for r, c in layout[n]:
        xs.append(centers[c])
        ys.append(centers[2-r])

    fig = plt.figure(figsize=(3,3))
    ax = plt.gca()

    ax.add_patch(plt.Rectangle((0,0), size, size, fill=False, linewidth=4))
    ax.scatter(xs, ys, s=pip_size)

    ax.set_xlim(-0.1, size+0.1)
    ax.set_ylim(-0.1, size+0.1)
    ax.set_aspect('equal')
    ax.axis('off')
    plt.show()

# Ví dụ:
draw_die(5)
