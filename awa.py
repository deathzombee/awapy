
class Bubble:
    def __init__(self, content=None):
        if isinstance(content, list):
            self.type = 'double'
            self.content = content
        else:
            self.type = 'simple'
            self.content = content
    
    def __str__(self):
        if self.type == 'double':
            return f"Double Bubble with {len(self.content)} bubbles"
        return f"Simple Bubble with value {self.content}"

class BubbleAbyss:
    def __init__(self):
        self.stack = []
    
    def submerge(self, x):
        if len(self.stack) == 0:
            raise ValueError("The Abyss is empty")
        if x == 0 or x >= len(self.stack):
            x = len(self.stack) - 1
        top_bubble = self.stack.pop()
        self.stack.insert(len(self.stack) - x, top_bubble)

    def emerge(self, x):
        if len(self.stack) == 0:
            raise ValueError("The Abyss is empty")
        if x == 0 or x >= len(self.stack):
            bubble = self.stack.pop()
        else:
            bubble = self.stack.pop(x)
        self.stack.insert(0,bubble)
    
    def blow(self, value):
        new_bubble = Bubble([Bubble(value)])
        self.stack.append(new_bubble)
    
    def pop(self):
        if not self.stack:
            raise ValueError("The Abyss is empty")
        top_bubble = self.stack.pop()
        if top_bubble.type == 'double':
            self.stack.extend(reversed(top_bubble.content))
        return top_bubble
    
    def read(self, input_string):
        double_bubble = Bubble([Bubble(ord(c)) for c in input_string if ord(c) < 128])
        self.stack.append(double_bubble)
    
    def print(self):
        if not self.stack:
            raise ValueError("The Abyss is empty")
        top_bubble = self.pop()
        if top_bubble.type == 'simple':
            print(chr(top_bubble.content), end='')
        elif top_bubble.type == 'double':
            for bubble in top_bubble.content:
                print(chr(bubble.content), end='')
            print()  # New line after all characters are printed

    def __str__(self):
        return "\n".join(str(bubble) for bubble in reversed(self.stack))

submerge_list=[2, 3, 4, 1, 6, 5, 3, 10, 20, 22, 25, 3, 0, 0, 2, 3, 4, 1, 6, 5, 3, 10, 20, 22, 25, 3, 0, 0, 0, 16, 26, 31]
abyss = BubbleAbyss()
input_string = "1o1i_awlaw_aowsay3wa0awa!iJlooHi"
abyss.read(input_string)
print("Before Pop:")
print(abyss)
abyss.pop()
for v in submerge_list:
   abyss.submerge(v)

print("After Pop:")
print(abyss)

for v in input_string:
    abyss.print()

print("")
