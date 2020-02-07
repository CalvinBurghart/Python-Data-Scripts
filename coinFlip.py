import matplotlib.pyplot as plt
import random
heads = 0
tails = 0
iteration_num = 1
x = [0]
y_tails = [0]
y_heads = [0]
y_diff = [100]
def coinFlip(x, y_tails, y_heads, y_diff, heads, tails, iteration_num):
    coin = random.randint(0,1) # grabs a random number (either 1 or 0)
    
    # prints heads if the number is zero or tails if the number is 1
    if (coin == 0) :
        print("""heads
              """)
        heads += 1
    else : 
        print("""tails
              """)
        tails += 1
    
    # prints information about the data
    print(str(heads) + " coin flips on heads and " + str(tails) + " coin flips on tails")
    
    # declared for use in the graph method
    if(heads > 0):
        over_heads =  ((abs(tails-heads)) / heads) * 100
    if(tails > 0):    
        over_tails =  ((abs(tails-heads)) / tails) * 100
    
    # displays the % difference in haeds and tails solutions
    if(heads > tails):
        print(str(over_heads) + "% difference")
        graph(x, y_tails, y_heads, y_diff, over_heads, heads, tails, iteration_num)
    else :
        print(str(over_tails) + "% difference")
        graph(x, y_tails, y_heads, y_diff, over_tails, heads, tails, iteration_num)
    
        
    # adds one to the iteration number    
    iteration_num += 1
    
    # ensures that the method can be run indefinately (untill we run out of memory)    
    while(iteration_num <= 1000):
        coinFlip(x, y_tails, y_heads, y_diff, heads, tails, iteration_num)
    
def graph(x, y_tails, y_heads, y_diff, percent, heads, tails, iteration_num):
    # adds the iteration number to the x axis and the percent difference to the y axis
    x.append(iteration_num)
    y_tails.append(tails)
    y_heads.append(heads)
    y_diff.append(percent)
    
    # plots the graph and labels it
    plt.plot(x, y_tails)
    plt.plot(x, y_heads)
    plt.xlabel('Coin Flips')
    plt.ylabel('Tails in Blue, Heads in Orange')
    
    plt.title('Graph of Heads and Tails Coin Flips')
    
    plt.show()
    
    # plots the difference graph
    
    plt.plot(x, y_diff)
    plt.xlabel('Coin Flips')
    plt.ylabel('% difference')
    
    plt.title('Graph of the difference between heads and tails')
    
    plt.show()
coinFlip(x, y_tails, y_heads, y_diff, heads, tails, iteration_num)