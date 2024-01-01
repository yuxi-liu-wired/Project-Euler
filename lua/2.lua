
f0 = 1
f1 = 2
sum = 0
while f1 < 4000000 do
    if f1 % 2 == 0 then
        sum = sum + f1
    end
    f0, f1 = f1, f0 + f1
end

print(sum)