class DeliveryPlanner:
    def __init__(self, depot):
        self.depot = depot
        self._remaining = None
        self._current = None
        self._route = None

    def plan(self, stops):
        self._remaining = list(stops)
        self._current = self.depot
        self._route = []
        while self._remaining:
            nearest = min(self._remaining, key=self._distance_from_current)
            self._route.append(nearest)
            self._remaining.remove(nearest)
            self._current = nearest
        return self._route

    def _distance_from_current(self, stop):
        return abs(stop[0] - self._current[0]) + abs(stop[1] - self._current[1])

    def total_distance(self, route):
        points = [self.depot, *route, self.depot]
        return sum(
            abs(b[0] - a[0]) + abs(b[1] - a[1])
            for a, b in zip(points, points[1:])
        )
