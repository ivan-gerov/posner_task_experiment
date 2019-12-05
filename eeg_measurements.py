
def getPreliminaryMeasures():
    NI_DIST = 38
    # NI_DIST = int(input('Nasion-Inion Distance: '))
    cz = NI_DIST/2
    fz_pz = cz-(NI_DIST*0.2)
    fpz_oz = NI_DIST * 0.1


    print(
        f'1. NI_DIST: {NI_DIST}',
        f'\n2. Cz (from Nasion): {cz}',
        f'\n3. Fz and Pz (from N or I): {fz_pz}',
        f'\n4. Fpz and Oz (from N or I): {fpz_oz}',
    )


CIRCUMFERENCE = 58
# CIRCUMFERENCE = int(input('Circuference: '))

po7_po8 = CIRCUMFERENCE * 0.1 



print(
    f'5. Circumference: {CIRCUMFERENCE}',
    f'\n6. PO7 and PO8 (from Oz): {po7_po8}')

PO7_POZ = 5
# PO7_POZ = int(input('PO7_POZ Distance: '))
    
po3_po4 = PO7_POZ/2


