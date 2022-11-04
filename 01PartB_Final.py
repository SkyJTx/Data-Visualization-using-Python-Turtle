class Data:
    
    import csv
    
    def __init__(self,file):
        self.file = file
    
    #convert str to float or int
    def conS2N(self,str):
        if float(str) % 1 == 0:
            return int(str)
        return float(str)
    
    #read csv file and append into a single list
    def readFile(self):
        try:
            datalist = []
            x = ""
            y = ""
            hir = []
            val = []
            color = []
            csv_file = open(self.file+".csv",mode="r")
            csv_reader = self.csv.reader(csv_file,delimiter = ',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    x = row[0]
                    y = row[1]
                    line_count = line_count + 1
                else:
                    hir.append(row[0])
                    val.append(self.conS2N(row[1]))
                    try:
                        color.append(row[len(row)-1])
                    except:
                        color.append("gold")
            datalist.append(self.file)
            datalist.append(x)
            datalist.append(hir)
            datalist.append(y)
            datalist.append(val)
            datalist.append(color)
            print(datalist)
            return datalist
        except:
            return ["","",[],"",[],[]]
                
class Line(Data):
    
    import turtle

    def __init__(self,file):
        Data.__init__(self,file)
        self.data = Data(file).readFile()
        self.tag = self.data[0] #Title
        self.x = self.data[1] #X_axis type
        self.y = self.data[3] #Y_axis type
        self.hir = self.data[2] #X_axis value
        self.val = self.data[4] #Y_axis value
        
        
    def screen(self,width,textSize):
        height = width
        #calculation
        start = width/8 #find chart start line
        end = 7*width/8 #find chart line end coordinate
        length = width-2*width/8 # find length of a chart line
        big_round = big_round = ((int(sorted(self.val)[len(self.val)-1]))//(10**(len(str(int(sorted(self.val)[len(self.val)-1])))-1))+1)*(10**(len(str(int(sorted(self.val)[len(self.val)-1])))-1)) #find rounded biggest data value element
        screen = self.turtle.Screen() #screen
        chart = self.turtle.Turtle() #chart
        line = self.turtle.Turtle() #graph
        screen.setup(width,height) #create screen
        screen.setworldcoordinates(0,0,width,height) #set (0,0) as bottom left corner and (width,height) as top right corner of the screen
        screen.title(self.tag) #create window title
        #config chart turtle
        chart.hideturtle()
        chart.speed(0)
        chart.pensize(width=5)
        #config graph turtle
        line.speed(1)
        line.pensize(width=3)
        line.color("gold")
        line.penup()
        line.setpos(start,start)
        line.speed(5)
        #draw chart line
        chart.penup()
        #write Title
        chart.setpos(width/2,height-start/3)
        chart.write(self.tag, move=False, align="center", font=("Segoe UI", int(4*textSize/3), "bold italic"))
        #write y axis
        chart.setpos(start,length+start+14*start/100)
        chart.write(self.y, move=False, align="center", font=("Segoe UI", int(105*textSize/90), "bold italic"))
        #write x axis
        chart.setpos(length+start+14*start/100,start+2*start/10)
        chart.write(self.x, move=False, align="center", font=("Segoe UI", int(105*textSize/90), "bold italic"))
        #write 0 as start
        chart.setpos(start-2*start/10,start-2*start/10)
        chart.write(0, move=False, align="right", font=("Segoe UI", int(105*textSize/90), "bold italic"))
        #draw chart line
        chart.setpos(start,start)
        chart.pendown()
        chart.setpos(start,end)
        chart.penup()
        chart.setpos(start,start)
        chart.pendown()
        chart.setpos(end,start)
        #draw y axis little line and write y axis value
        for i in range(1,7):
            chart.penup()
            chart.setpos(start-start/10,i*length/7+start)
            chart.pendown()
            chart.setpos(start+start/10,i*length/7+start)
            chart.penup()
            chart.setpos(start-2*start/10,i*length/7+start)
            chart.write("{:.2f}".format(i*big_round/6), move=False, align="right", font=("Segoe UI", int(textSize), "bold italic"))
        #draw x axis little line and write x axis data hierarch
        for i in range(1,len(self.hir)+1):
            chart.penup()
            chart.setpos(i*length/(len(self.hir)+1)+start,start+start/10)
            chart.pendown()
            chart.setpos(i*length/(len(self.hir)+1)+start,start-start/10)
            chart.penup()
            chart.setpos(i*length/(len(self.hir)+1)+start,start-4*start/10)
            chart.write(self.hir[i-1], move=False, align="center", font=("Segoe UI", int(textSize), "bold italic")) 
        #draw graph line
        for i in range(1,len(self.val)+1):
            line.setpos(i*length/(len(self.hir)+1)+start,start+self.val[i-1]/(big_round/6)*(length/7))
            line.dot(textSize*1.5)
            line.setpos(i*length/(len(self.hir)+1)+start,start+self.val[i-1]/(big_round/6)*(length/7))
            line.pendown()
        #config graph turtle again
        line.color("grey")
        line.speed(0)
        #write data value
        for i in range(1,len(self.val)+1):
            line.penup()
            line.setpos(i*length/(len(self.hir)+1)+start,start+self.val[i-1]/(big_round/6)*(length/7)+start/10)
            line.write(self.val[i-1], move=False, align="center", font=("Segoe UI", int(textSize), "bold italic")) 
        line.hideturtle()
        #make it always appear until user close the window
        self.turtle.mainloop()
       
    #check if the data or screen config is appropriate
    def display(self,width="",textSize=""):
        try:
            self.screen(width,textSize)
        except:
            #if an error occured
            try:
                self.screen(800,12)
                #if there is still an error occured
            except:
                if type(self.hir) is not list or type(self.val) is not list: #if x or y value is not list
                    print("DataInputError: Please check your data and try again.")
                else:
                    if self.tag == "" or self.x == "" or self.y == "" or self.hir == [] or self.val == []: #if no data were given 
                        print("DataInputError: Please check your data and try again.")
                    else: #otherwise
                        print("InterruptionWarning: Program is stopped working.")
                        
class Bar(Data):
    
    import turtle
    
    def __init__(self,file):
        Data.__init__(self,file)
        self.data = Data(file).readFile()
        self.tag = self.data[0] #Title
        self.x = self.data[1] #X_axis type
        self.y = self.data[3] #Y_axis type
        self.hir = self.data[2] #X_axis value
        self.val = self.data[4] #Y_axis value
        self.color = self.data[5] #Color
        
    def screen(self,width,textSize):
        height = width
        #calculation
        start = width/8 #find chart start line
        end = 7*width/8 #find chart line end coordinate
        length = width-2*width/8 # find length of a chart line
        big_round = big_round = ((int(sorted(self.val)[len(self.val)-1]))//(10**(len(str(int(sorted(self.val)[len(self.val)-1])))-1))+1)*(10**(len(str(int(sorted(self.val)[len(self.val)-1])))-1)) #find rounded biggest data value element
        screen = self.turtle.Screen() #screen
        chart = self.turtle.Turtle() #chart
        bar = self.turtle.Turtle() #graph
        screen.setup(width,height) #create screen
        screen.setworldcoordinates(0,0,width,height) #set (0,0) as bottom left corner and (width,height) as top right corner of the screen
        screen.title(self.tag) #create window title
        #config chart turtle
        chart.hideturtle()
        chart.speed(0)
        chart.pensize(width=5)
        #config graph turtle
        bar.speed(1)
        bar.pensize(width=3)
        bar.color("black")
        bar.penup()
        bar.setpos(start,start)
        bar.speed(10)
        #draw chart line
        chart.penup()
        #write Title
        chart.setpos(width/2,height-start/3)
        chart.write(self.tag, move=False, align="center", font=("Segoe UI", int(4*width/192), "bold italic"))
        #write y axis
        chart.setpos(start,length+start+14*start/100)
        chart.write(self.y, move=False, align="center", font=("Segoe UI", int(105*textSize/90), "bold italic"))
        #write x axis
        chart.setpos(length+start+14*start/100,start+2*start/10)
        chart.write(self.x, move=False, align="center", font=("Segoe UI", int(105*textSize/90), "bold italic"))
        #write 0 as start
        chart.setpos(start-2*start/10,start-2*start/10)
        chart.write(0, move=False, align="right", font=("Segoe UI", int(105*textSize/90), "bold italic"))
        #draw chart line
        chart.setpos(start,start)
        chart.pendown()
        chart.setpos(start,end)
        chart.penup()
        chart.setpos(start,start)
        chart.pendown()
        chart.setpos(end,start)
        #draw y axis little line and write y axis value
        for i in range(1,7):
            chart.penup()
            chart.setpos(start-start/10,i*length/7+start)
            chart.pendown()
            chart.setpos(start+start/10,i*length/7+start)
            chart.penup()
            chart.setpos(start-2*start/10,i*length/7+start)
            chart.write("{:.2f}".format(i*big_round/6), move=False, align="right", font=("Segoe UI", int(textSize), "bold italic"))
        #draw x axis little line and write x axis data hierarch
        for i in range(1,len(self.hir)+1):
            chart.penup()
            chart.setpos(i*length/(len(self.hir)+1)+start,start+start/10)
            chart.pendown()
            chart.setpos(i*length/(len(self.hir)+1)+start,start-start/10)
            chart.penup()
            chart.setpos(i*length/(len(self.hir)+1)+start,start-4*start/10)
            chart.write(self.hir[i-1], move=False, align="center", font=("Segoe UI", int(textSize), "bold italic")) 
        #draw graph bar
        for i in range(1,len(self.val)+1):
            bar.penup()
            bar.fillcolor(self.color[i-1])
            bar.begin_fill()
            bar.setpos((2*i-1)/2*length/(len(self.hir)+1)+start,start)
            bar.pendown()
            bar.setpos(((2*i-1)/2*length/(len(self.hir)+1)+start,start+self.val[i-1]/(big_round/6)*(length/7)))
            bar.setpos((2*i+1)/2*length/(len(self.hir)+1)+start,start+self.val[i-1]/(big_round/6)*(length/7))
            bar.setpos((2*i+1)/2*length/(len(self.hir)+1)+start,start)
            bar.end_fill()
        #config graph turtle again
        bar.color("grey")
        bar.speed(0)
        #write data value
        for i in range(1,len(self.val)+1):
            bar.penup()
            bar.setpos(i*length/(len(self.hir)+1)+start,start+self.val[i-1]/(big_round/6)*(length/7)+start/10)
            bar.write(self.val[i-1], move=False, align="center", font=("Segoe UI", int(textSize), "bold italic")) 
        bar.hideturtle()
        #make it always appear until user close the window
        self.turtle.mainloop()
    
    #check if the data or screen config is appropriate
    def display(self,width="",textSize=""):
        try:
            self.screen(width,textSize)
        except:
            #if an error occured
            try:
                self.screen(800,12)
                #if there is still an error occured
            except:
                if type(self.hir) is not list or type(self.val) is not list: #if x or y value is not list
                    print("DataInputError: Please check your data and try again.")
                else:
                    if self.tag == "" or self.x == "" or self.y == "" or self.hir == [] or self.val == []: #if no data were given 
                        print("DataInputError: Please check your data and try again.")
                    else: #otherwise
                        print("InterruptionWarning: Program is stopped working.")

#Work in Progress        
class Pie(Data):
    
    import turtle
    
    def __init__(self,file):
        Data.__init__(self,file)
        self.data = Data(file).readFile()
        self.tag = self.data[0] #Title
        self.x = self.data[1] #X_axis type
        self.y = self.data[3] #Y_axis type
        self.hir = self.data[2] #X_axis value
        self.val = self.data[4] #Y_axis value
        self.color = self.data[5] #Color
        
    def screen(self,width,textSize):
        height = width
        #calculation
        Sum = sum(self.val)
        radius = width/4
        #setup
        screen = self.turtle.Screen() #screen
        pie = self.turtle.Turtle()
        screen.setup(width,height) #create screen
        screen.setworldcoordinates(-width/2,-height/2,width/2,height/2) #set (-width/2,-height/2) as bottom left corner and (width/2,height/2) as top right corner of the screen
        screen.title(self.tag) #create window title
        #config pie turtle
        pie.speed(10)
        pie.color("gray")
        pie.penup()
        #write Title
        pie.setpos(0,height/2.25)
        pie.write(self.tag, move=False, align="center", font=("Segoe UI", int(4*width/192), "bold italic"))
        pie.setpos(0,0)
        #draw circle
        pie.sety(-radius)
        for i in range(len(self.val)):
            pie.fillcolor(self.color[i])
            pie.begin_fill()
            pie.pendown()
            pie.circle(radius, self.val[i]  * 360 / Sum)
            position = pie.position()
            pie.setpos(0,0)
            pie.end_fill()
            pie.penup()
            pie.sety(-radius)
            pie.setposition(position)
        pie.setpos(0,0)
        pie.penup()
        pie.speed(0)
        pie.sety(-radius*1.3)
        for i in range(len(self.hir)):
            pie.circle(radius*1.3, (self.val[i] * 360 / Sum)/2)
            pie.write(self.hir[i]+" , "+str(self.val[i]),font = ("Segoe UI", textSize, "bold italic"),align="center")
            pie.circle(radius*1.3, (self.val[i] * 360 / Sum)/2)
        pie.hideturtle()

        self.turtle.mainloop()
        
    #check if the data or screen config is appropriate
    def display(self,width="",textSize=""):
        try:
            self.screen(width,textSize)
        except:
            try:
                self.screen(800,12)
            except:
                if type(self.hir) is not list or type(self.val) is not list:
                    print("DataInputError: Please check your data and try again.")
                else:
                    if self.tag == "" or self.x == "" or self.y == "" or self.hir == [] or self.val == []:
                        print("DataInputError: Please check your data and try again.")
                    else:
                        print("InterruptionWarning: Program is stopped working.")
                        
#.csv format
""" 
123.csv ** color is optional
------------------------
x,y,color
x_value1,y_value1,color1
x_value2,y_value2,color2
x_value3,y_value3,color3
.
.
.
------------------------
print(Data("123").readFile())
------------------------
Output:
[
    "123", #Title/Topic
    "x", #X Axis
    [x_value1,x_value2,x_value3,...], #X Data/Value
    "y", #Y Axis
    [y_value1,y_value2,y_value3,...], #Y Data/Value
    [color1,color2,color3,...]
]
""" 

#Using LineChart
#Line(File Name as string).display(Squared window length,Text size) to visualize datas

#Example
#Line("Thailand Cumulative COVID-19 Confirm Case Every 6 Months").display()
#Line("The Attendances over this week").display()
#Line("ปริมาณน้ำฝนสัปดาห์นี้").display()

#Using BarChart
#Bar(File Name as string).display(Squared window length,Text size) to visualize datas

#Example
#Bar("Thailand Cumulative COVID-19 Confirm Case Every 6 Months").display()
#Bar("The Attendances over this week").display()
#Bar("ปริมาณน้ำฝนสัปดาห์นี้").display()

#Using PieChart
#Pie(File Name as string).display(Squared window length,Text size) to visualize datas

#Example
#Pie("Thailand Cumulative COVID-19 Confirm Case Every 6 Months").display()
#Pie("The Attendances over this week").display(1000,12)
#Pie("ปริมาณน้ำฝนสัปดาห์นี้").display()