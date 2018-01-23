class TreeNode:
   __slots__ = 'val', 'children', 'parent'

   def __init__(self, val, parent = None):

      self.val = val
      self.children = []
      self.parent = parent

   def getStringRep(self):#do not modify
      return self._getStringRep(0)
   def _getStringRep(self,depth ):#do not modify
      ret = self.val
      for c in self.children:
         
         ret +="\n"+"    "*depth+"+---"+(c._getStringRep(depth+1))
      return ret
   def __str__(self):#do not modify
      return str(self.val)
   def __repr__(self):#do not modify
      return str(self.val)
   def __eq__(self, other):#do not modify
      if type(self) != type(other):
         return False
      return self.val == other.val
class Tree:
   __slots__ = 'root', 'nodeLookup'

   def __init__(self): #do not modify
      self.root = None
      self.nodeLookup = dict()

   def getStringRep(self): #do not modify
      if self.root:
         return self.root.getStringRep()
      return "[empty]"

   def getNodeByValue(self, value): #do not modify
      return self.nodeLookup[value]


   def addRoot(self, value):#do not modify
      """
      Creates a new node using the value and places it at the root
      :param value: the value of the root
      """
      assert  value not in self.nodeLookup and not self.root 
      assert type(value) == str
      node = TreeNode(value)
      self.nodeLookup[value]=node
      self.root = node

   def addChildTo(self, newChildValue, parentValue):
      """
      Creates a new node using the newChildValue and adds it to the node representing the parentValue
      :param newChildValue: The value of the new child node
      :param parentValue: The value of the intended parent

      """

      assert parentValue in self.nodeLookup and newChildValue not in self.nodeLookup  
      assert type(newChildValue) == str and type(parentValue) == str
      node = TreeNode(newChildValue, parentValue)
      self.nodeLookup[parentValue].children.append(node)
      self.nodeLookup[newChildValue] = node


   def getHeight(self):
      """ Calculates the height of the tree"""
      if self.root is None:
         return -1
      elif len(self.root.children) == 0:
         return 0
      else:
         return 1+ self.getHeight()



   def getPathToRoot(self,nodeValue ):
      """
       Finds the path between the node specified by nodeValue and the root of the tree
      :param nodeValue: The value of the node
      :return: A list of nodes representing the path between the node and the root of the tree
      """
      assert nodeValue in self.nodeLookup
      assert type(nodeValue) == str
      pathToRoot = []
      if self.nodeLookup[nodeValue].parent != None:
         pathToRoot.append(self.nodeLookup[nodeValue].parent)
      return pathToRoot

   def getLCA(self,node1Value,node2Value):
      """
      Finds the lowest common ancestor (a.k.a. least common subsumer, most specfic subsumer,etc) of the nodes specfied by the two arguments (i.e. the first common ancestor you would encounter when moving up the tree from node1 and node2). 
      :param node1Value: The value of node1
      :param node2Value: The value of node2
      :return: The value of the node
      """
      assert node1Value in self.nodeLookup and node2Value in self.nodeLookup
      assert type(node1Value) == str and type(node1Value) == str
      if self.nodeLookup[node1Value].parent == None or self.nodeLookup[node2Value].parent == None :
         return None
      elif self.nodeLookup[node1Value].parent == self.nodeLookup[node2Value].parent:
         return (self.nodeLookup[node1Value].parent)
      else:
         self.getLCA(self.nodeLookup[node1Value].parent, self.nodeLookup[node2Value].parent)



   

def test():
   t = Tree()
   t.addRoot("thing")
   #add children here
   t.addChildTo("animal","thing")
   t.addChildTo("plant", "thing")

   t.addChildTo("mammal", "animal")

   t.addChildTo("dog", "mammal")
   t.addChildTo("cat", "mammal")
   t.addChildTo("human", "mammal")


   t.addChildTo("fish", "animal")
   t.addChildTo("tuna", "fish")
   
   #add the rest here
   

   print(t.getStringRep())
#height
   # print(t.getHeight())

#path to root
   # print("getPathToRoot('animal') =",t.getPathToRoot("animal"))
   # print("getPathToRoot('thing') =",t.getPathToRoot("thing"))
#LCA
   print("LCA('cat','dog') =",t.getLCA("cat","dog"))


if __name__ == '__main__':
   test()
