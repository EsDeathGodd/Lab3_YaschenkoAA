class Registration:
    def __init__(self, value):
        self.value = value

    def getMethod(self) -> str:
        if not isinstance(self.value,str):
            return None

        try:
            if self.value[0] == "+":

                return 1
            elif "@" in self.value:

                return 2
            else:

                return 3
        except Exception as e:
            print(f"Error happened during getMethod method of a Registration class:{e}")

test = Registration("+77-90000")
print(test.getMethod())




