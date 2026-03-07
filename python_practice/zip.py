# zip() function
# foo = [1, 2, 3]
# bar = ['apple', 'banana', 'cherry', 'date']

# for item in zip(foo, bar):
#     print(item)


# pickling in python
import pickle

data = {
    "name": "bharat",
    "age": 25,
    "city": "mumbai",
    "country": "india"
}

with open("data.pickle", "wb") as f:
    pickle.dump(data, f)

with open("data.pickle", "rb") as f:
    loaded_data = pickle.load(f)

print (loaded_data)