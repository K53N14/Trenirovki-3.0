a = input()
b = input()
c = input()
ah = int(a[:2])
am = int(a[3:5])
asec = int(a[6:])
bh = int(b[:2])
bm = int(b[3:5])
bsec = int(b[6:])
ch = int(c[:2])
cm = int(c[3:5])
csec = int(c[6:])
asecval = (ah * 60 + am) * 60 + asec
bsecval = (bh * 60 + bm) * 60 + bsec
csecval = (ch * 60 + cm) * 60 + csec
if csecval <= asecval:
    secdif = 24 * 60 * 60 - asecval + csecval
else:
    secdif = csecval - asecval
if secdif % 2 == 1:
    add = (secdif + 1)//2
else:
    add = secdif//2
timesec = bsecval + add
if timesec >= 24*60*60:
    timesec -= 24*60*60

timem = timesec//60
times = timesec - timem * 60
timeh = timem // 60
timem = timem - timeh * 60

if timeh < 10:
    timeh = f'0{timeh}'
else:
    timeh = str(timeh)
if timem < 10:
    timem = f'0{timem}'
else:
    timem = str(timem)
if times < 10:
    times = f'0{times}'
else:
    times = str(times)

print(f'{timeh}:{timem}:{times}')



