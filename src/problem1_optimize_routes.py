"""Problem 1: Optimize Air Routes

Amazon Prime Air - Find optimal forward and return route pairs that maximize
travel distance without exceeding the aircraft's maximum operating distance.

Time Complexity: O(n log n + m log m + n*m) where n=len(forward), m=len(return)
Space Complexity: O(1) auxiliary space (excluding result)

Author: EthanThePhoenix38
Date: 2026-01-08
Forked from: super30admin/Binary-Search-31
"""

from typing import List


def optimize_air_routes(
    max_travel_dist: int,
    forward_route_list: List[List[int]],
    return_route_list: List[List[int]]
) -> List[List[int]]:
    """
    Find all pairs of forward and return routes that optimally utilize aircraft capacity.
    
    Given a maximum travel distance and lists of forward/return routes, this function
    identifies all route pairs whose combined distance is maximum while not exceeding
    the aircraft's range.
    
    Args:
        max_travel_dist: Maximum operating travel distance of the aircraft (integer)
        forward_route_list: List of [route_id, distance] pairs for forward routes
        return_route_list: List of [route_id, distance] pairs for return routes
    
    Returns:
        List of [forward_id, return_id] pairs representing optimal routes.
        Returns [[]] if no valid route combination exists.
    
    Example:
        >>> optimize_air_routes(7000, [[1,2000],[2,4000],[3,6000]], [[1,2000]])
        [[2, 1]]
    
    Explanation: Combinations are [1,1]=4000, [2,1]=6000, [3,1]=8000.
    6000 is maximum without exceeding 7000.
    
    Algorithm:
        1. Sort both route lists by distance (O(n log n) + O(m log m))
        2. Use nested loops to find all optimal pairs (O(n*m) worst case)
        3. Track best distance and collect all pairs matching it
        4. Handle edge cases: empty lists, routes exceeding capacity
    
    Notes:
        - Input lists are modified (sorted in-place) for efficiency
        - Multiple pairs can have the same optimal distance
        - Empty input lists return [[]]
    """
    # Edge case: empty route lists
    if not forward_route_list or not return_route_list:
        return [[]]
    
    # Sort routes by distance (second element of each pair)
    # Time: O(n log n + m log m)
    forward_route_list.sort(key=lambda route: route[1])
    return_route_list.sort(key=lambda route: route[1])
    
    # Initialize tracking variables
    best_distance = -1  # Maximum valid distance found so far
    result = []  # Store all optimal route pairs
    
    # Two-pointer approach: iterate through all combinations
    # Outer loop: forward routes (smallest to largest distance)
    for forward_id, forward_dist in forward_route_list:
        
        # Inner loop: return routes (check all possibilities)
        # Note: We need ALL pairs with the same optimal distance
        for return_id, return_dist in return_route_list:
            current_distance = forward_dist + return_dist
            
            # Skip if this combination exceeds aircraft capacity
            if current_distance > max_travel_dist:
                # Optimization: Since return_route_list is sorted, all subsequent
                # return routes will also exceed the limit with this forward route
                break
            
            # Found a new best distance
            if current_distance > best_distance:
                best_distance = current_distance
                result = [[forward_id, return_id]]  # Reset result list
            
            # Found another pair with the same optimal distance
            elif current_distance == best_distance:
                result.append([forward_id, return_id])
    
    # Return empty pair if no valid routes found
    return result if best_distance != -1 else [[]]
