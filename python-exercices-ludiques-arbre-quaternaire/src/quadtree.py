from __future__ import annotations
class QuadTree:
    NB_NODES : int = 4
    node_list = []
    def __init__(self, hg: bool | QuadTree, hd: bool | QuadTree, bd: bool | QuadTree,bg: bool | QuadTree):
        self.node_list = [hg,hd,bg,bd]


    @property
    def depth(self) -> int:
        """ Recursion depth of the quadtree"""

        # definition des variables utilisés dans cette property
        child = 0
        nodes = self.node_list
        deep = 0

        """
        on parcourt l'ensemble des noeuds de l'arbre courrant, si un noeud est un autre arbre alors on compte 1 child 
        en plus et on regarde la profondeur de celui-ci, si elle supérieur à l'arbre courant alors on garde cette valeur
        sinon on compte 1 profondeur en plus 
        
        Si notre arbre n'a pas d'autre arbre enfant alors il retourne 1 comme profondeur
        
        """
        for item in nodes :
            if type(item) is QuadTree :
                child +=1
                if item.depth > deep :
                    deep = item.depth
                else :
                    deep += 1

        if child == 0:
            return 1

        return deep


    @staticmethod
    def fromFile(filename: str) -> QuadTree:
        """ Open a given file, containing a textual representation of a list"""
        with open(filename,'r',encoding='utf-8') as f:
            line = f.read()
        return QuadTree.fromList(eval(line))

    @staticmethod
    def fromList(data: list) -> QuadTree:
        """ Generates a Quadtree from a list representation"""
        liste_node = []

        """ 
            on parcourt chaque element de la liste récupéré dans le fichier d'entré et on regarde si c'est une liste ou 
            non, si oui alors on crée un arbre à partir de cette liste et on l'ajoute à final sinon on ajoute simplement
            l'element 
        """
        for item in data:
            typed_item = eval(str(item))
            if type(typed_item) is list :
                liste_node.append(QuadTree.fromList(item))
            elif type(typed_item) is bool or type(typed_item) is int :
                liste_node.append(item)

        return QuadTree(liste_node[0],liste_node[1],liste_node[3],liste_node[2])

class TkQuadTree(QuadTree):
    def paint(self):
        """ TK representation of a Quadtree"""
        pass

