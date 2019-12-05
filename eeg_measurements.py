import os

print(os.getcwd())


PARTICIPANT_NAME = input('Participant Name: ')


def get_EEG_positions():

    #     NI_DIST = 38
    NI_DIST = int(input('Nasion-Inion Distance: '))
    cz = NI_DIST/2
    fz_pz = round(cz-(NI_DIST*0.2), 2)
    fpz_oz = round((NI_DIST * 0.1), 2)

    step_1 = (
        f'\n1. N-I Distance: {NI_DIST}',
        f'\n2. Cz (from Nasion/ Inion): {cz}',
        f'\n3. Fz and Pz (from N or I): {fz_pz}',
        f'\n4. Fpz and Oz (from N or I): {fpz_oz}',
        '\n'
    )
    print(*step_1)

#     CIRCUMFERENCE = 58
    CIRCUMFERENCE = int(input('Circuference: '))

    po7_po8 = round((CIRCUMFERENCE * 0.1), 2)

    step_2 = (
        f'\n5. Circumference: {CIRCUMFERENCE}',
        f'\n6. PO7 and PO8 (from Oz): {po7_po8}',
        '\n'
    )
    print(*step_2)

    # PO7_Pz = 5
    po7_pz = int(input('PO7-Pz Distance: '))

    po3_po4 = round((po7_pz/2), 2)

    f7_f8 = round((CIRCUMFERENCE * 0.15), 2)

    step_3 = (
        f'\n7. PO7/PO8 to Pz distance: {po7_pz}',
        f'\n8. ->>> PO3/PO4 position (between PO7 and POz, from PO7): {po3_po4}'
        f'\n9. F7/F8 position (on Circ line): {f7_f8})',
        '\n'
    )
    print(*step_3)

#     f7_f8_dist = 12
    f7_f8_dist = int(input('Distance between F7 and F8 (over Fz): '))
    f1_f2 = round((f7_f8_dist * 0.125), 3)

    step_4 = (
        f'\n10. F7-F8 Distance: {f7_f8_dist}',
        f'\n11. Position of F1/F2 (from Fz): {f1_f2}'
    )

    print(*step_4)
    
    steps = [step_1, step_2, step_3, step_4]
    
    return steps

STEPS = get_EEG_positions()



def write_positions(participant_name,steps= STEPS):

    if os.path.exists('./data/positions') == False:
        os.mkdir('./data/positions')
    try:
        pos_file = open(f'./data/positions/{participant_name}.txt', 'x')
    except FileExistsError as e:
        pos_file = open(f'./data/positions/{participant_name}.txt', 'w+')


    for step in steps:
        for line in step:
            pos_file.write(line)

    pos_file.close()

write_positions(PARTICIPANT_NAME, STEPS)

