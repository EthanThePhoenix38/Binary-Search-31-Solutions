"""Problem 1: Optimize Air Routes

Amazon Prime Air - Find optimal forward and return route pairs that maximize
travel distance without exceeding the aircraft's maximum operating distance.

Time Complexity: O(n log n + m log m + n*m) where n=len(forward), m=len(return)
Space Complexity: O(1) auxiliary space (excluding result)

Author: EthanThePhoenix38
Date: 2026-01-08
Forked from: super30admin/Binary-Search-31
"""

from typing import List, Tuple


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
        2. Use two-pointer technique to find optimal pairs (O(n*m) worst case)
        3. Track best distance and collect all pairs matching it
        4. Handle edge case: routes with identical distances
        
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
        # Note: We can't use binary search directly because we need ALL pairs
        # with the same optimal distance, not just one
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


# Alternative optimal solution using two-pointer technique
# This is more efficient for the case where we only need one optimal pair
def optimize_air_routes_two_pointer(
    max_travel_dist: int,
    forward_route_list: List[List[int]],
    return_route_list: List[List[int]]
) -> List[List[int]]:
    """
    Optimized two-pointer solution.
    
    Time Complexity: O(n log n + m log m + n + m)
    Space Complexity: O(1) auxiliary
    
    Better for finding optimal pairs when we don't need to check all combinations.
    However, requires additional logic to find ALL pairs with max distance.
    """
    if not forward_route_list or not return_route_list:
        return [[]]
    
    # Sort both lists
    forward_route_list.sort(key=lambda x: x[1])
    return_route_list.sort(key=lambda x: x[1])
    
    left = 0  # Pointer for forward routes
    right = len(return_route_list) - 1  # Pointer for return routes (start from end)
    best_distance = -1
    result = []
    
    # Move pointers toward each other
    while left < len(forward_route_list) and right >= 0:
        fwd_id, fwd_dist = forward_route_list[left]
        ret_id, ret_dist = return_route_list[right]
        current_distance = fwd_dist + ret_dist
        
        if current_distance > max_travel_dist:
            # Total too high, decrease return distance
            right -= 1
        else:
            # Valid combination
            if current_distance > best_distance:
                best_distance = current_distance
                result = [[fwd_id, ret_id]]
            elif current_distance == best_distance:
                result.append([fwd_id, ret_id])
            
            # Try to find more combinations with this return route
            # by checking forward routes with same distance
            temp_left = left + 1
            while (temp_left < len(forward_route_list) and 
                   forward_route_list[temp_left][1] == fwd_dist):
                if current_distance == best_distance:
                    result.append([forward_route_list[temp_left][0], ret_id])
                temp_left += 1
            
            # Move to next forward route
            left += 1
    
    return result if best_distance != -1 else [[]]
