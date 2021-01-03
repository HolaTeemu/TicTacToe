import tkinter
from tkinter import font as tkFont
from tkinter import messagebox
import sqlite3
import time
import datetime

"""
Dictionaries for the GUI elements
"""

navigation_buttons = {
    "newgame_button": None,
    "results_button": None,
    "quit_button": None
}

# Game buttons
game_b = {
    "b1": None,
    "b2": None,
    "b3": None,

    "b4": None,
    "b5": None,
    "b6": None,

    "b7": None,
    "b8": None,
    "b9": None
}
canvases = {
    "logo": None
}

labels = {
    "logo_text": None
}

listboxes = {
    "results_listbox": None
}

frames = {
    "title_frame": None,
    "logo_frame": None,
    "newgame_button_frame": None,
    "results_button_frame": None,
    "quit_button_frame": None,
    "right_console_frame": None,
    "game_frame": None,
}

scrollbars = {
    "results_scrollbar": None
}

# Connect to the database and create a table if it doesn't exist already
db = sqlite3.connect("results.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS results "
           "(game_number INTEGER PRIMARY KEY AUTOINCREMENT, date TIMESTAMP NOT NULL, winner TEXT NOT NULL, "
           "time_elapsed FLOAT NOT NULL)")

# Create global variables
clicked = True
count = 0


def create_main_window():
    """
    Creates a main window for the interface and configures rows and columns
    """
    global main_window
    main_window = tkinter.Tk()
    main_window.title("TicTacToe")
    main_window.geometry("600x450+600+300")

    main_window.columnconfigure(0, weight=1)
    main_window.columnconfigure(1, weight=1)
    main_window.columnconfigure(2, weight=1)
    main_window.columnconfigure(3, weight=4)
    main_window.columnconfigure(4, weight=2)
    main_window.columnconfigure(5, weight=1)

    main_window.rowconfigure(0, weight=1)
    main_window.rowconfigure(1, weight=1)
    main_window.rowconfigure(2, weight=1)
    main_window.rowconfigure(3, weight=1)
    main_window.rowconfigure(4, weight=1)
    main_window.rowconfigure(5, weight=1)
    main_window.rowconfigure(6, weight=2)


def create_frames():
    """
    Creates frames for other elements. Other elements can be placed inside these frames.
    The frame can be inside the main window or inside another frame
    so the master parameter can be either a frame object or a window object.
    """
    frames["title_frame"] = tkinter.Frame(main_window)
    frames["title_frame"].grid(row=0, column=0, sticky='nsew')

    frames["logo_frame"] = tkinter.Frame(main_window)
    frames["logo_frame"].grid(row=1, column=0, sticky='nsew')

    frames["newgame_button_frame"] = tkinter.Frame(main_window)
    frames["newgame_button_frame"].grid(row=2, column=0, sticky='nsew')

    frames["results_button_frame"] = tkinter.Frame(main_window)
    frames["results_button_frame"].grid(row=3, column=0, sticky='nsew')

    frames["quit_button_frame"] = tkinter.Frame(main_window)
    frames["quit_button_frame"].grid(row=5, column=0, sticky='nsew')


def create_buttons():
    """
    Creates navigation buttons for the left console of the GUI.
    The handler is a function that executes when the button is pressed.
    """
    navigation_buttons["newgame_button"] = tkinter.Button(frames["newgame_button_frame"], text="New Game",
                                               height=2, width=20, command=create_game)
    navigation_buttons["newgame_button"].grid(row=1, column=0, sticky='nsew')
    navigation_buttons["newgame_button"].pack(side=tkinter.TOP)

    navigation_buttons["results_button"] = tkinter.Button(frames["results_button_frame"], text="Results",
                                               height=2, width=20, command=get_results)
    navigation_buttons["results_button"].grid(row=3, column=0, sticky='nsew')
    navigation_buttons["results_button"].pack(side=tkinter.TOP)

    navigation_buttons["quit_button"] = tkinter.Button(frames["quit_button_frame"], text="Quit",
                                            height=2, width=15, command=quit_program)
    navigation_buttons["quit_button"].grid(row=6, column=0, sticky='nsew')
    navigation_buttons["quit_button"].pack(side=tkinter.TOP)


