# Problem 14

[**Longest Collatz Sequence**](https://projecteuler.net/problem=14)

## Description:
The following iterative sequence is defined for the set of positive integers:

- $ n \mod 2 = 0 \to n_{i+1} = n_i / 2 $
- $ n \mod 2 \neq 0 \to n_{i+1} = 3 \cdot n_i $

Using the rule above and starting with 13, we generate the following sequence:
$$ 13 \to 40 \to 20 \to 10 \to 5 \to 16 \to 8 \to 4 \to 2 \to 1 $$

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.


## Task:
Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
