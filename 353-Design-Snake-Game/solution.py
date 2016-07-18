class SnakeGame(object):

    def __init__(self, width,height,food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height 
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.width, self.height, self.food = width, height, food
        self.foodCount = 0
        self.body = [0]
        self.directions = {'U': [-1, 0], 'L': [0, -1], 'R': [0, 1], 'D': [1, 0]}

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down 
        @return The game's score after the move. Return -1 if game over. 
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        head = self.body[0]
        tail = self.body.pop()
        x = head / self.width
        y = head % self.width
        newx = x + self.directions[direction][0]
        newy = y + self.directions[direction][1]
        newHead = newx * self.width + newy
        if (newx < 0 or newx >= self.height or newy < 0 or newy >= self.width
            or newHead in self.body):
            return -1
        self.body.insert(0, newHead)
        if (self.foodCount < len(self.food) and newx == self.food[self.foodCount][0] and 
            newy == self.food[self.foodCount][1]):
            self.foodCount += 1
            self.body.append(tail)
        return len(self.body) - 1

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)