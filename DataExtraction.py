


class ExtractionData:
    def __init__(self, CourseName, preq) -> None:
        self.CourseName = CourseName
        self.preq = preq

class ListNode:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None
class Graph:
    def __init__(self,counter) -> None:
        self.graph = {}
        self.counter = counter
    def add_connections(self,data):
        for i in range(len(data.preq)):
            if data.preq[i] == 'N/A':
                pass
            else:
                node = ListNode(data.CourseName)
                node.next = self.graph[data.preq[i]]
                self.graph[data.preq[i]] = node
    def add_labels(self, data):
        self.graph[str(data.CourseName)] = None

incrementor = 0   
def topologicalSortUtil(graph, v, visited,listofobjects,hashmap,pre,post):
        # Mark the current node as visited.
  global incrementor
  incrementor +=1
  pre[v] = incrementor
  visited[v] = True
  cur = graph.graph[listofobjects[v].CourseName]
        # Recur for all the vertices adjacent to this vertex
  while cur is not None:
    if visited[hashmap[cur.value]] == False:
      topologicalSortUtil(graph,hashmap[cur.value], visited,listofobjects,hashmap,pre,post)
    cur = cur.next
     #   for i in self.graph[v]:
      #      if visited[hashmap[i]] == False:
       #         self.topologicalSortUtil(i, visited, stack,listofobjects)
 
        # Push current vertex to stack which stores result
  #stack.append(listofobjects[v].CourseName)
  incrementor+=1
  post[v] = incrementor
    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
def topologicalSort(graph,listofobjects,hashmap,pre,post):
        # Mark all the vertices as not visited
  visited = [False]*graph.counter
 
        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
  for i in range(len(listofobjects)):
    if visited[i] == False:
                #print(self.graph[listofobjects[i].CourseName])
      topologicalSortUtil(graph,i, visited,listofobjects,hashmap,pre,post)
 
        # Print contents of the stack
  #print(stack[::-1])




file = open("Data.txt","r",newline=None)
flag = 0
list1 = []
list2 = []
listofobjects = list()
hashmap = {}
counter = 0
while True:
    data = file.readline() #reading the data through each line until data is present
    if not data:
        break
    vals = data.strip() #removing the leading and trailing characters in all data sets
    str1 = ''
    str2 = ''
    list1 = []
    list2 = []
    for i in vals:
        
        if i == '(' and flag == 0:
            flag = 1
            continue
        if flag == 1:
            if i == ')':
                break
            str2 = str2 + i
            continue
        else:
            str1 = str1 + i
            flag = 0
    flag = 0
    #print(str1)
    str1 = str1[:str1.index('-')-1]
    #print(str1)
    #print(str2)
    list1 = str2.split(' and ')
    length = len(list1)
    #print(list1)
    for i in list1:
        if ',' in i:
            list2 = i.split(', ')
            list2.append(list1[len(list1)-1])
            list1 = list2.copy()
            break
        else:
            continue
    #print(list1)
    listofobjects.append(ExtractionData(str1,list1))
    hashmap[str1] = counter
    counter+=1
graph = Graph(counter)
for i in range(len(listofobjects)):
    #print(listofobjects[i].CourseName, listofobjects[i].ID, listofobjects[i].preq)
    graph.add_labels(listofobjects[i])
    graph.add_connections(listofobjects[i])
'''    
for i in graph.graph:
    cur = graph.graph[i]
    print(i,end='')
    while cur is not None:
        print('->', end = '')
        print(cur.value, end = '')    
        cur = cur.next
    print()
''' 
pre = [0]*(graph.counter)
post = [0]*(graph.counter)

#post = []
topologicalSort(graph, listofobjects,hashmap,pre,post)

#print(pre)
#print(post)
j = 0
for i in hashmap:
  hashmap[i] = post[j]
  j+=1

#print(sorted(post,reverse=True))
#print(post.index(56))

for w in sorted(hashmap, key = hashmap.get, \
                reverse = True):
    print(w)
