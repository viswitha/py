class Tree:
	def __init__(self,name,designation):
		self.data={'name':name,'designation':designation,'both':name+" ("+designation+")"}
		self.parent=None
		self.children=[]
	def add_child(self,child):
		child.parent=self
		self.children.append(child)
	def get_level(self):
		level=0
		p=self.parent
		while p:
			level+=1
			p=p.parent
		return level
	def print_Tree(self,typ):
		space=' '*(self.get_level()*2)
		prefix=space+"|__" if self.parent else space
		print(prefix,self.data[typ])
		for child in self.children:
			child.print_Tree(typ)
def build_management_tree():
		ceo=Tree("Nilupul","CEO")
		cto=Tree("Chinmay","CTO")
		hr=Tree("Gels","HR Head")
		ih=Tree("Vishwa","Infrastructure Head")
		ih.add_child(Tree("Dhaval","Cloud Manager"))
		ih.add_child(Tree("Abhijit","App Manager"))
		ah=Tree("Aamir","Application Head")
		hr.add_child(Tree("Peter","Recruitment Manager"))
		hr.add_child(Tree("Waqas","Policy Manager"))
		cto.add_child(ih)
		cto.add_child(ah)
		ceo.add_child(cto)
		ceo.add_child(hr)
		return ceo
		
if __name__=="__main__":
	root_node=build_management_tree()
	root_node.print_Tree("name")
	root_node.print_Tree("designation")
	root_node.print_Tree("both")
