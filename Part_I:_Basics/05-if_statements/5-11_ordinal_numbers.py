numbers = list(range(1, 10))
print(numbers)

end = ""
for num in numbers:
    if num == 1:
        end = "st"
    elif num == 2:
        end = "nd"
    elif num == 3:
        end = "rd"
    else:
        end = "th"
    print(str(num) + end)
