#!/usr/bin/python3
""" 
*********************
!THIS IS A DOCSTRING!
*********************


SESRUC V0.3
-----------

BLOAT WARE
lsma

Sesruc is a platformer/adventure game written entirely in python.
It is being written on a Raspberry Pi using Nano as an editor.

So, my PC died, therefore I am forced to use an old (by now) model B 
Raspberry Pi v1, which, needless to say, is a bit slow graphics-wise.  How 
do you write a game without graphics?  You write a game with text.  Sesruc 
was born.

Some tips fore gameplay:
 - Don't hold keys down
 - Don't try to jump onto enemies
 - Dont fall too far (splat)
"""
# Import everything
import curses, random, time, pickle, os, os.path
from os.path import join  # I'm going to need this later


#  This is the closest thing I have to 'settings'
CHEATER = True # Use cheater keys?
starting_lives = 10 # How many lives does a new player start with?
WIDTH = 60     # Self explanatory
HEIGHT = 20    # Ditto

def wrap(t, w):
    """ 
    I spent hours searching through python modules for a function that would wrap
    text.  Then decided it would just be easier to write my own.
    """
    all = ""  # I'm not going to comment of this function
    cur = ""  # Figure it out your self, it's simple
    cnt = 0
    end = False
    for c in t:
        cur += c
        cnt += 1
        if cnt == w:
            end = True
        if end and c in (' ','\t'):
            all += cur+'\n'
            cur = ""
            cnt = 0
            end = False
    all += cur
    return all
    
# This is where the user's games and the levels are stored
user_file = os.path.expanduser("~/.platformer") 


# Make the user directory of there isn't one already
if not os.path.isdir(user_file):
    os.mkdir(user_file)
    print("\t\t\tHad to make game directory") # Let 'em know

# 
# Get the levels loaded/set up
#
if os.path.isfile(join(user_file, "levels")): # Check to see if it's there

    stream = open(join(user_file, "levels"), "rb") # open it
    game_data = pickle.load(stream) # load it
    stream.close() # close it
    del stream # not sure I actually need this
    
    # Here i extract some data so I can access it easier (maps[y][x] vs game_data["maps"][y][x]
    maps = game_data["maps"]
    g_tile = game_data["ground"]
    p_tile = game_data["point"]

else:
    # Uh-O!!
    print("Could not find level files.") # Alert the user to the problem
    print("Most likely, you have been a complete moron and deleted the map data.")

#
# Set up the users
#
games = {}  # This dict will hold all the users (or 'games') and their stats
tutorial = False # this allows the game to be more instructive at first
# Check to see if there is a games file, and load it if there is
if os.path.isfile(join(user_file, "games")):
    # This is pretty straight forward
    stream = open(join(user_file, "games"), "rb")
    games = pickle.load(stream)
    stream.close()
    del stream

else: # otherwise set tutorial to true (ie. he has never played before)
    tutorial = True
    

class Bullet:
    """Basic class for holding the data of one bullet
    would use dict but am lazy"""
    def __init__(self, x, y, dx):
        """Bullet(x, y, direction/speed) -> Bullet object"""
        self.x = x+dx
        self.y = y
        self.dx = dx

class Unit:
    """Holds all the info for one unit
    would use dict but someday might regret"""
    def __init__(self, data):
        self.tile,  pos,  self.side,  self.ai,  self.name,  self.val = data
        self.x = int(pos[0])
        self.y = int(pos[1])
        self.dir = random.choice((1,-1))
        self.cntr = 0
        self.max_cntr = 1
        

def do_dialog(screen, d):
    """Just goes through a conversation, allowing
    the user to follow a story-line"""
    screen.nodelay(0) # We want a delay, thank you very much
    for d in d: # Go through every quote
        screen.clear() # Clear the screen
        
        # This part prints the speaker in shiny letters and parenthesis
        screen.addstr(1,1,"(")
        screen.addstr(1,2+len(d[0]),")")
        screen.addstr(1,2,d[0],curses.A_BOLD)
        
        screen.addstr(3, 1, wrap(d[1], WIDTH)) # print the actual words
        
        # Wait for a keypress
        ch = screen.getch()
        
        # s will skip, q will quit, anything else will continue
        if ch == ord('s'): break
        elif ch == ord('q'):
            screen.nodelay(1)
            return False # oop - the user want's to quit!
            
    screen.nodelay(1) # Go back to ne delay mode
    return True # The user didn.t press 'q'
    
