# Problem 0
## Recursive Fibonacci Function Call Trace

The following is a trace demonstrating the sequence of function calls when computing the Fibonacci sequence recursively. Each indentation level represents a recursive call, showcasing how the recursion progresses until it reaches the base cases (fib(1) and fib(0)), and then computes and returns values upwards in the call stack.

fib(5)

    fib(4)
    
        fib(3)
        
            fib(2)
            
                fib(1)
                
                fib(0)
                
            fib(1)
            
        fib(2)
        
            fib(1)
            
            fib(0)
            
    fib(3)
    
        fib(2)
        
            fib(1)
            
            fib(0)
            
        fib(1)
        
        
This trace helps visualize the recursive nature of the Fibonacci sequence computation.

# Problem 1 - Merge K Arrays

## Time Complexity 

1) Building the Heap takes O(K) time.

2) The total time complexity for heapifying is O(K * log(K)).

3) The total time complexity for the while loop is O(K * N * log(K)).
   
4) Finally, we return the merged result, which has a size of K * N. This operation takes O(K * N) time.
   
Combining all the above steps, the overall time complexity of the algorithm is:

O(K)+O(Klog(K))+O(K⋅N⋅log(K))+O(K⋅N)

O(K⋅N⋅log(K))

This time complexity indicates that the algorithm is efficient, especially when K and N are large.

# Problem 3 

1) The time complexity for iterating through the array is O(N), where N is the number of elements in the array.

2) Since we potentially append N elements (in the case where there are no duplicates), the overall time complexity for this operation is O(N).

Therefore, the overall time complexity of the algorithm is O(N), where N is the number of elements in the input array. This indicates that the time taken by the algorithm grows linearly with the size of the input array.

