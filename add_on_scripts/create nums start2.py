bl_info = {
    "name": "Create Number Curves",
    "category": "Add",
    "author": "Andrea Springer",
    "version": (1, 0),
    "blender": (2, 90, 0),
}

import bpy


class OBJECT_OT_create_num_curves(bpy.types.Operator):
    """Number Curve Generation Script"""     
    bl_idname = "object.create_num_curves"        
    bl_label = "Create Number Curves"         
    bl_options = {'REGISTER', 'UNDO'}  

    def execute(self, context):

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
        
        return {'FINISHED'}

def menu_draw(self, context):
    self.layout.operator("object.create_num_curves")


def register():
    bpy.utils.register_class(OBJECT_OT_create_num_curves)
    bpy.types.VIEW3D_MT_add.prepend(menu_draw)


def unregister():
    bpy.utils.unregister_class(OBJECT_OT_create_num_curves)
    bpy.types.VIEW3D_MT_add.remove(menu_draw)

if __name__ == "__main__":
    register()



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
    
