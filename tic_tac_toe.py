from tkinter import *
from tkinter import font
from random import randint
import time

class Player():
    def __init__(self,name,marker):
        self.name = name
        self.marker = marker

class Game:
    p1 = Player('Player','X')
    p2 = Player('Computer','O')
    is_p1_turn = True
    game_over = False

    def __init__(self):
        self.root = Tk()
        self.root.geometry('318x400')
        self.root.title('Tic Tac Toe')
        self.root.maxsize(318,400)
        self.root.minsize(318,400)
        self.count = 0
        self.welcome_screen()
        self.root.mainloop()
    
    def welcome_screen(self):
        self.welcome_frame = Frame(self.root,bg='#DCE0E1')
        self.welcome_frame.pack(fill=BOTH,expand=True)

        Label(self.welcome_frame, text='Select the Game Mode',
                bg='#DCE0E1', fg='#000000',
                font=('',20)).pack(padx=10,pady=40)

        Button(self.welcome_frame, text='Player vs Computer',
                bg='#FFF000', fg='#000000',
                command=lambda: self.player_info_screen(1)).pack(padx=30,pady=30)
        
        Button(self.welcome_frame, text='Player vs Player',
                bg='#FFF000', fg='#000000',
                command=lambda: self.player_info_screen(2)).pack(padx=30)        

    def player_info_screen(self,player_number):
        self.welcome_frame.pack_forget()
        self.game_mode = player_number

        self.player_info_frame = Frame(self.root,bg='#DCE0E1')
        self.player_info_frame.pack(fill=BOTH,expand=True)

        Label(self.player_info_frame,text='Enter the Player Info',
                bg='#DCE0E1', fg='#000000',
                font=('',20)).pack(pady=30)
        
        entryList=[]
        for i in range(self.game_mode):
            l = Label(self.player_info_frame, bg='#DCE0E1')
            l.pack(pady=5)

            Label(l,text=f'Player {i+1}',bg='#DCE0E1',fg='#000000',font=('',12)).pack(side=LEFT,padx=20)
            entryList.append(Entry(l,bg='#DCE0E1',fg='#000000'))
            entryList[i].pack(side=LEFT)
            entryList[i].insert(0,f'Player {i+1}')

        Label(self.player_info_frame,text="Press Toss Button To Know Who's Turns Frist",
                bg='#DCE0E1', fg='#000000',
                font=('',10)).pack(pady=20)

        self.toss_bt = Button(self.player_info_frame,text='Toss',command=lambda: self.toss(entryList))
        self.toss_bt.pack()
    
    def toss(self,lst):
        self.toss_bt['state'] = DISABLED
        if randint(1,100) % 2 == 0:
            self.is_p1_turn = True
        else:
            self.is_p1_turn = False

        if self.game_mode == 2:
            self.p1.name = lst[0].get()
            self.p2.name = lst[1].get()
        else:
            self.p1.name = lst[0].get()
            self.p2.name = 'Computer'
        
        self.toss_frame = Frame(self.player_info_frame,bg='#DCE0E1')
        self.toss_frame.pack(fill=BOTH,expand=True)

        if self.is_p1_turn:
            Label(self.toss_frame,text=f'{self.p1.name} Wins\n Select Your Marker',
                    bg='#DCE0E1', fg='#000000',
                    font=('',10)).pack(pady=10)
            
            l=Label(self.toss_frame,bg='#DCE0E1')
            l.pack()
            Button(l, text='X', command=lambda: self.players_marker('X','O')).pack(side=LEFT,padx=20)
            Button(l, text='O', command=lambda: self.players_marker('O','X')).pack(side=LEFT,padx=20)
        elif self.game_mode == 2:
            Label(self.toss_frame,text=f'{self.p2.name} Wins',
                    bg='#DCE0E1', fg='#000000',
                    font=('',10)).pack(pady=10)
            
            l=Label(self.toss_frame,bg='#DCE0E1')
            l.pack()
            Button(l, text='X', command=lambda: self.players_marker('O','X')).pack(side=LEFT,padx=20)
            Button(l, text='O', command=lambda: self.players_marker('X','O')).pack(side=LEFT,padx=20)
        else:
            Label(self.toss_frame,text=f"{self.p2.name} Wins And Selects the 'O' marker",
                    bg='#DCE0E1', fg='#000000',
                    font=('',10)).pack(pady=15)
            self.is_p1_turn = False
            self.root.after(1000,self.set_comp_move)
    
    def set_comp_move(self):
        self.play_game()
        self.root.after(1000,self.computer_move)

    def players_marker(self,marker1,marker2):
        self.p1.marker = marker1
        self.p2.marker = marker2
        self.play_game()

    def play_game(self):
        self.player_info_frame.pack_forget()
        self.game_window()

    def game_window(self):
        self.game_window_frame = Frame(self.root, bg='#DCE0E1')
        self.game_window_frame.pack(fill=BOTH,expand=True)

        self.l1 = Label(self.game_window_frame,text='',font=('',20),bg='#DCE0E1', fg='#000000')
        self.l1.grid(row=0,column=0,columnspan=3,sticky=E+W,pady=20)

        if self.is_p1_turn:
            self.l1.config(text=self.p1.name + "'s Turns")
        else:
            self.l1.config(text=self.p2.name + "'s Turns")

        b1 = Button(self.game_window_frame,text=' ' ,font=('',15), width=6, height=3, command=lambda: self.on_click(1))
        b2 = Button(self.game_window_frame,text=' ' ,font=('',15), width=6, height=3, command=lambda: self.on_click(2))
        b3 = Button(self.game_window_frame,text=' ' ,font=('',15), width=6, height=3, command=lambda: self.on_click(3))
        b4 = Button(self.game_window_frame,text=' ' ,font=('',15), width=6, height=3, command=lambda: self.on_click(4))
        b5 = Button(self.game_window_frame,text=' ' ,font=('',15), width=6, height=3, command=lambda: self.on_click(5))
        b6 = Button(self.game_window_frame,text=' ' ,font=('',15), width=6, height=3, command=lambda: self.on_click(6))
        b7 = Button(self.game_window_frame,text=' ' ,font=('',15), width=6, height=3, command=lambda: self.on_click(7))
        b8 = Button(self.game_window_frame,text=' ' ,font=('',15), width=6, height=3, command=lambda: self.on_click(8))
        b9 = Button(self.game_window_frame,text=' ' ,font=('',15), width=6, height=3, command=lambda: self.on_click(9))
        
        b1.grid(row=1,column=0)
        b2.grid(row=1,column=1)
        b3.grid(row=1,column=2)
        b4.grid(row=2,column=0)
        b5.grid(row=2,column=1)
        b6.grid(row=2,column=2)
        b7.grid(row=3,column=0)
        b8.grid(row=3,column=1)
        b9.grid(row=3,column=2)

        self.gb_List = [b1,b2,b3,b4,b5,b6,b7,b8,b9]

        Label(self.game_window_frame,text='Tic Tac Toe',font=('',20),
                bg='#DCE0E1', fg='#000000').grid(row=4,column=0,columnspan=3,pady=10,sticky=EW)
    
    def on_click(self,index):
        if self.game_mode == 1:
            self.player_vs_computer_rule(index)
        else:
            self.player_vs_player_rule(index) 
    
    def player_vs_computer_rule(self,index):
        self.gb_List[index-1]['text'] = self.p1.marker
        self.gb_List[index-1]['state'] = DISABLED
        self.l1.config(text=self.p2.name + "'s Turns")
        self.count += 1
        self.check_result(self.p1)

        if self.count != 9 and not self.game_over:
            self.root.after(500,self.computer_move)

    def player_vs_player_rule(self,index):
        if self.is_p1_turn:
            self.gb_List[index-1]['text'] = self.p1.marker
            self.gb_List[index-1]['state'] = DISABLED
            self.count += 1
            self.check_result(self.p1)
            self.l1.config(text=self.p2.name + "'s Turns")
            self.is_p1_turn=False
        else:
            self.gb_List[index-1]['text'] = self.p2.marker
            self.gb_List[index-1]['state'] = DISABLED
            self.count += 1
            self.check_result(self.p2)
            self.l1.config(text=self.p1.name + "'s Turns")
            self.is_p1_turn=True


    def computer_move(self):
        run = True
        while run:
            box_num = randint(0,8)
            if self.gb_List[box_num]['state'] == DISABLED:
                continue
            else:
                run = False
                self.count += 1
                self.gb_List[box_num]['text'] = self.p2.marker
                self.gb_List[box_num]['state'] = DISABLED
                self.check_result(self.p2)
                self.l1.config(text=self.p1.name + "'s Turns")
    
    def check_result(self,player):
        for i in range(3):
            # vertical matching
            if self.gb_List[i*3]['text'] == self.gb_List[i*3+1]['text'] == self.gb_List[i*3+2]['text'] == player.marker:
                self.gb_List[i*3]['bg']=self.gb_List[i*3+1]['bg']=self.gb_List[i*3+2]['bg'] = 'green'
                self.root.after(500,lambda: self.display_massage('Congratulation',f'{player.name} win this Game'))
                
            # Horizondal matching            
            if self.gb_List[i]['text'] == self.gb_List[i+3]['text'] == self.gb_List[i+6]['text'] == player.marker:
                self.gb_List[i]['bg']=self.gb_List[i+3]['bg']=self.gb_List[i+6]['bg'] = 'green'
                self.root.after(500,lambda: self.display_massage('Congratulation',f'{player.name} win this Game'))
                
        # Diagonal matching
        if self.gb_List[0]['text'] == self.gb_List[4]['text'] == self.gb_List[8]['text'] == player.marker:
            self.gb_List[0]['bg']=self.gb_List[4]['bg']=self.gb_List[8]['bg'] = 'green'
            self.root.after(500,lambda: self.display_massage('Congratulation',f'{player.name} win this Game'))
            
        if self.gb_List[2]['text'] == self.gb_List[4]['text'] == self.gb_List[6]['text'] == player.marker:
            self.gb_List[2]['bg']=self.gb_List[4]['bg']=self.gb_List[6]['bg'] = 'green'
            self.root.after(500,lambda: self.display_massage('Congratulation',f'{player.name} win this Game'))
        
        if self.count == 9 and not self.game_over:
            self.root.after(500,lambda: self.display_massage('Draw','No one Wins'))
    
    def display_massage(self,massage_header,massage):
        self.game_over = True
        self.game_window_frame.pack_forget()
        
        self.massage_frame = Frame(self.root, bg='#DCE0E1')
        self.massage_frame.pack(fill=BOTH,expand=True)

        Label(self.massage_frame,text=massage_header+'\n'+massage,
                bg='#DCE0E1', fg='#000000',
                font=('',15)).pack(pady=30)
        
        Button(self.massage_frame,text='Rematch',bg='#FFF000', fg='#000000',command=self.rematch).pack(pady=5)
        Button(self.massage_frame,text='Main Menu',bg='#FFF000', fg='#000000',command=self.main_menu).pack(pady=5)
        Button(self.massage_frame,text='Exit',bg='#FFF000', fg='#000000',command=self.root.destroy).pack(pady=5)
        
    def main_menu(self):
        self.game_over = False
        self.count = 0
        self.massage_frame.pack_forget()
        self.welcome_frame.pack(fill=BOTH,expand=True)
    
    def rematch(self):
        self.game_over = False
        self.count = 0
        self.massage_frame.pack_forget()
        self.toss_bt['state'] = NORMAL
        self.toss_frame.pack_forget()
        self.player_info_frame.pack(fill=BOTH,expand=True)

if __name__ == "__main__":
    Game()