def create_game():
    """
    Creates the frames for the buttons and creates the buttons for the game and grids them correctly.
    """
    global clicked, count
    clicked = True
    count = 0
    font = tkFont.Font(family='Helvetica', size=28)

    # If scrollbar has been created to check results, destroy it when the game starts.
    if scrollbars["results_scrollbar"]:
        scrollbars["results_scrollbar"].grid_forget()

    frames["right_console_frame"] = tkinter.Frame(main_window, background='cyan')
    frames["right_console_frame"].grid(row=0, column=1, rowspan=7, columnspan=5, sticky='nsew')

    frames["game_frame"] = tkinter.Frame(main_window)
    frames["game_frame"].grid(row=1, column=3, rowspan=5, columnspan=2, sticky='nsew')
    frames["game_frame"].rowconfigure(0, weight=1)
    frames["game_frame"].rowconfigure(1, weight=1)
    frames["game_frame"].rowconfigure(2, weight=1)

    frames["game_frame"].columnconfigure(0, weight=1)
    frames["game_frame"].columnconfigure(1, weight=1)
    frames["game_frame"].columnconfigure(2, weight=1)

    button_text = tkinter.StringVar()
    button_text.set(" ")

    game_b["b1"] = tkinter.Button(frames["game_frame"], text=" ", height=1, width=2,
                                   font=font, command=lambda: on_click(game_b["b1"]))
    game_b["b2"] = tkinter.Button(frames["game_frame"], text=" ", height=1, width=2,
                                  font=font, command=lambda: on_click(game_b["b2"]))
    game_b["b3"] = tkinter.Button(frames["game_frame"], text=" ", height=1, width=2,
                                  font=font, command=lambda: on_click(game_b["b3"]))

    game_b["b4"] = tkinter.Button(frames["game_frame"], text=" ", height=1, width=2,
                                  font=font, command=lambda: on_click(game_b["b4"]))
    game_b["b5"] = tkinter.Button(frames["game_frame"], text=" ", height=1, width=2,
                                  font=font, command=lambda: on_click(game_b["b5"]))
    game_b["b6"] = tkinter.Button(frames["game_frame"], text=" ", height=1, width=2,
                                  font=font, command=lambda: on_click(game_b["b6"]))

    game_b["b7"] = tkinter.Button(frames["game_frame"], text=" ", height=1, width=2,
                                  font=font, command=lambda: on_click(game_b["b7"]))
    game_b["b8"] = tkinter.Button(frames["game_frame"], text=" ", height=1, width=2,
                                  font=font, command=lambda: on_click(game_b["b8"]))
    game_b["b9"] = tkinter.Button(frames["game_frame"], text=" ", height=1, width=2,
                                  font=font, command=lambda: on_click(game_b["b9"]))


    game_b["b1"].grid(row=0, column=0, sticky='nsew')
    game_b["b2"].grid(row=0, column=1, sticky='nsew')
    game_b["b3"].grid(row=0, column=2, sticky='nsew')

    game_b["b4"].grid(row=1, column=0, sticky='nsew')
    game_b["b5"].grid(row=1, column=1, sticky='nsew')
    game_b["b6"].grid(row=1, column=2, sticky='nsew')

    game_b["b7"].grid(row=2, column=0, sticky='nsew')
    game_b["b8"].grid(row=2, column=1, sticky='nsew')
    game_b["b9"].grid(row=2, column=2, sticky='nsew')

def create_results_listbox():
    """
    Creates a listbox for the results. Also grids it correctly.
    """
    if frames["game_frame"]:
        scrollbars["results_scrollbar"] = tkinter.Scrollbar(main_window, orient=tkinter.VERTICAL)
        scrollbars["results_scrollbar"].grid(row=0, column=6, rowspan=7, sticky='nse')

        listboxes["results_list"] = tkinter.Listbox(main_window, relief='solid',
                                                    yscrollcommand=scrollbars["results_scrollbar"].set)
        listboxes["results_list"].grid(row=0, column=1, rowspan=7, columnspan=5, sticky='nsew')
    else:
        scrollbars["results_scrollbar"] = tkinter.Scrollbar(main_window, orient=tkinter.VERTICAL)
        scrollbars["results_scrollbar"].grid(row=0, column=6, rowspan=7, sticky='nse')

        listboxes["results_list"] = tkinter.Listbox(main_window, relief='solid',
                                                    yscrollcommand=scrollbars["results_scrollbar"].set)
        listboxes["results_list"].grid(row=0, column=1, rowspan=7, columnspan=5, sticky='nsew')
    scrollbars["results_scrollbar"].config(command=listboxes["results_list"].yview)

def on_click(button):
    """
    Called when a button is clicked.
    Changes the text of the button to be X if the clicker is player 1.
    Checks if the game is won by either player by calling ifend-function.
    If the game is won by either player, then save the time and
    save the results to the database by calling save_result-function.
    Also tell the player with a pop up messagebox if they won or
    they clicked a button with a mark already inside.
    """
    # If clicked is True, the player clicking is player 1.
    # If False, then the player clicking is player 2.
    global clicked, count, start_time, end_time

    # Start the game timer when the first click is made
    if count == 0:
        start_time = time.perf_counter()

    # "X"
    if button["text"] == " " and clicked:
        button["text"] = "X"
        clicked = False
        count += 1
        end = check_ifend()
        if end:
            end_time = "{:.2}".format(time.perf_counter()-start_time)
            save_result(button["text"], end_time)
            messagebox.showinfo("Winner!", "Player 1 has won!")

    # "O"
    elif button["text"] == " " and not clicked:
        button["text"] = "O"
        clicked = True
        count += 1
        end = check_ifend()
        if end:
            end_time = "{:.2}".format(time.perf_counter()-start_time)
            save_result(button["text"], end_time)
            messagebox.showinfo("Winner!", "Player 2 has won!")
    else:
        messagebox.showinfo("Error", "There is already a mark in that square")


