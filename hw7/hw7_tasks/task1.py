class KeyValueStorage:
    def __init__(self, file_path):
        self._data = {}
        with open(file_path, 'r') as f:
            for line in f:
                key, value = line.strip().split('=')
                if value.isdigit():
                    value = int(value)
                elif value.replace('.', '', 1).isdigit():
                    value = float(value)
                if key in self.__dict__:
                    raise ValueError(f'Cannot use {key} as a key')
                self._data[key] = value

    def __getattr__(self, key):
        if key in self.__dict__:
            return self.__dict__[key]
        if key in self._data:
            return self._data[key]
        raise AttributeError(f'Attribute {key} not found')

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        if key in self.__dict__:
            self.__dict__[key] = value
        else:
            self._data[key] = value

    def __contains__(self, key):
        return key in self._data

    def keys(self):
        return self._data.keys()

    def values(self):
        return self._data.values()

    def items(self):
        return self._data.items()