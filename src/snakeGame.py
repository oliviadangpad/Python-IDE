# https://leetcode.com/problems/design-snake-game

from collections import deque
from typing import List

class SnakeGame:
    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.rows = height
        self.cols = width
        self.food = food
        self.directions = {
            "R":[0,1], "D":[1,0], "U":[-1,0], "L":[0,-1]
        }
        self.snake = deque([[0,0]])
        self.foodIndex = 0
    
    def move(self, direction: str) -> int:
        dx, dy = self.directions[direction]
        x, y = self.snake[-1]
        newHead = [x+dx, y+dy]
        crossesBoundary = not ( 0 <= newHead[0] <self.rows and 0 <= newHead[1] <self.cols)
        biteItself = newHead in self.snake and newHead != self.snake[0]
        if crossesBoundary or biteItself:
            return -1
        
        self.snake.append(newHead)
        if self.foodIndex < len(self.food) and newHead == self.food[self.foodIndex]:
            self.foodIndex += 1
        else:
            self.snake.popleft()
        
        return len(self.snake)-1

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)