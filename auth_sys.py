def correct():
    s, q, r, t, u, v = 0, 0, 0, 0, 0, 0
    x = input("enter password: ")

    if len(x) >= 10:
        s += 1

    for i in range(len(x)):
        if x[i] >= "A" and x[i] <= "Z":
            q += 1
        elif x[i] >= "s" and x[i] <= "z":
            r += 1
        elif (x[i] >= "1" and x[i] <= "9") or x[i] == "0":
            t += 1
        elif x[i] in ["@", "#", "$", "%", "&", "*", "!"]:
            u += 1

    for i in range(len(x) - 3):
        if x[i] == x[i + 1] == x[i + 2] == x[i + 3]:
            v += 1

    if len(x) >= 10 and q >= 2 and r >= 2 and t >= 2 and u >= 2 and v == 0:
        print("password set successfully.")
    else:
        if len(x) < 10:
            print("The password must be at least 10 characters long.")
        if q < 2:
            print("The password must contain at least 2 capital letters.")
        if r < 2:
            print("The password must contain at least 2 small letters.")
        if t < 2:
            print("The password must contain at least 2 digits.")
        if u < 2:
            print("The password must contain at least 2 special characters.")
        if v != 0:
            print("The password should not contain more than 3 characters consecutively.")
        correct()


username = input("enter username: ")
correct()
