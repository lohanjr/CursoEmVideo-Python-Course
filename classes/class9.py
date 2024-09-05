# MANIPULATING TEXT - Slicing | Analysis | Transformation
phrase = '  Course online of Python   '
print(phrase)
print('--Transformation--')
print('Transforming to uppercase: {}'.format(phrase.upper()))
print('Using .strip() to remove start and final spaces: {}'.format(phrase.strip()))
print('Using .strip() to remove final spaces only: {}'.format(phrase.rstrip()))
print('Separating by spaces: {}'.format(phrase.split()))
print('Showing only the 4th element, which has been separated: {}'.format(phrase.split()[3]))
print('Showing only the character 0 of the 4th element that was separated: {}'.format(phrase.split()[3][0]))
print('--Slicing--')
print('[9:14]: {}'.format(phrase.strip()[9:14])) # O inicio e inclusivo e o final e exclusivo
print('[:14:2]: {}'.format(phrase.strip()[:14:2])) # Comeco indefinido '0' e pulando de 2 em 2 casas
print('--Analysis--')
print('Sentence length: {} characters'.format(len(phrase.strip())))
print('Using .count() to count the number of letters -> o: {}x'.format(phrase.count('o')))
print('Using .find() to find the start of -> Python: {}º byte'.format(phrase.find('Python')))
print('Android in phrase?: {}'.format(('Android' in phrase)))
