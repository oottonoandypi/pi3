def searchTarget(self, matrix: List[List[int]], target: int) -> bool:
        x=0
        y=len(matrix[x])-1
        
        while x<len(matrix) and y>=0:
            if target==matrix[x][y]:
                return True
            elif target<matrix[x][y]:
                y-=1
            else:
                x+=1
        
        return False):
