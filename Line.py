import turtle

class LineChart():
    
    def __init__(self,datatag,hierarch,value,x_type,y_type):
        self.tag = datatag
        self.hir = hierarch
        self.val = value
        self.x = x_type
        self.y = y_type
        
    def screen(self,width,height):
        start = width/8
        end = 7*width/8
        length = width-2*width/8
        big_round = (sorted(self.val)[len(self.val)-1]//(10**(len(str(sorted(self.val)[len(self.val)-1]))-1))+1)*(10**(len(str(sorted(self.val)[len(self.val)-1]))-1))
        screen = turtle.Screen() #screen
        chart = turtle.Turtle() #chart
        line = turtle.Turtle() #t[2]
        screen.setup(width,height)
        screen.setworldcoordinates(0,0,width,height)
        screen.title(self.tag)
        chart.hideturtle()
        chart.speed(0)
        chart.pensize(width=5)
        line.speed(1)
        line.pensize(width=3)
        line.color("gold")
        line.penup()
        line.setpos(start,start)
        chart.penup()
        chart.setpos(width/2,height-start/3)
        chart.write(self.tag, move=False, align="center", font=("Segoe UI", int(width/50), "bold italic"))
        chart.setpos(start,length+start+14*start/100)
        chart.write(self.x, move=False, align="center", font=("Segoe UI", int(14*start/100), "bold italic"))
        chart.setpos(length+start+14*start/100,start)
        chart.write(self.y, move=False, align="left", font=("Segoe UI", int(14*start/100), "bold italic"))
        chart.setpos(start-2*start/10,start-2*start/10)
        chart.write(0, move=False, align="right", font=("Segoe UI", int(14*start/100), "bold italic"))
        chart.setpos(start,start)
        chart.pendown()
        chart.setpos(start,end)
        chart.penup()
        chart.setpos(start,start)
        chart.pendown()
        chart.setpos(end,start)
        for i in range(1,7):
            chart.penup()
            chart.setpos(start-start/10,i*length/7+start)
            chart.pendown()
            chart.setpos(start+start/10,i*length/7+start)
            chart.penup()
            chart.setpos(start-2*start/10,i*length/7+start)
            chart.write(int(i*big_round/6), move=False, align="right", font=("Segoe UI", int(12*start/100), "bold italic"))
        for i in range(1,len(self.hir)+1):
            chart.penup()
            chart.setpos(i*length/(len(self.hir)+1)+(len(self.hir)+1)/2+start,start+start/10)
            chart.pendown()
            chart.setpos(i*length/(len(self.hir)+1)+(len(self.hir)+1)/2+start,start-start/10)
            chart.penup()
            chart.setpos(i*length/(len(self.hir)+1)+(len(self.hir)+1)/2+start,start-4*start/10)
            chart.write(self.hir[i-1], move=False, align="center", font=("Segoe UI", int(12*start/100), "bold italic")) 
        for i in range(1,len(self.val)+1):
            line.setpos(i*length/(len(self.hir)+1)+(len(self.hir)+1)/2+start,start+self.val[i-1]/(big_round/6)*(length/7))
            line.dot(start/8)
            line.setpos(i*length/(len(self.hir)+1)+(len(self.hir)+1)/2+start,start+self.val[i-1]/(big_round/6)*(length/7))
            line.pendown()
        line.color("grey")
        line.speed(0)
        for i in range(1,len(self.val)+1):
            line.penup()
            line.setpos(i*length/(len(self.hir)+1)+(len(self.hir)+1)/2+start,start+self.val[i-1]/(big_round/6)*(length/7)+start/10)
            line.write(self.val[i-1], move=False, align="center", font=("Segoe UI", int(12*start/100), "bold italic")) 
        line.hideturtle()
        turtle.mainloop()

dataTitle = "The Numbers of Thailand Cumulative COVID-19 Confirm Case"
x_type = "Cases (People)"
y_type = "Time"
x_axis = ["Q2-2020","Q4-2020","Q2-2021","Q4-2021","Q2-2022"]
y_axis = [43,3787,26031,1920000,2910000]

l = LineChart(dataTitle,x_axis,y_axis,x_type,y_type)
l.screen(600,600)