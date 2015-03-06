""" 
This file will make and pickle all the game data for Sesruc.
I use it to update the game data.  Currently, it isn't finished.
lsma

This is an extended ASCII character chart:
32:  	33: !	34: "	35: #	36: $	37: %	38: &	39: '	40: (	41: )	
42: *	43: +	44: ,	45: -	46: .	47: /	48: 0	49: 1	50: 2	51: 3	
52: 4	53: 5	54: 6	55: 7	56: 8	57: 9	58: :	59: ;	60: <	61: =	
62: >	63: ?	64: @	65: A	66: B	67: C	68: D	69: E	70: F	71: G	
72: H	73: I	74: J	75: K	76: L	77: M	78: N	79: O	80: P	81: Q	
82: R	83: S	84: T	85: U	86: V	87: W	88: X	89: Y	90: Z	91: [	
92: \	93: ]	94: ^	95: _	96: `	97: a	98: b	99: c	100: d	101: e	
102: f	103: g	104: h	105: i	106: j	107: k	108: l	109: m	110: n	111: o	
112: p	113: q	114: r	115: s	116: t	117: u	118: v	119: w	120: x	121: y	
122: z	123: {	124: |	125: }	126: ~	127: 	128: 	129: 	130: 	131: 	
132: 	133: 	134: 	135: 	136: 	137: 	138: 	139: 	140: 	141: 	
142: 	143: 	144: 	145: 	146: 	147: 	148: 	149: 	150: 	151: 	
152: 	153: 	154: 	155: 	156: 	157: 	158: 	159: 	160:  	161: ¡	
162: ¢	163: £	164: ¤	165: ¥	166: ¦	167: §	168: ¨	169: ©	170: ª	171: «	
172: ¬	173: ­	174: ®	175: ¯	176: °	177: ±	178: ²	179: ³	180: ´	181: µ	
182: ¶	183: ·	184: ¸	185: ¹	186: º	187: »	188: ¼	189: ½	190: ¾	191: ¿	
192: À	193: Á	194: Â	195: Ã	196: Ä	197: Å	198: Æ	199: Ç	200: È	201: É	
202: Ê	203: Ë	204: Ì	205: Í	206: Î	207: Ï	208: Ð	209: Ñ	210: Ò	211: Ó	
212: Ô	213: Õ	214: Ö	215: ×	216: Ø	217: Ù	218: Ú	219: Û	220: Ü	221: Ý	
222: Þ	223: ß	224: à	225: á	226: â	227: ã	228: ä	229: å	230: æ	231: ç	
232: è	233: é	234: ê	235: ë	236: ì	237: í	238: î	239: ï	240: ð	241: ñ	
242: ò	243: ó	244: ô	245: õ	246: ö	247: ÷	248: ø	249: ù	250: ú	251: û	
252: ü	253: ý	254: þ	
"""

data = {}
data["ground"] = ('G','^',"þ")
# point codes: > 0: that many points, -1: a life, -2: a gun, -3:sign, ...
data["point"] = {'o':100, 'O':250, '*':500, chr(164):1000, chr(216): -1, chr(187): -2, 'H': -3}
data["water"] = ('~',)

maps = []


new_map = {"name": "Quiet Field"}
dialog = [("Narrator", "You have left the quiet serenity of you home villiage, etadpuod, not knowing why you walk so far from home, following a gut instinct."),]
new_map["dialog"] = {"start": dialog}
new_map["start_pos"] = (0,11)
new_map ["end"] = '&'
new_map["tiles"] = ["                                                                                                                                                                                         ",
                    "                                                                                                                                                                                         ",
                    "                                                                                                                                                                                         ",
                    "                                                                                                                                                                                         ",
                    "                                                                                                                                                                                         ",
                    "                                                                                                                                                                                       & ",
                    "                                                                                                                                                                                     GGGG",
                    "                                                                                                                                                                                   GGGGGG",
                    "                                                                                                                                                                                 GGGGGGGG",
                    "                                                                                                                                                                               GGGGGGGGGG",
                    "            GGGGGGGGGGGGGGGGGGGG                                                                                  GGGGGGGGG                                                  GGGGGGGGGGGG",
                    "     GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG                              GGGGGGGGGGGGGGG                             GGGGGGGGGGGGGGGGGGGGG                                      GGGGGGGGGGGGGGGG",
                    "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG                    GGGGGGGGGGGGGGGGGGGGGGGGGGGGG             GGGGGGGGGGGGGGGGGGGGGGGGGG                              GGGGGGGGGGGGGGGGGGGGGG",
                    "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG              GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG     GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG           GGGGGGGG     GGGGGGGGGGGGGGGGGGGGGGGGGG",
                    "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG      GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG   GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG",
                    "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG",]
