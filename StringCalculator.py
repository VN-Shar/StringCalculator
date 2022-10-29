class StringCalculator():

    Operators = set(['+', '-', '*', '/', '(', ')', '^'])

    Priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def formatExpression(self, string: str) -> list:
        if(len(string) == 0):
            raise Exception("Expression length must be > 0")

        result = list()
        string = string.replace(" ", "")
        number = ''
        if (string.startswith("-") or string.startswith("+")):
            number += string[0]

        string = string[1:]

        for character in string:
            if character in "0123456789.,":
                number += character
            else:
                if len(number) > 1 or (len(number) == 1 and number[0] not in self.Operators):
                    result.append(float(number))
                    result.append(character)
                    number = ''
        if (len(number) != 0):
            result.append(float(number))
        return result

    def infixToPostFix(self, string: str) -> list:
        stack = list()
        output = list()

        expression = self.formatExpression(string)

        for character in expression:

            if character not in self.Operators:
                output.append(character)

            elif character == '(':
                stack.append('(')

            elif character == ')':

                while stack and stack[-1] != '(':

                    output.append(stack.pop())

                stack.pop()

            else:

                while stack and stack[-1] != '(' and self.Priority[character] <= self.Priority[stack[-1]]:

                    output.append(stack.pop())

                stack.append(character)

        while stack:

            output.append(stack.pop())

        return output

    def evalPostfix(self, expression: list) -> float:
        s = list()
        for character in expression:

            if character not in self.Operators:
                s.append(character)

            elif len(s) >= 2:
                result = None
                a = s.pop()
                b = s.pop()
                if character == "+":
                    result = a + b
                elif character == "-":
                    result = b - a
                elif character == "*":
                    result = a * b
                elif character == "/":
                    result = b / a
                elif character == "^":
                    result = a ** b
                if result is not None:
                    s.append(result)
                else:
                    raise Exception("unknown value %s" % character)

        return s.pop()

    def calculateInfix(self, input: str) -> str:
        return str(self.evalPostfix(self.infixToPostFix(input)))
# Testing


strCal = StringCalculator()

print(strCal.calculateInfix("-4 * 4^ 2"))
