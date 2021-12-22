from bisect import bisect_left
import logging
import sys

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


class MKList:
    def __init__(self, l, key):
        self.l = l
        self.key = key

    def __len__(self):
        return len(self.l)

    def __getitem__(self, index):
        return self.key(self.l[index])


def uniq(lst):
    seen = set()
    seen_add = seen.add
    return [x for x in lst if not (x in seen or seen_add(x))]


with open(sys.argv[1], "r") as fh:
    next(fh)
    while True:
        try:
            t, M, K, N = [next(fh) for _ in range(0, 4)]
            logger.debug(f"Reading {t.strip()}")
        except StopIteration:
            break
        M = uniq([float(_) for _ in M.strip().split()])  # Metabolite mass
        K = uniq([float(_) for _ in K.strip().split()])  # Adduct
        N = [float(_) for _ in N.strip().split()]  # Signal
        logger.debug(f"{len(M)}, {len(K)}, {len(M) * len(K)}")

        # Transform M by N
        logger.debug("Adding K and M")
        MK = sorted(
            [
                (mj + ak, j, k)
                for j, mj in enumerate(M)
                for k, ak in enumerate(K)
                if mj + ak > 0
            ],
            key=lambda x: x[0],
        )
        logger.debug(f"{len(MK)}")
        for si in N:
            pos = bisect_left(MKList(MK, key=lambda x: x[0]), si)
            if pos == 0:
                result = MK[0]
            if pos == len(MK):
                result = MK[-1]
            before = MK[pos - 1]
            after = MK[pos]
            if after[0] - si < si - before[0]:
                result = after
            else:
                result = before
            print(result[1] + 1, result[2] + 1)