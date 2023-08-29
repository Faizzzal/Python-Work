# Q4. Write a function that takes a dictionary and returns
# a list of keys whose values are greater than a given number.

def reqd(dict, n):
    return [k for k, v in dict.items() if v > n]

dict = {"key1": 10, "key2": 15, "key3": 20, "key4": 5}
print(reqd(dict, 14))