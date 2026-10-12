class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        """
        1,2,4,2,3,5,3,4
        1,2,2,3,3,4,4,5

        {
         1: 1
         2: 2
         3: 2
         4: 2
         5: 1
        }
        """

        c = Counter(hand)
        totalCards = len(hand)
        cardsGrouped = 0

        while cardsGrouped < totalCards:
            smallest = min(c.keys())
            c[smallest] -= 1
            cardsGrouped += 1
            if not c[smallest]:
                del c[smallest]
            for _ in range(groupSize - 1):
                if not c[smallest + 1]:
                    return False
                c[smallest + 1] -= 1
                if not c[smallest + 1]:
                    del c[smallest + 1]
                smallest += 1
                cardsGrouped += 1
        
        return True

        