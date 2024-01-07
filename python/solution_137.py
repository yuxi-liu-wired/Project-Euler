# Idea of solution:
# By recurrence relation, we have
# $$
# G(x) = \frac{(G_2-G_1)x^2 + G_1 x}{1-x-x^2}
# $$

# Given any desired $G(x) = n$, we have a quadratic equation.

# When $G_1=G_2=1$, this gives $x = \frac{\pm \sqrt{5n^2+2n+1} - n-1}{2n}$. The golden nugget is found by solving $m^2 = 5n^2+2n+1$.

# Let $x = (5n+1), y = m$, this is the Pell-like equation of $x^2 - 5y^2 = -4$. This involves [something about the quadratic number field](https://math.stackexchange.com/questions/742181/find-all-integer-solutions-for-the-equation-5x2-y2-4), which I am unable to say more about.
