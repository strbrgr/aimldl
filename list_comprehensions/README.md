# List comprehensions in Python
Coming from JavaScript, List comprehensions were new to me. They provide a simple and concise way of performing transformations on Lists. 

Instead of writing:
```Python
values = [1,2,3,4,5]
altered_values = []
for v in values:
    altered_values.append(v*25)
```

We can achieve the same by writing:
```Python
values = [1,2,3,4,5]
altered_values = [v*25 for v in values]
```
