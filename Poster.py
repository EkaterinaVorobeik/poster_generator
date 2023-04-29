import random as r
from datetime import datetime
import colorsys
from drawBot import *

for i in range(30):
    newPage('A3')
    # COLORS
    colors = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9] 
    w = r.choice(colors)
    h,li,s = w, 0.5, 1 
    # color for PREFIX 
    rgb = colorsys.hls_to_rgb (h, li+0.1, s)
    # color for ROOT 
    comp2 = colorsys.hls_to_rgb(h, li+0.2, s-0.2)
    # color for SUFFIX 
    comp3 = colorsys.hls_to_rgb(h, li+0.3, s-0.1)
    # color for DATE
    comp = colorsys.hls_to_rgb(h, li+0.2, s-0.6)

    # BACKGROUND 
    fill(.8)
    rect(0, 0, width(),height()+10)

    # FONT PART
    fontLibraryBold = ['/Users/ekaterinavorobeva/Library/Fonts/Oswald-Bold.ttf', 
                       '/Users/ekaterinavorobeva/Library/Fonts/Roboto-Bold.ttf',
                       '/Users/ekaterinavorobeva/Library/Fonts/Lato-Black.ttf', 
                       '/Users/ekaterinavorobeva/Library/Fonts/Heebo-Bold.ttf', 
                       '/Users/ekaterinavorobeva/Library/Fonts/MavenPro-ExtraBold.ttf', 
                       '/Users/ekaterinavorobeva/Library/Fonts/Montserrat-ExtraBold.ttf', 
                       '/Users/ekaterinavorobeva/Library/Fonts/Teko-Bold.ttf', 
                       '/Users/ekaterinavorobeva/Library/Fonts/WorkSans-ExtraBold.ttf', 
                       '/Users/ekaterinavorobeva/Library/Fonts/Assistant-ExtraBold.ttf', 
                       '/Users/ekaterinavorobeva/Library/Fonts/Yantramanav-Black.ttf',
                       '/Users/ekaterinavorobeva/Library/Fonts/Arvo-Bold.ttf', 
                       '/Users/ekaterinavorobeva/Library/Fonts/BioRhyme-ExtraBold.ttf', 
                       '/Users/ekaterinavorobeva/Library/Fonts/Bitter-ExtraBold.ttf']

    fontLB1 = r.choice(fontLibraryBold)
    font_pathB1 = fontLB1
    fontLB2 = r.choice(fontLibraryBold)
    font_pathB2 = fontLB2
    fontLB3 = r.choice(fontLibraryBold)
    font_pathB3 = fontLB3
    fontLB4 = r.choice(fontLibraryBold)
    font_pathB4 = fontLB4

    # DATE
    def generate_date():
        now = datetime.now()
        date = now.strftime('%d/%m')
        return date

    date = generate_date()
    font_size = 30
    font(font_pathB4, font_size)
    lineHeight(font_size)
    fill(*comp)
    text(f'Today', (width()-70, 70), align = 'center')
    text(f'{date}', (width()-70, 30), align = 'center')

    # WORD CREATION PART 
    prefixes = ['Anti', 'De', 'Dis', 'Em', 'En', 'Fore', 'In', 'Im', 'Inter', 'Mid', 'Mis', 'Non', 'Over', 'Pre', 'Re', 'Semi', 'Sub', 'Super', 'Trans', 'Un', 'Under',]
            
    roots = ['anthropo', 'auto', 'bio', 'chron', 'dyna', 'dys', 'gram', 'graph', 'hetero', 'homo', 'hydr', 'hypo', 'logy', 'meter', 'micro', 'mis', 'mono', 'morph', 'nym', 'phil', 'phobia', 'phon', 'photo', 'pseudo', 'psycho', 'scope', 'techno', 'tele', 'therm']
        
    suffixes = ['able', 'ible', 'al', 'ial', 'ed', 'en', 'er', 'er', 'est', 'ful', 'ic', 'ing', 'ion', 'ity', 'ive', 'less', 'ly', 'ment', 'ness', 'ous', 's', 'es', 'y']

    term_p = r.choice(prefixes)
    term_r = r.choice(roots)
    term_s = r.choice(suffixes)

    # PRINT (PHASES)
    line11 = f'{term_p}' 
    line12 = f'{term_r}' 
    line13 = f'{term_s}.' 

    # MAIN PHRASE
    font_size = 200
    font(font_pathB1, font_size)
    lineHeight(font_size)

    fill(*rgb)
    cmykShadow((50, -50), 70, (0, 0, 0, 1))
    text(line11, (20, height()-180), align = 'left')

    font(font_pathB2, font_size)
    fill(*comp2)
    cmykShadow((50, -50), 70, (0, 0, 0, 1))
    text(line12, (20, height()-380), align = 'left')

    fill(*comp3)
    font(font_pathB3, font_size)
    cmykShadow((50, -50), 70, (0, 0, 0, 1))
    text(line13, (20, height()-580), align = 'left')


saveImage("~/Desktop/Poster.pdf")
