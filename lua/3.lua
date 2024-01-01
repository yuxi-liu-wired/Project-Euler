number = 600851475143
sqrt = math.floor(math.sqrt(number))
largest_prime = 0
i = 2
while sqrt > 1 do
    if number % i == 0 then
        if i > largest_prime then
            largest_prime = i
        end
        number = number / i
        sqrt = math.floor(math.sqrt(number))
    else 
        i = i + 1
    end
end

print(largest_prime)