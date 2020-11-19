import bpy

for i in range(0,21,1):
    obj = bpy.data.curves.new(type="FONT",name= str(i))
    num = str(i)
    myFontOb = bpy.data.objects.new(num, obj)
    myFontOb.data.body = str(i)
    bpy.context.collection.objects.link(myFontOb)
    
for i in range(30, 91, 10):
    pobj = bpy.data.curves.new(type="FONT", name= str(i))
    pnum = str(i)
    myPFontOb = bpy.data.objects.new(pnum, pobj)
    myPFontOb.data.body = str(i)
    bpy.context.collection.objects.link(myPFontOb)

zobj = bpy.data.curves.new(type="FONT",name= "00")
myZFontOb = bpy.data.objects.new("00", zobj)
myZFontOb.data.body = "00"
bpy.context.collection.objects.link(myZFontOb)

line = bpy.data.curves.new(type="FONT", name= "line")
FontLine = bpy.data.objects.new("line", line)
FontLine.data.body = "_" 
bpy.context.collection.objects.link(FontLine)

sixdot = bpy.data.curves.new(type="FONT", name= "6 dot")
mysixdot = bpy.data.objects.new("line", sixdot)
mysixdot.data.body = "6." 
bpy.context.collection.objects.link(mysixdot)

ninedot = bpy.data.curves.new(type="FONT", name= "9 dot")
myninedot = bpy.data.objects.new("line", ninedot)
myninedot.data.body = "9." 
bpy.context.collection.objects.link(myninedot)
    