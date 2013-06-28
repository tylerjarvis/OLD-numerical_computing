# Solutions to problem 1

def getFrame(m):
    coeffs = []
    k_max = int(sp.pi*2**(m+1))
    for k in xrange(k_max):
        coeffs.append(-2**m*(sp.cos((k+1)*2**(-m)) - sp.cos(k*2**(-m))))
    coeffs.append(-2**m*(1-sp.cos(k_max*2**(-m))))
    return sp.array(coeffs)

frame_4 = getFrame(4)
frame_6 = getFrame(6)
frame_8 = getFrame(8)

# Here's how to plot each one:
# plt.plot([x*2*sp.pi/len(frame_6) for x in range(len(frame_6))],frame_6,drawstyle='steps')

# Solutions to problem 2

def getDetail(m):
    coeffs = []
    k_max = int(sp.pi*2**(m+1))
    for k in xrange(k_max):
        coeffs.append(-2**m*(2*sp.cos((2*k+1)*2**(-m-1)) - sp.cos((k+1)*2**(-m)) - sp.cos(k*2**(-m))))
        print -2**m*(2*sp.cos((2*k+1)*2**(-m-1)) - sp.cos((k+1)*2**(-m)) - sp.cos(k*2**(-m)))
    if (2*sp.pi < (2*k_max+1)*2**(-m-1)):
        coeffs.append(-2**m*(1-sp.cos(k_max*2**(-m))))
    else:
        coeffs.append(-2**m*(2*sp.cos((2*k_max+1)*2**(-m-1)) - 1 - sp.cos(k*2**(-m))))
    return sp.coeffs(coeffs)

detail = getDetail(4)

# Here's how to plot the details
#b = []
#for i in detail:
#    b.extend([i,-i])
#plt.plot([x*2*sp.pi/len(b) for x in range(len(b))],b,drawstyle='steps')

# Here's how to calculate the frame for m=5
details = getDetail(4)
frame = getFrame(4)
frame_5 = sp.zeros(2*len(details))
for i in range(2*len(details)):
    frame_5[i] = frame[i/2] + (-1)**i*details[i/2]

# The solutions to problems three and four are contained in the dwt1D.py file