units = [('&', (183,5), 1, 0, "old man", 1000),]
new_map["units"] = units

points = []
new_map["points"] = points

maps.append(new_map)



new_map = {"name": "The Bridge"}
dialog = [("Narrator","You climb to the top of a mountain, and there, sitting on a thrown of hide is a wisened old man."),
          ("&","Welcome to the mountaintop, traveler.  I am the far-seer."),
          ("@","I am pleased to meet you. I don't know why I have strayed so far from the fields of my home, I felt pulled out toward the mountain."),
          ("&","Ah, I have seen many like you, called by the ever-fate out of the peacfull lands."),
          ("@","What does this all mean?"),
          ("&","Let me explain who I am, young one. I am the gate keeper to the lands beyond this mountain.  Every hundred years, or so, the ever-fate will call a mortal such as yourself into the undying lands, beyond, and it is my job to inform you of this, so you will be able to interpret your feelings."),
          ("@","Who is this 'ever-fate'? Is he, err, it a person?  What are the 'undying lands'? What --"),
          ("&","It is only my perogative to inform you of your status in his eyes, you must answer your own questions."),
          ("&","I will tell you one thing though, beware the yaledons (<)!")]
new_map["dialog"] = {"start": dialog}
new_map["end"] = None
new_map["start_pos"] = (0,3)
new_map["tiles"] = ["                                                                                                                                                                                                                ",
                    "                                                                                                                                                                                                                ",
                    "                                                                                                                                                                                                                ",
                    "                                                                                                                                                                                                                ",
                    "GGG                                                                                                                    GGGG                                                                                     ",
                    "GGGGG                                                                                                           GGG             GGGGGGG                                                                         ",
                    "GGGGGG                                                                                                                                                                                                          ",
                    "GGGGGGGG                         GGGGGGG                                                                                                 GGGGGGG                                                                ",
                    "GGGGGGGGG                                                                                                           GGGG    GGGGG                                                                               ",
                    "GGGGGGGGGGG          GGGGGGGGGG                                                                                                                                                                                 ",
                    "GGGGGGGGGGGGGG                        GGGGGGGG                                                                                       GGGGGGGG                                                                   ",
                    "GGGGGGGGGGGGGGGGG               GGGG                                                                                           GGG                                                                     GGGGGGGGG",
                    "GGGGGGGGGGGGGGGGGGGGG                                                                            G                  G         GG                                                        GGGGGGGGGGGGGGGGGGGGGGGG",
                    "GGGGGGGGGGGGGGGGGGGGGGGGGGG                                           GGGG                      GGGGGGGGGGGGGGGGGGGGGG                           GGGGGGGGGGGGGGGGGGGGGG           GGGGGGGGGGGGGGGGGGGGGGGGGGGGGG",
                    "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG                GGGGGGG           GGGGGGGG                  GG                    GG               GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG",
                    "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG~~~~~~~~~~~~~~~~~~~~~~GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG",]
                    
units = [('<', (40,14), 0, 1, "yaledon", 100),
         ('<', (60,14), 0, 1, "yaledon", 100),
         ('<', (80,14), 0, 1, "yaledon", 100),
         ('<', (100,12), 0, 1, "yaledon", 100),
         ('<', (110,12), 0, 1, "yaledon", 100),
         ('<', (130,14), 0, 1, "yaledon", 100),]
new_map["units"] = units

points = [(35,6,'o'),(36,6,'o'),(37,6,'o'),(38,6,'o'),(39,6,'o'),(41,9,'o'),(42,9,chr(216)),(43,9,chr(216)),(44,9,'o'),(113,4,'O'),(114,4,chr(216)),(115,4,'O'),(130,4,'o'),(131,4,'o'),(132,4,'o'),(133,4,'o'),(134,4,'o')]
new_map["points"] = points

maps.append(new_map)




new_map = {"name": "The Forest"}
dialog = [("Narrator","After crossing the bridge, you enter upon a heavily forested valley and continue down the road.  Little animals scurry away wherever you go.  You feel more pulled."),
          ("Tip","You can jump and walk on branches (^)"),]
