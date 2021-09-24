import sha1
import struct

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print(sha1.sha1(bytes("GeeksForGeeks", encoding='utf8')))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    original_message = "No one has completed lab 2 so give them all a 0"
    # original_hash = sha1.sha1(bytes(original_message, encoding='utf8'))

    m1_p1_l1 = sha1.get_m1_p1_l1(str.encode(original_message))
    # print(f'type(m1_p1_l1) {type(m1_p1_l1)}')
    # print(f'm1_p1_l1: {m1_p1_l1}')
    # print(f'len(m1_p1_l1): {len(m1_p1_l1)}')

    extension = ", except Matt Christensen. He gets 100%"
    m1_p1_l1_extension = m1_p1_l1 + str.encode(extension)

    print(f'Modified message (m1_p1_l1_extension): {m1_p1_l1_extension}')
    print(f'Modified message (m1_p1_l1_extension): (hex) {m1_p1_l1_extension.hex()}')

    new_mac = sha1.sha1(str.encode(extension))
    print(f'new_mac: {new_mac}')
    # print(f': {}')
    # print(f': {}')
    # print(f': {}')

    # print(''.join('{:02x}'.format(x) for x in m1_p1_l1_extension.encode('ascii')))
    # print(f'og_hash: {original_hash}')
    # print_hi('PyCharm')
