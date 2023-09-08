import datetime


blance=200 #global variable for account blance
#the menu or display screen
def menu():
    print('Evcplus')
    print(f'\t1.itus haraaga')
    print(f'\t2.ku shubo airtime ')
    print(f'\t3.ugu shub airtime ')
    print(f'\t4.uwareeji evc plus')
    print(f'\t5.warbixin kooban')
    print(f'\t6.mareynta ')

#1haraaga
def haraaga():
    global blance
    print(f'haraagaagu waa {blance}$')
#functionka qabanayo optionka labad ee ku shubo ku hadal
def kushubo():
    global blance
    try:
        amount=float(input('geli lacagta: '))
        if amount<blance:
            blance=blance-amount
            print(f'waxaad ku shubatay {amount}$ haraagaagu waa {blance}')
            transaction_detail = f"{datetime.datetime.now()}: waxaad ku shubatay {amount}$"
            transaction_file(transaction_detail)
        else:
            print(f'haraaga xisaabtada kuguma filna')
    except ValueError:
        print('waxqaldan gelisay')

#functionka qabanayo optionka sadaxaad ee ugu shub ku hadal
def ugu_shub():
    global blance
    try:
        numberka = input('fadlan geli lambarka ugu shubeesid adigo kabilabayo (061) ama (077): ')
        while (len(numberka)!=10) and numberka.isdigit()==True:
            print(f'nambar qaldan gelisay')
            numberka = input('fadlan geli lambarka ugu shubeesid adigo kabilabayo (061) ama (077): ')
        amount = float(input('geli lacagta: '))
        if amount < blance:
            blance = blance - amount
            print(f'waxaad {amount}$ ugu shubatay {numberka} haraagaagu waa {blance}')
            transaction_detail = f"{datetime.datetime.now()}: waxaad {amount}$ ugu shubatay {numberka}"
            transaction_file(transaction_detail)
        else:
            print(f'haraaga xisaabtada kuguma filna')
    except ValueError:
        print('wax qaldan so gelisay good bye!')


# lacag wareejinta midka qabanayo
def uwareeji():
    global blance
    try:
        numberka = input('fadlan geli lambarka u wareejineesid adigo kabilabayo (061) ama (077): ')
        while (len(numberka) != 10) and numberka.isdigit() == True: #hubin in numberka uu saxanyahay nambarka waa inuu ka koobnata 6-digit
            print(f'nambar qaldan gelisay')
            numberka = input('fadlan geli lambarka u wareejinesid adigo kabilabayo (061) ama (077) ')
        amount = float(input('geli lacagta: '))
        if amount < blance:
            blance = blance - amount
            print(f'waxaad {amount}$ u wareejisay {numberka} haraagaagu waa {blance}')
            transaction_detail=f"{datetime.datetime.now()}: waxaad {amount}$ u wareejisay {numberka}"
            transaction_file(transaction_detail) #transaction saving
        else:
            print(f'haraaga xisaabtada kuguma filna')
    except ValueError: # error handling
        print('wax qaldan so gelisay good bye!')


#function qabanaayo dhamaan transactions
def transaction_file(transaction_details):
    with open('transaction_log.txt','a') as file:
        file.write(transaction_details + "\n")

#warbixin fuctionkan wuxuu ku tusinaya dhaqadhaqaaqyada transaction fileka
def warbixin_kooban():
    print('1.wareejinti udambeesay')
    print('2.numberadi udambeeye e kaheshay')
    print('3. dhamaan dhaqdhaqaaqyadi sameese')
    try:
        usr_input=int(input('dooro adeega ubahantahe: '))
        if usr_input==1:
            file=open('transaction_log.txt','r')
            mylist=[]
            for line in file:
                mylist.append(line)
            print(mylist[-1])
        elif usr_input==2:
            print('no transaction to display')
        elif usr_input==3:
            file = open('transaction_log.txt', 'r')
            mylist = []
            for line in file:
                print(line)
    except ValueError:
        print('wax qaldan gelise macsalaama!')






#mareenta inti lagu soo daro pin files pin ama inti labadlo number sir
def maareynta():
    print('1.badal lambar sireedka')
    print('2.diwangeli lambar lumid')
    print('3. badal luqada')
    try:
        usr_input = int(input('dooro adeega ubahantahe: '))
        if usr_input==1:
            file=open('C:\\Users\\mohan\\PycharmProjects\\evcplus_project\\pins.txt','r')
            pins=[]
            for line in file:
                inline = int(line)
                pins.append(inline)
            badalid=int(input('geli binkaagi hore: '))
            if badalid in pins:
                pins.remove(badalid)
                mid_cusub=input('geli binka cusub: ')
                if (len(mid_cusub)!=4) or mid_cusub.isdigit()!=True:
                    print('pin qaldan gelise ')
                    mid_cusub = input('geli binka cusub: ')
                else:
                    confirmation=input('ku celi markale si aad uhubisid: ')
                    if confirmation==mid_cusub:
                        pins.append(confirmation)
                        file_pin=open('C:\\Users\\mohan\\PycharmProjects\\evcplus_project\\pins.txt','a')
                        file_pin.write(f'\n {confirmation}')
                        print('waad ku gulleysatay inaad badashid pinkaaaga mahadsanid')
                    else:
                        print('maadan saxin macsalaama! ')
            else:
                print('pinkaas maahin mid jira')
        elif usr_input==2:
            print('adeegaan weli lama keenin')
        elif usr_input==3:
            print('adeegaan weli lama keenin')
        else:
            print('number qaldan dooratay')
    except ValueError:
        print('wax qaldan gelise macsalaama!')










while True:
    print('welcome to evc Plus ')
    try:
        pinka=int(input('fadlan geli pinka: '))
        pins=[]
        with open('C:\\Users\\mohan\\PycharmProjects\\evcplus_project\\pins.txt', 'r') as file:
            for line in file:
                inline=int(line)
                pins.append(inline)
            if pinka in pins:
                display = menu()
                usr_choice = int(input('dooro mid kamid numberada kore: '))
                if usr_choice == 1:
                    itus = haraaga()
                    break
                elif usr_choice == 2:
                    success = kushubo()
                    break
                elif usr_choice == 3:
                    kaar = ugu_shub()
                    break
                elif usr_choice == 4:
                    warejin = uwareeji()
                    break
                elif usr_choice == 5:
                    warbixinada = warbixin_kooban()
                    break
                elif usr_choice == 6:
                    mareen = maareynta()
                    break
                else:
                    print('wax qaldan galisay')

    except ValueError:
        print('wax qaldan ayaad gelisay macsalaama ')