def setup():
    size(1000,1300)
    global n,m,rg,b,ndiff,mdiff
    n,m = 40,25
    rg = random(128)
    b = random(207,255)
    background(rg+2*n-4,128-rg+32+2*n-4,b)
    strokeWeight(4)

    ndiff = height/n
    mdiff = width/m
    r = [random(0.4,0.6)]
    rg = [rg]
    b = [b]
    for i in range(3,n-2):
        r += [r[0]+0.1*sin(i*3.14159*random(1,2)/(n-5))+random(-0.07,0.07)]
        s = createShape()
        s.beginShape()
        r1 = random(-25,25)
        r2 = random(-25,25)
        if (rg[-1]+r1)>=128:
            rg += [rg[-1]+random(-25,-4)]
        elif (rg[-1]+r1)<0:
            rg += [rg[-1]+random(4,25)]
        else:
            rg += [rg[-1]+r1]
        if (b[-1]+r2)>=255:
            b += [b[-1]+random(-25,-4)]
        elif (b[-1]+r2)<207:
            b += [b[-1]+random(4,25)]
        else:
            b += [b[-1]+r2]
        s.fill(rg[-1]+2*(n-i),128-rg[-1]+32+2*(n-i),b[-1])
        s.stroke(255)
        for j in range(m+1):
            f = abs(float(m*r[-1])-float(j))**(-1)
            ff = min(f,random(1,2))
            y = i*ndiff+ndiff/2-2*ff*random(ndiff)
            s.vertex(j*mdiff,y)
    
        #s.noStroke()
        s.vertex(width,height)
        s.vertex(0,height) #bottom corners
        s.endShape(CLOSE)
        shape(s,0,0)
    
    global rs
    rs = [2.0]
    
def draw():
    global rs
    background(rg[0]+2*n-4,128-rg[0]+32+2*n-4,b[0])
    r = [0.5]
    for i in range(3,n-2):
        r += [r[0]+0.1*sin(i*3.14159*2/(n-5)+3.14159*rs[-1])+random(-0.07,0.07)]
        s = createShape()
        s.beginShape()
        s.fill(rg[i-2]+2*(n-i),128-rg[i-2]+32+2*(n-i),b[i-2])
        s.stroke(255)
        for j in range(m+1):
            f = abs(float(m*r[-1])-float(j))**(-1)
            ff = min(f,random(1,2))
            y = i*ndiff+ndiff/2-2*ff*random(ndiff)
            s.vertex(j*mdiff,y) 
        s.vertex(width,height)
        s.vertex(0,height) #bottom corners
        s.endShape(CLOSE)
        shape(s,0,0) 
    rs += [rs[-1]-0.1]
    saveFrame("mountains-##.png")
#print(rg,b)
#save("mountains3.jpg")
