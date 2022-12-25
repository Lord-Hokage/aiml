def prog_no(n):
    with open (n+".txt") as file:
        lines=file.readlines()
        for line in lines:
            print(line)
