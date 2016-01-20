def bob_count2(s, bob):
    i = 0
    count = 0
    last = len(s) - len(bob)
    while i != last:
        if s[i:(i+len(bob))] == bob:
            count += 1
            i += 1
        else:
            i += 1

    print(count)

def main():
    count = 0
    bob = "bob"
    s = "obobobobbpobobobob"
    bob_count2(s, bob)


main()