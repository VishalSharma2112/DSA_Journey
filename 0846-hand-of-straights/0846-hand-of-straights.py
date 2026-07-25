class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        freq_maps = {}
        sorted_hand = sorted(hand)
        for i in sorted_hand:
            freq_maps[i] = freq_maps.get(i, 0)+1
        
        for card in sorted_hand:
            if freq_maps[card] == 0:
                continue
            
            for nxt in range(card, card+groupSize):
                if freq_maps.get(nxt, 0) == 0:
                    return False
                freq_maps[nxt] -= 1
        return True
        