# I decided to write a code that generates data filtering object from a list of keyword parameters:

class Filter:
    """
        Helper filter class. Accepts a list of single-argument
        functions that return True if object in list conforms to some criteria
    """
    """added * before argument functions, so we can take multiple values"""
    def __init__(self, *functions):
        self.functions = functions

    def apply(self, data):
        return [item for item in data if all(i(item) for i in self.functions)]


"""changed order of arguments in the isinstance function"""
# positive_even = Filter(lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int))
# print(positive_even.apply(range(100)))


def make_filter(**keywords):
    """
        Generate filter object for specified keywords
    """
    filter_funcs = []
    for key, value in keywords.items():
        """fixed variable conflict, so when user is entering different filters, for example name='Bill' and type='bird' 
        - there is empty output, because there are no such dictionaries"""
        def keyword_filter_func(values, key=key, value=value):
            return values[key] == value

        filter_funcs.append(keyword_filter_func)
        """using * we get several values for output"""
    return Filter(*filter_funcs)


sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {
        "is_dead": True,
        "kind": "parrot",
        "type": "bird",
        "name": "polly"
    }
]

res = make_filter(name='polly', type='person').apply(sample_data)
print(res)
# should return only second entry from the list

# There are multiple bugs in this code. Find them all and write tests for faulty cases.
