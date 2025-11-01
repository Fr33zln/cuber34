c = "c" #Kill nniiiiiiiiiggers
forward = "w"
backward = "s"
left = "a"
right = "d"
rotate_left = "arrow_left"
rotate_right = "arrow_right"
up = "q"
down = "r"

















class Hero():
    def __init__(self):
        self.cameraOn = True

        self.hero = loader.loadModel("smiley")
        #self.hero.setTexture(loader.loadTexture("block.png"))
        self.hero.setColor((0.8,0.8,0,1))
        self.hero.setPos(10)
        self.hero.setScale(0.3)
        self.hero.reparentTo(render)
        self.cameraBind()
        self.accept_events()

    def cameraBind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0,0,1.5)
        self.cameraOn = True
    
    def cameraUp(self):
        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos(Pos[0],pos[1],pos[2])
        base.camera.reparentTo(render)
        base.enableMouse()
        self.cameraOn = False



    def cameraChange(self):
        if self.cameraOn:
            self.cameraUp()
        else:
            self.cameraBind()

    def forward(self):
        angle = self.hero.getH() % 360
        self.move_to(angle)
    
    def backward(self):
        angle = (self.hero.getH()+180) % 360
        self.move_to(angle)

    def forward(self):
        angle = (self.hero.getH()+90) % 360
        self.move_to(angle)

    def forward(self):
        angle = (self.hero.getH()+270) % 360
        self.move_to(angle)
    
    
    def rotateLeft(self):
        self.Hero.setH(self.hreo.getH()+5)
    def rotateRight(self):
        self.Hero.setH(self.hreo.getH()-5)






    def accept_events(self):
        base.accept(camera,self.cameraChange)
    
    
        base.accept(rotate_left,self.rotateLeft)
        base.accept(rotate_left + "-repeat",self.rotateLeft)
        base.accept(rotate_right,self.rotateRight)
        base.accept(rotate_right + "-repeat",self.rotateRight)

