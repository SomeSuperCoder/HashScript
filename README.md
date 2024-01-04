# HashScript
A programming language for developing SmartContracts on the NeonSmartChain!

## Tutorial

### Variables

To declare a variable use the var keyword followed by a name, an equals sign and a value:

``var name = <value>``

Examples:
```javascript
var some_int = 34
```
```javascript
var some_float = 3.25
```
```javascript
var some_string = "HashSript is cool!"
```

The language supports multiple assignment with this syntax

```javascript
var a = var b = var c = 3
```

### Printing

To pint a value to the standard output use

``print(<value>)``

Examples:
```python
print("test")
```
```python
print(123)
```
```python
print(6.4)
```

### If statements

Example:
```python
var a = 1213

if a == 1 then
    print("Something")
elif a == 2 then
    print("Something 2")
else then
    print("Yet another something")
end
```
Or you can use the ":" symbol instead of the then keyword:
```python
var a = 1213

if a == 1:
    print("Something")
elif a == 2:
    print("Something 2")
else:
    print("Yet another something")
end
```

### Functions
To create a functon use the fun keyword
```kotlin
fun test()
    print("This is a function")
end

test()
```

Example how to use function arguments and how to return values:
```kotlin
fun square(a)
    return a ^ 2
end

print(square(2))
```

Simple functions (with only one expression) can be declared with this syntax:
```kotlin
fun square(a) -> a ^ 2

print(square(2))
```

Functions are first-class objects and can be assigned to a variable
```javascript
var square = fun (a) -> a ^ 2

print(square(2))
```

Aloso because of that you can pass a functions to other functions as arguments

```kotlin
fun i_will_do_something(callback)
    return callback(2)
end

print(i_will_do_something(fun (a) -> a ^ 2))
```
### While loop

How to create an infinite loop
```python
while True:
    print("In loop")
end
```

In a loop you can also us ethe ``break`` and ``continue`` keywords

### For loops
```python
for i = 0 to 6:
    print(i)
end
```

Output:
```
0
1
2
3
4
5
```

Use the step keyword to set a step
```python
for i = 0 to 6 step 2:
    print(i)
end
```

Output
```
0
2
4
```

The step can be negative. but you will have to explicitly set a range from a bigger number to a smaller number

```python
for i = 6 to 0 step -1:
    print(i)
end
```

Output:
```
6
5
4
3
2
1
```

Here's another example:
```python
for i = -5 to 6:
    print(i)
end
```

Output:
```
-5
-4
-3
-2
-1
0
1
2
3
4
5
```

### Lists

Here is how to create a list
```javascript
var my_list = [1, 2, 3, "coffee", "capybara"]
```

To add an element to a list use the plus operator:
```javascript
var my_list = [1, 2, 3, "coffee", "capybara"]
print(my_list)
my_list + "another item"
print(my_list)
```

Output:
```
1, 2, 3, coffee, capybara
1, 2, 3, coffee, capybara, another item
```

To remove an element from a list use the minus operator
```javascript
var my_list = [1, 2, 3, "coffee", "capybara"]
print(my_list)
my_list - 0
print(my_list)
```

Output:
```
1, 2, 3, coffee, capybara
2, 3, coffee, capybara
```

To get an element from a list use the division operator
```javascript
var my_list = [1, 2, 3, "coffee", "capybara"]
print(my_list / 0)
print(my_list / 1)
print(my_list / 3)
print(my_list / 4)
print(my_list / -1)
print(my_list / -2)
```
Output:
```
1
2
coffee
capybara
capybara
coffee
```

To combine two lists use the multiplication operator
```javascript
var list_one = [1, 2, 3]
var list_two = [4, 5, 6]
print(list_one * list_two)
```

Output
```
1, 2, 3, 4, 5, 6
```
