from tkinter import *
from random import randint

# * Player Class to set the players details
class Player():
    def __init__(self,name='',score=0):
        self.name=name
        self.score=score

# * Game Class
class Game():

    is_p1_turn = True
    
    def __init__(self):
        self.root = Tk()
        self.root.maxsize(800,600)
        self.root.minsize(800,600)
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

        Label(mode_select_frame,text='Select the Game Mode',bg='red',padx=50,pady=30).pack(padx=30,pady=20)

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
            Label(l2,text='Name of Player2').pack(side=LEFT,padx=190)
            self.entry_list.append(Entry(l2))
            self.entry_list[1].pack(side=LEFT)
        else:
            Label(l1,text='Name of Player').pack(side=LEFT,padx=190)
            self.entry_list.append(Entry(l1))
            self.entry_list[0].pack(side=LEFT)

        Button(self.player_details_frame,text='Start the Game',command=self.create_player).pack(pady=50)

    # * Create the Player Details
    def create_player(self):
        if self.is_mul_player:
            Game.p1 = Player(self.entry_list[0].get(),0)
            Game.p2 = Player(self.entry_list[1].get(),0)
        else:
            Game.p1 = Player(self.entry_list[0].get(),0)
            Game.p2 = Player('Computer',0)
        self.game_window()

    # * Game Window
    def game_window(self):
        self.welcome_frame.pack_forget()

        self.game_window_frame = Frame(self.root)
        self.game_window_frame.pack(fill=BOTH,expand=True)

        self.game_screen = Frame(self.game_window_frame,bg='red')
        self.game_screen.pack(fill=BOTH,expand=True,side=LEFT)

        self.update_game()

        self.score_frame = Frame(self.game_window_frame,bg='blue')
        self.score_frame.pack(fill=BOTH,expand=True)

        l1 = Label(self.score_frame)
        l1.pack(pady=10)
        Label(l1,text="Player 1",width=20,anchor=W).pack()
        Label(l1,text=self.p1.name).pack(side=LEFT)
        self.p1_score_label = Label(l1,text=self.p1.score)
        self.p1_score_label.pack(side=RIGHT)

        l2 = Label(self.score_frame)
        l2.pack(pady=10)
        Label(l2,text="Player 2",width=20,anchor=W).pack()
        Label(l2,text=self.p2.name).pack(side=LEFT)
        self.p2_score_label = Label(l2,text=self.p2.score)
        self.p2_score_label.pack(side=RIGHT)

        self.dice = Label(self.score_frame,text='',font=('times', 120))
        self.dice.pack(pady=20,fill=BOTH,expand=True)

        

        l3 = Label(self.score_frame)
        l3.pack(fill=BOTH,expand=True)
        Label(l3,text='Current Turn',anchor=W).pack(fill=X,pady=10)
        
        self.turn_label = Label(l3,text=self.p1.name,anchor=W)
        self.turn_label.pack(fill=X)

        Button(self.score_frame,text='Roll',command=self.roll_dice).pack(pady=10)
    
    def update_game(self):
        pass
    
    def score_update(self,point):
        if self.is_p1_turn:
            self.p1.score = self.p1.score + point
            self.p1_score_label.config(text=self.p1.score)
            self.turn_label.config(text=self.p2.name)
            self.is_p1_turn=False
        else:
            self.p2.score = self.p2.score + point
            self.p2_score_label.config(text=self.p2.score)
            self.turn_label.config(text=self.p1.name)
            self.is_p1_turn=True


        
    
    def roll_dice(self):
        dice_value = randint(0,5)
        dice_text = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
        self.dice.configure(text=dice_text[dice_value])
        self.score_update(dice_value+1)



if __name__ == "__main__":
    Game()