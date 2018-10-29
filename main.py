import tkinter, random


class Ball():
    def __init__(self, canvas):

        self.canvas = canvas
        # 球的半径
        self.radius = random.randint(20, 100)
        # 球的颜色
        self.color = '#%02x%02x%02x'% (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        # 球的初始位置
        self.xpos = random.randint(200, 1300)
        self.ypos = random.randint(50, 700)
        # 球移动的速度
        self.xvelocity = random.randint(2, 10)
        self.yvelocity = random.randint(2, 10)

    def create_ball(self):

        x1 = self.xpos - self.radius
        y1 = self.ypos - self.radius
        x2 = self.xpos + self.radius
        y2 = self.ypos + self.radius
        self.items = self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)

    def run_ball(self):

        # tkinter的Cancas有一个move函数
        self.canvas.move(self.items, self.xvelocity, self.yvelocity)

        # 移动后的位置
        self.xpos += self.xvelocity
        self.ypos += self.yvelocity
        # 撞墙
        if self.xpos - self.radius <= 0 or self.xpos + self.radius >= 1366:
            self.xvelocity = - self.xvelocity

        if self.ypos - self.radius <= 0 or self.ypos + self.radius >= 768:
            self.yvelocity = - self.yvelocity

        # self.canvas.after(200, self.run_ball())

        # ok


class Screen():
    """
    屏保
    属性：
    方法：

    """
    def __init__(self):
        self.root = tkinter.Tk()
        #取消边框
        self.root.overrideredirect(1)
        self.cvs = tkinter.Canvas(self.root, width=1366, height=768)
        self.cvs.pack()
        self.balls = []

        self.ball_num = random.randint(5, 20)
        for i in range(self.ball_num):
            self.ball = Ball(self.cvs)
            self.ball.create_ball()
            self.balls.append(self.ball)
        # 给一个事件绑定一个方法
        self.root.bind(sequence='<Motion>', func=self.myquit)
        # self.root.bind(sequence='<Key>', func=self.myquit)

        self.run_screen_saver()
        self.root.mainloop()

    def run_screen_saver(self):
        for ball in self.balls:
            ball.run_ball()
        # 200毫秒后再次调用run_screen_saver
        self.cvs.after(200, self.run_screen_saver)

    def myquit(self, e):
        self.root.destroy()

if __name__=='__main__':
    my_screen_saver = Screen()


        # self.ball_list = []
        # self.ball_list.append(self.ball.create_ball())


