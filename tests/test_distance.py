from mlproject.distance import haversine

def test_haversine():
    assert isinstance(haversine(48.865070, 2.380009, 51.2790212, 0.2723452),
                      float)
