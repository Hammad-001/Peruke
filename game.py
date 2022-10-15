import sys
import random
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.uic import loadUi
from winner import Winner
from rules import Rules



class Peruke(QMainWindow):
    def __init__(self):
        super(Peruke,self).__init__()
        loadUi('gui/game.ui',self)

        self.p1_tokens = {'protected':[[],[]],'unprotected':[[1,2,3,4,5,6],[6,5,4,3,2,1]]}
        self.p2_tokens = {'protected':[[],[]],'unprotected':[[1,2,3,4,5,6],[6,5,4,3,2,1]]}

        self.is_player_1 = True
        self.is_First_turn = True
        self.count = 0
        self.dice_val = []
        self.p1_caught = []
        self.p2_caught = []
        self.p1Score = 0
        self.p2Score = 0

        self.btn_roll.clicked.connect(self.generate_dices)
        
        self.p1P1.clicked.connect(self.btn_clicked)
        self.p1P2.clicked.connect(self.btn_clicked)
        self.p1P3.clicked.connect(self.btn_clicked)
        self.p1P4.clicked.connect(self.btn_clicked)
        self.p1P5.clicked.connect(self.btn_clicked)
        self.p1P6.clicked.connect(self.btn_clicked)

        self.p1S1.clicked.connect(self.btn_clicked)
        self.p1S2.clicked.connect(self.btn_clicked)
        self.p1S3.clicked.connect(self.btn_clicked)
        self.p1S4.clicked.connect(self.btn_clicked)
        self.p1S5.clicked.connect(self.btn_clicked)
        self.p1S6.clicked.connect(self.btn_clicked)
        
        self.p2P1.clicked.connect(self.btn_clicked)
        self.p2P2.clicked.connect(self.btn_clicked)
        self.p2P3.clicked.connect(self.btn_clicked)
        self.p2P4.clicked.connect(self.btn_clicked)
        self.p2P5.clicked.connect(self.btn_clicked)
        self.p2P6.clicked.connect(self.btn_clicked)

        self.p2S1.clicked.connect(self.btn_clicked)
        self.p2S2.clicked.connect(self.btn_clicked)
        self.p2S3.clicked.connect(self.btn_clicked)
        self.p2S4.clicked.connect(self.btn_clicked)
        self.p2S5.clicked.connect(self.btn_clicked)
        self.p2S6.clicked.connect(self.btn_clicked)

        self.btn_rules.clicked.connect(self.rules)
        

    def check_dice_vals(self):
        if not(self.is_First_turn):
            if len(self.dice_val) == 0:
                return True
            for i in self.dice_val:
                if self.is_player_1:
                    if i in self.p1_tokens['unprotected'][0] or i in self.p1_tokens['unprotected'][1] or i in self.p2_tokens['unprotected'][0] or i in self.p2_tokens['unprotected'][1] or i in self.p2_tokens['protected'][0] or i in self.p2_tokens['protected'][1]:
                        return True
                else:
                    if i in self.p2_tokens['unprotected'][0] or i in self.p2_tokens['unprotected'][1] or i in self.p1_tokens['unprotected'][0] or i in self.p1_tokens['unprotected'][1] or i in self.p1_tokens['protected'][0] or i in self.p1_tokens['protected'][1]:
                        return True
            return False
        else:
            if len(self.dice_val) == 0:
                return True
            for i in self.dice_val:
                if self.is_player_1:
                    if i in self.p1_tokens['unprotected'][1]:
                        return True
                else:
                    if i in self.p2_tokens['unprotected'][1]:
                        return True
            return False

    def generate_dices(self):
        if len(self.dice_val)  == 0:
            self.dice_val = [random.randint(1, 6) for i in range(3)]
            # self.dice_val = [3,3,3]
            self.dice_values.setText(str(self.dice_val[0])+"   "+str(self.dice_val[1])+"   "+str(self.dice_val[2]))
            if self.check_dice_vals() == False:
                self.dice_values.setText("No valid values")
                self.swap_player()


    def swap_player(self):
        if self.is_player_1: 
                self.is_player_1 = False
                self.player_label.setText("  Opponent's Turn")
        elif not(self.is_player_1):
            self.is_player_1 = True
            self.player_label.setText("     Your Turn")

    def first_check_btn(self,btn_name):
        vals = ""
        if btn_name[1] == '1' and self.is_player_1:
            if btn_name[2] == 'S':
                if int(btn_name[3]) in self.p1_tokens['unprotected'][1]:
                    if int(btn_name[3]) in self.dice_val:
                        self.dice_val.remove(int(btn_name[3]))
                        for i in self.dice_val:
                            vals = vals +  str(i) +"   "
                        self.dice_values.setText(vals)
                        self.p1_tokens['unprotected'][1].remove(int(btn_name[3]))
                        self.p1_tokens['protected'][1].append(int(btn_name[3]))
                        self.sending_button.setStyleSheet("background-color : yellow")
                        self.count +=1
                        if len(self.dice_val) == 0:
                            self.swap_player()
     
        if btn_name[1] == '2' and not(self.is_player_1):
            if btn_name[2] == 'S':
                if int(btn_name[3]) in self.p2_tokens['unprotected'][1]:
                    if int(btn_name[3]) in self.dice_val:
                        self.dice_val.remove(int(btn_name[3]))
                        for i in self.dice_val:
                            vals = vals +  str(i) +"   "
                        self.dice_values.setText(vals)
                        self.p2_tokens['unprotected'][1].remove(int(btn_name[3]))
                        self.p2_tokens['protected'][1].append(int(btn_name[3]))
                        self.sending_button.setStyleSheet("background-color : yellow")
                        self.count +=1
                        if len(self.dice_val) == 0:
                            self.swap_player()
        
        if self.check_dice_vals() == False :
            self.count += len(self.dice_val)
            self.swap_player()
            self.dice_val = []
            self.dice_values.setText("")

    def second_check_btn(self,btn_name):
        vals = ""
        if btn_name[1] == '1' and self.is_player_1:
            if btn_name[2] == 'S':
                if int(btn_name[3]) in self.p1_tokens['unprotected'][1]:
                    if int(btn_name[3]) in self.dice_val:
                        self.dice_val.remove(int(btn_name[3]))
                        for i in self.dice_val:
                            vals = vals +  str(i) +"   "
                        self.dice_values.setText(vals)
                        self.p1_tokens['unprotected'][1].remove(int(btn_name[3]))
                        self.p1_tokens['protected'][1].append(int(btn_name[3]))
                        self.sending_button.setStyleSheet("background-color : yellow")
                        self.count +=1
                        if len(self.dice_val) == 0:
                            self.swap_player()
            if btn_name[2] == 'P':
                if int(btn_name[3]) in self.p1_tokens['unprotected'][0]:
                    if int(btn_name[3]) in self.dice_val:
                        self.dice_val.remove(int(btn_name[3]))
                        for i in self.dice_val:
                            vals = vals +  str(i) +"   "
                        self.dice_values.setText(vals)
                        self.p1_tokens['unprotected'][0].remove(int(btn_name[3]))
                        self.p1_tokens['protected'][0].append(int(btn_name[3]))
                        self.sending_button.setStyleSheet("background-color : yellow")
                        self.count +=1
                        if len(self.dice_val) == 0:
                            self.swap_player()

        if btn_name[1] == '2' and self.is_player_1:
            if btn_name[2] == 'P':
                if int(btn_name[3]) in self.dice_val:
                    self.dice_val.remove(int(btn_name[3]))
                    for i in self.dice_val:
                        vals = vals +  str(i) +"   "
                    self.dice_values.setText(vals)
                    if int(btn_name[3]) in self.p2_tokens['protected'][0]:
                        self.sending_button.setStyleSheet("background-color: rgb(255, 147, 23)")
                        self.p2_tokens['protected'][0].remove(int(btn_name[3]))
                        self.p2_tokens['unprotected'][0].append(int(btn_name[3]))
                    elif int(btn_name[3]) in self.p2_tokens['unprotected'][0]:
                        self.p1_caught.append(int(btn_name[3]))
                        self.p2_tokens['unprotected'][0].remove(int(btn_name[3]))
                        self.sending_button.setStyleSheet("background-color: rgb(255, 11, 15)")
                    self.count +=1
                    if len(self.dice_val) == 0:
                        self.swap_player()
            if btn_name[2] == 'S':
                if int(btn_name[3]) in self.dice_val:
                    self.dice_val.remove(int(btn_name[3]))
                    for i in self.dice_val:
                        vals = vals +  str(i) +"   "
                    self.dice_values.setText(vals)
                    if int(btn_name[3]) in self.p2_tokens['protected'][1]:
                        self.sending_button.setStyleSheet("background-color: rgb(255, 147, 23)")
                        self.p2_tokens['protected'][1].remove(int(btn_name[3]))
                        self.p2_tokens['unprotected'][1].append(int(btn_name[3]))
                    elif int(btn_name[3]) in self.p2_tokens['unprotected'][1]:
                        self.p1_caught.append(int(btn_name[3]))
                        self.p2_tokens['unprotected'][1].remove(int(btn_name[3]))
                        self.sending_button.setStyleSheet("background-color: rgb(255, 11, 15)")
                    self.count +=1
                    if len(self.dice_val) == 0:
                        self.swap_player()

        if btn_name[1] == '2' and not(self.is_player_1):
            if btn_name[2] == 'S':
                if int(btn_name[3]) in self.p2_tokens['unprotected'][1]:
                    if int(btn_name[3]) in self.dice_val:
                        self.dice_val.remove(int(btn_name[3]))
                        for i in self.dice_val:
                            vals = vals +  str(i) +"   "
                        self.dice_values.setText(vals)
                        self.p2_tokens['unprotected'][1].remove(int(btn_name[3]))
                        self.p2_tokens['protected'][1].append(int(btn_name[3]))
                        self.sending_button.setStyleSheet("background-color : yellow")
                        self.count +=1
                        if len(self.dice_val) == 0:
                            self.swap_player()
            if btn_name[2] == 'P':
                if int(btn_name[3]) in self.p2_tokens['unprotected'][0]:
                    if int(btn_name[3]) in self.dice_val:
                        self.dice_val.remove(int(btn_name[3]))
                        for i in self.dice_val:
                            vals = vals +  str(i) +"   "
                        self.dice_values.setText(vals)
                        self.p2_tokens['unprotected'][0].remove(int(btn_name[3]))
                        self.p2_tokens['protected'][0].append(int(btn_name[3]))
                        self.sending_button.setStyleSheet("background-color : yellow")
                        self.count +=1
                        if len(self.dice_val) == 0:
                            self.swap_player()

        if btn_name[1] == '1' and not(self.is_player_1):
            if btn_name[2] == 'P':
                if int(btn_name[3]) in self.dice_val:
                    self.dice_val.remove(int(btn_name[3]))
                    for i in self.dice_val:
                        vals = vals +  str(i) +"   "
                    self.dice_values.setText(vals)
                    if int(btn_name[3]) in self.p1_tokens['protected'][0]:
                        self.sending_button.setStyleSheet("background-color: rgb(255, 147, 23)")
                        self.p1_tokens['protected'][0].remove(int(btn_name[3]))
                        self.p1_tokens['unprotected'][0].append(int(btn_name[3]))
                    elif int(btn_name[3]) in self.p1_tokens['unprotected'][0]:
                        self.p2_caught.append(int(btn_name[3]))
                        self.p1_tokens['unprotected'][0].remove(int(btn_name[3]))
                        self.sending_button.setStyleSheet("background-color: rgb(255, 11, 15)")
                    self.count +=1
                    if len(self.dice_val) == 0:
                        self.swap_player()

            if btn_name[2] == 'S':
                if int(btn_name[3]) in self.dice_val:
                    self.dice_val.remove(int(btn_name[3]))
                    for i in self.dice_val:
                        vals = vals +  str(i) +"   "
                    self.dice_values.setText(vals)
                    if int(btn_name[3]) in self.p1_tokens['protected'][1]:
                        self.sending_button.setStyleSheet("background-color: rgb(255, 147, 23)")
                        self.p1_tokens['protected'][1].remove(int(btn_name[3]))
                        self.p1_tokens['unprotected'][1].append(int(btn_name[3]))
                    elif int(btn_name[3]) in self.p1_tokens['unprotected'][1]:
                        self.p2_caught.append(int(btn_name[3]))
                        self.p1_tokens['unprotected'][1].remove(int(btn_name[3]))
                        self.sending_button.setStyleSheet("background-color: rgb(255, 11, 15)")
                    self.count +=1
                    if len(self.dice_val) == 0:
                        self.swap_player()

        if self.check_dice_vals() == False :
            self.count += len(self.dice_val)
            self.swap_player()
            self.dice_val = []
            self.dice_values.setText("")


    def btn_clicked(self):
        self.sending_button = self.sender()
        self.sending_button_name = self.sending_button.objectName()
        if self.is_First_turn: 
            if self.count <6:
                self.first_check_btn(self.sending_button_name)
            else:
                self.is_First_turn = False
        else:
            self.second_check_btn(self.sending_button_name)
            if len(self.p1_tokens['protected'][0]) + len(self.p1_tokens['unprotected']) == 0:
                self.p1Score = sum(self.p2_caught) + sum(self.p2_tokens['protected'][0]) + sum(self.p2_tokens['protected'][1])
                self.p2Score = sum(self.p1_caught) + sum(self.p1_tokens['protected'][0]) + sum(self.p1_tokens['protected'][1])
                self.winner()
            if len(self.p2_tokens['protected'][0]) + len(self.p2_tokens['unprotected']) == 0: 
                self.p1Score = sum(self.p2_caught) + sum(self.p2_tokens['protected'][0]) + sum(self.p2_tokens['protected'][1])
                self.p2Score = sum(self.p1_caught) + sum(self.p1_tokens['protected'][0]) + sum(self.p1_tokens['protected'][1])
                self.winner()

    def reset(self):
        self.p1_tokens = {'protected':[[],[]],'unprotected':[[1,2,3,4,5,6],[6,5,4,3,2,1]]}
        self.p2_tokens = {'protected':[[],[]],'unprotected':[[1,2,3,4,5,6],[6,5,4,3,2,1]]}

        self.is_player_1 = True
        self.is_First_turn = True
        self.count = 0
        self.dice_val = []
        self.p1_caught = []
        self.p2_caught = []
        self.p1Score = 0
        self.p2Score = 0
        self.dice_values.setText("")
        self.player_label.setText("  Player 1's Turn")

        self.p1P1.setStyleSheet("background-color: rgb(255, 147, 23)")
        self.p1P2.setStyleSheet("background-color: rgb(255, 147, 23)")
        self.p1P3.setStyleSheet("background-color: rgb(255, 147, 23)")
        self.p1P4.setStyleSheet("background-color: rgb(255, 147, 23)")
        self.p1P6.setStyleSheet("background-color: rgb(255, 147, 23)")
        self.p1P5.setStyleSheet("background-color: rgb(255, 147, 23)")

        self.p1S1.setStyleSheet("background-color: rgb(255, 147, 23)")
        self.p1S2.setStyleSheet("background-color: rgb(255, 147, 23)")
        self.p1S3.setStyleSheet("background-color: rgb(255, 147, 23)")
        self.p1S4.setStyleSheet("background-color: rgb(255, 147, 23)")
        self.p1S5.setStyleSheet("background-color: rgb(255, 147, 23)")
        self.p1S6.setStyleSheet("background-color: rgb(255, 147, 23)")
        
        self.p2P1.setStyleSheet("background-color: rgb(255, 147, 23)")
        self.p2P2.setStyleSheet("background-color: rgb(255, 147, 23)")
        self.p2P3.setStyleSheet("background-color: rgb(255, 147, 23)")
        self.p2P4.setStyleSheet("background-color: rgb(255, 147, 23)")
        self.p2P5.setStyleSheet("background-color: rgb(255, 147, 23)")
        self.p2P6.setStyleSheet("background-color: rgb(255, 147, 23)")

        self.p2S1.setStyleSheet("background-color: rgb(255, 147, 23)")
        self.p2S2.setStyleSheet("background-color: rgb(255, 147, 23)")
        self.p2S3.setStyleSheet("background-color: rgb(255, 147, 23)")
        self.p2S4.setStyleSheet("background-color: rgb(255, 147, 23)")
        self.p2S5.setStyleSheet("background-color: rgb(255, 147, 23)")
        self.p2S6.setStyleSheet("background-color: rgb(255, 147, 23)")
        self.help.close()


    def rules(self):
        self.help = QMainWindow()
        self.help_ui = Rules()
        self.help_ui.setupUi(self.help)
        self.help.show()

    def winner(self):
        self.help = QMainWindow()
        self.help_ui = Winner()
        self.help_ui.setupUi(self.help)
        self.help.show()
        self.help_ui.p1_score.setText(" P1 Score: "+str(self.p1Score))
        self.help_ui.p2_score.setText(" P2 Score: "+str(self.p2Score))
        if self.p1Score > self.p2Score:
            self.help_ui.win_label.setText("     Player 1 WON!!!")
        elif self.p1Score < self.p2Score:
            self.help_ui.win_label.setText("     Player 2 WON!!!")
        else:
            self.help_ui.win_label.setText("     Game Draw!!!!!!")
        self.help_ui.btn_ok.clicked.connect(self.reset)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Peruke()
    window.show()
    sys.exit(app.exec_())