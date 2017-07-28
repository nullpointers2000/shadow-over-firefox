# shadow - De Mysteriis Dom Firefox

true = True
false = False
none = None

class symbol:

    def __init__(self, kind = '', name = '', size = 0, has_vtable = false):

        self.kind = kind
        self.name = name
        self.size = size
        self.has_vtable = has_vtable

    def __str__(self):

        sstr = '0x%04x (%04d) %s\t%s' % (self.size, self.size, self.kind, self.name)

        if self.kind != 'class':
            return sstr

        if self.has_vtable == true:
            sstr += ' (vtable: yes)'
        else:
            sstr += ' (vtable: no)'

        return sstr

    def __eq__(self, other):
        return (self.name == other.name and self.kind == other.kind)

    def __contains__(self, key):
        return self.__eq__(key)

# EOF
