def conver(f):
    numerals = [
            {'letter': 'M', 'value': 1000},
            {'letter': 'D', 'value': 500},
            {'letter': 'C', 'value': 100},
            {'letter': 'L', 'value': 50},
            {'letter': 'X', 'value': 10},
            {'letter': 'V', 'value': 5},
            {'letter': 'I', 'value': 1},
        ]
    def arabic_to_roman(*args):
        number = f(*args)
        if type(number) is int:   
            remainder = number
            result = '' 
            for numeral_index in range(len(numerals)):
                numeral = numerals[numeral_index]
                next_numeral = numerals[numeral_index + 1] if numeral_index + 1 < len(numerals) else None

                factor = remainder / numeral['value']
                remainder -= factor * numeral['value']

                if next_numeral:
                    numeral_difference = numeral['value'] - next_numeral['value']
                    if (remainder - numeral_difference >= 0) and (numeral_difference > next_numeral['value']):
                        result += next_numeral['letter'] + numeral['letter']
                        remainder -= numeral_difference
                if factor > 0:
                    result += numeral['letter'] * factor
            return result
        else:
            return number
    return arabic_to_roman()