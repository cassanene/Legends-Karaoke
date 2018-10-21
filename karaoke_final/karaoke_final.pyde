add_library('minim')

from ddf.minim import Minim

def setup():
    size(1000, 512)
    global lineDisplayed
    global songStart
    global img
    lineDisplayed = 0
    back_img = loadImage("background.png")
    background(0)
    image(back_img, 0, 0, 1000, 512)
    global timeElapsed
    timeElapsed = 0
    global y_position
    global whit_img
    global MJ_img
    global bey_img
    global font
    global selectMode
    global lyrics
    global lyricTimes
    lyrics = WH_LYRICS
    lyricTimes = WH_LYRIC_TIMES
    selectMode = True
    y_position = 200
    whit_img = loadImage("Whitney.jpg")
    MJ_img = loadImage("MJ.png")
    bey_img = loadImage("BEY.jpg")

    
    minim = Minim(this)
    global whit_song
    global MJ_song
    global B_song
    whit_song = minim.loadFile ("IWillAlwaysLoveYou.mp3")
    MJ_song = minim.loadFile ("MJ.mp3")
    B_song = minim.loadFile ("Beyoncw.mp3")

def draw():
    global img
    global lineDisplayed
    global songStart
    global timeElapsed
    global i
    global line_num
    global num_letters
    global selectMode
    global lyrics
    global lyricTimes

    # SONG SELECT MODE
    if (selectMode):
        global y_position
        global whit_img
        global MJ_img
        global bey_img
        global font
        global back_img
        
        textSize(60)
        text("LEGENDS", 100, 70)
        
        textSize(55)
        text("Karaoke", 200, 120)
        
        image(whit_img, 100, 170, 100, 100)
        
        image(MJ_img, 100, 290, 100, 100)
        
        image(bey_img, 100, 410, 100, 100)
        
        textSize(25)
        text("SING WHITNEY", 250, 200)
        
        textSize(25)
        text("SING MICHAEL", 250, 330)
        
        textSize(25)
        text("SING BEYONCE", 250, 440)
        if mousePressed:
            selectMode = False
            if mouseY >= 170 and mouseY <= 270:
                lyrics = WH_LYRICS
                lyricTimes = WH_LYRIC_TIMES
                whit_song.play()
            elif mouseY >= 290 and mouseY <= 390:
                lyrics = MJ_LYRICS
                lyricTimes = MJ_LYRIC_TIMES
                MJ_song.play()
            elif mouseY >= 410 and mouseY <= 510:
                lyrics = B_LYRICS
                lyricTimes = B_LYRIC_TIMES
                B_song.play()
            songStart = millis()   
                    
    else:
        # SONG MODE
        back_img = loadImage("background.png")
        image(back_img, 0, 0, 1000, 512)
    
        # Progress Bar
        fill(random(0,255), random(0,255), random(0,255))
        rect(0, 10, 700, 10)    
        if timeElapsed < 207000:
            fill(255, 255, 255)
            rect(timeElapsed, 10, 1920, 10)
            timeElapsed += .05
        
        # Song Timing Stuff
        fill(255)
        currentTime = millis()
        text(currentTime / 1000, 950, 450)
        songElapsed = currentTime - songStart
    
    
        # Highlight Timing Stuff
        textSize(30)
        T = ((lyricTimes[lineDisplayed +1]) - (lyricTimes[lineDisplayed]))
        lyricsOnScreen = lyrics[lineDisplayed]
        percent = (((songElapsed) - (lyricTimes[lineDisplayed]))/float(T))
    
        # Draw Lyrics
        text(lyricsOnScreen, 100, 200)
        length = len(lyricsOnScreen)
        drawRedlyrics(lyricsOnScreen[0: int(length * percent)])
    
        # Advance Line
        if lineDisplayed < len(lyricTimes) - 1:
            if songElapsed > lyricTimes[lineDisplayed + 1]:
                lineDisplayed = lineDisplayed + 1
            
def drawRedlyrics(lyrics):
    fill(0, 255, 255)
    stroke(204, 102, 0)
    text(lyrics, 100, 200)

MJ_LYRIC_TIMES = [
0,
# gutair solo
25000,
39000,
42500,
45500,
49000,
53000,
57000, #8
60000,
63000,
# hook - 1:06
67000, 
70000,
73000,#
77000,
80000,#
# verse 2
87000,
90000,#
94000,#
97000,#
100000,#
104000,#
110000,#
109000,
#hook 2 - 1:54
113500,
117000,
120000,
123500,#
127000,
131000,
134500,
138000,
141000,
142000,
156000,
197000, 
200000,
203000,
207000    
]

