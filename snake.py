import tkinter as tk
import random

WIDTH = 500
HEIGHT = 500
CELL_SIZE = 20
DELAY = 120

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")

        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        self.direction = "Right"
        self.running = True
        self.score = 0

        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.food = self.spawn_food()

        self.root.bind("<KeyPress>", self.change_direction)
        self.update_game()

    def spawn_food(self):
        x = random.randrange(0, WIDTH, CELL_SIZE)
        y = random.randrange(0, HEIGHT, CELL_SIZE)
        return (x, y)

    def change_direction(self, event):
        key = event.keysym
        if key == "Up" and self.direction != "Down":
            self.direction = "Up"
        elif key == "Down" and self.direction != "Up":
            self.direction = "Down"
        elif key == "Left" and self.direction != "Right":
            self.direction = "Left"
        elif key == "Right" and self.direction != "Left":
            self.direction = "Right"

    def move_snake(self):
        head_x, head_y = self.snake[0]

        if self.direction == "Up":
            new_head = (head_x, head_y - CELL_SIZE)
        elif self.direction == "Down":
            new_head = (head_x, head_y + CELL_SIZE)
        elif self.direction == "Left":
            new_head = (head_x - CELL_SIZE, head_y)
        else:
            new_head = (head_x + CELL_SIZE, head_y)

        if (
            new_head[0] < 0 or new_head[0] >= WIDTH or
            new_head[1] < 0 or new_head[1] >= HEIGHT or
            new_head in self.snake
        ):
            self.game_over()
            return

        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.score += 1
            self.food = self.spawn_food()
        else:
            self.snake.pop()

    def draw(self):
        self.canvas.delete("all")

        for x, y in self.snake:
            self.canvas.create_rectangle(
                x, y, x + CELL_SIZE, y + CELL_SIZE,
                fill="green"
            )

        fx, fy = self.food
        self.canvas.create_rectangle(
            fx, fy, fx + CELL_SIZE, fy + CELL_SIZE,
            fill="red"
        )

        self.canvas.create_text(
            50, 10, fill="white",
            text=f"Score: {self.score}",
            anchor="nw"
        )

    def update_game(self):
        if self.running:
            self.move_snake()
            self.draw()
            self.root.after(DELAY, self.update_game)

    def game_over(self):
        self.running = False
        self.canvas.create_text(
            WIDTH // 2, HEIGHT // 2,
            fill="white",
            font=("Arial", 24),
            text=f"Game Over\nScore: {self.score}"
        )

def main():
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
