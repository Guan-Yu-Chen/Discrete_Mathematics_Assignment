# This code can run without a problem.
# 
# How to run: 
# 1. Input the network filename (e.g., input_100_400_1.sp)
# 2. It reads the file and stores the graph by adjacency matrix and adjacency list 
# 3. The program repeatedly asks the user to input a source node index (0 to exit).
# 4. If the input is not 0, it asks the user to choose:
#    (1) Adjacency Matrix or (2) Adjacency List.
# 5. Depending on the chosen structure, it prints the outgoing and incoming arcs of the input vertex.
#       Output format:
#       Please input the source vertex index (0 to exit): 15
#       Please choose (1) Adjacency Matrix (2) Adjacency List : 2
#       Outgoing arcs: (15, 16), (15, 79)
#       Incoming arcs: (14, 15), (19, 15)
# 6. Repeat steps 3–5 until the user inputs 0, which terminates the program.
# 
# This code is written by G07_H34121151  email H34121151@gs.ncku.edu.tw, on 2025/04/19

class Arc():
    def __init__(self, tail: int, head: int, length: int):
        self.tail = tail
        self.head = head
        self.length = length
    
    def toString(self) -> str:
        return f"({self.tail}, {self.head})"

class Node():
    def __init__(self, id: int):
        self.id = id
        self.arcs = []
        self.outDeg = 0
        self.inDeg = 0

    def addArc(self, arc: Arc):
        self.arcs.append(arc)

    def arcs2String(self) -> str:
        self.arcs.sort(key=lambda a: a.tail)
        a = ""
        for arc in self.arcs:
            a += f"{arc.toString()}, " 
        return a[:-2]


file = input("Input your network filename = ")
with open(file, 'r') as f:
    lines = f.readlines()
    for line in lines:
        data = line.split()
        if data[0] == 'n':
            node_num = int(data[1])
            matrix_a = [[0 for _ in range(node_num+1)] for _ in range(node_num+1)]
            matrix_c = [[0 for _ in range(node_num+1)] for _ in range(node_num+1)]
            adj_list = [Node(i) for i in range(node_num+1)]

        if data[0] == 'a':
            tail = int(data[1])
            head = int(data[2])
            length = int(data[3])
            matrix_a[tail][head] = 1
            matrix_c[tail][head] = length
            adj_list[tail].addArc(Arc(tail, head, length))

while True:
    index = int(input("Please input the source vertex index (0 to exit): "))
    if index == 0:
        print("Program end...")
        break

    m = input("Please choose (1) Adjacency Matrix (2) Adjacency List : ")
    outArcs = ""
    inArcs = ""

    if m == '1':
        for i in range(node_num+1):
            if matrix_a[index][i]:
                outArcs += f"({index}, {i}), "
            if matrix_a[i][index]:
                inArcs += f"({i}, {index}), "
        outArcs = outArcs[:-2]
        inArcs = inArcs[:-2]

    if m == '2':
        outArcs += adj_list[index].arcs2String()
        for node in adj_list:
            for arc in node.arcs:
                if arc.head == index:
                    inArcs += f"{arc.toString()}, "
        inArcs = inArcs[:-2]

    print(f"Outgoing arcs: {outArcs}")
    print(f"Incoming arcs: {inArcs}")
    print("")