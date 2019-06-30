class AirportSequence:
    def __init__(self, itineraries, start):
        itineraries.sort()
        self._itineraries = itineraries
        self._parameters = self._itineraries.copy()
        self._start = start
        self._result_arr = []

    def find_in_tuple(self, start):
        for i in self._parameters:
            if i[0] == start:
                self._parameters.remove(i)
                return i
        return '0'

    def iterator(self):
        for i in self._itineraries:
            aux = self.find_in_tuple(self._start)
            if aux == '0':
                return None
            else:
                self._result_arr.append(aux[0])
                self._start = aux[1]
        self._result_arr.append(self._start)
        return self._result_arr