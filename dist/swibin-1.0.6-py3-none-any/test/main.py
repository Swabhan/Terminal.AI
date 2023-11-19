from helpers.vectormath import transpose, subtract, proj
from swibin import with_handler

def GramSchmidt(A):
    AT = transpose(A)
    GT = []
    for i in range(len(AT)):
        GT.append(AT[i])
        for j in range(i):
            GT[i] = subtract(GT[i], proj(GT[i], GT[j]))
    G = transpose(GT)
    return G


@with_handler
def main():
  A4 = [[1,4,8],
        [2,0,1],
        [0,5,5],
        [3,8,6]]
  G4 = GramSchmidt(A4)

  assert G4 == [[1.0, 4.0, 8.0]]


if __name__ == "__main__":
  main()
