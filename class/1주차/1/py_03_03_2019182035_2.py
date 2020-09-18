import turtle

c=0
while(c<=5):
    turtle.penup()
    turtle.goto(c*100,0)
    turtle.pendown()
    turtle.goto(c*100,500)
    c+=1

c=0
while(c<=5):
    turtle.penup()
    turtle.goto(0,c*100)
    turtle.pendown()
    turtle.goto(500,c*100)
    c+=1
    
turtle.exitonclick()
