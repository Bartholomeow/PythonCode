def brackets_are_correct(text):
    
    brackets = []
    for i in range(len(text)):
        if text[i] == '(':
            brackets.append(text[i])
        elif text[i] == ')':
            if len(brackets) == 0:
                print('Скобки расставлены неверно')
                return
            if brackets[-1] == '(':
                brackets.pop()
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
brackets_are_correct('')
brackets_are_correct('()(())')
# brackets_are_correct(input())