new_map["dialog"] = {"start": dialog}
new_map["end"] = None
new_map["start_pos"] = (0,10)
new_map["tiles"] = ["                                                                                                                                                                                         ",
                    "                                                                                                                                                                                         ",
                    "                                                                                                                                                                                         ",
                    "                                                                                                                                                                                         ",
                    "                                                                                                                                                                                         ",
                    " ,.  .,   .,  , ,,,    .,  . .. . .   ,                                                                                             ^^^                                                  ",
                    ";::'#);;:(;{'.:,;)(  ::;#(.:;:#}::;)%%',. ,  . ..   . , .,.^^^^^^^, ,  ,, , ,             ,, .,  ..,,.  , ,.  .                                                                          ",
                    "%%:%%)%%({%%:;{%%}%%.%::%;)%%(%{%%::}';::'#);;:(;{'.:,;)(  ::;#(.:,);^^^^^^^^^ .,.,,...,.'(:,;)(  ::;#(.:,);:#}')  ,,. ,.. .^^^^^^,... ,. ^^^^^^. ,. ,. .., ,. .. ,, ,.,. .,., ,.        ",
                    "(:){':;;#(:;(:;::,:,.:{#::;);:.#}:;):;'(%%;::^^^^^^^^^^{%%:;{%%}%%.%::%;)%%(%{%#(:){':;;#(:;(:;::,:,.:{#::;);:):)^^^^^^^':;;#(:;(:;::,:,.:{#::;);:.#}:;{'#(:){':;;#(:;(:;)))             ",
                    "||''||'||'|'||'|'||'||'|'|''||''|'  ||'#(:){':;;#(:;(:;::,:,.:{#::;);:.#}:;{%%)%;)%{%%:%)':;  ;:({#:;.:.,:  {{..)':%%:%%)%%({%%:;{%^^^%.%::%;)%%(%{%::}%#%:;')%%(:;%%%%{:;;%}            ",
                    "||  || || |||||| || || |||| || ||   || ||''||''|'|'|'|'||'|''|'||||''|''||' ;#::;(#;;);: |'|'||''||'||'||'|'|'|'|;;::'#);;:(;{'.:,;)(  ::;#(.:,);^^^{#::;;,:#(#)''|'||'||'||'            ",
                    "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG||  || |||||| |||| |||| |||| || ||GGG '|'| |''||'  |||||||||||||||||||||||||'|'||'|'||''||||'|||'|||'||'|'''||'|'|'||'|||'|'||GG||||'|    GGGGGGGG",
                    "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG||| ||||||GGGGGGGGGGGGGGGGGGGGGGGGGGG||||||||||||||||||||||||||||||||||||||||||||||||||GGGGGGGGGGGGGGGGGGGGG",
                    "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG",]
                    
                    
units = [('<', (40,11), 0, 1, "yaledon", 100),
         ('<', (55,11), 0, 1, "yaledon", 100),
         ('<', (70,11), 0, 1, "yaledon", 100),
         ('<', (120,12), 0, 1, "yaledon", 100),
         ('<', (140,12), 0, 1, "yaledon", 100),
         ('<', (150,12), 0, 1, "yaledon", 100),
         ('<', (160,12), 0, 1, "yaledon", 100),]
new_map["units"] = units

points = [(133,4,'*'),(134,4,chr(216)),(135,4,'*'),(61,5,'o'),(62,5,'o'),(63,5,'o'),(64,5,'o'),(65,6,'o')]
new_map["points"] = points

maps.append(new_map)



new_map = {"name": "The Valley"}
dialog = [("Narrator","You come out of the forest abruptly and are at once faced with a jagged and scared land, torn by some ancient war of titans.  Smoke rises in the distance."),
          ("Tip","Don't try to walk where there is no ground."),]
