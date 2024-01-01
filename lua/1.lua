total = 0
max = 1000
for i = 1, max-1 do -- 1 to 1000, not including 1000
    if i % 3 == 0 or i % 5 == 0 then
        total = total + i
    end
end

print(total)