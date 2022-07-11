def flatten(arr):
    if len(arr) == 0:
        return []
    if not isinstance(arr[0], list):
        return [arr[0]] + flatten(arr[1:])
    else:
        return flatten(arr[0]) + flatten(arr[1:])



obj1 = {
  "outer": 2,
  "obj": {
    "inner": 2,
    "otherObj": {
      "superInner": 2,
      "notANumber": True,
      "alsoNotANumber": "yup"
    }
  }
}

obj2 = {
  "a": 2,
  "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
  "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
  "d": 1,
  "e": {"e": {"e": 2}, "ee": 'car'}
}

def nestedEvenSum(obj, sum=0):
    for key in obj:
        if type(obj[key]) is dict:
            sum += nestedEvenSum(obj[key])
        elif type(obj[key]) is int and obj[key]%2==0:
            sum += obj[key]

    return sum


def stringifyNumbers(obj):
    for key in obj:
        if type(obj[key]) is dict:
            obj[key] = stringifyNumbers(obj[key])
        elif not isinstance(obj[key], str):
            obj[key] = str(obj[key])

    return obj

print(stringifyNumbers(obj2))