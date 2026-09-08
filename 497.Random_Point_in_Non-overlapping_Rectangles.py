#497. Random Point in Non-overlapping Rectangles
import random
import math
class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects=rects
        self.area=[]
        self.total_area=0
        for i in rects:
            ai,bi,xi,yi=i[0],i[1],i[2],i[3]
            self.area.append((xi-ai+1)*(yi-bi+1))
            self.total_area+=(xi-ai+1)*(yi-bi+1)
        self.area=[i/self.total_area for i in self.area]
        #print(self.rects)
        
    def pick(self) -> List[int]:
        index=random.choices(self.rects,weights=self.area,k=1)[0]
        points=[]
        ai,bi,xi,yi=index[0],index[1],index[2],index[3]
        x=random.randint(ai,xi)
        y=random.randint(bi,yi)
        return [x,y]
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
