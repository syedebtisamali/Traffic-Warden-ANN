import neural as nn
from matplotlib import pyplot as plt


def calculate(x1, x2):
    result = nn.neuron([x1, x2], [0.8, 0.6], -5)
    return "green" if result > 0 else "red"

def main():
    for x in range(0, 31):
        for y in range(0, 31):
            color = calculate(x, y)
            plt.scatter(x, y, color=color)
    
    plt.title('Traffic Light Decision Plot')
    plt.xlabel('car_count')
    plt.ylabel('time_waited')
    plt.show()

if __name__ == "__main__":
    main()