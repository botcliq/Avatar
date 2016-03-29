class Graph(dict):
    def __init__(self, vs = [], es = []):
        """ create a New graph. (vs) is a list of vertices;
        (es is a list of edges.)
        """
        for v in vs:
            self.add_vertex(v)

        for e in es:
            self.add_edges(e)

    def add_vertex(self, v):
        """ Add v to the graph
        :param v:
        :return None:
        """
        self[v] = {}

    def add_edges(self, e):
        """  add (e) to a graph by adding an entity to both directions.
        If there is already an edge connecting the vertices the new edge will replace it.
        :param e:
        :return None:
        """
        v,w = e
        self[v][w] = e
        self[w][v] = e

    def remove_edge(self,e):
        """
        get the edge name and remove the edge from the graph.
        :param e:
        :return:
        """
        try :
            del self[e[0]][e[1]]
            del self[e[1]][e[0]]
            print "edge deleted succesfully"
        except:
            print "THE EDGE is not present"

    def get_edges(self, v, w):
        """
        The function will take two vertices as inout and return the edge if it exist between them
        :param v  'vertex v':
        :param w  'vertex w':
        :return edge:
        """
        try :
            if self[v][w]:
                return self[v][w]
        except:
            return None

    def vertices(self):
        """
        get list of all the vertex present.
        :return [v]:
        """
        return self.keys()

    def edges(self):
        """
        return the list of all the edges in a graph.
        :return [e]:
        """
        edges = []
        for a in self.values():
            for i in a.values():
                edges.append(i)
        return set(edges)

    def out_vertices(self,v):
        """
        get list of all the connected vertices from a given vertices
        :param v:
        :return [v]:
        """
        out_vertices = []
        for i in self.get(v):
            #for key in i.keys():
            out_vertices.append(i)
        return out_vertices

    def out_edges(self,v):
        """
        return a list of all out edges connected to a given vertices.
        :param v:
        :return [e]:
        """
        out_edges = []
        for a in self.get(v):
            try :
                out_edges.append(self[v][a])
            except:
                pass
        return out_edges

    def is_connected(self):


class Vertex(object):
    def __init__(self, label = ''):
        self.label = label

    def __repr__(self):
        return 'Vertex(%s)' %repr(self.label)

    __str__ = __repr__

class Edge(tuple):
    def __new__(cls, e1, e2):
        return tuple.__new__(cls, (e1, e2))

    def __repr__(self):
        return 'Edge(%s, %s)' % (repr(self[0]),repr(self[1]))

    __str__ = __repr__