new_map["dialog"] = {"start": dialog, "soldier": [("$","Who passes the borders of Reidlos?"),("@","I am just, well, um, me.  This old man said I am being called by the 'ever-fate', whatever that is, and I should seek the undying lands."),("$","Well, you don't look very dangerous.  Be carefull, though. You are in the lands of my lord, Baron Namseroh, and there's no telling how he will take to strangers.  Come to think of it, I have heard of this ever-fate before.  One person who could help you is the Tinker, but he is imprisoned in the highest tower of the Baron's castle.")]}
new_map["end"] = None
new_map["start_pos"] = (0,8)
new_map["tiles"] = ["                                                                                                                                                                                                                      ",
                    "                                                                                                                                                                                                                      ",
                    "                                                                                                                                                                                                                      ",
                    "                                                                                                                                                                                                                      ",
                    " ;:#;:,.,#:;;:;.:;...                                                                         GGGGGGGGG                                                   GGG                                                         ",
                    ";%%:,{%%:%%;(%{%;:;;;                                                            GGGGGGGGGGG                                            GGG                                                                           ",
                    ",  :(#:;;:,'{;#:(%;%.:                                      GGGGGGG                                               GGGGG                              GGG                                                              ",
                    "|''|'||'|''|'|'';#;:'                                                  GGGGGGGG                                                    GGG     G                 GG                                                       ",
                    "|||| || |||| || '||'                               GGGGGG                                           GG         G                               GGG                                                                    ",
                    "GGGGGGGGGGGGGGGG ||                                        GGG                   GGG                                   GGG      G                             GGG                               GGG                   ",
                    "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG              GGG                                          GG    GG     GGG   G                GGs~s~s~~s~~~s ~~ s~~s~s~ s~~ sGGGGG              GGG    GGGG                          ",
                    "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG                                                                        GG~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~GGGGG                 G              GG           GGGGG",
                    "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG     GGGGGG        GGGGGGG    G     G        G           GGGGGG~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~GGGGGGGGGGGGGGG                      GGGGGGGGGGGGGGGGG"]
                    
                    
units = [('$', (211,10), 1, 0, "soldier", 800),(" ", (129,8), 1, 0, "tell_lava", 0),(" ", (121,8), 1, 0, "tell_lava", 0)]

new_map["units"] = units

points = [(73,6,'o'),(74,6,'o'),(75,6,'o'),(76,6,'o'),(77,6,'o'),(78,6,'o'),
          (97,3,'o'),(98,3,'O'),(99,3,'Ø'),(100,3,'Ø'),(101,3,'O'),(102,3,'o'),]
new_map["points"] = points

maps.append(new_map)


