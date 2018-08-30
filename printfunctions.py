'''Created on Aug 27, 2018

@author: srees
'''
from pyspark import SparkContext, SparkConf
def firstprint():
    print("first print")
   
if __name__ == '__main__':
    firstprint()
    conf = SparkConf().setAppName("Phrase Search")
    sc = SparkContext(conf=conf)
    sc.parallelize([1,2,3,4,5], 2).collect()
    
    
    
 
