import pytest
from src.problem1_optimize_routes import optimize_air_routes


class TestOptimizeAirRoutes:
    """Test cases for the optimize_air_routes function."""

    def test_basic_example(self):
        """Test with basic example from problem statement."""
        result = optimize_air_routes(7000, [[1,2000],[2,4000],[3,6000]], [[1,2000]])
        assert result == [[2, 1]]

    def test_multiple_optimal_pairs(self):
        """Test with multiple optimal route pairs."""
        result = optimize_air_routes(10000, [[1,3000],[2,5000],[3,7000]], [[1,3000],[2,5000]])
        assert [2,2] in result or [3,1] in result

    def test_no_valid_route(self):
        """Test with no valid route combination."""
        result = optimize_air_routes(5000, [[1,10000]], [[1,10000]])
        assert result == [[]]

    def test_empty_lists(self):
        """Test with empty forward or return route lists."""
        result = optimize_air_routes(7000, [], [[1,2000]])
        assert result == [[]]
        result = optimize_air_routes(7000, [[1,2000]], [])
        assert result == [[]]

    def test_exact_match(self):
        """Test when the sum exactly matches maxTravelDist."""
        result = optimize_air_routes(7000, [[1,3000]], [[1,4000]])
        assert result == [[1, 1]]

    def test_single_route_each(self):
        """Test with single route in each list."""
        result = optimize_air_routes(5000, [[1,2000]], [[1,2000]])
        assert result == [[1, 1]]

    def test_large_distance_difference(self):
        """Test with large distance differences."""
        result = optimize_air_routes(10000, [[1,1000],[2,9000]], [[1,500],[2,500]])
        assert result == [[2, 1]] or result == [[2, 2]]

    def test_multiple_return_options(self):
        """Test with multiple return route options for optimal forward route."""
        result = optimize_air_routes(10000, [[1,5000]], [[1,4000],[2,4000],[3,4500]])
        assert result == [[1, 3]]

    def test_all_routes_too_long(self):
        """Test when all route combinations exceed maxTravelDist."""
        result = optimize_air_routes(5000, [[1,3000],[2,4000]], [[1,3000],[2,4000]])
        assert result == [[]]

    def test_edge_case_zero_distance(self):
        """Test with zero distance routes."""
        result = optimize_air_routes(1000, [[1,0],[2,500]], [[1,0],[2,500]])
        assert result == [[2, 2]]

    def test_many_optimal_pairs(self):
        """Test with many optimal pairs at same distance."""
        result = optimize_air_routes(10000, [[1,5000],[2,5000],[3,5000]], [[1,4000],[2,4000],[3,4000]])
        assert len(result) == 9  # All combinations should be optimal

    def test_performance_large_input(self):
        """Test performance with large input sizes."""
        forward = [[i, i*100] for i in range(1, 1001)]
        return_routes = [[i, i*100] for i in range(1, 1001)]
        result = optimize_air_routes(100000, forward, return_routes)
        assert isinstance(result, list)
        assert len(result) > 0
