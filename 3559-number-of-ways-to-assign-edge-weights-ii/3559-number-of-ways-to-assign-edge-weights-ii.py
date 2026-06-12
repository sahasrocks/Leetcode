# Commented code
class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], 
                        queries: List[List[int]]) -> List[int]:
        n = len(edges) + 1

        # If tree only has 2 nodes, then each query either has 
        # answer 0 (u and v are the same node) or 1 (u and v 
        # are different nodes)
        # 7 of 589 test cases.  (1%)  June 2026
        if n == 2:
            return [abs(u - v)  for u,v in queries]

        # Convert the edges to an array of links for each node.  
        # The arrays are more useful when traversing the tree.
        def buildGraph(edges: List[List[int]]) -> None:
            for u,v in edges:
                graph[u].append(v)
                graph[v].append(u)
            return
        
        # Traverse the tree.  Find the maximum level of the tree.  
        # For each node, find the level in the tree (0..maxLevel), 
        # and parent node.
        def dfs(node: int, parent: int, level: int) -> None:
            nonlocal graph, levels, parents, maxLevel
            levels[node] = level
            if level > maxLevel:  maxLevel = level
            parents[node] = parent
            for child in graph[node]:
                if child == parent:  continue
                dfs(child, node, level + 1)
            return

        # Fill the ancestor 2-D array.  The ancestor array is arranged 
        # as ancestor[k][u], where u is the node for which ancestor 
        # nodes are wanted, and k is distance as a power of 2, back to 
        # the pow(2,k)'th ancestor of node u.  So that ancestor[3][17] 
        # is the pow(2,3)'th==8th ancestor of node 17.  And 
        # ancestor[0][5] is the pow(2,0)'th==1st ancestor of node 5.
        # This 2-D ancestor array makes it quick to move up the tree to 
        # any desired ancestor level of a node.
        def fillAncestors() -> None:
            nonlocal ancestors, ancestorSize
            for level2k in range(0, ancestorSize):
                ancestors[level2k][0] = 0
            for level2k in range(1, ancestorSize):
                ancCur = ancestors[level2k]
                ancPrv = ancestors[level2k - 1]
                for u in range(n + 1):
                    ancCur[u] = ancPrv[ancPrv[u]]
            return

        # Find the edge distance between any two tree nodes u and v.  
        # This routine always makes u the deeper node, unless u and v 
        # are at the same level.  Methods for distance are:
        # 1) u and v are the same node
        #       Distance is zero.
        # 2) u is a descendent of v:
        #       Distance is the difference in levels of u and v.
        # 3) u and v have a lowest common ancestor (LCA) that is higher 
        #    in the tree than both u and v.
        #       Distance is the distance between u and the LCA, plus the 
        #       distance between v and the LCA.
        #
        # To find the lowest common ancestor (LCA) of u and v, first 
        # ascend the tree from u to the same level as v, if not already 
        # at the same level.  When reaching the same level, is reached 
        # node v by ascending from node u, then u is a descendant of 
        # v, so just return the difference in levels.  Otherwise u and v 
        # are on separate branches, so a lowest common ancestor must be 
        # found.  Ascend from both that same-level-u-ancestor and v, 
        # until a common ancestor node is reached.  Ascending the tree 
        # is done non-linearly by steps of sizes that are decreasing 
        # powers of 2.
        #
        # Use the ancestor[][] array to quickly ascend the tree by steps 
        # of decreasing powers of 2.  As an example, to ascend upward from 
        # node u, to the 11th ancestor of u, first jump to node 
        # u' = ancestor[3][u] which is the 8th==pow(2,3)'th ancestor of u.  
        # Then jump to node u'' = ancestor[1][u'], which is jumping to the 
        # 2nd==pow(2,1)'th ancestor but starting from node u'.  Finally 
        # jump to node u''' = ancestor[0][u''], which is jumping to the 
        # 1st==pow(2,0)'th ancestor but starting from node u''.  Therefore 
        # u''' will be the 11th ancestor node of u, but found in only 3 
        # jumps.  Notice that 11 == 8+2+1 == pow(2,3) + pow(2,1) + pow(2,0), 
        # and that 8,2,1 correspond to the set bits (1-bits) in the value 11.  
        # This allows finding x'th ancestor of any node in log base 2 time, 
        # or more precisely, in x.bit_count() jumps.
        def distance(u: int, v: int) -> int:
            nonlocal ancestors, levels
            # # If u and v are the same node, then the distance between 
            # # them is zero.  (Not needed because this condition is 
            # # eliminated before this function is called.)
            # if u == v:  return 0

            # Make sure u is deeper in the tree than v.
            if levels[u] < levels[v]:   
                u, v = v, u

            # Move upward from u to be the same level as v.  Move upward 
            # in steps of size pow(2,k) for decreasing k.
            uCur = u
            vCur = v
            uExtra = levels[u] - levels[v]
            if uExtra > 0:
                for k in range(uExtra.bit_length() - 1, -1, -1):
                    if uExtra & (1 << k):
                        uCur = ancestors[k][uCur]
            
            # After ascending from u up to the same level as v, if node 
            # v has been reached by the ascension from u, then u is a 
            # descendant of v, and the distance between is simply the 
            # difference in levels.
            if uCur == vCur:
                return uExtra

            # Move upward from uCur and vCur, until a common ancestor is 
            # found.  Move upward in steps of size pow(2,k) for decreasing k, 
            # but only move upward each pow(2,k) step if that move of both 
            # nodes updard will still be in separate brances of the tree.  
            # After moving upward as far as possible in separate branches, 
            # then the direct parent of those two nodes will be the least 
            # common ancestor node of u and v.
            for k in range(levels[vCur].bit_length() - 1, -1, -1):
                if ancestors[k][uCur] != ancestors[k][vCur]:
                    uCur = ancestors[k][uCur]
                    vCur = ancestors[k][vCur]
            return levels[u] + levels[v] - levels[ancestors[0][uCur]] * 2


        # Build the graph from the edges.
        graph = [[] for _ in range(n + 1)]
        buildGraph(edges)

        # Recursively traverse the tree to find the level, parent, and range 
        # of leaf-path numbers for each node of the tree.
        levels = [None] * (n + 1)
        parents = [None] * (n + 1)
        maxLevel = 0
        dfs(1, 0, 0)

        # Fill in the ancestor[][] array with power-of-2'th ancestors nodes 
        # for each tree node.  The pow(2,0)'th==1st ancestor of each node 
        # is its parent.
        ancestorSize = maxLevel.bit_length()
        ancestors = [parents  if k == 0 else  [None] * (n + 1)  
                        for k in range(ancestorSize)]
        fillAncestors()

        # Process each query.  Find the distance dist between nodes u and v 
        # as the number of edges on a path between the nodes.  If assigning 
        # weights to each edge on the path as eith weight 0 or weight 1, this 
        # will give pow(2,dist) different path-weight configurations.  This 
        # leetcode problem wants the number of these path configuration of 
        # edge weights, such that the sum of the edge weights on the path is 
        # odd.  Of the pow(2,dist) different configurations of edge weights, 
        # half will have an odd sum.  Therefore the number of odd sums is 
        # pow(2,dist-1), unless dist==0 which will have zero odd summed 
        # combinations.
        # 
        # Use a cache of queries and answers, to speed up duplicate queries.  
        # Only about 5% of test cases have any duplicate queries, but this 
        # caching seems to slightly speed up the runtime.
        cache = dict()
        result = [None] * len(queries)
        for i, (u, v) in enumerate(queries):
            ans = cache.get(u * 1_000_000 + v)
            if ans is None:
                ans = 0  if u == v else  pow(2, distance(u, v) - 1, 1_000_000_007)
                cache[u * 1_000_000 + v] = ans
            result[i] = ans
        return result