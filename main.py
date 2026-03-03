import neural as nn

def main():
    #input, weight
    x1, w1 = 10, 0.8 # car_count
    x2, w2 =  5, 0.6 # time_waited
    z = -5 # bias

    result = nn.neuron([x1, x2], [w1, w2], z)

    print("Neuron output:", result)

    if result > 0:
        print("GREEN LIGHT")
    else:
        print("RED LIGHT")

if __name__ == "__main__":
    main()