import heapq

class HuffmanNode(object):
    def __init__(self, freq, char=None, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    # used mainly for debugging purposes
    def __repr__(self):
        return "HuffmanNode(char=%s, freq=%s)" % (self.char, self.freq)

    # needed for node comparison. Utilized to order the nodes appropriately
    # in the priority queue
    def __lt__(self, other):
        return self.freq < other.freq

    def isLeaf(self):
        return (self.left == None and self.right == None)

def buildHTree(freqData):
    huffmanNodes = []
    for char in freqData:
        huffmanNodes.append(HuffmanNode(freqData[char], char))
    # the list of huffmanNodes is transformed into a priority queue to keep
    # track of the minimum-frequency Huffman Nodes
    heapq.heapify(huffmanNodes)
    while (len(huffmanNodes) > 1):
        # obtain the two minimum-frequency Huffman nodes 
        child1 = heapq.heappop(huffmanNodes)
        child2 = heapq.heappop(huffmanNodes)
        parent = HuffmanNode(child1.freq + child2.freq, left=child1, right=child2)
        heapq.heappush(huffmanNodes, parent)
    return None if huffmanNodes == [] else heapq.heappop(huffmanNodes)

def hTreeToHCode(hTree):
    code = dict()
    # a left edge represents a 0 bit, a right edge represents a 1 bit, and
    # the path from the root to a leaf gives the code word for the character 
    # stored at that leaf.
    def getCode(hNode, curCode=""):
        if (hNode == None): return
        if (hNode.left == None and hNode.right == None):
            code[hNode.char] = curCode
        getCode(hNode.left, curCode + "0")
        getCode(hNode.right, curCode + "1")
    getCode(hTree)
    return code

def encode(s, freqData):
    hTree = buildHTree(freqData)
    hCode = hTreeToHCode(hTree)
    hEncoded = ""
    for char in s:
        hEncoded += hCode[char]
    return hEncoded.strip()

def decode(s, freqData):
    hTree = buildHTree(freqData)
    decodedStr = ""
    curTreeNode = hTree
    for charCode in s:
        if (charCode == "0"):
            curTreeNode = curTreeNode.left
        else:
            curTreeNode = curTreeNode.right
        if (curTreeNode.isLeaf()):
            decodedStr += curTreeNode.char
            curTreeNode = hTree
    return decodedStr

freqData = {"e":5, "o":2, "m":1, "c":1, "r":2, "f":3}
encodedStr = encode("morefreecofee", freqData)
print("encodedStr", encodedStr)
decodedStr = decode(encodedStr, freqData)
print("decodedStr", decodedStr)
