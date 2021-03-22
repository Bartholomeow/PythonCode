def brackets_are_correct(text):
    """Determine if brackets in text are correct"""
    brackets = []
    for i in range(len(text)):
        if text[i] in ['(', '{', '[']:
            brackets.append(text[i])
        elif text[i] in [')', '}', ']']:
            if len(brackets) == 0:
                print('Скобки расставлены неверно')
                return
            if brackets[-1] == '(' and text[i] == ')':
                brackets.pop()
            elif brackets[-1] == '{' and text[i] == '}':
                brackets.pop()
            elif brackets[-1] == '[' and text[i] == ']':
                brackets.pop()
            else:
                print('Скобки расставлены неверно')
                return
    print('Скобки расставлены верно' if len(brackets)
          == 0 else 'Скобки расставлены неверно')


print('Введите последовательность круглых скобок')
brackets_are_correct('()')
brackets_are_correct(')')
brackets_are_correct('(')
brackets_are_correct('())')
brackets_are_correct('(()')
brackets_are_correct('(())')
brackets_are_correct('()()')
brackets_are_correct('()()(')
brackets_are_correct('{]')
brackets_are_correct('{[}]')
brackets_are_correct('{}')
brackets_are_correct('{([])}')
brackets_are_correct('()(())')
# brackets_are_correct(input())
