from tkinter import Button,Label,Frame,Entry,Tk,Canvas,BOTH,LEFT,RIGHT,W,X,NORMAL,DISABLED
from random import randint
from PIL import ImageTk,Image

# * Player Class to set the players details
class Player():
    def __init__(self,name,score,position,marker):
        self.name=name
        self.score=score
        self.position = position
        self.marker = marker
        self.can_start = False
    
    def change_position(self):
        if (self.score-1)%10 == 0:
            self.position[1] = self.position[1] - 60
            self.position[3] = self.position[3] - 60
        elif int((self.score-1)/10) % 2 != 0:
            self.position[0] = self.position[0] - 60
            self.position[2] = self.position[2] - 60
        else:
            self.position[0] = self.position[0] + 60
            self.position[2] = self.position[2] + 60
    

# * Game Class
class Game():

    is_p1_turn = True
    after_id = None
    root_after_id = None
    counter = 0

    snake_zone = {
        27:[[[310, 530, 330, 510],[310, 590, 330, 570],[250, 590, 270, 570]],5],
        40:[[[70, 470, 90, 450],[70, 530, 90, 510],[130, 590, 150, 570]],3],
        43:[[[190, 410, 210, 390],[130, 470, 150, 450],[130, 530, 150, 510]],18],
        54:[[[430, 350, 450, 330],[490, 410, 510, 390],[550, 410, 570, 390]],31],
        66:[[[250, 290, 270, 270],[310, 290, 330, 270],[250, 350, 270, 330]],45],
        76:[[[250, 230, 270, 210],[250, 290, 270, 270],[130, 290, 150, 270]],58],
        89:[[[490, 170, 510, 150],[430, 230, 450, 210],[430, 290, 450, 270]],53],
        99:[[[70, 110, 90, 90],[70, 170, 90, 150],[130, 170, 150, 150],[130, 230, 150, 210],[70, 290, 90, 270],[70, 350, 90, 330],[10, 350, 30, 330]],41],
    }

    ladder_zone = {
        4:[[[250, 530, 270, 510],[250, 470, 270, 450]],25],
        13:[[[370, 470, 390, 450],[370, 410, 390, 390],[310, 350, 330, 330]],46],
        33:[[[490, 350, 510, 330]],49],
        50:[[[490, 290, 510, 270],[490, 230, 510, 210]],69],
        42:[[[130, 290, 150, 270],[130, 230, 150, 210]],63],
        62:[[[10, 170, 30, 150],[10, 110, 30, 90]],81],
        74:[[[430, 110, 450, 90],[490, 50, 510, 30]],92],
    }
    
    def __init__(self):
        self.root = Tk()
        self.root.maxsize(800,600)
        self.root.minsize(800,600)

        self.root.title('Snake & Ladder')
        self.location = ''
        for i in __file__.split('/')[1:-1]:
            self.location = self.location + '/' + i
        
        self.icon = Image.open(self.location + '/assets/icon.png')
        self.icon = ImageTk.PhotoImage(self.icon)
        self.root.iconphoto(False,self.icon)

        self.background = Image.open(self.location + '/assets/background.jpg')
        self.background = ImageTk.PhotoImage(self.background)
        
        self.welcome_screen()        

        self.root.mainloop()
    
    # * Create the welcome Screen
    def welcome_screen(self):
        self.welcome_frame = Frame(self.root)
        self.welcome_frame.pack(fill=BOTH,expand=True)

        mode_select_frame = Frame(self.welcome_frame)
        mode_select_frame.pack(fill=BOTH,expand=True)

        self.player_details_frame = Frame(self.welcome_frame)
        self.player_details_frame.pack(fill=BOTH,expand=True)

        Label(mode_select_frame,text='Select the Game Mode',font=('',30),padx=50,pady=30).pack(padx=30,pady=20)

        Button(mode_select_frame,text='Player VS Player',command=lambda: self.set_game_mode(True)).pack(side=LEFT,padx=180)
        Button(mode_select_frame,text='Computer VS Player',command=lambda: self.set_game_mode(False)).pack(side=LEFT)

    # * Set the Game Mode
    def set_game_mode(self,is_mul_player):
        self.player_details_frame.pack_forget()
        self.player_details_frame = Frame(self.welcome_frame)
        self.player_details_frame.pack(fill=BOTH,expand=True)
        
        l1 = Label(self.player_details_frame)
        l1.pack(fill=BOTH,expand=True)

        self.is_mul_player = is_mul_player
        self.entry_list=[]
        if is_mul_player:
            l2 = Label(self.player_details_frame)
            l2.pack(fill=BOTH,expand=True)
            
            Label(l1,text='Name of Player1').pack(side=LEFT,padx=190)
            self.entry_list.append(Entry(l1))
            self.entry_list[0].pack(side=LEFT)
            self.entry_list[0].insert(0,'Player 1')
            Label(l2,text='Name of Player2').pack(side=LEFT,padx=190)
            self.entry_list.append(Entry(l2))
            self.entry_list[1].pack(side=LEFT)
            self.entry_list[1].insert(0,'Player 2')
        else:
            Label(l1,text='Name of Player').pack(side=LEFT,padx=190)
            self.entry_list.append(Entry(l1))
            self.entry_list[0].pack(side=LEFT)
            self.entry_list[0].insert(0,'Player')

        Button(self.player_details_frame,text='Start the Game',command=self.create_player).pack(pady=50)

    # * Create the Player Details
    def create_player(self):
        if self.is_mul_player:
            Game.p1 = Player(self.entry_list[0].get(),1,[10,590,30,570],'red')
            Game.p2 = Player(self.entry_list[1].get(),1,[25,575,45,555],'blue')
        else:
            Game.p1 = Player(self.entry_list[0].get(),1,[10,590,30,570],'red')
            Game.p2 = Player('Computer',1,[25,575,45,555],'blue')
        self.game_window()

    # * Game Window
    def game_window(self):
        self.welcome_frame.pack_forget()

        self.game_window_frame = Frame(self.root)
        self.game_window_frame.pack(fill=BOTH,expand=True)

        self.game_screen = Canvas(self.game_window_frame)
        self.game_screen.pack(fill=BOTH,expand=True,side=LEFT)

        self.game_screen.create_image(300,310,image=self.background)
        self.game_screen.create_oval(self.p1.position,fill='red')
        self.game_screen.create_oval(self.p2.position,fill='blue')

        # * Score Frame
        score_frame = Frame(self.game_window_frame)
        score_frame.pack(fill=BOTH,expand=True)

        l1 = Label(score_frame)
        l1.pack(pady=10)
        Label(l1,text="Player 1",width=23,anchor=W,fg=self.p1.marker).pack()
        Label(l1,text=self.p1.name,fg=self.p1.marker).pack(side=LEFT)
        self.p1_score_label = Label(l1,text=self.p1.score,fg=self.p1.marker)
        self.p1_score_label.pack(side=RIGHT)

        l2 = Label(score_frame)
        l2.pack(pady=10)
        Label(l2,text="Player 2",width=23,anchor=W,fg=self.p2.marker).pack()
        Label(l2,text=self.p2.name,fg=self.p2.marker).pack(side=LEFT)
        self.p2_score_label = Label(l2,text=self.p2.score,fg=self.p2.marker)
        self.p2_score_label.pack(side=RIGHT)

        self.dice = Label(score_frame,text='',font=('times', 120))
        self.dice.pack(pady=20,fill=BOTH,expand=True)

        l3 = Label(score_frame)
        l3.pack(fill=BOTH,expand=True)
        Label(l3,text='Current Turn',anchor=W).pack(fill=X,pady=10)
        
        self.turn_label = Label(l3,text=self.p1.name,anchor=W,fg=self.p1.marker)
        self.turn_label.pack(fill=X)

        self.roll = Button(score_frame,text='Roll',command=self.roll_dice)
        self.roll.pack(pady=10)
    
    def roll_dice(self):
        self.roll['state'] = DISABLED
        dice_value = randint(0,5)
        dice_text = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
        self.dice.configure(text=dice_text[dice_value])
        if self.is_mul_player:
            self.player_vs_player(dice_value+1)
        else:
            self.player_vs_com(dice_value+1)

    def player_vs_com(self,point):
        if self.p1.score + point + self.counter > 100:
            self.update_score()
        elif self.p1.can_start:
            if point == 1:
                if self.counter == 2:
                    self.counter = 0
                    self.update_score()
                else:
                    self.counter += 1
                    self.roll['state'] = NORMAL
            else:     
                self.update_game_screen(point+self.counter)
                self.counter = 0
        elif point == 1:
            self.after_id = self.game_screen.after(250,lambda: self.update_game_screen(1))
            self.p1.can_start = True
        else:
            self.update_score()         

    def computer_move(self):
        dice_value = randint(0,5)
        dice_text = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
        self.dice.configure(text=dice_text[dice_value])
        point = dice_value+1

        if self.p2.score + point + self.counter > 100:
            self.update_score()
        elif self.p2.can_start:
            if point == 1:
                if self.counter == 2:
                    self.counter = 0
                    self.update_score()
                else:
                    self.counter += 1
                    self.game_screen.after(200,self.computer_move)
            else:
                self.update_game_screen(point+self.counter)
                self.counter = 0
        elif point == 1:
            self.update_game_screen(point)
            self.p2.can_start = True
        else:
            self.update_score()

    def player_vs_player(self,point):
        if self.is_p1_turn:
            if self.p1.score + point + self.counter > 100:
                self.update_score()
            elif self.p1.can_start:
                if point == 1:
                    if self.counter == 2:
                        self.counter = 0
                        self.update_score()
                    else:
                        self.counter += 1
                        self.roll['state'] = NORMAL
                else:     
                    self.update_game_screen(point+self.counter)
                    self.counter = 0
            elif point == 1:
                self.update_game_screen(point)
                self.p1.can_start = True
            else:
                self.update_score()
        else:
            if self.p2.score + point + self.counter > 100:
                self.update_score()
            elif self.p2.can_start:
                if point == 1:
                    if self.counter == 2:
                        self.counter = 0
                        self.update_score()
                    else:
                        self.counter += 1
                        self.roll['state'] = NORMAL
                else:
                    self.update_game_screen(point+self.counter)
                    self.counter = 0
            elif point == 1:
                self.update_game_screen(point)
                self.p2.can_start = True
            else:
                self.update_score()
    
    def update_game_screen(self,point):
        if point == 0:
            self.root.after_cancel(self.root_after_id)
            self.rule_chacking()
        else:
            if self.is_p1_turn:
                self.p1.score = self.p1.score + 1
                self.p1.change_position()
                
                self.game_screen.create_image(300,310,image=self.background)
            
                self.game_screen.create_oval(self.p1.position,fill=self.p1.marker)
                self.game_screen.create_oval(self.p2.position,fill=self.p2.marker)
                self.root_after_id = self.root.after(200,lambda: self.update_game_screen(point-1))
            else:
                self.p2.score = self.p2.score + 1
                self.p2.change_position()

                self.game_screen.create_image(300,310,image=self.background)
            
                self.game_screen.create_oval(self.p1.position,fill=self.p1.marker)
                self.game_screen.create_oval(self.p2.position,fill=self.p2.marker)
                self.root_after_id = self.root.after(200,lambda: self.update_game_screen(point-1))
    
    def rule_chacking(self):
        if self.is_p1_turn:
            is_p1 = True
            p1 = self.p1
        else:
            is_p1 = False
            p1 = self.p2
        
        if p1.score == 100:
            self.winner(p1.name)
        else:
            if p1.score in self.snake_zone:
                positions, socre = self.snake_zone[p1.score]
                self.update_position(positions, len(positions),is_p1)
                p1.score = socre
            elif p1.score in self.ladder_zone:
                positions, socre = self.ladder_zone[p1.score]
                self.update_position(positions, len(positions),is_p1)
                p1.score = socre
        
        self.update_score()
    
    def update_position(self,positions,length,is_p1):
        if length == 0:
            self.game_screen.after_cancel(self.after_id)
        else:
            if is_p1:
                self.p1.position = positions[-length]
                self.game_screen.create_image(300,310,image=self.background)
                self.game_screen.create_oval(self.p1.position,fill=self.p1.marker)
                self.game_screen.create_oval(self.p2.position,fill=self.p2.marker)
            else:
                x1,y1,x2,y2 = positions[-length]
                self.p2.position = [x1+15,y1-15,x2+15,y2-15]
                self.game_screen.create_image(300,310,image=self.background)
                self.game_screen.create_oval(self.p2.position,fill=self.p2.marker)
                self.game_screen.create_oval(self.p1.position,fill=self.p1.marker)
            self.after_id = self.game_screen.after(250,lambda: self.update_position(positions, length-1,is_p1))

    def update_score(self):
        self.roll['state'] = NORMAL
        if self.is_p1_turn:
            self.p1_score_label.config(text=self.p1.score)
            self.turn_label.config(text=self.p2.name,fg=self.p2.marker)
            self.is_p1_turn=False
        else:
            self.p2_score_label.config(text=self.p2.score)
            self.turn_label.config(text=self.p1.name,fg=self.p1.marker)
            self.is_p1_turn=True
        
        if not (self.is_p1_turn or self.is_mul_player):
            self.roll['state'] = DISABLED
            self.game_screen.after(200,self.computer_move)

    def winner(self,name):
        self.game_window_frame.pack_forget()
        
        self.result_frame = Frame(self.root)
        self.result_frame.pack(fill=BOTH,expand=True)

        Label(self.result_frame,text=name+" is the Winner",font=('',30)).pack(fill=BOTH,expand=True,pady=10)

        Button(self.result_frame,text='Rematch',command=self.rematch).pack(pady=20)
        Button(self.result_frame,text='Main Manu',command=self.restart).pack(pady=20)
        Button(self.result_frame,text='Exit',command=self.root.quit).pack(pady=20)

    def rematch(self):
        self.result_frame.pack_forget()
        self.p1.score = self.p2.score = 1
        self.p1.position = [10,590,30,570]
        self.p2.position = [25,575,45,555]
        self.counter = 0
        self.p1.can_start = self.p2.can_start = False
        self.is_p1_turn = True
        self.game_window()

    def restart(self):
        self.result_frame.pack_forget()
        self.p1.score = self.p2.score = 1
        self.p1.position = [10,590,30,570]
        self.p2.position = [25,575,45,555]
        self.counter = 0
        self.p1.can_start = self.p2.can_start = False
        self.is_p1_turn = True
        self.welcome_screen()


if __name__ == "__main__":
    Game()
