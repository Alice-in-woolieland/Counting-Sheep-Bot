import random

def dictToLists(dictionary):
    dicti = dict(dictionary)
    keys = list(dicti)
    print(keys)
    defs = []
    for i in range(len(dicti)):
        defs.append(dicti[str(keys[i])])
    return keys, defs

def generateExplosion():
    list = ["https://media4.giphy.com/media/oe33xf3B50fsc/giphy.gif", "https://i.gifer.com/origin/d7/d7ac4f38b77abe73165d85edf2cbdb9e_w200.gif", "https://media2.giphy.com/media/26tPdwMm4jyClgxTq/giphy.gif", "https://i.gifer.com/origin/a0/a07ad08920f303f655251b1a0b353b86_w200.gif", 'https://tenor.com/view/house-explosion-explode-boom-kaboom-gif-19506150']
    returned = random.choice(list)
    print(returned)
    return returned

def generateFlip():
    list = ["https://media.tenor.com/8QCJ-T8XP9kAAAAC/anime-flip.gif", "https://media.tenor.com/kvxt9X-gXqQAAAAM/anime-clannad.gif", "https://media.tenor.com/D5OWYMGcAzAAAAAM/escondido-catedrales.gif", "https://thumbs.gfycat.com/AdvancedViciousArcticwolf-size_restricted.gif", "https://pa1.narvii.com/5783/0c9a721f4ea807fcabd70163de8a55e9b542198a_00.gif", "https://pa1.narvii.com/5723/3b12ad0ff8f0008129ce15cfc3b78137cb156d86_hq.gif", "https://media.tenor.com/fH6MPYB5JjUAAAAC/anime-attack.gif", "https://media.discordapp.net/attachments/1094050332063051867/1095772773802065950/animesher.com_gif-attack-nichijou-1725947.gif", "https://i.pinimg.com/originals/59/cc/96/59cc9691e7a3398fe751b28f92d2dac6.gif", "https://media.tenor.com/nRreDVnv36MAAAAM/anime-dokuro-chan.gif", "https://thumbs.gfycat.com/TatteredScholarlyAcaciarat-size_restricted.gif", "https://i.makeagif.com/media/11-21-2018/8JZQrx.gif", "https://64.media.tumblr.com/621a43bd65d81950d1f09c42cb6a36ba/5e8d49e4af36b4ef-b8/s540x810/64bc3b8467dbb97f543596e8a8a3b674605d8d8c.gif"]
    returned = random.choice(list)
    print(returned)
    return returned

def generateUnflip():
    list = ['https://media.discordapp.net/attachments/854046409933586434/1026745164246556722/image0.gif', 'https://media.tenor.com/_0w13xK66ZUAAAAC/uwu-cute.gif', 'https://media.discordapp.net/attachments/1070911453386784829/1096956586276163707/Tumblr_l_56552159858899.gif', 'https://media.tenor.com/WTKJwI7PpHUAAAAC/yipee-meme.gif', 'https://media.tenor.com/4bJYCzqrbvQAAAAC/lwa-little-witch-academia.gif', 'https://media.tenor.com/w0Rv_cu3bJAAAAAC/kitty-cute.gif', 'https://images-ext-1.discordapp.net/external/pvFpGLrVhaMHj5w5W-zdoFbfCbQ-xkiMWUSWNG4szsQ/https/media.tenor.com/yMnSqO98_kIAAAPo/kitty.mp4']
    returned = random.choice(list)
    print(returned)
    return returned
