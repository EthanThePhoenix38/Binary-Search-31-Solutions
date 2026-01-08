import pytest
from src.problem2_h_index_ii import h_index


class TestHIndex:
    """Test cases for the h_index function."""

    def test_basic_example(self):
        """Test with basic example from problem statement."""
        result = h_index([0, 1, 3, 5, 6])
        assert result == 3

    def test_all_zeros(self):
        """Test with all zero citations."""
        result = h_index([0, 0, 0, 0])
        assert result == 0

    def test_all_high_citations(self):
        """Test when all citations are high."""
        result = h_index([10, 20, 30, 40, 50])
        assert result == 5

    def test_single_element_zero(self):
        """Test with single element array with zero."""
        result = h_index([0])
        assert result == 0

    def test_single_element_positive(self):
        """Test with single element array with positive value."""
        result = h_index([10])
        assert result == 1

    def test_ascending_sequence(self):
        """Test with ascending sequence."""
        result = h_index([1, 2, 3, 4, 5])
        assert result == 3

    def test_h_index_at_start(self):
        """Test when h-index is at the start of array."""
        result = h_index([5, 6, 7, 8, 9])
        assert result == 5

    def test_h_index_at_end(self):
        """Test when h-index is at the end of array."""
        result = h_index([0, 0, 0, 1])
        assert result == 1

    def test_duplicate_values(self):
        """Test with duplicate citation values."""
        result = h_index([2, 2, 2, 2, 2])
        assert result == 2

    def test_large_gaps(self):
        """Test with large gaps in citation values."""
        result = h_index([0, 1, 100])
        assert result == 1

    def test_exactly_h_papers(self):
        """Test when exactly h papers have h citations."""
        result = h_index([4, 4, 4, 4])
        assert result == 4

    def test_two_elements(self):
        """Test with two elements."""
        result = h_index([1, 2])
        assert result == 1

    def test_performance_large_array(self):
        """Test performance with large sorted array."""
        citations = list(range(10000))
        result = h_index(citations)
        assert isinstance(result, int)
        assert 0 <= result <= len(citations)

    def test_all_same_high_value(self):
        """Test with all papers having same high citation count."""
        result = h_index([100, 100, 100, 100, 100])
        assert result == 5

    def test_descending_to_ascending_threshold(self):
        """Test threshold transition."""
        result = h_index([0, 1, 4, 5, 6])
        assert result == 3
