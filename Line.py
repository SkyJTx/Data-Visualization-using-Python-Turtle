class LineChart():
    
    import turtle
    
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
        screen = self.turtle.Screen() #screen
        chart = self.turtle.Turtle() #chart
        line = self.turtle.Turtle() #t[2]
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
        chart.setpos(length+start+14*start/100,start+2*start/10)
        chart.write(self.y, move=False, align="center", font=("Segoe UI", int(14*start/100), "bold italic"))
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
        self.turtle.mainloop()

dataTitle1 = "Thailand Cumulative COVID-19 Confirm Case Every 6 Months" 
x_type1 = "Cases (People)"
y_type1 = "Time"
x_axis1 = ["Q2-2020","Q4-2020","Q2-2021","Q4-2021","Q2-2022"] # At least it has to be an array with the same length as y_axis
y_axis1 = [43,3787,26031,1920000,2910000] # Has to be only an array(List,Tuple) of numbers

dataTitle2 = "The Attendances over this week"
x_type2 = "Attendance (People)"
y_type2 = "Day"
x_axis2 = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
y_axis2 = [40,20,21,35,42]

dataTitle3 = "ปริมาณน้ำฝนสัปดาห์นี้"
x_type3 = "ปริมาณน้ำฝน (mm)"
y_type3 = "วัน"
x_axis3 = ["อาทิตย์","จันทร์","อังคาร","พุธ","พฤหัสฯ","ศุกร์","เสาร์"]
y_axis3 = [10,0,20,30,0,0,0]

#l = LineChart(dataTitle1,x_axis1,y_axis1,x_type1,y_type1)
#l.screen(600,600)
#m = LineChart(dataTitle2,x_axis2,y_axis2,x_type2,y_type2)
#m.screen(600,600)
n = LineChart(dataTitle3,x_axis3,y_axis3,x_type3,y_type3)
n.screen(600,600)