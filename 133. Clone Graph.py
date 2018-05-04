class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):   
        def cloneNode_dfs(node,map):
            if map.has_key(node):
                return map[node]
                ##访问当前点，这里不是简单的print，而是复制，若已经复制，则返回副本  
                #若没有副本，则复制一份，同样处理其邻接点  
            else:
                clone = UndirectedGraphNode(node.label)
                map[node] = clone
                #访问其邻居节点  
                for neighbor in node.neighbors:
                    clone.neighbors.append(cloneNode_dfs(neighbor,map))
            return clone
        
        if node==None:return None
        map={}
        return cloneNode_dfs(node,map)
        
       #使用map存储一个映射，key是原节点，value是复制的节点，map的作用在于替代bfs和dfs中的visit数组，一旦map中出现了映射关系，
       就说明已经复制完成，也就是已经访问过了。
       递归中的return只能返回上一层递归,这可以看作是跳出递归的一种方式，返回map[node]，即使回溯回到了上一个节点
#----------------------------------DFS----------------------------------
       
       cloneNode函数输入一个node，准确的说是一个graph，因为这个node，还记录了其neighbors node. neighbors 还有neighbors。所以graph中任意一个node，其实就相当于linkedlist的head。其实返回的也是一个graph，copy的graph。这样就可以理解下面这句code了

也可以这样理解，这里self.cloneNode函数就是clone一个Node，对于node.neighbors内每个neighbor，都要进行clone，然后添加到其neighbors来。

clone.neighbors.append(self.cloneNode(neighbor, nodeMap))

# --------------------- BFS--------------------------------------
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node == None:return None
        queue = []
        nodemap = {}
        newhead = UndirectedGraphNode(node.label)
        nodemap[node] = newhead
        queue.append(node)
        while queue:
            t = queue.pop()
            for neighbor in t.neighbors:
                if neighbor not in nodemap:
                    clone = UndirectedGraphNode(neighbor.label)
                    nodemap[t].neighbors.append(clone)
                    nodemap[neighbor] = clone
                    queue.append(neighbor)
                else:
                    nodemap[t].neighbors.append(nodemap[neighbor])
        return newhead


bfs采用的是迭代的方式，利用一个队列存储要遍历的点，出队列的时候遍历所有的邻居，
用map来记录是否遍历过，是visited的作用
都是遍历，所以时间复杂度为O(N)







