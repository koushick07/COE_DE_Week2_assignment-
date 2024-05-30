def merge_the_tools(string, k):
    n = len(string)

    def word_form(items):
        visit = set()
        for i in items:
            if i not in visit:
                yield i
                visit.add(i)

    while string:
        word = string[0:k]
        string = string[k:]
        
        print (''.join(word_form(word)))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)        