MJ_LYRICS = [
"Beat It - Michael Jackson",
"[GUITAR SOLO]",
"They told him, don't you ever come around here",
"Don't wanna see your face, you better disappear",
"The fire's in their eyes and their words are really clear",
"So beat it, just beat it",
"You better run, you better do what you can",
"Don't wanna see no blood, don't be a macho man",
"You wanna be tough, better do what you can",
"So beat it, but you wanna be bad",
# [Hook]
"Just beat it, beat it, beat it, beat it",
"No one wants to be defeated",
"Showin' how funky and strong is your fight",
"It doesn't matter who's wrong or right",
"Just beat it (beat it)",

# [Verse 2]
"They're out to get you, better leave while you can",
"Don't wanna be a boy, you wanna be a man",
"You wanna stay alive, better do what you can",
"So beat it, just beat it",
"You have to show them that you're really not scared",    
"You're playin' with your life, this ain't no truth or dare",
"They'll kick you, then they'll beat you then they'll tell you it's fair",
"So beat it, but you wanna be bad",

# [Hook]
"Just beat it, beat it, beat it, beat it",
"No one wants to be defeated",
"Showin' how funky and strong is your fight",
"It doesn't matter who's wrong or right",
"Just beat it, beat it, beat it, beat it",
"No one wants to be defeated",
"Showin' how funky and strong is your fight",
"It doesn't matter who's wrong or right",
"Just beat it (beat it)",
"Beat it (beat it)",

"[GUITAR SOLO]",

# [Hook]
"Beat it, beat it, beat it, beat it",
"No one wants to be defeated",
"Showin' how funky and strong is your fight",
"It doesn't matter who's wrong or right",
]

B_LYRIC_TIMES = [
    0, #1
    20000, #2
    22000, #3
    24000, #4
    27000, #5
    30000, #6
    33000, #7
    35000, #8
    37000, #9
    39000, #10
    41000, #11
    44000, #12     
    47000, #13
    51000, #14
    54000, #15
    57000, #16
    60000, #17
    63000, #18
    65000, #19
    68000, #20
    71000, #21
    72600, #22
    75000, #23
    78000, #24
    80000, #25
    83000, #26
    86000, #27
    88000, #28
    91000, #29
    93000, #30
    95000, #31
    97000, #32
    100000, #33
    102000, #34
    104000, #35
    106000, #36
    109000, #37
    114000, #38
    117000, #39
    119000, #40
    122000, #41
    125000, #42
    128000, #43
    131000, #44
    133000, #45
    136000, #46
    139000, #47
    142000, #48
    145000, #49
    148000, #50
    150000, #51
    153000, #52
    156000, #53
    159000, #54
    161000, #55
    163000, #56
    165000, #57
    168000, #58
    170000, #59
    172000, #60
    175000, #61
    177000, #62
    179000, #63
    182000, #64
    185000, #65
    188000, #66
    # 190000, #67
    # 192000, #68
    # 195000, #69
    # 198000, #70
    # 200000, #71
    # 202000, #72
    # 205000, #73
    # 208000, #74 
    # 210000, #75
    # 212000, #76
    # 215000, #77
    # 218000, #78
    # 220000, #79
    # 222000, #80
    # 224000, #81
    # 227000, #82
    # 230000, #83
    # 232000, #84
    # 236000, #85
    # 238000, #86
    # 240000, #87
    # 243000, #88
    # 246000, #89
    # 248000, #90
    # 250000, #91
    # 253000, #92
]

