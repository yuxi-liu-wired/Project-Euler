function number_to_digits(number, base)
    local digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    local result = {}
    while number > 0 do
        table.insert(result, 1, digits:sub((number % base) + 1, (number % base) + 1))
        number = math.floor(number / base)
    end
    return result
end

function is_palindrome(s)
    local str = tostring(s)
    local reversed = string.reverse(str)
    return str == reversed
end

largest_palindrome = 0
minimum = 100
maximum = 999
for sum = 2*maximum, 2*minimum, -1 do
    local smaller = sum - maximum
    local larger = sum - smaller
    while smaller <= larger do
        if is_palindrome(smaller * larger) then
            largest_palindrome = math.max(largest_palindrome, smaller * larger)
        end
        smaller = smaller + 1
        larger = larger - 1
    end
    if largest_palindrome > 0 then
        break
    end
end

print(largest_palindrome)