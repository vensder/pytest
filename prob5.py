def uniqueValues(aDict):
    return sorted([k for k in aDict if all(aDict[k] != aDict[o] for o in aDict if o != k)])
