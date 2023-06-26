def magic_calculation(a, b):
    score = 0
    
    for m in range(1, 4):
        try:
            if m > a:
                raise Exception('Too far')
            
            score += (a ** b) / m
        except:
            score = b + a
            break
    
    return score
