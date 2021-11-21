with open('/Frontend/main_page.html') as inf:
    src = [line.strip() for line in inf.readlines()]
    print(*src)
