print ("‼ FACTORIAL OR NON FACTORIAL NUMBERS ‼")

while True:
    number = int (input("enter an integer number: "))

    m=1
    n=1

    while number >= m:
        
        m = m * n
        n = n + 1

        if number == m:
            print ("✅Yes✅")
            break
        elif number < m:
            print ("❌No❌")
            break