class Data:
    
    import csv
    
    def __init__(self,file):
        self.file = file
    
    def conS2N(self,str):
        if float(str) // 1 == 0:
            str = int(str)
        else:
            str = float(str)
        return str
    
    def readFile(self):
        try:
            datalist = []
            x = ""
            y = ""
            hir = []
            val = []
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
            datalist.append(self.file)
            datalist.append(x)
            datalist.append(hir)
            datalist.append(y)
            datalist.append(val)
            print(datalist)
            return datalist
        except:
            return ["","","",[],[]]
                
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
        #กูต้อง readfile ด้วยเหรอ
        
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
        #draw chart line
        line.setpos(start,start)
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
                        
#Using LineChart
#LineChart(File Name).screen(Squared window length,Text size) to visualize datas

#Line("Thailand Cumulative COVID-19 Confirm Case Every 6 Months").display()
#Line("The Attendances over this week").display()
#Line("ปริมาณน้ำฝนสัปดาห์นี้").display()
Line("โสภณเหี่ยโอมิเตอร์").display()
