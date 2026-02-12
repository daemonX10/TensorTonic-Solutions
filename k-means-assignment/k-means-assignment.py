def k_means_assignment(points, centroids):
    """
    Assign each point to the nearest centroid.
    """
    # Write code here
    assignments = []
    for point in points:
        min_dist = float("inf")
        min_idx = 0

        for idx , centroid in enumerate(centroids):
            distance = 0
            for dim in range(len(point)):
                distance+= (point[dim] - centroid[dim])**2
            if distance <min_dist:
                min_dist = distance
                min_idx = idx
        assignments.append(min_idx)
    return assignments



