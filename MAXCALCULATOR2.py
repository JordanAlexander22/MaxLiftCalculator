#Jordan Covo
#1st project
#july 17 2019
def yes_or_no(reply):
    reply= 'y'

    while "the answer is invalid":
        reply = str(input(question+' (y/n): ')).lower().strip()
        if reply[0] == 'y':
            return True
        if reply[0] == 'n':
            return False

while True:
    Welcome= 'Hello and welcome to one rep max calculator, Please follow the prompt below'
    print (Welcome)

    reps= int(input('Rep Count?'))

    initial_weight= int(input('Weight lifted?'))

    bench_max=(.0333 * reps + 1) * initial_weight
    print (bench_max)

    reply= 'y'

    question= 'Do you want another calculation?'

    if (not yes_or_no(reply)):
        break




