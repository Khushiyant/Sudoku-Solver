'''Basic Import the basic libraries'''

from logic import solveSudoku
from tkinter import Button,Tk,Entry,LEFT,Frame

inp =   [[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]]
grid =   [[0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]]

if __name__ == "__main__":
    my_font = ("arial",18)
    
    root = Tk()     ## Initalisation of GUI ##
    root.resizable(width=False,height=False)    ## Fixing the GUI geometry ##
    root.title("Sudoku Solver")

    ''' Elements Declaration '''

    frame1 = Frame(root)
    frame1.pack(side=LEFT)
    frame2 = Frame(root)
    frame2.pack(side = LEFT)

    '''Code to generate checkboard pattern'''

    for i in range(9):
        for j in range(9):
            if i in [0,1,2,6,7,8] and j in [3,4,5] or i in [3,4,5] and j in [0,1,2,6,7,8]:
                grid[i][j] = Entry(frame1,bg="gray",highlightcolor="yellow",font=my_font,width=2)
                grid[i][j].grid(row=i,column=j)
            else:
                grid[i][j] = Entry(frame1,bg="white",highlightcolor="yellow",font=my_font,width=2)
                grid[i][j].grid(row=i,column=j)
    '''
    This Function perform the following tasks:
    -> getting the entered values in grid
    -> passing the fetched values to sovleSudoku()
    -> assigning the solved grid to GUI
    '''
    def access():
        for a in range(9):
            for b in range(9):
                if grid[a][b].get == "":
                    inp[a][b] = 0
                else:
                    inp[a][b] = int(grid[a][b].get())
        lg.solveSudoku(inp)
        for n in range(9):
            for m in range(9):
                grid[n][m].delete(0,str(inp[n][m]))
                grid[n][m].insert(0,str(inp[n][m]))

    solve = Button(frame2,text="Solve",height=12,fg="blue",font=("arial",15),activebackground="skyblue",command=access)
    solve.pack(side=LEFT)

    root.mainloop()     ## End of GUI ##
