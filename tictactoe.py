class Tictactoe:
    number_of_games=0
    player_1=0
    player_2=0
    game_running=False
    def __init__(self,n=3,p1_symbol='x',p2_symbol='o'):
        self.n=n
        self.grid=[[None]*n for i in range(self.n)]
        self.p1_symbol=p1_symbol
        self.p2_symbol=p2_symbol
        Tictactoe.game_running=True

    def check_horizontal(self,symbol):
        m=[symbol]*self.n
        for i in range(self.n):
            if(self.grid[i]==m):
                cells=set([(i,j) for j in range(self.n)])
                return {'cells':cells,'state':'matched','symbol':symbol}
        else:
            return {'cells':None,'state':'not_matched'}
        
    def check_vertical(self,symbol):
        m=[symbol]*self.n
        grid_transposed=[[self.grid[i][j] for i in range(self.n)] for j in range(self.n)]
        for i in range(self.n):
            if(grid_transposed[i]==m):
                cells=set([(j,i) for j in range(self.n)])
                return {'cells':cells,'state':'matched','symbol':symbol}
        else:
            return {'cells':None,'state':'not_matched'}
        
        
    def check_diagonal(self,symbol):
        m=[symbol]*self.n
        diag_1=[self.grid[i][i] for i in range(self.n)]
        diag_2=[self.grid[i][(self.n-1)-i] for i in range(self.n)]
        if(m==diag_1):
            diagonal=[(i,i) for i in range(self.n)]
            return {'cells':diagonal,'state':'matched','symbol':symbol}
        elif(m==diag_2):
            diagonal=[(i,self.n-1-i) for i in range(self.n)]
            return {'cells':diagonal,'state':'matched','symbol':symbol}
        else:
            return {'cells':None,'state':'unmatched'}
    
    def check_win(self,symbol):
        state_h=self.check_horizontal(symbol)
        state_v=self.check_vertical(symbol)
        state_d=self.check_diagonal(symbol)
        
        if(state_h['state']=='matched'):
            return state_h
        elif(state_v['state']=='matched'):
            return state_v
        elif(state_d['state']=='matched'):
            return state_d
        else:
            return {'state':'unmatched'}

    def check(self):
        if(self.check_win(self.p1_symbol)['state']=='matched'):
            Tictactoe.game_running=False
            self.player_1+=1
            self.number_of_games+=1
            return f"{self.p1_symbol} has won"
        
        elif(self.check_win(self.p2_symbol)['state']=='matched'):
            Tictactoe.game_running=False
            self.player_2+=1
            self.number_of_games+=1
            return f"{self.p2_symbol} has won"
        else:
            count=0
            for i in range(self.n):
                if None not in self.grid[i]:
                    count+=1
            if(count==self.n):
                Tictactoe.game_running=False
                return "Game Draw"
            else:
                return "Game is running"
    

    def p1_move(self,x,y):

        if(Tictactoe.game_running and self.grid[x][y]==None):
            self.grid[x][y]=self.p1_symbol

        else:
            print("Game has ended")

    def p2_move(self,x,y):
        if(Tictactoe.game_running and self.grid[x][y]==None):
            self.grid[x][y]=self.p2_symbol
        else:
            print("Game has ended")

    def reset(self):
        self.grid=[[None]*self.n for i in range(self.n)]
