from tkinter import *

tk = Tk()
width = 500
height = 400
canvas = Canvas(tk, width=width, height=height)
canvas.pack()

class Game:
    def __init__(self):
        self.canvas = canvas
        self.paddleId = canvas.create_rectangle(0, 0, 100,10, fill='blue')
        self.canvas.move(self.paddleId, 250, 390)
        self.paddleX = 0
        self.canvas.bind_all('<KeyPress-Left>', self.left)
        self.canvas.bind_all('<KeyPress-Right>', self.right)

        self.ballId = canvas.create_oval(10, 10, 25, 25, fill='red')
        self.canvas.move(self.ballId, 300, 100)
        self.masterspeed = 4
        self.ballX = self.masterspeed
        self.ballY = -1 * self.masterspeed

        self.tk = tk
        self.animate()

        tk.mainloop()




    def drawPaddle(self):
        self.canvas.move(self.paddleId, self.paddleX, 0)
        pos = self.canvas.coords(self.paddleId)
        if pos[0] <= 0:
            self.paddleX = 0
        elif pos[2] >= 500:
            self.paddleX = 0



    def left(self, evt):
        self.paddleX = -3

    def right(self, evt):
        self.paddleX = 3

    def drawBall(self):
        self.canvas.move(self.ballId, self.ballX, self.ballY)
        ballPos = self.canvas.coords(self.ballId)
        paddlePos = self.canvas.coords(self.paddleId)
        if ballPos[1] <= 0:
            self.ballY = self.masterspeed
        if ballPos[3] >= height:
            tk.destroy()
        if ballPos[0] <= 0:
            self.ballX = self.masterspeed
        if ballPos[2] >= width:
            self.ballX = -1 * self.masterspeed
        if ballPos[3] >= 390 and ballPos[0] >= paddlePos[0] and ballPos[2] <= paddlePos[2]:
            self.ballY = -1 * self.masterspeed


    def animate(self):
        self.drawPaddle()
        self.drawBall()
        self.tk.after(20, self.animate)



Game()

tk = Tk()
width = 500
height = 400
canvas = Canvas(tk, width=width, height=height)
canvas.pack()

class Game:
    def __init__(self):
        self.canvas = canvas
        self.paddleId = canvas.create_rectangle(0, 0, 100,10, fill='blue')
        self.canvas.move(self.paddleId, 250, 390)
        self.paddleX = 0
        self.canvas.bind_all('<KeyPress-Left>', self.left)
        self.canvas.bind_all('<KeyPress-Right>', self.right)

        self.ballId = canvas.create_oval(10, 10, 25, 25, fill='red')
        self.canvas.move(self.ballId, 300, 100)
        self.masterspeed = 4
        self.ballX = self.masterspeed
        self.ballY = -1 * self.masterspeed

        self.tk = tk
        self.animate()

        tk.mainloop()




    def drawPaddle(self):
        self.canvas.move(self.paddleId, self.paddleX, 0)
        pos = self.canvas.coords(self.paddleId)
        if pos[0] <= 0:
            self.paddleX = 0
        elif pos[2] >= 500:
            self.paddleX = 0



    def left(self, evt):
        self.paddleX = -3

    def right(self, evt):
        self.paddleX = 3

    def drawBall(self):
        self.canvas.move(self.ballId, self.ballX, self.ballY)
        ballPos = self.canvas.coords(self.ballId)
        paddlePos = self.canvas.coords(self.paddleId)
        if ballPos[1] <= 0:
            self.ballY = self.masterspeed
        if ballPos[3] >= height:
            tk.destroy()
        if ballPos[0] <= 0:
            self.ballX = self.masterspeed
        if ballPos[2] >= width:
            self.ballX = -1 * self.masterspeed
        if ballPos[3] >= 390 and ballPos[0] >= paddlePos[0] and ballPos[2] <= paddlePos[2]:
            self.ballY = -1 * self.masterspeed


    def animate(self):
        self.drawPaddle()
        self.drawBall()
        self.tk.after(20, self.animate)



