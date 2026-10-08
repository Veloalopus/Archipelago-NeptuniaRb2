import re
from BaseClasses import Region
from .logic_rules import NepRB2Logic
from .options import NepRb2Options

from typing import Dict,List



def evaluate_rule(existing_rule: str, player: int, options:NepRb2Options):
    """
    This method converts a rule from the existing randomizer to a lambda which can be passed to AP.
    The existing randomizer evaluates a defined logic expression, which it seperates into 5 classes:
        - OpLit
        - OpAnd
        - OpOr
        - OpNot

    OpLit is used to evaluate a single literal statement. This can be having an item, or
    can be more complex (e.g. conjunction of literals), which is combined into a single literal
    in the existing randomizer. For the more complicated literals, Ive defined methods above to
    translate them, and placed them in the below "literal_eval_map". If its not in the below map,
    assume the literal is an item which we can check the state for.

    The other Ops are self explanatory, and are translated accordingly.

    :str existing_rule: The existing rule as an string.
    :player int: the relevant player

    :returns: An evaluatable labmda with one argument (for state)

    :raises ValueError: the passed in existing_rule is not a valid OpX object.
    """
    #convert string into a OpX objeect

    if isinstance(existing_rule, OpLit):
        literal = existing_rule.name
        literal_eval_map = {
            "": lambda _: True,
            "None": lambda _: True,
            "True": lambda _:True,
            "False": lambda _: False
        }
        

        if literal in literal_eval_map:
            return literal_eval_map[literal]
        
        split = literal.split(" ")
        match split[0]:
            case "Item":
                if len(split) == 4:
                    return lambda state: NepRB2Logic.has_item(split[1],split[2],state,player,int(split[3]))
                else:
                    return lambda state: NepRB2Logic.has_item(split[1],split[2],state,player)
            case "Level":
                return lambda state: NepRB2Logic.has_level(int(split[1]),state,player)
            case "Power":
                return lambda state: NepRB2Logic.has_power(int(split[1]),state,player)
            case "Defense":
                return lambda state: NepRB2Logic.has_defense(int(split[1]),state,player)
            case "Dungeon":
                return lambda state: NepRB2Logic.dungeon_unlocked(split[1],state,player)
            case "Enemy":
                return lambda state: NepRB2Logic.can_reach_enemy(literal.split(" ",1)[1],state,player)
            case "Tracker":
                return lambda state: NepRB2Logic.has_ApEvent(split[1],state,player)
            case "DungeonState":
                return lambda state: NepRB2Logic.has_dungeon_state(split[1],split[2],state,player)
                
        raise ValueError(f"Invalid Rule. {literal}")

    elif isinstance(existing_rule, OpNot):
        expr = evaluate_rule(existing_rule.expr, player, options)
        return lambda state: not expr(state)
    elif isinstance(existing_rule, OpOr):
        expr_l = evaluate_rule(existing_rule.exprL, player, options)
        expr_r = evaluate_rule(existing_rule.exprR, player, options)
        return lambda state: expr_l(state) or expr_r(state)
    elif isinstance(existing_rule, OpAnd):
        expr_l = evaluate_rule(existing_rule.exprL, player, options)
        expr_r = evaluate_rule(existing_rule.exprR, player, options)
        return lambda state: expr_l(state) and expr_r(state)
    raise ValueError("Invalid Expression recieved.")


isExpr = lambda s : not type(s) is str
def parse_expression_logic(line):
    if line == "" or line == "()":
        line = "True"
    line = line.replace('&&', '&').replace('||', '|')
    tokens = (s.strip() for s in re.split('([()&|!~])', line))
    tokens = [s for s in tokens if s]
    # Stack-based parsing. pop from [tokens], push into [stack]
    # We push an expression into [tokens] if we want to process it next iteration.
    tokens.reverse()
    stack = []
    while len(tokens) > 0:
        next = tokens.pop()
        if isExpr(next):
            if len(stack) == 0:
                stack.append(next)
                continue
            head = stack[-1]
            if head == '&':
                stack.pop()
                exp = stack.pop()
                assert isExpr(exp)
                tokens.append(OpAnd(exp, next))
            elif head == '|':
                stack.pop()
                exp = stack.pop()
                assert isExpr(exp)
                tokens.append(OpOr(exp, next))
            elif head in '!~':
                stack.pop()
                tokens.append(OpNot(next))
            else:
                stack.append(next)
        elif next in '(&|!~':
            stack.append(next)
        elif next == ')':
            exp = stack.pop()
            assert isExpr(exp)
            paren = stack.pop()
            assert paren == '('
            tokens.append(exp)
        else: # string literal
            # Literal parsing
            tokens.append(OpLit(next))
    assert len(stack) == 1
    return stack[0]

class OpLit(object):
    def __init__(self, name):
        self.name = name
    def evaluate(self, variables):
        return variables[self.name]
    def __str__(self):
        return self.name
    __repr__ = __str__

class OpNot(object):
    def __init__(self, expr):
        self.expr = expr
    def evaluate(self, variables):
        return not self.expr.evaluate(variables)
    def __str__(self):
        return '(NOT %s)' % self.expr
    __repr__ = __str__

class OpOr(object):
    def __init__(self, exprL, exprR):
        self.exprL = exprL
        self.exprR = exprR
    def evaluate(self, variables):
        return self.exprL.evaluate(variables) or self.exprR.evaluate(variables)
    def __str__(self):
        return '(%s OR %s)' % (self.exprL, self.exprR)
    __repr__ = __str__

class OpAnd(object):
    def __init__(self, exprL, exprR):
        self.exprL = exprL
        self.exprR = exprR
    def evaluate(self, variables):
        return self.exprL.evaluate(variables) and self.exprR.evaluate(variables)
    def __str__(self):
        return '(%s AND %s)' % (self.exprL, self.exprR)
    __repr__ = __str__
