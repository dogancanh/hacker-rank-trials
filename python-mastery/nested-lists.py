if __name__ == '__main__':
    students  = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students[name] = score

    temp = min(students.values())
    temp2 = min(x for x in students.values() if x!=temp)
    lix = sorted(key for key in students if students[key] == temp2)
     
    print("\n".join(lix))