Game()

tk = Tk()
width = 500
height = 400
canvas = Canvas(tk, width=width, height=height)
canvas.pack()

class Game:
    def __init__(self):
        self.canvas = canvas
        self.paddleId = canvas.create_rectangle(0, 0, 100,10, fill='blue')
        self.canvas.move(self.paddleId, 250, 390)
        self.paddleX = 0
        self.canvas.bind_all('<KeyPress-Left>', self.left)
        self.canvas.bind_all('<KeyPress-Right>', self.right)

        self.ballId = canvas.create_oval(10, 10, 25, 25, fill='red')
        self.canvas.move(self.ballId, 300, 100)
        self.masterspeed = 4.5
        self.ballX = self.masterspeed
        self.ballY = -1 * self.masterspeed

        self.tk = tk
        self.animate()

        tk.mainloop()




    def drawPaddle(self):
        self.canvas.move(self.paddleId, self.paddleX, 0)
        pos = self.canvas.coords(self.paddleId)
        if pos[0] <= 0:
            self.paddleX = 0
        elif pos[2] >= 500:
            self.paddleX = 0



    def left(self, evt):
        self.paddleX = -3

    def right(self, evt):
        self.paddleX = 3

    def drawBall(self):
        self.canvas.move(self.ballId, self.ballX, self.ballY)
        ballPos = self.canvas.coords(self.ballId)
        paddlePos = self.canvas.coords(self.paddleId)
        if ballPos[1] <= 0:
            self.ballY = self.masterspeed
        if ballPos[3] >= height:
            tk.destroy()
        if ballPos[0] <= 0:
            self.ballX = self.masterspeed
        if ballPos[2] >= width:
            self.ballX = -1 * self.masterspeed
        if ballPos[3] >= 390 and ballPos[0] >= paddlePos[0] and ballPos[2] <= paddlePos[2]:
            self.ballY = -1 * self.masterspeed


    def animate(self):
        self.drawPaddle()
        self.drawBall()
        self.tk.after(20, self.animate)



Game()

tk = Tk()
width = 500
height = 400
canvas = Canvas(tk, width=width, height=height)
canvas.pack()

class Game:
    def __init__(self):
        self.canvas = canvas
        self.paddleId = canvas.create_rectangle(0, 0, 100,10, fill='blue')
        self.canvas.move(self.paddleId, 250, 390)
        self.paddleX = 0
        self.canvas.bind_all('<KeyPress-Left>', self.left)
        self.canvas.bind_all('<KeyPress-Right>', self.right)

        self.ballId = canvas.create_oval(10, 10, 25, 25, fill='red')
        self.canvas.move(self.ballId, 300, 100)
        self.masterspeed = 5
        self.ballX = self.masterspeed
        self.ballY = -1 * self.masterspeed

        self.tk = tk
        self.animate()

        tk.mainloop()




    def drawPaddle(self):
        self.canvas.move(self.paddleId, self.paddleX, 0)
        pos = self.canvas.coords(self.paddleId)
        if pos[0] <= 0:
            self.paddleX = 0
        elif pos[2] >= 500:
            self.paddleX = 0



    def left(self, evt):
        self.paddleX = -3

    def right(self, evt):
        self.paddleX = 3

    def drawBall(self):
        self.canvas.move(self.ballId, self.ballX, self.ballY)
        ballPos = self.canvas.coords(self.ballId)
        paddlePos = self.canvas.coords(self.paddleId)
        if ballPos[1] <= 0:
            self.ballY = self.masterspeed
        if ballPos[3] >= height:
            tk.destroy()
        if ballPos[0] <= 0:
            self.ballX = self.masterspeed
        if ballPos[2] >= width:
            self.ballX = -1 * self.masterspeed
        if ballPos[3] >= 390 and ballPos[0] >= paddlePos[0] and ballPos[2] <= paddlePos[2]:
            self.ballY = -1 * self.masterspeed


    def animate(self):
        self.drawPaddle()
        self.drawBall()
        self.tk.after(20, self.animate)



