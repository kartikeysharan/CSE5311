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
