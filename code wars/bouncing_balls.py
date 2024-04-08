#question link :https://www.codewars.com/kata/5544c7a5cb454edb3c000047/python
def bouncing_ball(h, bounce, window):
    c=0
    if(bounce>0 and bounce<1 and h>window and h>0):
        if(h>window):
            c+=1
        while(h>window):
            h*=bounce
            if(h>window):
                c+=2
        print(c)
    else:
        print(-1)
bouncing_ball(3,1, 1.5)