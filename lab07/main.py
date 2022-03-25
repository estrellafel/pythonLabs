import matplotlib.pyplot as plt

def main():
    fn = open('./data.txt')

    data = []
    line = fn.readline()
    while line:
        split_line = line.split()
        data.append(float(split_line[split_line.index('num_switch') + 1]))
        line = fn.readline()
    make_graph(data)

def make_graph(y_data):
    x_data = [i for i in range(-1, 100)]
    plt.figure(figsize=(8,6), facecolor='mistyrose')
    # plt.xlim(0, 125)
    # plt.ylim(0, 125)
    plt.grid(color='gainsboro')
    plt.xlabel('Timestep', fontsize='16', color = 'maroon')
    plt.ylabel('Number of Agents Who Switch Tasks', fontsize='16', color = 'maroon')
    plt.title('Agents Switching Task at Timesteps', fontsize='22', color = 'maroon')
    lp = plt.plot(y_data, color='red', linewidth=2.5, ls='dotted')
    ax = plt.gca()
    ax.set_facecolor('seashell')
    ax.spines['bottom'].set_color('maroon')
    ax.spines['top'].set_color('maroon') 
    ax.spines['right'].set_color('maroon')
    ax.spines['left'].set_color('maroon')
    ax.tick_params(colors='maroon', which='both')
    plt.show()

if __name__ == '__main__':
    main()
