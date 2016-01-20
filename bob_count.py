def bob_count2(s, bob):
    i = 0
    j = 3
    count = 0
    last = len(s)
    while i != last:
        if s[i:j] == bob:
            count += 1
            print(s[i:j])
            i += 1
            j += 1
        else:
            print(s[i:j])
            i += 1
            j += 1


    print(count)

def main():
    count = 0
    bob = "bob"
    s = "obobobobbpobobobob"
    bob_count2(s, bob)


main()