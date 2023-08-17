import os
import cv2
import numpy as np

def extract(photo):
    numbers=[]
    # Her harf için tarama yap
    for digit in os.listdir('./numbers'):
        template = cv2.imread(f'./numbers/{digit}')
        w, h = template.shape[:-1] # resim boyutları

        # sayının resim içinde olup olmadığını bulma
        res = cv2.matchTemplate(photo, template, cv2.TM_CCOEFF_NORMED) 
        threshold = .73 # eşik değeri
        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            
            # bulunan her resmin üzerini çizip tekrar bulunmasını engelliyoruz
            cv2.line(photo, (pt[0] + int(w/2), pt[1]), (pt[0] + int(w/2), pt[1] + int(h/2)), (0, 0, 255), 1)
            rounded = round(pt[0]/10)*10

            # bulunanların listeye eklenmesi
            numbers.append(
                {
                    'Loc': int(rounded),
                    'Number': int(digit[0])
                }
            )
        
        # tekrar eden değerleri listeden silme
        of = []
        for si in numbers:
            key = si["Loc"]
            if key not in of:
                of.append(key)
            else:
                numbers.remove(si)
            

    # resmin son halinin kaydedilmesi
    cv2.imwrite('result.png', photo)

    # bulunan sayıları soldan sağa doğru sıralama
    newNumbers = sorted(numbers, key=lambda k: k['Loc'])
    # print(newNumbers)
    captcha = ''
    for i in newNumbers:
        captcha += str(i['Number'])

    print(captcha + "\n")
    return captcha