word = set(input("Please enter the word : "))

left_hand  = set('q, w, e, r, t, a, s, d, f, g, z, x, c, v, b')

right_hand = set('y, u, i, o, p, h, j, k, l, n, m')



print((word - left_hand != set()) and (word - right_hand != set()))