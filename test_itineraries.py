from itineraries import AirportSequence

def test_challenge():
    air_seq = AirportSequence([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], 'YUL')
    assert air_seq.iterator() == ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']

def test_failure():
    air_seq = AirportSequence([('SFO','COM'), ('COM', 'YYZ')], 'COM')
    assert air_seq.iterator() == None

def test_lexicographically():
    air_seq = AirportSequence([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], 'A')
    assert air_seq.iterator() == ['A', 'B', 'C', 'A', 'C']

def test_brazilian():
    air_seq = AirportSequence([('SPO', 'RJ'), ('RJ', 'POA'), ('POA', 'BH')], 'SPO')
    assert air_seq.iterator() == ['SPO', 'RJ', 'POA', 'BH']

def test_brazilian_failure():
    air_seq = AirportSequence([('SPO', 'RJ'), ('RJ', 'POA'), ('POA', 'BH')], 'POA')
    assert air_seq.iterator() == None