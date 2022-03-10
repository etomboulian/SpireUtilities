from json import JSONEncoder

class SpireJsonEncoder(JSONEncoder):
    def default(self, o):
        return self.remove_empty_elements(o.__dict__)

    def remove_empty_elements(self, d):
        
        def empty(x):
            return x is None or x == {} or x == []
            
        if not isinstance(d, (dict, list)):
            return d
        elif isinstance(d, list):
            return [v for v in (self.remove_empty_elements(v) for v in d) if not empty(v)]
        else:
            return {k: v for k, v in ((k, self.remove_empty_elements(v)) for k, v in d.items()) if not empty(v)}