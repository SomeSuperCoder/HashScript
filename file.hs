fun i_will_do_something(callback)
    return callback(2)
end

print(i_will_do_something(fun (a) -> a ^ 2))