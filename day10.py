from typing import List, Dict
from math import floor

OPENING_CHARS = ['(', '[', '{' ,'<']
POINTS_TABLE_SYNTAX_ERROR = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

POINTS_TABLE_AUTOCOMPLETE = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

def get_opening_char(closing_char: str):
    if closing_char == ')': return '('
    elif closing_char == ']': return '['
    elif closing_char == '}': return '{'
    else: return '<'

def calculate_syntax_error_highscore(lines: List[str]):
    overall_score = 0
    for line in lines:
        characters = list(line.strip())
        line_score = 0
        opened = []
        for char_index in range(len(characters)):
            character = line[char_index]
            if character in OPENING_CHARS: opened.append(character)
            else:
                if len(opened) == 0 or get_opening_char(character) != opened.pop():
                    line_score = POINTS_TABLE_SYNTAX_ERROR[character]
                    break
        overall_score += line_score
    return overall_score

def calculate_autocomplete_middlescore(lines: List[str]):
    line_scores = []
    for line in lines:
        characters = list(line.strip())
        opened = []
        syntax_error_detected = False
        for char_index in range(len(characters)):
            character = line[char_index]
            if character in OPENING_CHARS: opened.append(character)
            else:
                if len(opened) == 0 or get_opening_char(character) != opened.pop():
                    syntax_error_detected = True
                    break
        if not syntax_error_detected:
            line_score = 0
            opened.reverse() # reverse list to start with the last added opening character
            for char in opened:
                line_score = (line_score * 5) + POINTS_TABLE_AUTOCOMPLETE[char]
            line_scores.append(line_score)
    
    line_scores.sort()
    return line_scores[floor(len(line_scores)/2)]

# tests
def test_syntax_check():
    f = open('day10_test_input.txt', 'r')
    lines = f.readlines()

    high_score = calculate_syntax_error_highscore(lines)
    assert high_score == 26397, 'should be 26397'

    middle_score = calculate_autocomplete_middlescore(lines)
    assert middle_score == 288957, 'should be 288957'

def main():
    f = open('day10_input.txt', 'r')
    lines = f.readlines()

    # part 1
    high_score = calculate_syntax_error_highscore(lines)
    print(f'Result for part 1 is {high_score}')

    # part 2
    middle_score = calculate_autocomplete_middlescore(lines)
    print(f'Result for part 2 is {middle_score}')

if __name__ == "__main__":
    main()