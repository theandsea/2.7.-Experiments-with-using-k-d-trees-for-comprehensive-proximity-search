import math
import matplotlib.pyplot as plt

def readdate(datafile,labelfile):
    # data
    data=[]
    with open(datafile) as f:
        while True:
            line=f.readline().replace("\n","").replace("\r","")
            if line is None or len(line)<1:
                break
            else:
                values=line.split(",")
                wine=[]
                for i in range(len(values)):
                    # print(repr(values[i])) # check special
                    wine.append(float(values[i]))
                data.append(wine)

    # label
    label=[]
    with open(labelfile) as f:
        while True:
            line=f.readline().replace("\n","").replace("\r","")
            if line is None or len(line)<1:
                break
            label.append(int(line))

    """
    # classify the data to see the regulation
    for i in range(1,3+1):
        print("class=",i)
        for j in range(len(data)):
            if label[j]==i:
                print(data[j])
    """
    return data,label

def eucliddist(a,b):
    """
    compute the euclidean distance between two wines
    :param a:
    :param b:
    :return:
    """
    d2=0
    w=[1,1,1,1,0.1, 1,1,1,1,1, 1,1,0.01]
    for i in range(len(a)):
        d2+=((a[i]-b[i])*w[i])**2
    return math.sqrt(d2)


def nearest(data,label):
    """
    predict the ith element according to nearest kth(k<i) and its label
    get the number of errors
    :param data:
    :param label:
    :return:
    """
    assert isinstance(data,list) and isinstance(label,list)

    error=0
    distlist=[]
    errlist=[]
    for i in range(1,len(data)):
        # find the nearest
        near=0
        mindist=eucliddist(data[i],data[0])
        for j in range(0,i):
            dist=eucliddist(data[i],data[j])
            if mindist>dist:
                mindist=dist
                near=j
        # check with label
        # print(label[near],label[i])
        distlist.append(mindist)
        if label[near]!=label[i]:
            error +=1
            errlist.append(1) # another
        else:
            errlist.append(0)

    return error,errlist,distlist

def aver_dist(y):
    """
    compute the pre-i average
    :param distlist:
    :return:
    """
    index=[]
    aver=[]
    t=0
    sum=0
    for i in range(len(y)):
        t+=1
        sum+=y[i]
        index.append(i+2)
        aver.append(sum/t)
    return index,aver


def fvalplt(x,y,title="",xstr="",ystr=""):
    plt.title(title)
    plt.xlabel(xstr)
    plt.ylabel(ystr)
    plt.plot(x, y)
    plt.show()


data,label=readdate("bottle-data.txt","bottle-labels.txt")
error,errlist,distlist=nearest(data,label)
print(error)
""""""
near_x,near_y=aver_dist(distlist)
fvalplt(near_x,near_y,title="plot of average nearest distance versus index",xstr="i",ystr="Di")
err_x,err_y=aver_dist(errlist)
fvalplt(err_x,err_y,title="plot of fraction of errors versus index",xstr="i",ystr="Ei")



