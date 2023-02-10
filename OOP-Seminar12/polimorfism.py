class Snake():
    def move(self):
        print("Ползет")

class Slug(Snake):
    def move(self):
        print("Скользит")


snake = Snake()
snake.move()
slug = Slug()
slug.move()