new_map = {"name": "The Castle"}
dialog = [("Narrator","You stumble over a ridge, covered in soot, and see a great castle of many towers.  There is a swarm of activity around its base.  Many soldiers are between you and the forstress.  Unfortunately, none of them look very freindly."),("Tip", "They're not!")]
new_map["dialog"] = {"start": dialog,}
new_map["end"] = '&'
new_map["restrict_view"] = True
new_map["start_pos"] = (109,60)
new_map["tiles"] = ["                                                                                                                                                                           ",
                    "                                                                                                                                                                           ",
                    "                                                                                                                                                                           ",
                    "                                                                                                                                                                           ",
                    "                                                                                                                                                                           ",
                    "                                                                                                                     þþ              þþ                                    ",
                    "                                                                                                                      þþþþþþ    þþþþþþ                                     ",
                    "                                                                                                                      þ              þ                                     ",
                    "                                                                                                                      þ   þþþþþþþþþþþþ                                     ",
                    "                                                                                                                      þ  þþ    þ     þ                                     ",
                    "                                                                                                                      þ              þ                                     ",
                    "                                                                                                                      þþþþþþþþþþþ    þ                                     ",
                    "                                                                                                                      þ              þ                                     ",
                    "                                                                                                þþ              þþ    þ              þ    þþ              þþ               ",
                    "                                                                                                 þþþþþ      þþþþþ     þ   þþþþþþþþþþþþ     þþþþþ      þþþþþ                ",
                    "                                                                                                 þ              þ     þ              þ     þ              þ                ",
                    "                                                                                                 þ   þþþ        þ     þ              þ     þ        þþþ   þ                ",
                    "                                                                                                 þ              þ     þþþþþþ    þþþþþþ     þ              þ                ",
                    "                                                                                                 þ        þþþþþþþ     þ              þ     þþþþþþþ        þ                ",
                    "                                                                                                 þ              þ     þ              þ     þ              þ                ",
                    "                                                                                                 þ              þ     þ              þ     þ              þ                ",
                    "                                                                                                 þþþþþþþ        þ     þ þþþþþþþþþþþþ þ     þ        þþþþþþþ                ",
                    "                                                                                                 þ              þ     þ              þ     þ              þ                ",
                    "                                                                                                 þ              þ     þ              þ     þ              þ                ",
                    "                                                                                                 þ        þþþþþþþ     þþ            þþ     þþþþþþþ        þ                ",
                    "                                                                                                 þ              þ     þþþ          þþþ     þ              þ                ",
                    "                                                                                                 þ              þ     þþþþ        þþþþ     þ              þ                ",
                    "                                                                                                 þþþþþþþ        þ     þþþþþþþ  þþþþþþþ     þ        þþþþþþþ                ",
                    "                                                                                                 þ              þ     þ              þ     þ              þ                ",
                    "                                                                                                 þ              þ     þ              þ     þ              þ                ",
                    "                                                                                                 þ        þþþþþþþ     þ    þþþþþþ    þ     þþþþþþþ        þ                ",
                    "                                                                                                 þ              þ     þ     þ  þ     þ     þ              þ                ",
                    "                                                                                                 þ              þ     þþþþ        þþþþ     þ              þ                ",
                    "                                                                                                 þþþþþþþ        þ     þ              þ     þ        þþþþþþþ                ",
                    "                                                                                                 þ              þ     þ              þ     þ              þ                ",
                    "                                                                                                 þ              þ     þ    þþþþþþ    þ     þ              þ                ",
                    "                                                                                                 þ        þþþþþþþ     þ              þ     þþþþþþþ        þ                ",
                    "                                                                                                 þ              þ     þ              þ     þ              þ                ",
                    "                                                                                                 þ              þþþþþþþþþþþþ    þþþþþþþþþþþþ              þ                ",
                    "                                                                                                 þ              |     |              |     |              þ                ",
                    "                                                                                                 þþþþþþþþþþþþþþ | /^\ | ...  þþ  ... | /^\ | þþþþþþþþþþþþþþ                ",
                    "                                                                                                 þ            þ | |_| |    þþþþþþ    | |_| | þ            þ                ",
                    "                                                                                                 þ              |     |  þþþþþþþþþþ  |     |              þ                ",
                    "                                                                                                 þþþþþþþþþþþþþþþþþþþþþþþþþþþþþþþþþþþþþþþþþþþþþþþþþþþ   þþþþ                ",
                    "                                                                                                  þ                                                þþ   .þ                 ",
                    "                                                                                                  þþþþ                                          þþþþþþþ  þ                 ",
                    "                                                                                                  þ                   þþþþþþþþþþ                   þ     þ                 ",
                    "                                                                                                  þþþþþ     þþþþ        þþþþþþ        þþþþ     þþþþþ     þ                 ",
                    "                                                                                                  þ          þþ                        þþ          þ  þþþþ                 ",
                    "                                                                                                  þþþþþþ        þþþþþþ    þþ    þþþþþþ        þþþþþþ     þ                 ",
                    "                                                                                                  þþþþ           þþþþ     þþ     þþþþ           þþþþ     þ                 ",
                    "                                                                                                  þ                                                þþþþ  þ                 ",
                    "                                                                                                  þþþþþþþþþ    þþþþþþþþþþþ   þþþþþþþ    þþþþþþþ   þþ     þ                 ",
                    "                                                                                                  þ     .        .     þ .   .     .    .     .   .þ     þ                 ",
                    "                                                                                                  þ      .. þþ ..      þ  þ  þ  þ þþþ þ  þ  þ  þ  þþ    þþ                 ",
                    "                                                                                                  þ        .þþ.        þ                           þþþ   þ                 ",
                    "                                                                                                  þ   þþþ        þþþ   þ þ þþþ þ  þ  þ  þ  þþþþ  þ þ     þ                 ",
                    "                                                                                                  þ        þþþþ        þ                           þ     þ                 ",
                    "                                                                                                  þ                    þþ  þ  þ  þ  þ þþþ þ  þ  þ  þ  þþþþ                 ",
                    "                                                                                                  þ    þþþ     þþþþþþ  þþ                         þþ     þ                 ",
                    "                                                                                                  þ   þþ               þþþ                       þþþ     þ                 ",
                    "                                                                                                  þ          þ         þþþþþþþþþþ      þþþþþþþþþþþþþþþþ  þ                 ",
                    "                                                                                                  þ            þ       þ        .      .           þ     þ                 ",
                    "                                                                                                  þ þþ       þ   þ     þ        .þþþþþþ.    þþ     þ     þ                 ",
                    "                                                                                                  þ               þþ   þ                     þ  þ  þ  þþþþ                 ",
                    "                                                                                                  þ                    þ     þþþþ  þþ  þþþþ  þ þþþ þ     þ                 ",
                    "                                                                                                 þþþþþþ    þþþ         þ      þþ   þþ   þþ   þþþþþþþ     þ                 ",
                    "                                                                                                 þþ                 þþþþ                     þ     þþþþ  þ                 ",
                    "                                                                                                þþþ                    þ  þþþþþþþþþþþþþþþþþþþþ     þ     þ                 ",
                    "                                                                                                þþþ      þþþþþþþ                                   þ     þ                 ",
                    "                                                                                                  þ                    þ                         þ þ  þþþþ                 ",
                    "GGGGGGGGGGGG                                          GGGGGGGGG                                þþ                     þþþ                       þþ       þ                 ",
                    "GGGGGGGGGGGGGGGGGGGGGGGGGGGG                   GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG                þþGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG  T  T T   T  ",
                    "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG"]
                    
         # Main Block
