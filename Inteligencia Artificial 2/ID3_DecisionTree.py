import pandas
import numpy

class ID3_DecisionTree:
    def __init__(self):
        self.X = None
        self.Y = None
        self.root = None

    def fit(self,X,Y):
        self.X = X
        self.Y = Y
        n = len(X)
        idx = numpy.arange(n)
        self.root = Node.create_node(self.X,self.Y,idx)

    def predict(self,X):
        Y = []
        for i in range(len(X)):
            sample = X[i, :]
            aux = self.root
            while (type(aux) is not NodeLeaf):
                var = aux.var
                ans = sample[var]
                index = 0
                for e in range(len(aux.children_values)):
                    if (aux.children_values[e] == ans):
                       index = e
                aux = aux.children_nodes[index]
            Y.append(aux.to_string(' '))
        return Y

    def to_string(self):
        return self.root.to_string('')

class Node:
    def __init__(self,X,Y,idx):
        self.idx = []

    def to_string(self,space):
        raise NotImplementedError('Abstract method')

    def create_node(X,Y,idx):
        print('Create node:',len(idx))
        h = Node.__entropy(Y,idx)
        if h<=.1:
            return NodeLeaf(Y,idx)
        #if h!=0:
        X_ = X[idx,:]
        Y_ = Y[idx]
        #Calcular las ganancias de cada una de las variables
        nsamples,nvar = X_.shape
        G = numpy.zeros((nvar),float)
        for i in range(nvar):
            G[i] = h
            uI,cI = numpy.unique(X_[:,i],return_counts=True)
            for k,u in enumerate(uI):
                wk = cI[k]/nsamples
                hk = Node.__entropy(Y_,X_[:,i]==u)
                G[i]-= wk*hk
        i = numpy.argmax(G)
        # Construir el nodo de decision y mandar construir los nodos hijo
        node = NodeDecision(i,idx)
        for k,u in enumerate(numpy.unique(X[:,i])):
            idxu = numpy.arange(len(X)) #idxu = [0,1,2,...,nsamples]
            idxu = idxu[X[:,i]==u]
            idxk = [val for val in idxu if val in idx] #intersection(idx,idxu]
            if len(idxk)>0:
                node.add_child(u,Node.create_node(X,Y,idxk))
        return node

    def __entropy(Y, idx):
        Y_ = Y[idx]
        # Y_: subvector de Y, sólo con los registros de idx
        n = len(Y_)
        uY, c = numpy.unique(Y_, return_counts=True)
        # uY: valores únicos Y_,   c:contadores de los valores únicos
        p = c / n
        return -sum(p * numpy.log2(p))

class NodeLeaf(Node):
    def __init__(self,Y,idx):
        self.label = Y[idx[0]]

    def to_string(self,space):
        return '\n'+space+'Leaf:'+str(self.label)

class NodeDecision(Node):
    def __init__(self,var,idx):
        self.idx = idx
        self.var = var #Variable por la que pregunta
        self.children_values = [] #Los valores que te llevan a esos hijos.
        self.children_nodes = [] #Los nodos hijos como tal
    def add_child(self,value,node):
        self.children_values.append(value)
        self.children_nodes.append(node)

    def to_string(self,space):
        s = '\n'+space+str(self.var)+'?'
        for i in range(len(self.children_values)):
            s+= '\n'+space+' -'+'value:'+str(self.children_values[i])
            s+= self.children_nodes[i].to_string(space+'  ')
        return s