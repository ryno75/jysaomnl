def recursive_convert(obj):
    '''
    Recursively traverses an iterable object converting from either yaml to
    json or vice-versa.

    :param obj: An object (initially an iterable)
    :type: dict|list|str|int

    :return: The object with its keys interpolated
    :rtype: obj
    '''
    def recurse(obj):
        # handle dictionaries
        if isinstance(obj, dict):
            for k, v in obj.items():
                obj[k] = recurse(v)
        # handle lists
        elif isinstance(obj, list):
            obj = [recurse(i) for i in obj]
        # base case
        elif isinstance(obj, str):
            # Replace key with value if obj == key
            for k, v in kvpairs.items():
                if obj == "<%-" + "%s" % k + "-%>":
                    obj = obj.replace("<%-" + "%s" % k + "-%>", v)
        return obj

    return recurse(obj)

