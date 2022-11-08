class result:
    def __init__(self, list):
        self.list = list

    def run(self):
        self.myFunc()

    def myFunc(self):
        for col in self.list:       
            for row in col:  
                print(row, end="\n")


if __name__ == '__main__':
    new_List = [["Mark",55],["Sue",87]]
    newResult = result(new_List)
    print(newResult.run())
