import numpy as np

## Numpy Array vs. Python List
a = [1, 2, 3]
b = [q * 2 for q in a]
print(a)
print(b)

a = np.array([1, 2, 3])
a * 2
print(a)

a = [1, 2, 3]
b = [4, 5, 6]
[q + r for q, r in zip(a, b)]
print(a)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
a + b
print(a)

## 1. Vectors, the 1D Arrays
a = np.array([1., 2., 3.])
print(a)

a.dtype

print(a.shape)

np.zeros(3, int)

b.dtype

np.zeros_like(a)

a = np.array([1, 2, 3])

np.zeros_like(a)

np.ones_like(a)

np.empty_like(a)

np.full_like(a, 7)

### Array initialisation
np.arange(6)

np.arange(2, 6)

np.arange(1, 6, 2)

np.linspace(0, 0.5, 6)

### Vector indexing
a = np.arange(1, 6)

a[1]

a[2:4]

a[-2:]

a[::2]

a[[1,3,4]]

a[2] = 7

a = np.array(list(np.arange(1, 8)) + list(np.arange(6, 0, -1)))

np.any(a > 5)

a[a > 5]

np.all(a > 5)

a[a > 5] = 0

a[(a >= 3) & (a <= 5)] = 0

np.where(a > 5)

a > 5

np.nonzero(a > 5)

a[a < 5] = 0; a[a >= 5] = 1

np.clip(a, 3, 5)

### Vector operations
a = np.array([1, 2])
b = np.array([4, 8])
a + b

a = np.array([1, 2])
b = np.array([4, 8])
a - b

a = np.array([4, 8])
b = np.array([2, 5])
a * b

a = np.array([4, 8])
b = np.array([2, 5])
a / b

a = np.array([4, 8])
b = np.array([2, 5])
a // b

a = np.array([3, 4])
b = np.array([2, 3])
a ** b

a = np.array([1, 2])
a + 3

a = np.array([1, 2])
a - 3

a = np.array([1, 2])
a * 3

a = np.array([1, 2])
a / 3

a = np.array([1, 2])
a // 3

a = np.array([1, 2])
a ** 3

np.array([2, 3]) ** 2

np.sqrt(np.array([4, 9]))

np.exp(np.array([1, 2]))

np.log(np.array([np.e, np.e ** 2]))

### Scalar product
# scalar product van 2 vectoren
a = np.array([1, 2])
b = np.array([3, 4])
np.dot(a, b)
a @ b


# #### Cross
# geen flauw idee wat deze functie doet ?
a = np.array([2, 0, 0])
b = np.array([0, 3, 0])
np.cross(a, b)


# #### trigonometry
np.sin(np.array([np.pi, np.pi / 2]))
np.arcsin(np.array([0., 1.]))
np.hypot(np.array([3., 5.]), np.array([4., 12.]))

a = np.array([1.1, 1.5, 1.9, 2.5])
np.floor(a)
np.ceil(a)
np.round(a)
a = np.array([1, 2, 3])
np.max(a)
a.max()
a.argmax()
a.sum()
a.var()
a.std()
a.mean()


# Leuke oefening: Zelf de variantie uitrekenen over deze simpele array. Eerst de formulie optekenen in markdown.
#
# variantie: som van het kwadratisch verschil van alle elementen met het gemiddelde, gemiddelde is x met een streepje erboven.
var1 = np.sum((a - a.mean())**2) / len(a)
var1

std1 = var1**0.5
std1

# ### sorting and reversing
a[::-1]
np.sort(a[::-1])


# ## 2. Matrices, the 2D Arrays

a = np.array([[1, 2, 3],
              [4, 5, 6]])

a.dtype

a.shape

np.zeros((3, 2))

np.full((3, 2), 7.)

np.ones((3, 2), int)

np.empty((3, 2))

np.eye(3)

np.eye(3, 4)

# ### Random matrix generation
np.random.randint(0, 10, [3, 2])

np.random.rand(2, 3)

np.random.normal(10, 2, [3, 2])

a = np.arange(1, 13)
a.shape = (3, 4)
a

a[1, 2]

a[1, :]

a[:, 2]

a[:, 1:3]

a[-2:, 1:3]

a[::2, 1::2]


# ### the axis argument
# tot hier gebleven, volgende keer verder
#