def disable_buttons():
    """
    Disables the game buttons.
    """
    for key in game_b:
        game_b[key]['state'] = "disabled"


def change_color(color, *args):
    """
    Changes the button color. The parameter "color" tells the desired color and
    *args is the buttons which color needs to be changed.
    :param color: Color that the button is changed to.
    :param args: Buttons that needs their color changed.
    """
    for button in args:
        button["background"] = color


def check_ifend():
    """
    Checks if either player has won the game or if the game has ended in a draw.
    Doesnt do anything if the count is less than 5 since the game cannot end before that.
    If the game is won by either player. Change color of the winning buttons. If tie, the buttons turn red.

    :return: True if the game has been won by either player.
    """

    if count >= 5:
        # Row's for both X's and O's
        if game_b["b1"]["text"] == game_b["b2"]["text"] == \
                game_b["b3"]["text"] and game_b["b1"]["text"] != " ":
            change_color("green", game_b["b1"], game_b["b2"], game_b["b3"])
            disable_buttons()
            return True
    
        elif game_b["b4"]["text"] == game_b["b5"]["text"] == \
                game_b["b6"]["text"] and game_b["b4"]["text"] != " ":
            change_color("green", game_b["b4"], game_b["b5"], game_b["b6"])
            disable_buttons()
            return True
    
        elif game_b["b7"]["text"] == game_b["b8"]["text"] == \
                game_b["b9"]["text"] and game_b["b7"]["text"] != " ":
            change_color("green", game_b["b7"], game_b["b8"], game_b["b9"])
            disable_buttons()
            return True
    
        # Column's for both X's and O's
        elif game_b["b1"]["text"] == game_b["b4"]["text"] == \
                game_b["b7"]["text"] and game_b["b1"]["text"] != " ":
            change_color("green", game_b["b1"], game_b["b4"], game_b["b7"])
            disable_buttons()
            return True
    
        elif game_b["b2"]["text"] == game_b["b5"]["text"] == \
                game_b["b8"]["text"] and game_b["b2"]["text"] != " ":
            change_color("green", game_b["b2"], game_b["b5"], game_b["b8"])
            disable_buttons()
            return True
    
        elif game_b["b3"]["text"] == game_b["b6"]["text"] == \
                game_b["b9"]["text"] and game_b["b3"]["text"] != " ":
            change_color("green", game_b["b3"], game_b["b6"], game_b["b9"])
            disable_buttons()
            return True
    
        # Diagonals for both X's and O's
        elif game_b["b1"]["text"] == game_b["b5"]["text"] == \
                game_b["b9"]["text"] and game_b["b1"]["text"] != " ":
            change_color("green", game_b["b1"], game_b["b5"], game_b["b9"])
            disable_buttons()
            return True
    
        elif game_b["b3"]["text"] == game_b["b5"]["text"] == \
                game_b["b7"]["text"] and game_b["b3"]["text"] != " ":
            change_color("green", game_b["b3"], game_b["b5"], game_b["b7"])
            disable_buttons()
            return True
    
        elif count == 9:
            for key in game_b:
                game_b[key]["background"] = 'red'
            disable_buttons()
            end = "{:.2}".format(time.perf_counter()-start_time)
            save_result("Draw", end)
            messagebox.showinfo("Draw game",  "Draw!")


def quit_program():
    """
    Quits the program by destroying the tkinter main window
    Also closes the database connection
    """
    main_window.destroy()
    db.close()


def get_results():
    """
    Gets the results from the database and formats them into a string.
    After formatting the string, prints the results in the listbox.
    """
    create_results_listbox()
    for game_number, date, winner, time_elapsed in db.execute("SELECT * FROM results"):
        result = "Game#:{} - Played: {} - Winner: '{}' - Elapsed time: {} sec".\
            format(game_number, date, winner, time_elapsed)
        listboxes["results_list"].insert(tkinter.END, result)


def save_result(winner, time_elapsed):
    """
    Saves the result of the game into the database.
    :param winner: Winner of the game
    :param time_elapsed: Time elapsed in the played game.
    """
    try:
        db.execute("INSERT INTO results (date, winner, time_elapsed) VALUES (?, ?, ?)",
                   (datetime.datetime.now().date(), winner, time_elapsed))
    except sqlite3.Error:
        db.rollback()
    else:
        db.commit()


def main():
    create_main_window()
    create_frames()
    create_buttons()
    create_game()

    # Load the logo, create a canvas for it and put the logo inside it.
    kuva = tkinter.PhotoImage(file="logotictactoe.png")
    canvases["logo"] = tkinter.Canvas(frames["logo_frame"], height=70, width=70)
    canvases["logo"].pack(expand=True)
    canvases["logo"].create_image(0, 0, image=kuva, anchor='nw')
    # Create label for the game "name"
    labels["title_text"] = tkinter.Label(frames["title_frame"], text="TicTacToe Project")
    labels["title_text"].pack(side=tkinter.BOTTOM)

    tkinter.mainloop()


if __name__ == "__main__":
    main()
