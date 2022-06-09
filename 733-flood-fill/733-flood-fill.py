class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        startColor = image[sr][sc]
        
        if startColor != newColor:
            self.fill(image, sr, sc, startColor, newColor)
        
        return image
        
    def fill(self, image: List[List[int]], r:int, c:int, start:int, new: int):
        if image[r][c] == start:
            image[r][c] = new
        
            if r > 0:
                self.fill(image, r - 1, c, start, new)
            if c > 0:
                self.fill(image, r, c - 1, start, new)
            if r < len(image) - 1:
                self.fill(image, r + 1, c, start, new)
            if c < len(image[0]) - 1:
                self.fill(image, r, c + 1, start, new)