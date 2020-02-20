import math
import matplotlib.pyplot as plt
import numpy as np
#---------------------------------------------------
def main():
    #User inputs the function they want to graph
    print("Please input a function to graph. Exponents " +
          "are denoted with ** (Example: x**2 + 1): ", end="")
    userInput = input()
    f = lambda x: eval(userInput)
    x = np.linspace(0, 1, 100) #Ranges from 0-1
    
    #User inputs the amount of iterations they want in the cobweb
    print("Please input the iterations to perform in the diagram: ", end="")
    iterations = int(input())
    
    #User inputs the seed value to use
    print("Please input a seed value to use for x0: ", end="")
    seed = float(input())
    
    #Plot the function y = x
    baseFunction = lambda x: x
    plt.plot(x, baseFunction(x))
    
    #Plot the user function
    plt.plot(x, f(x))
    
    #Plot the cobweb diagram in a loop that runs iterations times.
    #Begin at (x0, base(x0)), then go to (x0, F(x0))
    i = 0
    while (i < iterations):
        #Plot the VERTICAL line
        point1 = [seed, baseFunction(seed)]
        point2 = [seed, f(seed)]
        xvals  = [point1[0], point2[0]]
        yvals  = [point1[1], point2[1]]
        plt.plot(xvals, yvals, 'k')
        
        #Plot the HORIZONTAL line
        point3 = [seed, f(seed)]
        point4 = [f(seed), baseFunction(f(seed))]
        xvals  = [point3[0], point4[0]]
        yvals  = [point3[1], point4[1]]
        plt.plot(xvals, yvals, 'k')
        seed = f(seed)
        
        #Iterate
        i += 1
    
    #Show the plot
    plt.show()
#---------------------------------------------------
if __name__== "__main__":
    main()