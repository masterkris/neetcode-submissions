class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        # first thought: Dijkstra's algorithm
        # adjacency list for graph
        # weighted graph, minimum path

        # min_times dict
        # min_heap, push tuples
        # keep min on top

        # build the graph
        graph = defaultdict(list)

        for u, v, time in times:
            graph[u].append((v, time)) # get to v in time

        # store shortest distances found
        min_times = {}
        min_heap = [(0, k)] # (distance from source to node, node), starting at node k

        while min_heap:
            time_k_to_i, i = heapq.heappop(min_heap) # closest node

            # [(1,1), (5,4), (2,3)]
            # (1, 1)

            if i in min_times: # seen before, ignore
                continue
            
            # finalize shortest distance (smallest from k to i)
            min_times[i] = time_k_to_i # never changed after this

            for nei, nei_time in graph[i]: # explore neighbors
                if nei not in min_times:
                    heapq.heappush(min_heap, (time_k_to_i + nei_time, nei)) # push new distances
        
        if len(min_times) == n: # all nodes visited
            return max(min_times.values())
        else:
            return -1
        