B_LYRICS = [
    "Bring the beat in", #1
    "Honey, Honey", #2
    "I can see the stars", #3
    "All the way from here", #4
    "Can't you see the glow", #5
    "On the Window Pane", #6
    "I can feel the sun", #7
    "Whenever you're near", #8
    "Every time you touch me", #9
    "I just melt away", #10
    "Now everybody ask me why", #11
    "I'm smiling out from ear to ear", #12
    "But I know, oh woah", #13
    "Nothing's perfect, but it's worth it", #14
    "After fighting through my tears", #15
    "And finally you put me first", #16
    "Baby it's you", #17
    "You're the one I love", #18
    "You're the one I need", #19
    "You're the only one I see", #20
    "Come on baby it's you", #21
    "You're the one that gives your all", #22
    "You're the one I can always call",  #23
    "When I need to make everything stop", #24
    "Finally, you put my love on top", #25
    "Ooh! come on baby", #26
    "You put my love on top", #27
    "Top, top, top, top", #28
    "You put my love on top", #29
    " (Ooh ooh)", #30
    "(Come on baby)", #31
    "You put my love on top top top top top", #32
    "My love on top", #33
    "Baby, baby", #34
    "I can hear the wind", #35
    "Whipping past my face", #36
    "As we dance the night away", #37
    "And boy your lips tastes", #38
    "Like a night of champagne", #39
    "As I kiss you again and again",  #40
    "And again and again", #41
    "Now everybody ask me why I'm smiling out from ear to ear", #42
    "But I know", #43
    "Nothing's perfect", #44
    "But it's worth it after fighting",  #45
    "Through my tears", #46
    "And finally you put me first", #47
    "Baby it's you", #48
    "You're the one I love", #49
    "You're the one I need", #50
    "You're the only one I see", #51 
    "Come on, baby it's you", #52
    "You're the one that gives your all", #53
    "You're the one I can always call", #54
    "When I need to make everything stop", #55
    "Finally, you put my love on top", #56
    "Ooh!  baby", #57
    "You put my love on top", #58
    "Top top top top", #59
    "You put my love on top", #60
    "Ooh ooh", #61
    "Come on baby", #62
    "You put my love on top", #63
    "Top top top top", #64
    "Put my love on top", #65
    "My love on top", #66
    # "Baby it's you", #67
    # "You're the one I love", #68
    # "You're the one I need", #69
    # "You're the only thing I see", #70
    # "Come on, baby it's you", #71
    # "You're the one that gives your all", #72
    # "You're the one that always calls", #73
    # "When I need you baby", #74
    # "Everything stops", #75
    # "Finally, you put my love on top", #76
    # "Baby, you're the one that I love", #77
    # "Baby you're all I need", #78
    # "You're the only one I see", #79
    # "Come on, baby it's you", #80
    # "You're the one that", #81
    # "Gives your all", #82
    # "You're the one I always calls", #83
    # "When I need you everything stops", #84
    # "Finally you put my love on top", #85
    # "Baby ‘cause you're the one",  #86
    # "That I love", #87
    # "Baby you're the one that I need", #88
    # "You're the only man I see", #89
    # "Baby baby it's you", #90
    # "You're the one that", #91
    # "Gives your all", #92
    # "You're the one that always calls", #93
    # "When I need you", #94
    # "Everything stops", #95
    # "Finally, you put my love on top", #96
    # "Baby 'cause you're the one", #97
    # "That I love", #98
    # "Baby you're the one that I need", #99
    # "You're the only one I see", #100
    # "Baby baby it's you", #101
    # "You're the one that", #102
    # "Gives your all", #103
    # "You're the one that always calls", #104
    # "When I need you", #105
    # "Everything stops", #106
    # "Finally you put my love on top" #107
]            
    

WH_LYRIC_TIMES = [
    0, #1
    10000, #2
    20000, #3
    27500, #4
    42000, #5
    56300, #6
    66300, #7
    76300, #8
    83000, #9
    91000, #10
    98000, #11
    104500, #12
    118300, #13
    126500, #14
    156000, #15
    163300, #16
    168700, #17
    175700, #18
    187700, #19
    198000, #20
    205000, #21
    212000, #22
    221000, #23
    228000, #24
    242700, #25
    250000, #26
]

WH_LYRICS = [
    "If I should stay", #1
    "I would only be in your way", #2
    "So I'll go, but I know", #3
    "I'll think of you every step of the way", #4
    "And I will always love you", #5
    "I will always love you", #6
    "You, my darling you. Hmm", #7
    "Bittersweet memories", #8
    "that is all I'm taking with me", #9
    "So, goodbye. Please, don't cry", #10
    "We both know I'm not what you, you need", #11
    "And I will always love you", #12
    "I will always love you", #13
    "(Instrumental solo)", #14
    "I hope life treats you kind", #15
    "And I hope you have all you've dreamed of", #16
    "And I wish to you, joy and happiness", #17
    "But above all this, I wish you love", #18
    "And I will always love you", #19
    "I will always love you", #20
    "  I will always love you", #21
    "I will always love you", #22
    "  I will always love you", #23
    "I, I will always love you", #24
    "You, darling, I love you", #25
    "Ooh, I'll always, I'll always love you" #26
]
