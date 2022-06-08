import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,
                             QPushButton, QComboBox,QApplication,QLabel)
from tictactoe import Tictactoe
from functools import partial

class TicTacToe(QWidget):

    def __init__(self):
        super().__init__()
        self.turn=0
        self.initUI()
        self.text_game=QLabel('Game started')
        self.text_turn=QLabel('')


    def initUI(self):

        self.grid = QGridLayout()
        self.choice_text=QLabel('Choose Grid size ')
        self.choice_text.resize(100,100)
        self.combo = QComboBox(self)
        self.combo.addItems([str(i) for i in range(3,10)])
        self.start_button=QPushButton('Start')
        
        self.setLayout(self.grid)
        
        self.grid.addWidget(self.choice_text)
        self.grid.addWidget(self.combo)
        self.grid.addWidget(self.start_button)
        
       

        
        self.start_button.clicked.connect(self.showGrid)
        self.move(0,0)
        self.resize(800,600)
        self.setWindowTitle('Tictactoe')
        self.show()


    def showGrid(self):
        init_value=int(self.combo.currentText())
        print(f"Grid with {init_value}x{init_value}")
        self.t=Tictactoe(init_value)
        self.start_button.deleteLater()
        self.choice_text.deleteLater()
        self.combo.deleteLater()
        
        self.buttons=[QPushButton('') for i in range(self.t.n*self.t.n)]
        
        posx=0
        posy=0
        self.grid.setSpacing(2)
        for i in range(self.t.n*self.t.n):
            self.buttons[i].setFixedSize(100,100)
            self.buttons[i].clicked.connect(partial(self.buttonClicked,(posx,posy)))
            self.grid.addWidget(self.buttons[i],posx,posy)
            self.buttons[i].setText(None)
            posy+=1
            if(posy>self.t.n-1):
                posy=posy%self.t.n
                posx+=1

        reset_button=QPushButton('Reset')
        self.grid.addWidget(self.text_game)
        self.grid.addWidget(self.text_turn)
        self.grid.addWidget(reset_button)
        reset_button.clicked.connect(self.reset_grid)

    def buttonClicked(self,val):
        print(f"Button clicked: {val}")
        if(self.turn==0):
            self.t.p1_move(val[0],val[1])
        else:
            self.t.p2_move(val[0],val[1])

        self.switchState(val[0],val[1])
    
    def reset_grid(self):
        self.t.reset()
        for i in range(self.t.n*self.t.n):
            self.buttons[i].setText(None)
        self.t.game_running=True

    
    def switchState(self,x,y):
        if(self.turn==0):
            print(x*self.t.n+y)
            self.buttons[x*self.t.n+y].setText(self.t.grid[x][y])
            self.turn=1
            self.text_game.setText(self.t.check())
            if(self.t.game_running):
                self.text_turn.setText(f"{self.t.p2_symbol} turn")
            else:
                self.text_turn.setText("Game ended,press reset button.")
        else:
            print(x*self.t.n+y)
            self.buttons[x*self.t.n+y].setText(self.t.grid[x][y])
            self.text_turn.setText("")
            self.turn=0
            self.text_game.setText(self.t.check())
            
            if(self.t.game_running):
                self.text_turn.setText(f"{self.t.p1_symbol} turn")
            else:
                self.text_turn.setText("Game ended,press reset button.")



def main():
    app = QApplication(sys.argv)
    game = TicTacToe()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