# This is called bu curses.wrapper to start the game
def start_game(screen, game_name):
    """start_game(screen, game_name) -> fun"""
    # If it is the user's first game, will offer guidance
    if tutorial:
        # if there is a tutorial file, use it
        if os.path.isfile(join(user_file, "tutorial")):
            stream = open(join(user_file, "tutorial"), "rb")
            tu = pickle.load(stream)
            stream.close()
            del stream
        
        # Otherwise, use the hardcoded tutorial
        else:
            tu=["Use the right and left arrow keys to move.",
                "Use the up arrow keys to jump.",
                "Press 'q' to quit and save.",
                "The ground will be made up of 'G's.",
                "Units will be brighter",
                "Although jumping on top of an enemy unit will kill it, it is very hard to do this, so it is recomended you don't even try.",
                "You get points from moving over coin symbols, like o or O.",
                "Points are shown after a '+' at the top of the game.",
                "You will lose a life if you fall or jump a long way down or touch an enemy unit.",
                "Lives are displayed as ']'s at the top of the game.",
                "To complete a level, follow the instructions or just get to the right edge of the map.",
                "The level name and number are displayed in the top-right corner of the game.",
                "Before every level there will be some dialog.",
                "Pay attention, because it will instruct you further."]
        
        # This basically just asks the user if it wants a primer
        screen.nodelay(0)
        screen.clear()
        screen.addstr(0,0,"FIRST TIMER".center(WIDTH), curses.A_REVERSE)
        screen.addstr(2,0,"It looks like this is your first time,".center(WIDTH))
        screen.addstr(3,0,"would you like a primer?".center(WIDTH))
        screen.addstr(4,0,"(Y/N)".center(WIDTH))
        answ = screen.getch()
        
        # Yes, guide me oh lerned tutorial!
        if answ not in (ord('n'),ord('N')):
            
            answ = ""
            start = 0
            while answ != ord('c'):
                
                # Draw everything
                screen.clear()
                screen.addstr(0,0,"FIRST TIMER - PRIMER".center(WIDTH), curses.A_REVERSE)
                
                i = 2 # 'i' controls the scrolling mechanism
                for t in tu[start:]:
                    for l in wrap(t, WIDTH-10).splitlines():
                        if i < HEIGHT-3:
                            screen.addstr(i,0,l.center(WIDTH))
                            i += 1
                
                # If they're not at the bottom, ask them to scroll down
                if len(tu)-start > HEIGHT-11:
                    screen.addstr(HEIGHT-1,(WIDTH//2)-8," - PRESS ENTER - ", curses.A_REVERSE)
                
                # If they are at the bottom, tell them to continue
                else:
                    screen.addstr(HEIGHT-1,0," - Press 'c' to start! - ".center(WIDTH), curses.A_BOLD)
                
                # Blah, blah, blah, user input
                answ = screen.getch()
                if answ == ord('q'):
                    return
                if answ == 10 and start < len(tu) and len(tu)-start >= HEIGHT-10:
                    start += 1 # Scroll down
        
        # No, I will climb the cliffs of learning without assistance!
        elif answ == ord('q'):
            return

    # Setup curses info
    curses.noecho() # Dont display input
    screen.nodelay(1)# Set up getch() settings
    
    #
    # Initialize variables
    #
    game = games[game_name]  # stores information for the current game
    
    level = game[0] # level number    
    map = maps[level]["tiles"] # current map data
    map_name = maps[level]["name"] # name of the map
    start_pos = maps[level]["start_pos"] # where you start
    end_stage = maps[level]["end"] # how the game ends
    units = [Unit(u) for u in maps[level]["units"]] # load all the units into Unit objects
    point_map = maps[level]["points"] # Where are the points?
    heard_it = [] # This keeps track of dialog you have heard, so you don't have to hear it over and over
    # note on 'heard_it'
    #  This really is here to block the situation, where when you trigger a 
    #  dialog, it keeps retriggering, because there is no time to move of 
    #  the trigger.  TO DO: make a better system for fixing this.
    
    new_level = True # Set to true -> advance to the next stage
    # Initialy set to true so the user gets the starting dialog of the 
    # level he is jumping back into.
    level -= 1 # When new level is true, this var is also incremented. see above
        
    redraw = True # Set to true will redraw the screen
    
    pause = False # true to pause game
    
    you_X, you_Y = start_pos # your actual x and y
    you_dir = 1		# which direction your facing (for bullets)
    you_gun = False	# Do you have a gun??
    last_X = you_X	#
    last_Y = you_Y	# where you were last
    new_X = you_X	#
    new_Y = you_Y	# where you might be able to be next
    
    score = game[1] # Game score
    new_score = False # When set to True, will flash points
    new_life = False  # When set to True, will flash lives
    falling = 0     # Keeps tract how far you fall
    lives = game[2] # lives
    hurt = False    # this variable controld the character flashing if it has lost a life
    died = False	# Will return you to start of level on True
    
    message = str(game) # Message to print
    wait_a_bit = 0      # Game will pause this many seconds
    
    last_key = False # what was the last key pressed?
    
    bullets = [] # all bullets currently vissible
    reload = 0   # character gun reload counter
    jumping = None  # is the character jumping (None when not, and posative integer when is)
    flying = False  # Are you flying?? ie. gravity no longer effects you
    
        
    game_loop = True # is the game running?
    while game_loop == True:
        if new_level:
            # Advance to the next map
            level += 1
            if level >= len(maps): # Goes back to level 0 at the end
            	level = 0
            	
            # This part gets all the data for the new stage
            #  see above for specifics for each var
            map = maps[level]["tiles"]
            map_name = maps[level]["name"] 
            start_pos = maps[level]["start_pos"]
            end_stage = maps[level]["end"]
            units = [Unit(u) for u in maps[level]["units"]]
            point_map = maps[level]["points"]
            heard_it = []
            
            # Reset you variables
            you_X,you_Y = start_pos
            jumping = None
            
            # Show dialog, but exit if the user pressed q
            if not do_dialog(screen, maps[level]["dialog"]["start"]):
                game_loop = "save"
            
            # Reset neew_level
            new_level = False
            # Redraw the screen
            redraw=True
            # Cancel any waits about to go into effect
            wait_a_bit = 0
        
        #
        # Waiting Stuff
        #
        
        # This bit is pretty straight forward
        while pause:
            screen.addstr(HEIGHT//2, 0, "PAUSED".center(WIDTH))
            screen.nodelay(0)
            ch = screen.getch()
            if ch == ord('p'):
                pause = False
            if ch == ord('q'):
                game_loop = "save"
            screen.nodelay(1) # return to no delay mode
            redraw = True # Make sure to redraw the screen (to cover up "PAUSED")
        
        # This part waits for a specified amount of time
        #  Used to allow the user to notice important messages
        if wait_a_bit > 0:
            screen.noutrefresh()
            curses.doupdate()
            time.sleep(wait_a_bit)
            wait_a_bit = 0
            curses.flushinp()
            redraw = True


                
        #
        # Reset all the variables
        #
        last_X = you_X
        last_Y = you_Y
        new_X = you_X
        new_Y = you_Y
        
        #
        # Update the bullets
        #
        if you_gun:
            for bullet in bullets:
                # Move it:
                bullet.x += bullet.dx
                
                # Did it hit an enemy?
                for u in units:
                    if u.side == 0 and int(u.x) == int(bullet.x) and int(u.y)==int(bullet.y):
                        bullets.remove(bullet)
                        units.remove(u)
                
                # Make sure to redraw if the bullet is in the viewing ares
                if abs(you_X-int(bullet.x)) < WIDTH//2 and abs(you_Y-int(bullet.y)) < HEIGHT//2:
                    redraw = True
                
                # And destroy is if it has hit something, or leaft the map
                if not 0 < int(bullet.x) < len(map[0])-1 or not 0 <= int(bullet.y) < len(map) or map[int(bullet.y)][int(bullet.x)] in g_tile:
                    bullets.remove(bullet)

        
        #
        # Update Units
        #
        for u in units:
            # initialize vars
            ny = u.y
            nx = u.x
            
            # On u.cntr:
            #   This is a simple counter which will limit how fast the unit 
            #   can move.  Specifically, it disallows the unit to make a 
            #   move while the counter is non-zero.
            if u.cntr == 0:
            
                if u.ai == 1:    # AI1: pase AI, will pase back and forth
                    nx += u.dir
                u.cntr = u.max_cntr # reset the counter
            else:
                u.cntr -= 1 # move closer to making a move
              
            # Unit gravity
            if ny < len(map)-2 and map[ny+1][int(nx)] not in g_tile:
                ny += 1
            
            # Evaluate new moves, and make changes
            if 0 <= abs(int(nx)) < len(map[0]) and 0 <= ny < len(map):
            
                # If we haven't run into a wall
                if map[ny][int(nx)] not in g_tile:
                
                    # Redraw if we are in the viewing area
                    if (int(u.x) != int(nx) or u.y != ny) and abs(you_X-int(nx)) < WIDTH//2 and abs(you_Y-ny) < HEIGHT//2:
                        redraw = True
                        
                    # The player and the unit are in the same tile!
                    if u.x == you_X and u.y == you_Y: 
                    
                        # If it's an enemy
                        if u.side == 0:
                            
                            # And the user was stupid
                            if falling == 0:
                                # He dies
                                lives -= 1
                                message = "Hit by a "+u.name
                                redraw = False
                                wait_a_bit = 3
                                died = True
                            
                            # What's this? He was jumping!!
                            else:
                                # Enemy is destroyed
                                units.remove(u)
                                score += u.val
                                message = "Killed a "+u.name
                                redraw = True
                        
                        # It's a freind, time for boring dialog
                        elif u.side == 1:
                            if u.name in maps[level]["dialog"] and u.name not in heard_it:
                                do_dialog(screen, maps[level]["dialog"][u.name])
                                redraw = True
                                heard_it.append(u.name)
                    
                    # This bit keeps pasers from falling off cliffs
                    if u.ai == 1 and map[ny+1][int(nx)] not in g_tile:
                        u.dir = -u.dir
                    else:
                        # apply movement
                        u.x = nx
                        u.y = ny
                
                # We hit a wall!
                else:
                    # Turn around
                    if u.ai == 1:
                        u.dir = -u.dir
            
            
                    
                
        #
        # gravity mechanism
        #
        if you_Y < len(map)-1 and map[you_Y+1][you_X] not in g_tile and not flying:
            new_Y += 1   # Down you go
            falling += 1 # keep tract of how far you fall
            
        else:
            # If you far too fall, deduct a life
            if falling > 8:
                lives -= 1
                hurt = 1
                redraw = True
            # In any case, reset the fall counter
            falling = 0
        
        # 
        # User input
        #
        ch = screen.getch()
        curses.flushinp()
        if ch:
            # Quit when a 'q' is pressed
            if ch == ord('q'):
                game_loop = "save"
                return
            
            #
            # CHEATER stuff
            #
            elif ch == ord('a') and CHEATER: # advance to the next level
                new_level = True
            
            elif ch == ord('g') and CHEATER: # get a gun
                you_gun = not you_gun
            
            elif ch == ord('f') and CHEATER: # fly
                flying = not flying
            
            elif ch == ord('l') and CHEATER: # get a life, really, why are you reading this?
                lives += 1
            
            # Movement left and right, pretty straight forard
            elif ch == curses.KEY_LEFT:
                new_X = you_X - 1
                you_dir = -1
            elif ch == curses.KEY_RIGHT:
                new_X = you_X + 1
                you_dir = 1
            
            # Jump
            #  The jumping mechanism is too confusing, therefore I will 
            #  make no comment about it.
            elif ch == curses.KEY_UP:
                if map[you_Y+1][you_X] in g_tile:
                    jumping = 0
                
            
            # Not really sure why I have this  
            #  Someday, it will come in usefull. I know.
            elif ch == curses.KEY_DOWN:
                new_Y = you_Y + 1
                
                
            # fire gun
            elif you_gun and ch == ord(' ') and not reload:
                # make a bullet
                bullets.append(Bullet(float(you_X), float(you_Y), float(you_dir)*((random.random()//2)+1.25)))
                # reload
                reload = 11
            
            # pause the game
            elif ch == ord('p'):
                pause = True
            
            time.sleep(0.04) # we don't want the game to be too fast!
  
  
        #
        # Jumping mechanism
        #
        if jumping != None: # if we are jumping:
            if jumping > 3: # and we have reached the peak of our jump
                jumping = None # stop jumping, and let gravity do its job
            else: 	# Otherwise
                new_Y = you_Y - 1 # move up
                jumping += 1	# and add one to the jump counter
                
        #
        # Movement logic
        #
        # if the place we are moving to is...
        #  /-----------------inside the map-----------------\
        # 					and..		  /----it's open space----\
        if 0 <= new_X < len(map[0])-1 and 0 <= new_Y < len(map)-1 and map[new_Y][new_X] not in g_tile:
            # Make it where we are
            you_X = new_X
            you_Y = new_Y
            
            # If end_stage is the tile we are on, we finish the level
            if map[you_Y][you_X] == end_stage:
                message = "You have reached your goal!"
                redraw = True
                wait_a_bit = 2
                new_level = True
            
            # Are we able to pick up and thingys?
            for p in point_map:
                if p[0] == you_X and p[1] == you_Y:
                    point_map.remove(p)
                    
                    if p_tile[p[2]] > 0:	# It's a point
                        score += p_tile[p[2]]
                        new_score = True
                        
                    elif p_tile[p[2]] == -1:	# It's a life
                        lives += 1
                        new_life = True
                        
                    elif p_tile[p[2]] == -2:	# It's a bun, err, gun
                        you_gun = True
                        message = "You have picked up a gun"
                    break
                     
            
        # So it's not in the map and a legal space, therefore:
        # If it's the right edge of the map, and end_stage is None or 'edge':
        elif new_X == len(map[0])-1 and end_stage in (None, 'edge'):
            # We pass the level
            message = "You have reached your goal!"
            redraw = True
            wait_a_bit = 2
            new_level = True
        
        # If we are below the map
        elif new_Y == len(map)-1:
            # We die
            lives -= 1
            message = "You have fallen into a pit!"
            wait_a_bit = 2
            died = True
        
        
        # If you died:
        if died:
            died = False
            # Go back to the start
            new_X,new_Y = start_pos
            you_X,you_Y = start_pos
            redraw = False # and don't redraw
        #
        #  Redraw
        #
        #    If we have moved
        if last_X != you_X or last_Y != you_Y or redraw:
            redraw = False # reset redraw
            screen.clear() # clear the screen
            
            # These are the positions of the viewing space
            sx = max(0,you_X-(WIDTH//2))		# left
            ex = min(len(map[0]),you_X+(WIDTH//2))	# right
            sy = max(0,you_Y-(HEIGHT//2))		# top
            ey = min(len(map), you_Y+(HEIGHT//2))	# bottom
            
            
            # Draw the map
            i = 1
            for row in map[sy:ey]: # only get the rows in the viewing space
                screen.addstr(i, 0, row[sx:ex])
                i += 1
            
            # Draw the points/lives
            for p in point_map:
                if sx < p[0] < ex and sy < p[1] < ey:
                    screen.addstr((p[1]+1)-sy,p[0]-sx,p[2])
                
            # Draw units
            for u in units:
                if sx < int(u.x) < ex and sy < int(u.y) < ey:
                    screen.addstr((u.y+1)-sy,int(u.x)-sx,u.tile,curses.A_BOLD)
            
            # Draw you, (highlighted if you have just lost a life)
            if hurt:
                screen.addstr((you_Y+1)-sy, you_X-sx, "@", curses.A_REVERSE)
                screen.addstr(HEIGHT+2, 0, " * OUCH! * ", curses.A_REVERSE)
                hurt -= 1 # reset the hurt counter (not just true or false so we can keep it for a few frames)
            else:
            	screen.addstr((you_Y+1)-sy, you_X-sx, "@", curses.A_BOLD)
            
            # Draw bullets
            for bullet in bullets:
                if sx < int(bullet.x) < ex and sy < int(bullet.y) < ey:
                    # Draw it:
                    screen.addstr((int(bullet.y)+1)-sy, int(bullet.x)-sx, "-")


            # Draw the info
            screen.addstr(0, 0, "SESRUC")
            
            # Points
            if new_score: # flash if you gained points
                screen.addstr(0, 8, "+"+str(score), curses.A_REVERSE)
                new_score = False
            else:
                screen.addstr(0, 8, "+"+str(score))
            
            
            # Lives
            if new_life: # flash if you got a new life
                for i in range(lives): screen.addstr(0, 14+i, "]", curses.A_REVERSE)
                new_life = False
            else:
                for i in range(lives): screen.addstr(0, 14+i, "]")
                
            # Level name and number
            screen.addstr(0, WIDTH-10-len(map_name), "Level "+str(level+1)+": "+map_name)
        
        
        # Print the message, if any
        if message != None:
            screen.addstr(HEIGHT+2, 0, str(message))
            message = None
            
        
        # Draw your reloading status
        if you_gun:
            if reload:
                reload -= 1
                screen.addstr(0,25,"RELOADING")
            else:
                screen.addstr(0,25,"READY    ")
        
        # Here is where you lose
        if lives < 0:
            game_loop = "died"
            del games[game_name]
            stream = open(join(user_file, "games"), "wb")
            pickle.dump(games, stream)
            stream.close()

    # User died fair and square
    if game_loop == "died":
        #
        # FaNcY GaMe OvEr SiGn
        #
        x = 0
        m = 0
        while True:
            curses.flushinp()
            screen.clear()
            if x == 0:
                screen.addstr((HEIGHT//2)+1, (WIDTH//2)-5, "GAME OVER!")
            elif x == 1:
                screen.addstr((HEIGHT//2)+1, (WIDTH//2)-5, "GAME OVER!", curses.A_BOLD)
            elif x == 2:
                screen.addstr((HEIGHT//2)+1, (WIDTH//2)-5, "GAME OVER!", curses.A_REVERSE)
                x = -1
            x += 1
            m += 1
            if m > 10: screen.addstr((HEIGHT//2)+2, (WIDTH//2)-7, "press any key")
            if screen.getch() != -1 and m > 10: break
            time.sleep(0.2)
    
    # User quit (save)   
    elif game_loop == "save":
        # Restore the user info
        games[game_name] = [level, score, lives]
        
        # And save it
        stream = open(join(user_file, "games"), "wb")
        pickle.dump(games, stream)
        stream.close()
        
def main_menu(screen):
    """main_menu(screen) -> a main menu"""
    # Set up a new user at once if this is the first run
    if tutorial:
        screen.addstr(0,0,"WELCOME TO SESRUC!".center(WIDTH), curses.A_REVERSE)
        screen.addstr(2,0,"What is your name?".center(WIDTH))
        
        name = ""
        input_x = (WIDTH//2)
        ch = screen.getch()
        while ch != 10:
            if 97 <= ch <= 122:
                name += chr(ch)
            elif ch == curses.KEY_BACKSPACE and len(name):
                name = name[:-1]
                
            screen.addstr(3, 0, str(name).center(WIDTH))
           
            ch = screen.getch()
            if ch == 10 and name == "": ch = 0
                    
        
        #		 level  score  lives
        games[name] =  [ 0,     0,     starting_lives]
        stream = open(join(user_file, "games"), "wb")
        pickle.dump(games, stream)
        stream.close()
        del stream
        
        start_game(screen, name)
        

    selected = 0
    while True:
        items = ["Continue Game", "New Game", "Credits", "Exit"] # Items on the menu
        if len(games) == 0: items.remove("Continue Game") # oop - there is no game to continue
        
        # Setup curses settings
        screen.clear()
        curses.noecho()
        screen.nodelay(0)
        
        # Draw it all
        screen.addstr(0,0,"SESRUC V0.3".center(WIDTH), curses.A_REVERSE)
        i = 2
        for item in items:
            x = int((float(WIDTH)/2.0)-(float(len(item))/2.0))
            screen.addstr(i,x,item)
            if selected == i-2:
                screen.addstr(i,x,item,curses.A_REVERSE)
            i += 1
        
        # Get user input
        ch = screen.getch()
        
        # Move the selection up and down
        if ch == curses.KEY_UP and selected > 0: selected -= 1
        elif ch == curses.KEY_DOWN and selected < len(items)-1: selected += 1
        
        # The user selected something
        elif ch == 10:
            # Continue Game
            #  Display the list of games and ask the user to select one to 
            #  continue.  Thougoughly dumby-proof.
            if items[selected] == "Continue Game" and len(games):
                screen.clear()
                curses.echo()
                screen.addstr(0,0,"WHO ARE YOU".center(WIDTH), curses.A_REVERSE)
                
                max_len = 0
                users = []
                for u in games.keys():
                    users.append(u)
                    if len(u) > max_len: max_len = len(u)
                users.sort()
                
                i = 1
                for u in users:
                    screen.addstr(i, 0, u.center(WIDTH))
                    i += 1
                 
                input_x = (WIDTH//2)-(max_len//2)
                text = str(screen.getstr(i, input_x, max_len+1))[2:-1]
                while text.strip('\n') not in users:
                    if len(text.strip('\n')) == 0: break
                    test = str(screen.getstr(i, input_x, max_len+1))[2:-1]
                
                if text.strip('\n') in users: start_game(screen, text)
                
            # New Game
            #  Ask for a new name for the game, make the new game, and then 
            #  start the game with the new game name.
            elif items[selected] == "New Game":
                screen.clear()
                screen.addstr(0,0,"WHAT IS YOUR NAME".center(WIDTH), curses.A_REVERSE)
                
                users = []
                for u in games.keys():
                    users.append(u)

                text = ""
                input_x = (WIDTH//2)
                ch = screen.getch()
                while ch != 10:
                    if 97 <= ch <= 122:
                        text += chr(ch)
                    elif ch == curses.KEY_BACKSPACE and len(text):
                        text = text[:-1]
                        
                    screen.addstr(1, 0, str(text).center(WIDTH))
                    
                    ch = screen.getch()
                    
                if text:
                    if text in users:
                        screen.addstr(0,0,"THAT USER ALREADY EXISTS".center(WIDTH), curses.A_REVERSE)
                        screen.addstr(1,0,"Should I replace them?".center(WIDTH))
                        
                        ch = screen.getch()
                        while ch not in (ord('y'), ord('n')):
                            ch = screen.getch()
                            
                        if ch == ord('y'):
                            games[text] = [0,0,starting_lives]
                            
                            start_game(screen, text)
                    else:
                        games[text] = [0,0,starting_lives]
                        
                        start_game(screen, text)
            
            # The best part
            elif items[selected] == "Credits":
                screen.clear()
                
                
                credits = ["Ballads of Sesruc","V0.3","","---","","Game Design", "Stan Asjes", "", "---","","Level Design", "Stan Asjes", "","---","" ,"Programming", "Stan Asjes","","---","","Special Thanks","Whoever wrote python curses", "", "---","","Written entirely using nano", "in python on a raspberry pi", "", "- --- -", "", ""]
                logo = ["  ____     __     ____       ___  ___________  ",
                	" |  __ \  | |    /  _ \     /   \|____   ____| ",
                	" | |  | | | |   |  / | |   / /^\ \    | |      ",
                	" | |__| | | |   | |  | |  / |___| \   | |      ",
                	" |  __  | | |   | |  | | |   ___   |  | |      ",
                	" | |  | | | |   | |  | | |  /   \  |  | |      ",
                	" | |__| | |  \__| |_ / | | |     | |  | |      ",
                	" \_____/   \_____\____/  |_|     |_|  |_|      ",
                	"  _    _    _      ___      _____    _______   ",
                	" | |  | |  | |    /   \    |  __  \ |  _____|  ",
                	" | |  | |  | |   / /^\ \   | |  \ | | |        ",
                	" | |  | |  | |  / /___\ \  | |__| | |  \____   ",
                	" | |  | |  | | |  _____  | |    _/  |  _____|  ",
                	" |  | | | |  | | |     | | | |\ \   | |        ",
                	"  |  \| |/  |  | |     | | | | \ \  |  \____   ",
                	"   \_______/   |_|     |_| |_|  \_\ |_______|  ",
                	"                                               "]
                
                y = HEIGHT
                while y >= -len(credits)+1:
                    screen.addstr(0,0,"CREDITS".center(WIDTH), curses.A_REVERSE)
                    i = 1
                    
                    for cr in credits:
                        if y+i > 0 and y+i < HEIGHT+1:
                            screen.addstr(y+i, 0, cr.center(WIDTH))
                        
                        i += 1
                        
                    for cr in logo:
                        if y+i > 0 and y+i < HEIGHT+1:
                            screen.addstr(y+i, (WIDTH//2)-(len(cr)//2), cr, curses.A_REVERSE)
                        
                        i += 1
                    
                    screen.noutrefresh()
                    curses.doupdate()
                    time.sleep(0.2)
                    screen.clear()
                    y -= 1
                
                i = 2
                for l in logo:
                    screen.addstr(i, (WIDTH//2)-(len(l)//2), l, curses.A_REVERSE)
                    i += 1
                    
                screen.addstr(0,0,"CREDITS".center(WIDTH), curses.A_REVERSE)
                
                screen.noutrefresh()
                curses.doupdate()
                time.sleep(6)
            
            # END IT ALL
            elif items[selected] == "Exit":
                return
curses.wrapper(main_menu)

# In loving memory of Primula Q. Flugellmire.
#