units = [('$', (30, 72), 0, 1, "soldier", 200),('$', (35, 72), 0, 1, "soldier", 200),('$', (40, 72), 0, 1, "soldier", 200), # First pit
         ('$', (80, 72), 0, 1, "soldier", 200),('$', (85, 72), 0, 1, "soldier", 200),('$', (90, 72), 0, 1, "soldier", 200), # Second pit
         ('$', (100, 71), 0, 1, "soldier", 200),('$', (105, 71), 0, 1, "soldier", 200),('$', (110, 71), 0, 1, "soldier", 200),('$', (110, 68), 0, 1, "soldier", 200), # Vestibule
         ('$', (115, 58), 0, 1, "soldier", 200),('$', (115, 55), 0, 1, "soldier", 200),('$', (105, 54), 0, 1, "soldier", 200),						# Top of Vest...
         ('$', (125, 71), 0, 1, "soldier", 200),('$', (130, 71), 0, 1, "soldier", 200),('$', (135, 71), 0, 1, "soldier", 200),('$', (140, 71), 0, 1, "soldier", 200), # Second room
         ('$', (125, 67), 0, 1, "soldier", 200),('$', (130, 67), 0, 1, "soldier", 200),('$', (127, 64), 0, 1, "soldier", 200),('$', (137, 64), 0, 1, "soldier", 200),
         ('$', (125, 60), 0, 1, "soldier", 200),('$', (140, 60), 0, 1, "soldier", 200),('$', (125, 59), 0, 1, "soldier", 200),('$', (140, 59), 0, 1, "soldier", 200), # Top of Second room
         ('$', (105, 51), 0, 1, "soldier", 200),('$', (120, 51), 0, 1, "soldier", 200),('$', (130, 51), 0, 1, "soldier", 200),('$', (140, 51), 0, 1, "soldier", 200), # Boss room
         ('$', (105, 48), 0, 1, "soldier", 200),('$', (105, 46), 0, 1, "soldier", 200),('$', (105, 44), 0, 1, "soldier", 200),
         ('$', (145, 44), 0, 1, "soldier", 200),('$', (145, 44), 0, 1, "soldier", 200),('$', (145, 44), 0, 1, "soldier", 200),
         ('$', (110, 46), 0, 1, "soldier", 200),('$', (115, 48), 0, 1, "soldier", 200),('$', (130, 48), 0, 1, "soldier", 200),('$', (135, 46), 0, 1, "soldier", 200),
         # Towers
         ('$', (150, 66), 0, 1, "soldier", 200),('$', (148, 60), 0, 1, "soldier", 200),('$', (151, 50), 0, 1, "soldier", 200),('$', (151,47), 0, 1, "soldier", 200), # Side path 
         ('$', (144, 17), 0, 1, "soldier", 200),('$', (144, 29), 0, 1, "soldier", 200),('$', (150, 20), 0, 1, "soldier", 200),('$', (150,32), 0, 1, "soldier", 200), # Rigth Tower
         ('$', (127, 34), 0, 1, "soldier", 200),('$', (125, 29), 0, 1, "soldier", 200),('$', (130, 20), 0, 1, "soldier", 200),('$', (127,13), 0, 1, "soldier", 200), # Middle Tower
         ('$', (140, 42), 0, 1, "soldier", 200),('$', (110, 42), 0, 1, "soldier", 200),
         ('$', (112, 17), 0, 1, "soldier", 200),('$', (98, 23), 0, 1, "soldier", 200),('$', (112, 29), 0, 1, "soldier", 200),('$', (98, 35), 0, 1, "soldier", 200),  # Left  Tower
         ]
         
         
new_map["units"] = units

points = []
new_map["points"] = points

maps.append(new_map)


data["maps"] = maps

import pickle, os.path

stream = open(os.path.expanduser("~/.platformer/levels"), "wb")
pickle.dump(data, stream)
stream.close()
