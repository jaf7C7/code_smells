from planner import DeliveryPlanner


def test_visits_the_nearest_stop_next():
    planner = DeliveryPlanner(depot=(0, 0))
    assert planner.plan([(5, 5), (1, 0), (2, 1)]) == [(1, 0), (2, 1), (5, 5)]


def test_chooses_each_stop_relative_to_the_last_one_visited():
    planner = DeliveryPlanner(depot=(0, 0))
    assert planner.plan([(3, 0), (0, 4), (6, 1)]) == [(3, 0), (6, 1), (0, 4)]


def test_does_not_change_the_list_of_stops():
    stops = [(5, 5), (1, 0)]
    DeliveryPlanner(depot=(0, 0)).plan(stops)
    assert stops == [(5, 5), (1, 0)]


def test_empty_list_of_stops_gives_empty_route():
    assert DeliveryPlanner(depot=(0, 0)).plan([]) == []


def test_total_distance_includes_return_to_depot():
    planner = DeliveryPlanner(depot=(0, 0))
    assert planner.total_distance([(1, 0), (2, 1), (5, 5)]) == 20


def test_planner_can_be_reused():
    planner = DeliveryPlanner(depot=(0, 0))
    planner.plan([(9, 9)])
    assert planner.plan([(2, 0), (1, 0)]) == [(1, 0), (2, 0)]


def test_measures_distance_in_every_direction():
    planner = DeliveryPlanner(depot=(0, 5))
    assert planner.plan([(4, 5), (0, 0)]) == [(4, 5), (0, 0)]
