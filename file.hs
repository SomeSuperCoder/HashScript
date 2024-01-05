fun fibonacci(n)
    print(n)
    if n == 1 or n == 2 then
        return 1
    end
    return fibonacci(n - 1) + fibonacci(n - 2)
end

print(fibonacci(50))
