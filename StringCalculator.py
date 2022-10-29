class StringCalculator():

    Operators = set(['+', '-', '*', '/', '(', ')', '^'])

    Priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def infixToPostFix(self, string: str) -> list:
        stack = list()
        output = list()

        for character in string:

            if character not in self.Operators:
                output += character

            elif character == '(':
                stack.append('(')

            elif character == ')':

                while stack and stack[-1] != '(':

                    output += stack.pop()

                stack.pop()

            else:

                while stack and stack[-1] != '(' and self.Priority[character] <= self.Priority[stack[-1]]:

                    output += stack.pop()

                stack.append(character)

        while stack:

            output += stack.pop()

        return output

    def evalPostfix(self, expression: list) -> float:
        s = list()
        for symbol in expression:
            if symbol == " ":
                continue

            if symbol in "0123456789":
                s.append(int(symbol))

            elif len(s) >= 2:
                result = None
                a = s.pop()
                b = s.pop()
                if symbol == "+":
                    result = a + b
                elif symbol == "-":
                    result = b - a
                elif symbol == "*":
                    result = a * b
                elif symbol == "/":
                    result = b / a
                if result is not None:
                    s.append(result)
                else:
                    raise Exception("unknown value %s" % symbol)

        return s.pop()

    def calculateInfix(self, input: str) -> str:
        try:
            return str(self.evalPostfix(self.infixToPostFix(input)))
        except Exception:
            return "Error"
# Testing

strCal = StringCalculator()

print(strCal.calculateInfix("-4 * 5- 2/2 - 3"))
