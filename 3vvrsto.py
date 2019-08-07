import bottle
import model
import random

igra = model.Igra()
second = True
@bottle.get('/AI_learns/')
def leanAI():

    igra.learn()

    return bottle.redirect('http://127.0.0.1:8080/new')


@bottle.get('/new')
def newgame():
    igra.polje = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    if random.randint(0, 1) == 1:
        igra.polje = igra.bot1.nasledni(igra.polje, "l1")
        second = False
    else:
        second = True
    return bottle.redirect('http://127.0.0.1:8080/')


@bottle.get('/place/<mesto>')
def place2(mesto):
    print(mesto)

    if igra.polje[int(mesto) // 3][int(mesto) % 3] != 0:
        return bottle.redirect('http://127.0.0.1:8080/')

    igra.dodaj(int(mesto))
    info = igra.konec(igra.polje)

    if info == 1:
        place("Zmagal si")
        igra.izpisi(igra.polje, 1)
    if info == 2 :
      place("Izenačeno je")
      igra.izpisi(igra.polje, 1)

    if  info == -1:
        place("Izgubil")
        igra.izpisi(igra.polje, 1)

    if second:
        igra.polje = igra.bot1.nasledni(igra.polje, "l2")
    else:
        igra.polje = igra.bot1.nasledni(igra.polje, "l1")
    info = igra.konec(igra.polje)

    if info == 2 :
      place("Izenačeno je")
      igra.izpisi(igra.polje, 1)

    if  info == -1:
        place("Izgubil si")
        igra.izpisi(igra.polje, 1)

    igra.izpisi(igra.polje, 1)

    return bottle.redirect('http://127.0.0.1:8080/')


@bottle.get('/')
def place(end=0):

    win = model.countratio[1]
    lose = model.countratio[-1]
    pat = model.countratio[2]

    ar = {}
    for x in range(9):

        ar[x] = igra.polje[x // 3][x % 3]

        if ar[x] == 0:
            ar[x] = "empty.png"

        if ar[x] == 1:
            ar[x] = "x.png"

        if ar[x] == -1:
            ar[x] = "o.png"

    if end == 0:
        return bottle.template('view/igra.tpl', win=win, lose=lose, pat=pat, ime0=ar[0], ime1=ar[1], ime2=ar[2], ime3=ar[3], ime4=ar[4], ime5=ar[5], ime6=ar[6], ime7=ar[7], ime8=ar[8])

    else:
        print("jaaaaa")
        return bottle.redirect(f'http://127.0.0.1:8080/end/{end}')


@bottle.get('/end/<end>')
def placement2(end):

    ar = {}
    for x in range(9):

        ar[x] = igra.polje[x // 3][x % 3]

        if ar[x] == 0:
            ar[x] = "empty.png"

        if ar[x] == 1:
            ar[x] = "x.png"

        if ar[x] == -1:
            ar[x] = "o.png"

    return bottle.template('view/konec.tpl', wl=end, ime0=ar[0], ime1=ar[1], ime2=ar[2], ime3=ar[3], ime4=ar[4], ime5=ar[5], ime6=ar[6], ime7=ar[7], ime8=ar[8])


@bottle.get("/static/<filename>")
def server_static(filename):
    return bottle.static_file(filename, root="./images")


bottle.run(reloader=True, debug=True)
