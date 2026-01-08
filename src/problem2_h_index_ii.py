"""Problem 2: H-Index II

Calculate the h-index of a researcher given a sorted array of citations.
Optimized binary search solution for O(log n) time complexity.

The h-index is defined as the maximum value of h such that the researcher
has published at least h papers that have each been cited at least h times.

Time Complexity: O(log n) - Binary search on sorted array
Space Complexity: O(1) - Constant auxiliary space

Author: EthanThePhoenix38
Date: 2026-01-08
Forked from: super30admin/Binary-Search-31
LeetCode: https://leetcode.com/problems/h-index-ii/
"""

from typing import List


def h_index(citations: List[int]) -> int:
    """
    Calculate the h-index using binary search on a sorted citations array.
    
    The h-index is the largest number h such that the researcher has at least
    h papers with h or more citations each. Since the array is sorted in
    non-descending order, we can use binary search to find this value efficiently.
    
    Args:
        citations: Sorted list of citation counts per paper (ascending order)
                  Must satisfy: 1 <= len(citations) <= 10^5
                               0 <= citations[i] <= 1000
    
    Returns:
        The h-index value (integer >= 0)
    
    Examples:
        >>> h_index([0, 1, 3, 5, 6])
        3
        Explanation: [0,1,3,5,6] means 5 papers total.
                     - 3 papers have >= 3 citations (3, 5, 6)
                     - Remaining 2 papers have <= 3 citations
                     Therefore h-index = 3
        
        >>> h_index([1, 2, 100])
        2
        Explanation: 2 papers have >= 2 citations (2, 100)
        
        >>> h_index([100])
        1
        Explanation: 1 paper with >= 1 citation
    
    Algorithm:
        The key insight is that for a sorted array citations:
        - At index mid, we have (n - mid) papers from mid to end
        - If citations[mid] >= (n - mid), then h >= (n - mid) is achievable
        - We binary search to find the maximum valid h
    
    Visualization for [0, 1, 3, 5, 6]:
        Index:     0  1  2  3  4
        Citations: 0  1  3  5  6
        Papers:    5  4  3  2  1  (n - index)
        
        At index 2: citations[2]=3, papers=3, 3>=3 ✓ → h >= 3 possible
        At index 1: citations[1]=1, papers=4, 1<4 ✗ → need more citations
    
    Time Complexity: O(log n)
        - Binary search divides search space in half each iteration
        - log2(n) iterations maximum
    
    Space Complexity: O(1)
        - Only uses a constant number of variables (left, right, mid)
        - No recursion or additional data structures
    """
    n = len(citations)
    
    # Edge case: empty array (not expected per constraints, but defensive)
    if n == 0:
        return 0
    
    # Binary search bounds
    # left: minimum possible h-index (0)
    # right: maximum possible h-index (n)
    left, right = 0, n
    
    # Binary search for the largest valid h-index
    while left < right:
        # Find middle index
        mid = (left + right) // 2
        
        # Calculate how many papers we have from mid to end
        papers_count = n - mid
        
        # Check if h-index of papers_count is achievable
        # We need at least papers_count papers with >= papers_count citations
        if citations[mid] >= papers_count:
            # citations[mid] >= papers_count means:
            # - Paper at mid has enough citations
            # - All papers after mid also have enough (array is sorted)
            # - So we have at least papers_count papers with >= papers_count citations
            # Try to find a larger h by searching left half
            right = mid
        else:
            # citations[mid] < papers_count means:
            # - Paper at mid doesn't have enough citations
            # - We need fewer papers (higher h) or more citations
            # Search right half (fewer papers, higher citations)
            left = mid + 1
    
    # At convergence, left == right
    # h-index = n - left (number of papers from left to end)
    return n - left
