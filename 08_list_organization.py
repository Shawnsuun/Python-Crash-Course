#sort by letters(method)
cars=['bmw','audi','toyota','subaru']
cars.sort()
print(cars)

#sort by reverse letters
cars=['bmw','audi','toyota','subaru']
cars.sort(reverse=True)
print(cars)

#sort by letters(function)
cars=['bmw','audi','toyota','subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

#reverse(method)
cars=['bmw','audi','toyota','subaru']
print(cars)
cars.reverse()
print(cars)

#length(function)
cars=['bmw','audi','toyota','subaru']
print(len(cars))

#pratice 3-8
destinations=['Interlaken','Miami','Barcelona','Los Angeles','San Francisco']
print(destinations)
print(sorted(destinations))
print(destinations)
destinations.reverse()
print(destinations)
destinations.reverse()
print(destinations)
destinations.sort()
print(destinations)
destinations.sort(reverse=True)
print(destinations)

#pratice 3-9
candidates=['Abby','Betty','Candy','Daisy']
print(len(candidates))

#pratice 3-10
candidates=['Abby','Betty','Candy','Daisy']
print(candidates[0].upper())
message=f"Hello,{candidates[1]}"
print(message)
candidates[0]='Alice'
print(candidates)
candidates.append('Flore')
print(candidates)
candidates.insert(1,'Alyce')
print(candidates)
del candidates[1]
print(candidates)
poped_candidate=candidates.pop(2)
print(candidates)
print(poped_candidate)
candidates.remove('Flore')
print(candidates)
candidates.sort(reverse=True)
print(candidates)
print(sorted(candidates))
candidates.reverse()
print(candidates)
print(len(candidates))
#last of the list
print(candidates[-1])