Game()

tk = Tk()
width = 500
height = 400
canvas = Canvas(tk, width=width, height=height)
canvas.pack()

class Game:
    def __init__(self):
        self.canvas = canvas
        self.paddleId = canvas.create_rectangle(0, 0, 100,10, fill='blue')
        self.canvas.move(self.paddleId, 250, 390)
        self.paddleX = 0
        self.canvas.bind_all('<KeyPress-Left>', self.left)
        self.canvas.bind_all('<KeyPress-Right>', self.right)

        self.ballId = canvas.create_oval(10, 10, 25, 25, fill='red')
        self.canvas.move(self.ballId, 300, 100)
        self.masterspeed = 4.5
        self.ballX = self.masterspeed
        self.ballY = -1 * self.masterspeed

        self.tk = tk
        self.animate()

        tk.mainloop()




    def drawPaddle(self):
        self.canvas.move(self.paddleId, self.paddleX, 0)
        pos = self.canvas.coords(self.paddleId)
        if pos[0] <= 0:
            self.paddleX = 0
        elif pos[2] >= 500:
            self.paddleX = 0



    def left(self, evt):
        self.paddleX = -3

    def right(self, evt):
        self.paddleX = 3

    def drawBall(self):
        self.canvas.move(self.ballId, self.ballX, self.ballY)
        ballPos = self.canvas.coords(self.ballId)
        paddlePos = self.canvas.coords(self.paddleId)
        if ballPos[1] <= 0:
            self.ballY = self.masterspeed
        if ballPos[3] >= height:
            tk.destroy()
        if ballPos[0] <= 0:
            self.ballX = self.masterspeed
        if ballPos[2] >= width:
            self.ballX = -1 * self.masterspeed
        if ballPos[3] >= 390 and ballPos[0] >= paddlePos[0] and ballPos[2] <= paddlePos[2]:
            self.ballY = -1 * self.masterspeed


    def animate(self):
        self.drawPaddle()
        self.drawBall()
        self.tk.after(20, self.animate)



Game()

tk = Tk()
width = 500
height = 400
canvas = Canvas(tk, width=width, height=height)
canvas.pack()

class Game:
    def __init__(self):
        self.canvas = canvas
        self.paddleId = canvas.create_rectangle(0, 0, 100,10, fill='blue')
        self.canvas.move(self.paddleId, 250, 390)
        self.paddleX = 0
        self.canvas.bind_all('<KeyPress-Left>', self.left)
        self.canvas.bind_all('<KeyPress-Right>', self.right)

        self.ballId = canvas.create_oval(10, 10, 25, 25, fill='red')
        self.canvas.move(self.ballId, 300, 100)
        self.masterspeed = 5
        self.ballX = self.masterspeed
        self.ballY = -1 * self.masterspeed

        self.tk = tk
        self.animate()

        tk.mainloop()




    def drawPaddle(self):
        self.canvas.move(self.paddleId, self.paddleX, 0)
        pos = self.canvas.coords(self.paddleId)
        if pos[0] <= 0:
            self.paddleX = 0
        elif pos[2] >= 500:
            self.paddleX = 0



    def left(self, evt):
        self.paddleX = -3

    def right(self, evt):
        self.paddleX = 3

    def drawBall(self):
        self.canvas.move(self.ballId, self.ballX, self.ballY)
        ballPos = self.canvas.coords(self.ballId)
        paddlePos = self.canvas.coords(self.paddleId)
        if ballPos[1] <= 0:
            self.ballY = self.masterspeed
        if ballPos[3] >= height:
            tk.destroy()
        if ballPos[0] <= 0:
            self.ballX = self.masterspeed
        if ballPos[2] >= width:
            self.ballX = -1 * self.masterspeed
        if ballPos[3] >= 390 and ballPos[0] >= paddlePos[0] and ballPos[2] <= paddlePos[2]:
            self.ballY = -1 * self.masterspeed


    def animate(self):
        self.drawPaddle()
        self.drawBall()
        self.tk.after(20, self.animate)



Game()
